# Performance Optimization - ALL SHIP ECOMBOX

## Performance Targets

| Metric | Target | Critical | Tool |
|--------|--------|----------|------|
| App cold start | < 3s | < 5s | Flutter DevTools |
| Scan → Record | < 500ms | < 1s | Stopwatch |
| Video transition | < 500ms | < 1s | Stopwatch |
| FPS during recording | ≥ 25 | ≥ 15 | Performance overlay |
| Memory usage | < 200MB | < 300MB | DevTools |
| APK size | < 30MB | < 50MB | `flutter build` |

## Flutter Performance

### Build Optimization

```dart
// ✅ const constructors
const SizedBox(height: 16); // Good
SizedBox(height: 16);       // Bad - rebuilds

// ✅ RepaintBoundary cho complex widgets
RepaintBoundary(
  child: CameraPreview(),
)

// ✅ ListView.builder cho long lists
ListView.builder(
  itemCount: videos.length,
  itemBuilder: (_, i) => VideoCard(videos[i]),
)
```

### Image Optimization

```dart
// ✅ Cached network images
CachedNetworkImage(
  imageUrl: thumbnailUrl,
  placeholder: (_, __) => Shimmer(),
  errorWidget: (_, __, ___) => Icon(Icons.error),
)

// ✅ Resize thumbnails
Image.file(
  file,
  cacheWidth: 200,  // Decode at smaller size
  cacheHeight: 200,
)
```

### Async Best Practices

```dart
// ✅ compute() cho heavy work
final thumbnail = await compute(generateThumbnail, videoPath);

// ✅ Isolate cho encoding
Isolate.spawn(encodeVideo, params);

// ✅ Stream instead of loading all
Stream<Video> searchVideos(String query) async* {
  // Yield results as found
}
```

## Video Recording Performance

### Camera Settings

```dart
// ✅ Use appropriate resolution
final cameras = await availableCameras();
final controller = CameraController(
  cameras.first,
  ResolutionPreset.high,  // 720p, not ultraHigh
  enableAudio: true,
  imageFormatGroup: ImageFormatGroup.yuv420,
);
```

### Encoding Pipeline

```yaml
TIPS:
  - Hardware encoding (MediaCodec/VideoToolbox)
  - Fragmented MP4 for crash safety
  - Background thread for file I/O
  - Pre-allocate file buffers
```

## Memory Management

```dart
// ✅ Dispose controllers
@override
void dispose() {
  _cameraController.dispose();
  _videoController.dispose();
  _animationController.dispose();
  super.dispose();
}

// ✅ Cancel streams
late StreamSubscription _scannerSubscription;

@override
void dispose() {
  _scannerSubscription.cancel();
  super.dispose();
}

// ✅ Clear large collections
void clearOldData() {
  _videoCache.clear();
  imageCache.clear();
}
```

## Database Performance

```dart
// ✅ Indexes cho search columns
CREATE INDEX idx_orders_code ON orders(code);
CREATE INDEX idx_videos_order_id ON videos(order_id);
CREATE INDEX idx_videos_created ON videos(created_at);

// ✅ Batch operations
await db.transaction((txn) async {
  for (final video in videos) {
    await txn.insert('videos', video.toMap());
  }
});

// ✅ Limit queries
SELECT * FROM videos 
ORDER BY created_at DESC 
LIMIT 50 OFFSET 0;
```

## APK Size Optimization

```yaml
# analysis_options.yaml
flutter:
  uses-material-design: true
  
# Chỉ include assets cần thiết
assets:
  - assets/audio/  # Beep sounds only

# ProGuard (android/app/proguard-rules.pro)
-keep class io.flutter.** { *; }
```

### Build Optimizations

```bash
# Split APKs by ABI
flutter build apk --split-per-abi

# Obfuscate
flutter build apk --obfuscate --split-debug-info=debug_info/
```

## Profiling Checklist

```markdown
BEFORE RELEASE:
[ ] Profile on low-end device (2GB RAM)
[ ] Check memory leaks with DevTools
[ ] Verify FPS during recording
[ ] Test with 1000+ videos in DB
[ ] Check storage cleanup performance
[ ] Verify cold start time
```

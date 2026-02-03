# Coding Conventions - ALL SHIP ECOMBOX

## Ngôn Ngữ & Framework

### Flutter (Mobile)
- **Dart Version:** Dart 3.x (null safety required)
- **Flutter Version:** Flutter 3.x stable channel
- **State Management:** Provider hoặc Riverpod (ưu tiên simplicity)
- **Architecture:** Clean Architecture với separation of concerns

### Electron (Desktop)
- **TypeScript:** Required (strict mode)
- **Node.js:** LTS version
- **UI:** HTML/CSS với modern web standards

## Naming Conventions

### Files & Directories

```dart
// Flutter
lib/
├── core/               // Core utilities, constants
├── data/               // Data layer (repositories, data sources)
├── domain/             // Business logic, entities
├── presentation/       // UI (screens, widgets)
├── services/           // Platform services
└── main.dart

// File naming: snake_case
video_recording_service.dart
order_repository.dart
camera_preview_widget.dart
```

### Code Naming

```dart
// Classes: PascalCase
class OrderRepository {}
class VideoRecordingService {}

// Variables, functions: camelCase  
final orderCode = "SPX123456789";
void startRecording() {}

// Constants: SCREAMING_SNAKE_CASE
const int MAX_RECORDING_DURATION_MS = 300000; // 5 minutes
const String DEFAULT_VIDEO_RESOLUTION = "1280x720";

// Private members: prefix with underscore
class VideoService {
  final _recorder = VideoRecorder();
  void _processFrame() {}
}
```

### Video & File Naming

```
FORMAT: {order_code}_{type}_{timestamp}.mp4

Ví dụ:
  SPX038294671_packing_20260203_103052.mp4
  VN72849301_return_20260203_143021.mp4
  TK9928374_shipping_20260203_160045.mp4

THUMBNAIL:
  {order_code}_{type}_{timestamp}_thumb.jpg
```

### Directory Structure for Videos

```
videos/
├── 2026/
│   ├── 02/
│   │   ├── 03/
│   │   │   ├── SPX038294671_packing_20260203_103052.mp4
│   │   │   └── SPX038294671_packing_20260203_103052_thumb.jpg
│   │   └── 04/
│   │       └── ...
│   └── 03/
│       └── ...
```

## Code Style

### Flutter/Dart

```dart
// GOOD: Use const constructors
const EdgeInsets.all(16.0);
const Text('Label');

// GOOD: Prefer final over var
final orders = await repository.getOrders();

// GOOD: Use null-aware operators
final name = user?.name ?? 'Unknown';

// GOOD: Named parameters for clarity
void startRecording({
  required String orderCode,
  required CameraSource source,
  Duration? maxDuration,
});

// GOOD: Extension methods for reusability
extension DateTimeX on DateTime {
  String toVideoTimestamp() => DateFormat('yyyyMMdd_HHmmss').format(this);
}
```

### Error Handling

```dart
// GOOD: Use Result pattern for expected failures
sealed class Result<T> {}
class Success<T> extends Result<T> { final T data; }
class Failure<T> extends Result<T> { final AppError error; }

// GOOD: Graceful degradation
Future<void> startRecording() async {
  try {
    await _camera.start();
  } on CameraNotAvailableException {
    // Fallback: notify user, allow manual input
    _showCameraUnavailableDialog();
  }
}
```

### Documentation

```dart
/// Service responsible for video recording operations.
/// 
/// Handles camera initialization, recording lifecycle,
/// and video file management.
/// 
/// Example:
/// ```dart
/// final service = VideoRecordingService();
/// await service.startRecording(orderCode: 'SPX123');
/// // ... recording ...
/// await service.stopRecording();
/// ```
class VideoRecordingService {
  /// Starts recording video for the given order.
  /// 
  /// [orderCode] - The order identifier, will be embedded in the video.
  /// [source] - Camera source to use (front, rear, external).
  /// 
  /// Throws [CameraNotAvailableException] if no camera is available.
  Future<void> startRecording({
    required String orderCode,
    CameraSource source = CameraSource.rear,
  });
}
```

## Video Processing Specs

### Encoding Settings

```yaml
STANDARD PROFILE (default):
  Resolution: 1280x720 (720p)
  FPS: 20
  Codec: H.264 Main Profile
  Bitrate: VBR, target 2 Mbps, max 4 Mbps
  Keyframe interval: 2 seconds
  Audio: AAC 64kbps mono
  Result: ~4-6 MB / 30 seconds

HIGH QUALITY PROFILE:
  Resolution: 1920x1080 (1080p)  
  FPS: 24
  Codec: H.264 High Profile
  Bitrate: VBR, target 4 Mbps, max 8 Mbps
  Keyframe interval: 2 seconds
  Audio: AAC 128kbps stereo
  Result: ~8-12 MB / 30 seconds
```

### Container Format

```
CONTAINER: Fragmented MP4 (fMP4)

Lý do:
- Không mất data nếu app crash giữa chừng
- Có thể phát lại ngay cả khi chưa finalize
- Android MediaMuxer hỗ trợ native
- iOS AVAssetWriter tự quản lý fragment
```

## Git Conventions

### Branch Naming

```
feature/scan-barcode-camera
fix/camera-disconnect-handling  
hotfix/video-corruption-ios
refactor/video-service-cleanup
```

### Commit Messages

```
feat: add continuous scan mode for order processing
fix: handle camera disconnect during recording
docs: update README with setup instructions
refactor: extract video encoding to separate service
test: add unit tests for OrderRepository
```

## Testing Requirements

### Unit Tests
- Business logic: 80%+ coverage
- Services: Test happy path + error cases
- Repositories: Mock data sources

### Integration Tests
- Camera recording workflow
- Scanner input processing
- Database operations

### Device Testing
- Android: Test on 15-20 popular models (Samsung A-series, Xiaomi Redmi, OPPO A, Vivo Y)
- iOS: Test on iPhone 12+ and iPad
- Desktop: Windows 10/11, macOS 12+

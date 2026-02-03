# Video Overlay (Timestamp + Location)

## Mô tả
Hiển thị timestamp (ngày giờ) và vị trí GPS trực tiếp trên video như một lớp overlay, tăng tính xác thực của bằng chứng.

## Ví dụ Overlay

```
+--------------------------------------------------+
|                                                  |
|                                                  |
|                 VIDEO CONTENT                    |
|                                                  |
|                                                  |
|--------------------------------------------------+
| 📅 03/02/2026 10:35:47 | 📍 21.0285, 105.8542   |
| Allship Record v1.0.0  | 📦 SPX038294671        |
+--------------------------------------------------+
```

## Thông tin hiển thị

| Item | Format | Ví dụ |
|---|---|---|
| Ngày giờ | `dd/MM/yyyy HH:mm:ss` | 03/02/2026 10:35:47 |
| Tọa độ GPS | `lat, lng` (6 số thập phân) | 21.028511, 105.854167 |
| Mã đơn | Order code | SPX038294671 |
| Phiên bản app | `vX.Y.Z` | v1.0.0 |

## Quyền cần cấp

### Android (`AndroidManifest.xml`)
```xml
<!-- Location permissions -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

<!-- Optional: Background location (if needed) -->
<!-- <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" /> -->
```

### iOS (`Info.plist`)
```xml
<key>NSLocationWhenInUseUsageDescription</key>
<string>Allship Record cần vị trí để gắn vào video làm bằng chứng đóng hàng, giúp xác thực địa điểm khi xảy ra tranh chấp.</string>
```

## Kỹ thuật triển khai

### 1. Timestamp (Dễ)
```dart
String getTimestamp() {
  final now = DateTime.now();
  return DateFormat('dd/MM/yyyy HH:mm:ss').format(now);
}
```
- Cập nhật mỗi giây trên overlay.
- Không cần quyền.

### 2. Location (Trung bình)

#### Package sử dụng
```yaml
dependencies:
  geolocator: ^10.1.0
  geocoding: ^2.1.1  # Optional: convert coordinates to address
```

#### Flow lấy location
```dart
Future<Position?> getCurrentLocation() async {
  // 1. Check permission
  LocationPermission permission = await Geolocator.checkPermission();
  if (permission == LocationPermission.denied) {
    permission = await Geolocator.requestPermission();
  }
  
  // 2. Handle denied
  if (permission == LocationPermission.deniedForever) {
    return null; // Show "N/A" on overlay
  }
  
  // 3. Get position with timeout
  try {
    return await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high,
      timeLimit: Duration(seconds: 10),
    );
  } catch (e) {
    return null;
  }
}
```

### 3. Render Overlay

#### Option A: Software Overlay (Đơn giản)
- Dùng `Stack` widget đặt `Text` lên `CameraPreview`.
- Sau khi quay, dùng FFmpeg để burn text vào video.

```dart
// FFmpeg command
final cmd = '-i input.mp4 -vf "drawtext=text=\'$timestamp\':x=10:y=H-30:fontsize=24:fontcolor=white" output.mp4';
```

**Ưu điểm**: Đơn giản.
**Nhược điểm**: Cần xử lý sau khi quay, tốn thời gian.

#### Option B: Hardware Overlay (Khuyến nghị)
- Ghi timestamp/location vào metadata MP4.
- Render realtime overlay trong preview.
- Burn overlay trong quá trình encoding (không cần post-process).

**Ưu điểm**: Nhanh, không cần FFmpeg.
**Nhược điểm**: Phức tạp hơn.

## Edge Cases

| Trường hợp | Xử lý |
|---|---|
| User từ chối quyền location | Hiển thị "📍 N/A" trên overlay |
| GPS chậm (trong nhà) | Fallback sang last known location hoặc Network location |
| Không có GPS (emulator) | Hiển thị "📍 Demo Mode" |
| Timezone khác UTC | Luôn dùng local timezone của thiết bị |

## Cài đặt cho User

```
+--------------------------------------------------+
|           CÀI ĐẶT OVERLAY                        |
+--------------------------------------------------+
|                                                  |
|  📅 Hiển thị ngày giờ        [    🔘 Bật    ]   |
|  📍 Hiển thị vị trí          [    🔘 Bật    ]   |
|  📦 Hiển thị mã đơn          [    🔘 Bật    ]   |
|  📱 Hiển thị phiên bản app   [    ○ Tắt    ]   |
|                                                  |
|  Vị trí overlay:             [Dưới cùng    ▼]   |
|  Cỡ chữ:                     [Trung bình   ▼]   |
|                                                  |
+--------------------------------------------------+
```

## Ưu tiên
**P1** - Phase 2 (Enhancement).

## Dependencies mới

```yaml
# Thêm vào pubspec.yaml
dependencies:
  geolocator: ^10.1.0
  geocoding: ^2.1.1      # Optional
  ffmpeg_kit_flutter: ^6.0.3  # Nếu dùng Option A
```

## Tham chiếu
- [Geolocator Package](https://pub.dev/packages/geolocator)
- [FFmpeg drawtext filter](https://ffmpeg.org/ffmpeg-filters.html#drawtext)

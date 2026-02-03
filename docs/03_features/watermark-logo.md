# Watermark Logo Shop

## Mô tả
Gắn logo của shop lên góc video để branding và chống giả mạo video.

## Vị trí Watermark

```
+--------------------------------------------------+
| [LOGO]                                           |
|                                                  |
|                 VIDEO CONTENT                    |
|                                                  |
|--------------------------------------------------+
| Timestamp | GPS | Order Code                     |
+--------------------------------------------------+
```

- **Mặc định**: Góc trên phải.
- **Có thể thay đổi**: 4 góc + center.

## Cấu hình

### Upload Logo
- Format: PNG với transparent background.
- Max size: 200x200px.
- Lưu trong app storage.

### Settings UI
```
+--------------------------------------------------+
|           WATERMARK LOGO                         |
+--------------------------------------------------+
|                                                  |
|  Logo hiện tại: [THUMBNAIL]  [Thay đổi]          |
|                                                  |
|  Vị trí:        [Góc trên phải  ▼]              |
|  Độ trong suốt: [━━━━━●━━━━━] 70%               |
|  Kích thước:    [Nhỏ ○] [Vừa ●] [Lớn ○]         |
|                                                  |
+--------------------------------------------------+
```

## Kỹ thuật

### Render Watermark
```dart
// Option 1: Overlay trên preview (realtime)
Stack(
  children: [
    CameraPreview(),
    Positioned(
      top: 10, right: 10,
      child: Opacity(opacity: 0.7, child: Image.asset('logo.png')),
    ),
  ],
)

// Option 2: Burn vào video sau khi quay (FFmpeg)
```

## Ưu tiên
**P2** - Phase 2.

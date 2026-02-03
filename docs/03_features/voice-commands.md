# Voice Commands (Điều khiển Giọng nói)

## Mô tả
Cho phép user điều khiển app bằng giọng nói, đạt được "hands-free" thực sự khi đang đóng hàng.

## Lệnh hỗ trợ

| Lệnh | Hành động |
|---|---|
| "Quay tiếp" / "Tiếp tục" | Bắt đầu quay đơn mới |
| "Dừng lại" / "Xong" | Dừng quay, lưu video |
| "Hủy" / "Bỏ qua" | Hủy video hiện tại |
| "Tra cứu [mã đơn]" | Tìm video theo mã |

## Kỹ thuật triển khai

### Package sử dụng
```yaml
dependencies:
  speech_to_text: ^6.3.0
```

### Quyền cần cấp
**Android** (`AndroidManifest.xml`):
```xml
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

**iOS** (`Info.plist`):
```xml
<key>NSSpeechRecognitionUsageDescription</key>
<string>Allship Record cần quyền microphone để điều khiển bằng giọng nói.</string>
```

### Flow xử lý
```dart
// 1. Luôn lắng nghe (always-on listening)
// 2. Detect wake word (optional): "Hey Allship"
// 3. Recognize command
// 4. Execute action
// 5. Audio feedback confirmation
```

## Ưu tiên
**P1** - Phase 2.

## Thách thức
- Background noise từ môi trường đóng hàng.
- Accent/giọng địa phương.
- Battery consumption khi always-on.

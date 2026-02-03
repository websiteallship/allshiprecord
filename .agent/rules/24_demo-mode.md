---
description: Quy tắc cho Demo Mode (Chế độ Demo)
globs: ["**/*.dart", "**/main.*"]
---

# Demo Mode Rules

## 1. Mục đích
Cho phép test app đầy đủ mà không cần phần cứng thật (camera, scanner).

## 2. Kích hoạt

### Via Environment Variable
```dart
const bool kDemoMode = bool.fromEnvironment('DEMO_MODE', defaultValue: false);

// Run với:
// flutter run --dart-define=DEMO_MODE=true
```

### Via Settings (Debug build only)
```dart
if (kDebugMode) {
  // Hiển thị toggle Demo Mode trong Settings
}
```

## 3. Hành vi trong Demo Mode

| Component | Hành vi thật | Hành vi Demo |
|---|---|---|
| Camera | Stream từ hardware | Loop video sample |
| Scanner | Input từ HID device | Random code mỗi 5s |
| Storage | Ghi file thật | Log only, không ghi |
| Location | GPS thật | Tọa độ giả (Hà Nội) |

## 4. UI Indicator

### PHẢI hiển thị rõ ràng
```
+--------------------------------------------------+
| ⚠️ CHẾ ĐỘ DEMO - Không ghi video thật            |
+--------------------------------------------------+
```

- Badge màu vàng/cam góc trên màn hình.
- Watermark trên camera preview.

## 5. Data trong Demo Mode

### Fake Data Generator
```dart
class DemoDataGenerator {
  static String randomOrderCode() {
    final prefixes = ['SPX', 'VN', 'SPXVN'];
    final prefix = prefixes[Random().nextInt(prefixes.length)];
    final number = Random().nextInt(999999999).toString().padLeft(9, '0');
    return '$prefix$number';
  }
}
```

### Không lưu vào DB thật
- Sử dụng in-memory SQLite.
- Hoặc prefix table với `demo_`.

## 6. Khi KHÔNG dùng Demo Mode

- ❌ Trong production build.
- ❌ Khi đang quay video thật.
- ❌ Trong release/signed APK.

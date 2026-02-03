# Home Screen Widget

## Mô tả
Widget trên home screen cho phép user 1-tap mở app và bắt đầu quay ngay, không cần navigate qua menu.

## Widget Design

### Android Widget
```
+---------------------------+
|                           |
|  🎬 ALLSHIP RECORD        |
|                           |
|  [📦 Đóng hàng]           |
|                           |
|  Hôm nay: 25 đơn          |
+---------------------------+
```

Size: 2x2 hoặc 4x1.

### iOS Widget
- Small (2x2): Chỉ icon + 1 action.
- Medium (4x2): Thêm stats.

## Kỹ thuật

### Android
```kotlin
// Sử dụng home_widget package
// Widget viết bằng Kotlin/XML
```

### iOS
```swift
// WidgetKit (iOS 14+)
// SwiftUI
```

### Flutter Package
```yaml
dependencies:
  home_widget: ^0.4.1
```

## Actions từ Widget

| Tap | Hành động |
|---|---|
| Tap icon | Mở app vào màn hình quay |
| Tap "Đóng hàng" | Mở thẳng màn hình Packing |
| Long press | Mở app settings |

## Ưu tiên
**P2** - Phase 5.

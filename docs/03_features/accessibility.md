# Accessibility (Hỗ trợ Người khuyết tật)

## Mô tả
Đảm bảo app có thể sử dụng được bởi người khuyết tật (thị giác, thính giác, vận động).

## Hỗ trợ Screen Reader

### Semantic Labels
```dart
Semantics(
  label: 'Nút bắt đầu quay video đóng gói',
  button: true,
  child: ElevatedButton(
    onPressed: () {},
    child: Text('Đóng hàng'),
  ),
)
```

### Announce Changes
```dart
// Thông báo cho screen reader
SemanticsService.announce('Đã quét mã SPX123456789', TextDirection.ltr);
```

## Hỗ trợ Thị giác

### Contrast Ratio
- Text/Background: Tối thiểu 4.5:1.
- Large text: Tối thiểu 3:1.

### Scalable Text
```dart
// Không dùng fixed font size
Text(
  'Mã đơn',
  style: Theme.of(context).textTheme.bodyLarge,
  // Không dùng: fontSize: 16 (fixed)
)
```

### Color Blindness
- Không chỉ dùng màu để truyền đạt thông tin.
- Kết hợp icon/text với màu.

## Hỗ trợ Vận động

### Large Touch Targets
- Minimum: 48x48 dp.
- Khoảng cách giữa các nút: 8dp.

### Voice Control
- Tích hợp Voice Commands (F022).
- Giảm phụ thuộc vào touch.

## Testing

### Tools
- Android: TalkBack.
- iOS: VoiceOver.
- Flutter: `flutter run --enable-accessibility`.

### Checklist
- [ ] Screen reader đọc đúng thứ tự.
- [ ] Tất cả buttons có label.
- [ ] Contrast ratio đạt chuẩn.
- [ ] Touch targets đủ lớn.

## Ưu tiên
**P2** - Phase 5.

# Testing Guidelines

## 1. Unit Testing
-   **Scope:** Logic xử lý chuỗi mã vạch, tính toán dung lượng, format tên file.
-   **Coverage Target:** 80% cho các hàm utility.
-   **Framework:** `test` (Dart), `jest` (JS).

## 2. Integration Testing (Device)
Phần khó nhất là test Camera và Scanner thật.
-   **Mock Hardware:** Tạo các lớp giả lập (Mock) cho Camera và Scanner để chạy test trên máy ảo/CI.
    -   `MockScanner`: Gửi chuỗi ký tự ảo sau mỗi 2 giây.
    -   `MockCamera`: Phát video lặp lại từ file sample thay vì camera thật.

## 3. Demo Mode (Chế độ Demo)
Cho phép test toàn bộ app logic mà không cần phần cứng thật.

### Kích hoạt Demo Mode
```dart
// Trong main.dart hoặc settings
const bool kDemoMode = bool.fromEnvironment('DEMO_MODE', defaultValue: false);

// Run với: flutter run --dart-define=DEMO_MODE=true
```

### Hành vi trong Demo Mode
- **Camera**: Hiển thị video sample loop thay vì camera thật.
- **Scanner**: Tự động "quét" mã ngẫu nhiên mỗi 5 giây.
- **Storage**: Fake ghi file (chỉ log, không tạo file thật).
- **UI**: Hiển thị badge "DEMO MODE" góc màn hình.

### Lợi ích
- Test trên emulator/máy ảo.
- Demo cho khách hàng mà không cần setup phần cứng.
- AI có thể test logic app.

## 3. Manual Testing (Checklist)
Do sự đa dạng thiết bị, mỗi phiên bản release cần test tay trên thiết bị thật theo kịch bản:
-   [ ] Cắm rút Camera đột ngột khi đang quay.
-   [ ] Cắm rút Scanner.
-   [ ] Để App chạy qua đêm (Long run test) xem có crash/tràn bộ nhớ không.
-   [ ] Test kịch bản full bộ nhớ (Storage Full).

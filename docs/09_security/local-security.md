# Bảo mật Local Storage

Vì App hoạt động Local-first, dữ liệu nằm hoàn toàn trên thiết bị của user. Bảo mật tập trung vào việc ngăn chặn truy cập trái phép vật lý.

## 1. Mã hóa File (Optional)
Đối với Enterprise version:
-   Video và Database có thể được mã hóa bằng AES-256.
-   Key giải mã lưu trong Secure Enclave (iOS) hoặc Keystore (Android).
-   -> Nếu mất máy, kẻ gian không thể lấy video ra xem được.

## 2. App Lock
-   Cho phép đặt PIN Code hoặc FaceID/Fingerprint để mở App.
-   Ngăn nhân viên xóa video hoặc tò mò xem lại các đơn hàng cũ trái phép.

## 3. Chống xóa nhầm (OS Level)
-   Trên Android 11+: Sử dụng cấu hình `Scoped Storage`. Các app khác không thể xóa file video do Allship Record tạo ra (trừ khi user cấp quyền đặc biệt).

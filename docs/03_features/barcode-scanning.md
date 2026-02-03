# Tính năng: Quét Mã Vận Đơn

Đây là điểm khởi đầu của mọi quy trình trong ứng dụng.

## 1. Các loại mã hỗ trợ
Hệ thống hỗ trợ tất cả các định dạng mã phổ biến được sử dụng bởi các đơn vị vận chuyển tại Việt Nam (Shopee Express, GHTK, GHN, Viettel Post, J&T...):
-   **1D Barcode:** Code 128, Code 39, EAN-13.
-   **2D Code:** QR Code, Data Matrix.

## 2. Nguồn quét (Input Sources)

Có 3 cách nhập mã vào hệ thống:

### A. Camera Scan (Dùng Camera điện thoại/Webcam)
-   **Cơ chế:** Sử dụng thư viện ML Kit (Mobile) để detect mã từ luồng video preview.
-   **Ưu điểm:** Tiện lợi, không cần mua thêm thiết bị.
-   **Nhược điểm:** Tốc độ chậm hơn scanner chuyên dụng, khó quét trong điều kiện thiếu sáng hoặc mã bị nhăn/mờ.
-   **UX:** Hiển thị khung chữ nhật (Reticle) trên màn hình để hướng dẫn người dùng căn chỉnh.

### B. Bluetooth Scanner (HID Mode)
-   **Cơ chế:** Máy quét kết nối qua Bluetooth và hoạt động giả lập bàn phím. App lắng nghe sự kiện key press.
-   **Ưu điểm:** Tốc độ cực nhanh (< 0.1s), chính xác 99.9%, quét được mã mờ/xước tốt hơn camera.
-   **Lưu ý:** Trên iOS, kết nối HID sẽ làm ẩn bàn phím ảo. Cần có UI không phụ thuộc bàn phím.

### C. USB Scanner (OTG / PC)
-   **Cơ chế:** Cắm trực tiếp vào cổng USB (PC) hoặc qua đầu chuyển OTG (Android). Hoạt động giả lập bàn phím.
-   **Ưu điểm:** Ổn định nhất, không lo hết pin như Bluetooth.

## 3. Logic Xử lý Input
Để phân biệt giữa **Người dùng gõ tay** và **Máy quét bắn**, hệ thống dựa vào tốc độ nhập liệu:
-   **Máy quét:** Gửi toàn bộ chuỗi ký tự (ví dụ: `SPX123456`) trong thời gian rất ngắn (< 50ms).
-   **Người gõ:** Khoảng thời gian giữa các phím > 100ms.

Quy trình:
1.  Nhận input.
2.  Validate định dạng (Regex check: `^[A-Z0-9]+$`, độ dài...).
3.  Nếu hợp lệ -> Kích hoạt quy trình quay video.
4.  Nếu không hợp lệ -> Phát âm thanh cảnh báo "Beep lỗi".

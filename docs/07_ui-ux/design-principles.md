# Nguyên tắc Thiết kế UI/UX

## 1. Triết lý chung: Hands-free & High Contrast
Ứng dụng được sử dụng trong môi trường nhà kho, ánh sáng có thể phức tạp, nhân viên thao tác nhanh và thường đứng xa màn hình (1-2m).

### Nguyên tắc 1: Hands-free (Không chạm)
-   UI ở chế độ Đóng hàng phải thiết kế để **không cần thao tác chạm**.
-   Mọi trạng thái chuyển đổi (Bắt đầu quay -> Đang quay -> Lưu) phải tự động hoàn toàn dựa trên Scanner Input.

### Nguyên tắc 2: Tương phản cao (High Contrast)
-   Sử dụng màu sắc rực rỡ, độ tương phản mạnh để dễ nhìn từ xa.
-   Trạng thái **ĐANG QUAY (RECORDING)** phải cực kỳ nổi bật (ví dụ: Viền đỏ nhấp nháy toàn màn hình).

### Nguyên tắc 3: Âm thanh là phản hồi chính
-   Vì nhân viên không nhìn màn hình liên tục, âm thanh (Beep/Boop) đóng vai trò xác nhận thao tác thành công hay thất bại.

## 2. Màu sắc Trạng thái (Color System)
-   🔵 **Xanh Dương (Ready):** Sẵn sàng, chờ quét mã.
-   🔴 **Đỏ (Recording):** Đang quay video. (Danger/Active).
-   🟢 **Xanh Lá (Success):** Lưu thành công.
-   🟠 **Cam (Warning):** Cảnh báo (Trùng mã, bộ nhớ đầy).
-   ⚫ **Xám (Disabled):** Tính năng chưa kích hoạt.

## 3. Typography
-   Sử dụng Font không chân (Sans-serif) đậm, rõ ràng (như Roboto, Inter).
-   Kích thước chữ (Font size) lớn hơn bình thường 20-30% để dễ đọc từ xa.

# Tính năng: Tra cứu & Tìm kiếm Video

Khả năng tìm lại video nhanh chóng khi có khiếu nại là giá trị cốt lõi của phần mềm.

## 1. Phương thức tìm kiếm

### A. Tìm theo Mã Vận Đơn (Chính)
-   **Input:** Nhập tay hoặc dùng scanner quét mã vào ô tìm kiếm.
-   **Tốc độ:** Tức thì (< 1ms) nhờ Index DB.
-   **Kết quả:** Hiển thị tất cả video liên quan đến mã đó (Packing, Shipping, Return).

### B. Tìm theo Thời gian
-   Chọn ngày (Date Picker).
-   Hiển thị danh sách video theo trình tự thời gian trong ngày.
-   Phù hợp để: Kiểm tra lại xem "Sáng nay đóng được bao nhiêu đơn" hoặc "Khoảng 10h sáng ai đóng đơn này".

### C. Tìm theo Trạng thái (Filter)
-   Lọc các video có tag `return` (hàng hoàn).
-   Lọc các video có tag `damaged` (hư hỏng).

## 2. Giao diện Kết quả
Hiển thị dạng danh sách thẻ (Card list):

```text
--------------------------------------------------
[THUMBNAIL ẢNH]    Mã: SPX123456789
                   Loại: Đóng gói (Packing)
                   Thời gian: 03/02/2026 10:30:15
                   Thời lượng: 45s
                   Thiết bị: Samsung A54
                   [NÚT XEM]  [NÚT CHIA SẺ]
--------------------------------------------------
```

## 3. Trình phát Video (Player)
-   Hỗ trợ Zoom/Pan: Để soi kỹ chi tiết mã đơn hoặc sản phẩm trên video.
-   Playback Speed: 0.5x, 1.0x, 2.0x (Tua nhanh để kiểm tra).
-   Snapshot: Nút chụp ảnh màn hình từ video để lấy bằng chứng tĩnh.

# Chiến lược Khôi phục (Recovery Strategies)

## 1. Crash Recovery (Ứng dụng bị tắt đột ngột)
Nếu App bị tắt ngang (Crash, Hết pin, iOS kill background) khi đang xử lý:

### Khi khởi động lại App:
1.  **Check Temp Folder:** Kiểm tra xem có file video `.mp4` nào chưa hoàn thiện (thiếu `moov` atom) hoặc chưa được đánh index vào DB không.
2.  **Repair:**
    -   Sử dụng `ffmpeg` (trên Desktop) hoặc `mp4parser` (Mobile) để sửa lỗi file video nếu cần.
    -   Move file vào thư mục chính thức (`/videos/YYYY/...`).
3.  **Re-index:** Tạo record trong SQLite cho video đó với trạng thái `crashed_recovery`.
4.  **Thông báo:** "Phát hiện 1 video chưa được lưu từ phiên trước. Đã khôi phục thành công."

## 2. Data Corruption (Hỏng Database)
SQLite file có thể bị hỏng.

-   **Auto Backup:** App tự động backup file `.db` mỗi ngày ra file `.db.bak`.
-   **Restore:** Khi không mở được DB chính, tự động load file backup gần nhất và báo cáo user.

## 3. Storage Full (Hết bộ nhớ - Critical)
Khi dung lượng trống cực thấp (< 500MB):
1.  **Chặn quay:** Không cho phép quay video mới.
2.  **Bắt buộc dọn dẹp:** Hiện màn hình yêu cầu user xóa bớt dữ liệu hoặc cắm thẻ SD/Ổ cứng mới.

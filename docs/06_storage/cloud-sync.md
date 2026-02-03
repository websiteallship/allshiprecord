# Cloud Sync & Backup (Optional)

Tính năng này dành cho gói nâng cao (Premium) hoặc các Shop muốn đảm bảo an toàn dữ liệu tuyệt đối.

## 1. Cơ chế Sync
Sử dụng kiến trúc **Metadata First**.

### Step 1: Sync Metadata (Real-time)
-   Ngay khi quay xong, thông tin đơn hàng (mã, thời gian, path, size...) được đẩy lên Cloud Database nhỏ nhẹ.
-   **Lợi ích:** Chủ shop ngồi nhà có thể mở Web Dashboard thấy ngay "Nhân viên A vừa đóng xong đơn SPX123".

### Step 2: Sync Video (Background / On-Demand)
Video dung lượng lớn nên không sync tức thì để tránh nghẽn mạng.

**Chế độ Sync:**
1.  **WiFi Only:** Chỉ upload khi có WiFi.
2.  **Selected Only:** Chỉ upload video Hàng Hoàn (quan trọng) hoặc video do user chọn thủ công.
3.  **Full Clone:** Upload toàn bộ (Yêu cầu băng thông và storage lớn).

## 2. Cloud Storage Provider
Hỗ trợ tích hợp các dịch vụ lưu trữ phổ biến giá rẻ để user tự cấu hình (BYOS - Bring Your Own Storage):
-   **Google Drive:** Miễn phí 15GB đầu.
-   **OneDrive:** Tích hợp sẵn trong nhiều gói Office.
-   **AWS S3 / R2 / MinIO:** Cho khách hàng Enterprise cần API.

## 3. Lợi ích khi dùng Cloud
-   **Truy cập từ xa:** Xem lại video đóng hàng tại kho ngay trên điện thoại của chủ shop khi đang đi du lịch.
-   **Chia sẻ bằng chứng:** Tạo Public Link (có thời hạn) để gửi cho Shopee/Lazada support mà không cần upload thủ công file MP4 50MB.
-   **An toàn:** Mất điện thoại/hỏng ổ cứng không mất dữ liệu.

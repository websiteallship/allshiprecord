# Quyền Riêng tư Dữ liệu (Data Privacy)

Allship Record cam kết tôn trọng quyền riêng tư tối đa theo triết lý Local-First.

## 1. Không thu thập dữ liệu (No Tracking)
-   App **KHÔNG** gửi bất kỳ dữ liệu video, hình ảnh, hay thông tin đơn hàng nào về máy chủ của chúng tôi (trừ khi bật tính năng Cloud Sync của chính user).
-   App **KHÔNG** sử dụng các tracker quảng cáo hay analytics xâm phạm (chỉ collect Crash Report ẩn danh).

## 2. Cloud Sync (User Control)
-   Nếu user chọn bật Cloud Sync: Dữ liệu được upload lên tài khoản Google Drive/S3 **của chính user**.
-   Chúng tôi không đứng giữa (No Middle-man). App kết nối trực tiếp từ Device -> Cloud Provider của user.

## 3. Quyền truy cập (Permissions)
App chỉ xin các quyền tối thiểu cần thiết:
-   `CAMERA`: Để quay video và quét mã.
-   `MICROPHONE`: Để thu âm thanh trong video (Optional - có thể tắt).
-   `STORAGE`: Để lưu video.
-   `BLUETOOTH`: Để kết nối máy quét.

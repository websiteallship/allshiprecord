# Xử lý Lỗi Camera

Camera là thành phần quan trọng nhất nhưng cũng dễ gặp sự cố nhất (đặc biệt là cáp USB lỏng, driver treo hoặc app iOS bị kill).

## 1. Mất kết nối khi ĐANG QUAY (Critical)
**Tình huống:** Đang quay ở giây thứ 15 thì Camera bị rút cáp hoặc treo.

**Quy trình Xử lý (Recovery Workflow):**
1.  **Detect:** App nhận sự kiện `onCameraError` hoặc `onDisconnect`.
2.  **Emergency Save:** Ngay lập tức finalize (đóng) file MP4 đang ghi dở.
    -   Nhờ dùng định dạng **Fragmented MP4**, 15 giây video trước đó VẪN XEM ĐƯỢC bình thường, không bị corrupt.
    -   Đánh dấu Database: `status = 'partial'`, `duration = 15s`.
3.  **Alert:**
    -   Phát âm thanh **ALARM** (còi hú) liên tục để nhân viên dừng tay.
    -   Hiện màn hình đỏ cảnh báo lỗi.
4.  **Auto Reconnect:** App tự động thử kết nối lại camera (Retry) trong nền mỗi 3 giây (tối đa 5 lần).
5.  **User Action:**
    -   Nếu kết nối lại thành công -> Hỏi user: "Quay tiếp đơn cũ hay Tạo đơn mới?".
    -   Nếu thất bại -> Yêu cầu kiểm tra dây cáp hoặc chọn camera khác.

## 2. Mất kết nối khi CHỜ (Idle)
**Tình huống:** Đang ở màn hình chờ quét mã, camera bị mất hình.

**Quy trình:**
1.  Hiện icon "Camera Disconnected" trên màn hình preview.
2.  Tự động retry kết nối lại.
3.  Vẫn cho phép Scanner hoạt động (nếu có scanner bluetooth).
4.  Nếu user quét mã trong lúc này -> App sẽ switch sang chế độ "Text Only" (chỉ ghi nhận đã đóng hàng, không có video) hoặc chặn lại tùy cấu hình Strict Mode.

## 3. Lỗi Camera bị chiếm dụng (Resource Busy)
**Tình huống:** User mở App khác (như Zalo Video Call) làm App Allship không chiếm được quyền Camera.
-   **Thông báo:** "Camera đang được sử dụng bởi ứng dụng khác."
-   **Hành động:** Hướng dẫn User đóng app kia và quay lại.

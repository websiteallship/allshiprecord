# Xử lý Lỗi Scanner

## 1. Scanner Bluetooth mất kết nối
**Tình huống:** Máy quét hết pin hoặc đi quá xa điện thoại.

**Quy trình:**
1.  **Phat hiện:** Sự kiện `BluetoothDeviceDisconnected`.
2.  **Thông báo:** Hiện Toast/Snackbar "Scanner offline".
3.  **Fallback:**
    -   Tự động kích hoạt **Camera Scan Mode** (dùng camera điện thoại để quét thay thế).
    -   Hiển thị Reticle (khung ngắm) trên màn hình camera.
4.  **Recovery:** Khi Scanner kết nối lại -> Tự động tắt Camera Scan Mode, quay về dùng Scanner vật lý.

## 2. Scanner không nhận mã (Mã mờ/rách)
**Tình huống:** Phiếu in bị mờ, nhăn hoặc máy in hết mực. Quét 3-5 lần không được.

**Quy trình:**
1.  **Phát hiện:** Không có input nào hợp lệ trong 10 giây hoặc input rác liên tục.
2.  **Gợi ý:**
    -   Hiển thị hướng dẫn: "Vuốt phẳng phiếu in", "Bật đèn Flash".
    -   Hiện nút **"Nhập tay"** to rõ ràng.
3.  **Thao tác thủ công:**
    -   User bấm "Nhập tay".
    -   Bàn phím hiện lên.
    -   User gõ mã vận đơn (chỉ cần 4-5 số cuối nếu hệ thống hỗ trợ Fuzzy Search, hoặc phải gõ full để chính xác).

## 3. Scanner gửi ký tự lạ (Encoding Issue)
**Tình huống:** Một số máy quét Trung Quốc gửi kèm ký tự lạ hoặc sai encoding.
-   **Hiện tượng:** Mã `SPX` biến thành `RZW` hoặc có thêm `[ Enter ]` ở giữa.
-   **Giải pháp:**
    -   Cho phép user vào Settings -> Calibrate Scanner.
    -   Yêu cầu quét 1 mã chuẩn.
    -   App tự động detect pattern sai và lưu rule replace (ví dụ: luôn remove ký tự đầu tiên).

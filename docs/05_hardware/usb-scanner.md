# Tích hợp Máy Quét USB

## 1. Yêu cầu phần cứng
-   Kết nối: USB-A (cho PC) hoặc qua OTG Adapter (cho Android).
-   Chế độ: USB HID Keyboard (Mặc định của hầu hết máy quét).

## 2. Tích hợp trên Android (qua OTG)
Android hỗ trợ rất tốt USB HID. Cắm là chạy (Plug & Play).
-   Hệ thống nhận diện như một Physical Keyboard.
-   App xử lý sự kiện `onKey` tương tự như Bluetooth Scanner.

## 3. Tích hợp trên Desktop (Electron)
Trên PC, máy quét USB cũng hoạt động như bàn phím. Tuy nhiên, vấn đề lớn nhất là **Focus Loss**.
-   *Vấn đề:* Nếu App bị mất focus (ví dụ user click sang Zalo/Excel), máy quét sẽ "bắn" mã vào cửa sổ Zalo/Excel đó thay vì App Allship.
-   *Giải pháp:*
    1.  **Global Keyboard Hook:** Sử dụng thư viện node native (như `iohook` hoặc `uiohook-napi`) để lắng nghe phím bấm toàn hệ thống ngay cả khi App không focus.
    2.  **Logic phân biệt:**
        -   Tính toán tốc độ gõ (WPM).
        -   Scanner bắn 10-15 ký tự trong < 50ms -> Chắc chắn là Scanner -> Capture và xử lý.
        -   Người gõ phím -> Bỏ qua.
    3.  **Always on Top (Optional):** Giữ cửa sổ App luôn ở trên cùng trong lúc đóng hàng.

## 4. Lưu ý cấu hình Scanner
Một số máy quét mặc định thêm ký tự prefix/suffix lạ. App cần có tính năng "Calibrate Scanner" (Quét thử mã mẫu) để detect xem máy quét có đang gửi thêm ký tự thừa nào không và tự động trim bỏ.

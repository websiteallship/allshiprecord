# Tích hợp Máy Quét Bluetooth (Scanner)

## 1. Yêu cầu phần cứng
-   **Chế độ kết nối:** Hỗ trợ **Bluetooth HID** (Basic Keyboard Mode).
-   **Tương thích:** Android, iOS, Windows, macOS.
-   **Ví dụ dòng máy:** Honeywell Voyager 1202g, Zebra CS3070, các dòng máy quét Trung Quốc giá rẻ (Netum, Eyoyo...).

## 2. Cơ chế hoạt động (HID Mode)
Máy quét hoạt động như một bàn phím Bluetooth.
-   Khi quét mã `ABC-123`, máy quét gửi chuỗi ký tự: `A` -> `B` -> `C` -> `-` -> `1` -> `2` -> `3` kèm theo ký tự kết thúc (thường là `Enter`).

## 3. Tích hợp trên Mobile App (Flutter)

### Vấn đề: Keyboard ảo bị ẩn (iOS)
Trên iOS, khi kết nối thiết bị Bluetooth HID, hệ điều hành mặc định ẩn bàn phím ảo (Soft Keyboard) đi vì nghĩ rằng user đang dùng bàn phím vật lý.
-   *Ảnh hưởng:* User không thể nhập tay ghi chú hoặc sửa mã nếu cần.
-   *Giải pháp:*
    -   Thiết kế UI hạn chế nhập liệu text trong lúc đang ở màn hình Scan.
    -   Cung cấp nút "Hiện bàn phím" trong App: Tạm thời ngắt kết nối scanner (hoặc dùng API `SystemChannels.textInput.invokeMethod('TextInput.show')` nếu OS cho phép) để hiện bàn phím ảo.
    -   Trên iPad: Có nút toggle bàn phím ảo trên thanh bar.

### UX Flow
1.  App lắng nghe sự kiện `RawKeyboardListener`.
2.  Bộ đệm (Buffer) gom các ký tự nhận được.
3.  Nếu nhận ký tự `Enter` (`\n` hoặc `\r`):
    -   Kiểm tra buffer.
    -   Nếu buffer match Regex mã đơn -> Xử lý (Start Recording).
    -   Clear buffer.

## 4. Hướng dẫn Pairing cho User
1.  Bật nguồn máy quét.
2.  Quét mã cấu hình "Bluetooth HID Mode" trong sách hướng dẫn của máy quét (quan trọng, vì một số máy mặc định là SPP mode).
3.  Vào Bluetooth Settings trên điện thoại -> Chọn máy quét -> Pair.
4.  Mở App Allship -> Thử quét mã test.

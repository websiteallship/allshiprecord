# Hệ thống Âm thanh Phản hồi (Audio Feedback)

Nhân viên đóng gói thường không nhìn màn hình. Âm thanh là kênh giao tiếp chính.

| Tên | Loại âm thanh | Ngữ cảnh sử dụng | Ý nghĩa với User |
|---|---|---|---|
| **Beep Start** | 1 tiếng "Beep" (Tone cao, ngắn) | Khi quét mã thành công và bắt đầu quay. | "OK, đã nhận mã. Làm việc đi." |
| **Beep Transition** | 2 tiếng "Beep-Beep" (Nhanh) | Khi đang quay đơn A mà quét mã đơn B (Continuous Mode). | "OK, đã lưu đơn cũ, chuyển sang đơn mới." |
| **Boop Error** | 1 tiếng "Boop" (Tone trầm, dài) | Khi mã quét không hợp lệ hoặc lỗi định dạng. | "Lỗi rồi, quét lại đi." |
| **Warning** | 3 tiếng "Beep-Beep-Beep" | Khi quét trùng mã đơn đang quay, hoặc bộ nhớ sắp đầy. | "Chú ý! Có vấn đề cần kiểm tra." |
| **Success Ding** | Tiếng "Ding" (Vang, trong trẻo) | Khi bấm nút "Hoàn tất" hoặc lưu video thành công thủ công. | "Xong việc." |
| **Alarm** | Tiếng còi báo động (Liên tục) | Khi Camera bị mất kết nối hoặc App bị Crash/Kill. | "DỪNG LẠI NGAY! Hệ thống hỏng." |

## Yêu cầu kỹ thuật
-   Âm thanh phải to, rõ, không bị rè.
-   Có thể tùy chỉnh âm lượng riêng cho App (độc lập với nhạc chuông điện thoại nếu được).
-   Load sẵn vào bộ nhớ (Preload) để phát ngay lập tức (Zero latency).

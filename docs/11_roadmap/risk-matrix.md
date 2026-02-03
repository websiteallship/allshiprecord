# Ma trận Rủi ro (Risk Matrix)

| Rủi ro | Tác động | Khả năng | Giải pháp (Mitigation) |
|---|---|---|---|
| **iOS kill app background** | Cao | Cao | Dùng Fragmented MP4 để không mất dữ liệu. Cảnh báo user không thoát app. Pre-recording buffer. |
| **Hết dung lượng bộ nhớ** | Cao | Cao | Auto-cleanup quyết liệt. Cảnh báo sớm. Chặn quay khi quá đầy. |
| **Android Camera phân mảnh** | TB | Cao | Dùng CameraX. Test trên các dòng máy phổ biến (Samsung, Xiaomi, Oppo). Cho phép chỉnh FPS/Resolution thấp xuống. |
| **Mất kết nối Camera/Scanner** | TB | TB | Cơ chế Auto-reconnect. Cảnh báo âm thanh (Alarm) ngay lập tức. |
| **Quét nhầm mã cũ** | Thấp | TB | Duplicate Check: Cảnh báo nếu quét trùng mã vừa mới xử lý xong. |

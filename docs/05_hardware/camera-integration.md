# Tích hợp Camera

## 1. Android Camera (Mobile)
Thị trường Android phân mảnh rất lớn (Samsung, Xiaomi, OPPO, Vivo...). API Camera gốc (`Camera2`) thường xuyên gặp vấn đề tương thích trên các dòng máy lạ hoặc giá rẻ.

### Giải pháp: CameraX
Sử dụng **CameraX** (Jetpack library của Google) làm lớp abstraction.
-   Tự động xử lý các vấn đề device-specific (xoay ảnh, hdr, flash...).
-   Hỗ trợ `PreviewUseCase`, `ImageAnalysisUseCase` (cho quét mã) và `VideoCaptureUseCase` đồng thời.

### Các vấn đề thường gặp & Khắc phục
-   **Lag Preview:** Giảm resolution preview xuống (không cần Full HD cho preview, chỉ cần 720p hoặc 480p).
-   **Nóng máy:** Giới hạn FPS preview xuống 24 hoặc 30 (không dùng 60 fps). Tắt các thuật toán làm đẹp/AI có sẵn của hãng.
-   **Mất focus:** Luôn set chế độ `Continuous Auto Focus`. Cho phép user "Tap to Focus" nếu máy lấy nét sai.

## 2. Webcam (Desktop)
Sử dụng chuẩn **WebRTC** (`navigator.mediaDevices.getUserMedia`).
-   Ưu điểm: Driver do OS quản lý, Electron chỉ việc gọi API chuẩn.
-   Hỗ trợ cắm nhiều Webcam: App cho phép chọn `deviceId` để switch giữa các camera (Cam toàn cảnh vs Cam cận cảnh).

### Vấn đề "Hot-plug"
Electron đôi khi không phát hiện webcam mới cắm vào sau khi App đã bật.
-   Giải pháp: Nút "Refresh Camera List" gọi lại `enumerateDevices()` thủ công.

## 3. IP Camera (RTSP)
Dành cho hệ thống giám sát kho lớn. App đóng vai trò như đầu ghi (NVR).
-   Protocol: RTSP (`rtsp://user:pass@192.168.1.x:554/stream`).
-   Thư viện: Sử dụng `ffmpeg` (spawn child process) để decode luồng RTSP -> Chuyển thành MJPEG hoặc HLS stream -> Hiển thị lên UI Electron.
-   *Lưu ý:* Độ trễ (Latency) của IP Camera thường cao (1-3s). Không phù hợp để quét mã nhanh (cần pre-recording buffer).

# Technology Stack Chi tiết

## 1. Mobile App (Primary MVP)
-   **Framework:** **Flutter** (Dart)
    -   *Lý do:* Render 60/120fps ổn định (Impeller engine), kiểm soát hardware (Camera/Bluetooth) tốt qua Native Channels.
-   **Camera Library:** `camera` (Official Flutter Team) + Custom Native Code (nếu cần tối ưu hardware encoding).
-   **Barcode Library:** `google_mlkit_barcode_scanning` (Sử dụng Google ML Kit on-device, tốc độ cực nhanh, support QR & Barcode).
-   **Local Database:** `sqflite` (SQLite plugin cho Flutter).
-   **State Management:** BLoC (Business Logic Component) - Tiêu chuẩn công nghiệp cho Flutter app phức tạp.

## 2. Desktop App (Phase 2)
-   **Framework:** **Electron** (JavaScript/TypeScript)
    -   *Lý do:* WebRTC mature cho camera, ecosystem Node.js khổng lồ.
-   **Camera:** WebRTC API (`navigator.mediaDevices.getUserMedia`).
-   **Video Recorder:** MediaRecorder API.
-   **Database:** `better-sqlite3` (Node.js binding trực tiếp, hiệu năng cao nhất).
-   **IP Camera:** Tích hợp `ffmpeg` hoặc `gstreamer` qua `child_process` để decode RTSP stream.

## 3. Core Technologies (Shared)

### Video Encoding
-   **Codec:** **H.264 (AVC)**
    -   *Profile:* Main Profile
    -   *Compatibility:* 100% thiết bị mobile & desktop, upload được lên mọi sàn TMĐT.
    -   *Performance:* Encoding bằng Hardware (Hardware Acceleration) cực nhanh và tiết kiệm pin trên chip ARM.
-   **Container:** **Fragmented MP4 (fMP4)**
    -   *Lợi ích:* Ghi file theo từng đoạn nhỏ. Nếu App crash hoặc mất nguồn đột ngột, file video vẫn xem được đến giây cuối cùng, không bị lỗi corrupt header như MP4 thường.

### Database
-   **Engine:** **SQLite**
-   *Đặc điểm:* Serverless, zero-configuration, transactional.
-   *Phiên bản:* SQLite 3.x

### Protocol
-   **Scanner Input:** **Human Interface Device (HID)**
    -   Hoạt động như một bàn phím vật lý.
    -   Không phụ thuộc driver hay SDK độc quyền.

# Video Processing Pipeline

Video là tài sản quan trọng nhất của hệ thống. Pipeline xử lý video được thiết kế để đảm bảo hiệu năng và độ an toàn dữ liệu.

## 1. Pipeline Diagram

```
[CAMERA SOURCE]
(Raw Frames: NV21/YUV420)
       |
       v
[RESOLUTION SCALING]
Input: Camera Max Resolution (4K, 1080p...)
Output: Target Resolution (1280x720 hoặc 1920x1080)
       |
       v
[ENCODING STAGE]
Encoder: H.264 (Hardware Acceleration)
Control: VBR (Variable Bit Rate)
FPS: 20-24
       |
       v
[MUXING STAGE]
Format: Fragmented MP4 (fMP4)
Mục tiêu: Crash resilience (chống lỗi file khi crash)
       |
       v
[FILE SYSTEM WRITE]
Path: /videos/YYYY/MM/DD/...
Buffer: Disk I/O Optimization
```

## 2. Key Parameters

### Resolution
-   **Standard:** 1280x720 (720p). Đủ rõ để đọc mã vận đơn và nhìn thấy sản phẩm. Tối ưu dung lượng.
-   **High Quality:** 1920x1080 (1080p). Dành cho seller cần bằng chứng chi tiết cao.

### Codec & Bitrate
Sử dụng **H.264** với **VBR** (Variable Bitrate).
-   **Target Bitrate:** 2 Mbps (720p) - 4 Mbps (1080p).
-   **Max Bitrate:** 4 Mbps (720p) - 8 Mbps (1080p).
-   Lý do dùng VBR: Khi khung hình tĩnh (đang dán băng keo, hoặc chờ quét đơn), bitrate tự động giảm xuống rất thấp để tiết kiệm dung lượng. Chỉ tăng lên khi có chuyển động nhanh.

### Frame Rate (FPS)
-   **20 FPS:** Đủ mượt cho mục đích bằng chứng. Không cần 30 hay 60 FPS như quay phim giải trí để tiết kiệm 30-50% dung lượng.

### Keyframe Interval (GOP)
-   **2 giây:** Giúp video dễ dàng seek (tua) và đảm bảo chất lượng file fMP4 tốt hơn.

## 3. Cơ chế bảo vệ dữ liệu (Crash Resilience)
Sử dụng **Fragmented MP4**. Video được ghi thành các chunk nhỏ (ví dụ 2 giây/chunk) liên tiếp vào file.
-   **Bình thường:** File kết thúc với `moov` atom hoàn chỉnh.
-   **Sự cố (Mất điện/Crash):** File thiếu `moov` atom cuối cùng nhưng các `moof` atom (movie fragments) trước đó vẫn hợp lệ. Phần mềm xem video hiện đại vẫn có thể phát lại phần đã được ghi mà không báo lỗi "Corrupted File".

# Risk Management - ALL SHIP ECOMBOX

## Ma Trận Rủi Ro

```
                        TÁC ĐỘNG
                 Thấp    Trung bình    Cao
            +----------+----------+----------+
    Cao     |          |    R3    | R1  R2   |  ← Cần giải quyết ngay
            |          |         |          |
XÁC SUẤT   +----------+----------+----------+
   Trung    |    R6    | R4  R5  |    R7    |  ← Cần kế hoạch mitigation
   bình     |          |         |          |
            +----------+----------+----------+
    Thấp    |    R9    |    R8   |          |  ← Monitor
            |          |         |          |
            +----------+----------+----------+
```

## Rủi Ro Theo Mức Độ

### R1: iOS Background Recording Restriction (CAO × CAO)

**Vấn đề:** iOS không cho phép app tiếp tục quay video khi chuyển background. Nhận cuộc gọi, mở notification → video dừng đột ngột.

**Mitigation:**
- Fragmented MP4: chỉ mất segment cuối (~2-5s)
- Cảnh báo: "Không chuyển app trong khi quay"
- Detect video bị interrupt → hỏi quay tiếp hay quay mới
- Gợi ý bật Do Not Disturb

### R2: Scanner Bluetooth HID ẩn bàn phím ảo iOS (CAO × CAO)

**Vấn đề:** Kết nối scanner Bluetooth HID → iOS ẩn bàn phím ảo → không nhập liệu tay được.

**Mitigation:**
- Thiết kế UI không phụ thuộc keyboard ảo
- Nút "Nhập tay": tạm disconnect Bluetooth → hiện keyboard → reconnect
- iPad: option "Show keyboard" có sẵn

### R3: Đa dạng thiết bị Android (CAO × TRUNG BÌNH)

**Vấn đề:** Camera2 API hoạt động khác nhau trên Samsung, Xiaomi, OPPO...

**Mitigation:**
- Dùng CameraX (Jetpack) thay vì Camera2 trực tiếp
- Test 15-20 model phổ biến VN (Samsung A-series, Xiaomi Redmi, OPPO A, Vivo Y)
- Fallback resolution: 720p → 640×480 → default
- Device compatibility database từ user reports

### R4: Electron USB Camera Hot-plug (TRUNG BÌNH × TRUNG BÌNH)

**Vấn đề:** `enumerateDevices()` không detect USB camera cắm sau khi app đã chạy

**Mitigation:**
- Nút "Refresh camera list" manual
- Polling `enumerateDevices()` mỗi 5s trong Settings
- Hướng dẫn cắm camera trước khi mở app

### R5: IP Camera RTSP Latency (TRUNG BÌNH × TRUNG BÌNH)

**Vấn đề:** RTSP stream có thể delay 1-3s, disconnect khi WiFi yếu

**Mitigation:**
- IP Camera phù hợp cho giám sát tổng thể, không phải per-order recording
- Ưu tiên USB webcam (latency < 100ms)
- Nếu dùng IP Camera: pre-recording buffer 3s

### R6: Fragmented MP4 Corruption (TRUNG BÌNH × THẤP)

**Vấn đề:** App crash hoặc hết pin → file MP4 corrupt

**Mitigation:**
- Fragmented MP4: chỉ mất fragment cuối
- MP4 repair routine khi app khởi động
- Android MediaMuxer, iOS AVAssetWriter hỗ trợ native

### R7: Dung Lượng Thiết Bị Mobile (TRUNG BÌNH × CAO)

**Vấn đề:** Seller 500+ đơn/ngày: 2.5GB/ngày → 75GB/tháng. Điện thoại tầm trung chỉ có 64-128GB.

**Mitigation:**
- Dashboard hiển thị rõ dung lượng
- Cảnh báo sớm khi storage < 20%
- Auto-cleanup policy configurable
- Khuyến nghị seller lớn dùng Desktop hoặc Cloud

### R8: Mã Vận Đơn Bị Mờ (THẤP × TRUNG BÌNH)

**Mitigation:**
- Luôn có option nhập tay
- Nhiều algorithm detect (ML Kit → ZXing → ZBar fallback)
- Hỗ trợ 1D barcode và QR code
- Cho phép zoom camera

### R9: Đồng Bộ Thời Gian Scanner-Camera (THẤP × THẤP)

**Mitigation:**
- Pre-recording buffer: giữ 2-3s video trong memory
- Khi nhận event quét → góp buffer vào đầu video
- Video thực tế bắt đầu trước lúc quét 2s

## Điểm Rủi Ro Theo Nền Tảng

| Platform | Camera | Scanner | Encoding | Storage | Overall |
|----------|--------|---------|----------|---------|---------|
| Android | 8/10 | 2/10 | 3/10 | 5/10 | **4.5/10** |
| iOS | 2/10 | 6/10 | 2/10 | 5/10 | **4.5/10** |
| Desktop (Electron) | 3/10 | 1/10 | 3/10 | 1/10 | **3.2/10** |

## BYOD (Bring Your Own Device) Risks

| Rủi Ro | Tác Động | Giải Pháp |
|--------|----------|-----------|
| Nhân viên nghỉ việc, video bị xóa | CAO | Sync metadata lên cloud, backup hàng tuần |
| Máy cũ, camera mờ | TRUNG BÌNH | App detect chất lượng camera, cảnh báo |
| Hết bộ nhớ vì ảnh/video cá nhân | CAO | Storage quota riêng, cảnh báo sớm |
| Nhân viên không muốn cài app | TRUNG BÌNH | App nhẹ (<30MB), không thu thập data cá nhân |
| iOS kill app nền | CAO | Fragmented MP4, audio alert khi interrupt |
| Đa dạng Android | TRUNG BÌNH | Test nhiều model, fallback resolution |

## Nguyên Tắc Xử Lý Lỗi

1. **KHÔNG BAO GIỜ block workflow vì lỗi thiết bị**
2. Luôn có fallback: Scanner mất → Camera scan → Nhập tay
3. Luôn lưu partial video, không để mất hoàn toàn
4. Audio feedback là kênh chính (nhân viên không nhìn màn hình)
5. Auto-retry với exponential backoff
6. Log lỗi để debug sau

## Decision Matrix

| Quyết định | Lựa chọn | Lý do chính |
|------------|----------|-------------|
| Mobile framework | **Flutter** | Performance camera tốt, single codebase |
| Desktop framework | **Electron** | WebRTC camera mature, multi-camera |
| Video codec | **H.264** | Tương thích 100%, encoding nhanh trên ARM |
| Storage | **Local-first** | Zero cost, không cần internet, privacy |
| Database | **SQLite** | Nhẹ, nhanh, không cần server |
| Barcode SDK | **Google ML Kit** | Free, chính xác, offline capable |
| Scanner protocol | **Bluetooth HID** | Universal, không cần SDK riêng |

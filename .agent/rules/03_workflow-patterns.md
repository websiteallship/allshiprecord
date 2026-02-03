# Workflow Patterns - ALL SHIP ECOMBOX

## Core Workflows

### 1. Đóng Hàng (Packing) - Main Flow

```
USER                          APP                          SYSTEM

  Mở app, chọn "Đóng hàng"
  --------------------------->
                              Khởi tạo camera preview
                              Khởi tạo scanner listener
                              ---------------------------->
                              <--- Camera ready -----------
  <-- Hiện camera preview ---

  ============================================================
  BƯỚC 1: QUÉT MÃ VẬN ĐƠN
  ============================================================

  Cách 1: Đưa mã vạch         Camera frame processing
  vào camera            ----> ML Kit Barcode Detection

  HOẶC
  Cách 2: Quét bằng           Nhận input từ HID keyboard
  scanner Bluetooth/USB ----> event (ẩn TextField focus)

  HOẶC
  Cách 3: Nhập tay      ----> Manual input field

                              Validate mã:
                              - Regex check format
                              - Duplicate check
                              - Length check

                              IF mã hợp lệ:
                              - Tạo record trong DB
                              - Hiển thị mã trên UI (overlay)
                              -> CHUYỂN SANG BƯỚC 2

  ============================================================
  BƯỚC 2: TỰ ĐỘNG BẮT ĐẦU QUAY VIDEO
  ============================================================

                              startRecording()
                              - Format: MP4 fragmented
                              - Path: /videos/YYYY/MM/DD/{order_code}...mp4
                              - Overlay: mã đơn + timestamp trên video
                              - Indicator: [REC]
  <-- Thấy "Đang quay" -----

  Thực hiện đóng gói          Recording continuously...
  hàng hóa trước camera       Timer hiển thị trên UI

  ============================================================
  BƯỚC 3: KẾT THÚC QUAY - 3 CÁCH
  ============================================================

  Cách A: Quét mã đơn         stopRecording(current)
  TIẾP THEO           ------> saveVideo(current)
  (Continuous mode)            startRecording(next)
                               -> Quay lại BƯỚC 1 (seamless)

  Cách B: Nhấn nút            stopRecording()
  "Hoàn tất"          ------> saveVideo()
                               -> Về màn hình chờ quét

  Cách C: Auto-timeout        IF recording_time > 300s:
  (5 phút)                     stopRecording() + saveVideo()
                               ALERT: "Video đã dừng do quá thời gian"
```

### 2. Nhận Hàng Hoàn (Return Processing)

```
USER                          APP                          SYSTEM

  Mở app, chọn "Nhận hoàn"
  --------------------------->

  ============================================================
  BƯỚC 1: QUÉT MÃ HÀNG HOÀN
  ============================================================

  Quét mã vận đơn
  (camera/scanner/nhập tay)
  --------------------------->
                              Validate + Tìm trong DB:

                              CASE 1: Tìm thấy đơn cũ (đã có video packing)
  <-- Hiện thông tin: ------  Hiển thị:
  "Đơn SPX123456789"          - Mã đơn
  "Đã đóng: 03/02 10:30"      - Ngày đóng gói gốc
  "Video đóng: 35 giây"       - Link xem video đóng gốc

                              CASE 2: Không tìm thấy (đơn mới)
  <-- "Đơn mới. Tiếp tục    Tạo record mới trong DB
       quay video?" --------

  ============================================================
  BƯỚC 2: QUAY VIDEO MỞ GÓI
  ============================================================

  Mở gói hàng hoàn             Recording...
  trước camera
  - Tình trạng bao bì
  - Sản phẩm bên trong
  - Có đúng hàng không
  - Hàng có bị hư không

  ============================================================
  BƯỚC 3: ĐÁNH GIÁ TÌNH TRẠNG (sau khi dừng quay)
  ============================================================

  Nhấn "Hoàn tất"
  --------------------------->
                              stopRecording()

                              Hiện popup đánh giá:
  <-- Chọn tình trạng: -----
  [ ] Hàng nguyên vẹn
  [ ] Hàng bị hư hỏng    ---> Gán tag vào video record
  [ ] Sai hàng / thiếu        return_status: 'damaged'
  [ ] Hàng giả / tráo

  Ghi chú: [___________] ---> notes: "Vỡ góc hộp, thiếu phụ kiện sạc"
```

## Continuous Scan Mode - State Machine

```
CONTINUOUS SCAN MODE STATE MACHINE
====================================

State: READY (chờ quét)
  |
  |-- [EVENT: Nhận mã barcode từ scanner hoặc camera]
  |
  v
State: VALIDATING
  |
  |-- Mã hợp lệ? --YES--> Tạo order record trong DB
  |                       Chuyển sang RECORDING
  |
  |-- Mã hợp lệ? --NO---> Phát âm báo "beep lỗi"
  |                       Hiện thông báo 2 giây
  |                       Quay lại READY
  v
State: RECORDING
  |
  |-- Video đang quay...
  |-- Timer hiển thị trên màn hình
  |-- Overlay: mã đơn + thời gian
  |
  |-- [EVENT: Nhận mã barcode MỚI (mã khác)]
  |     |
  |     v
  |   TRANSITION (<500ms):
  |     1. stopRecording(video_hiện_tại)
  |     2. saveToFile() + generateThumbnail() [background]
  |     3. updateDatabase() [background]
  |     4. startRecording(video_mới) với mã mới
  |     5. Phát âm "beep thành công"
  |     --> Vẫn ở state RECORDING nhưng cho đơn mới
  |
  |-- [EVENT: Nhận CÙNG mã barcode (trùng lặp)]
  |     |
  |     v
  |   Phát âm cảnh báo "đã quét rồi"
  |   Tiếp tục recording, không làm gì
  |
  |-- [EVENT: Nhấn nút "Dừng"]
  |     |
  |     v
  |   stopRecording() + save + về READY
  |
  |-- [EVENT: Timeout 5 phút]
  |     |
  |     v
  |   stopRecording() + save
  |   Hiện cảnh báo "Video đã tự động dừng"
  |   Về READY
```

## Audio Feedback System

Nhân viên đóng gói thường **KHÔNG NHÌN màn hình** khi làm việc. Âm thanh là kênh phản hồi chính.

| Âm Thanh | Ý Nghĩa | Khi Nào |
|----------|---------|---------|
| "Beep" ngắn (cao) | Quét thành công, bắt đầu quay | Khi nhận mã hợp lệ |
| "Beep beep" (2 tiếng) | Dừng video cũ, bắt đầu mới | Khi quét mã mới (continuous) |
| "Boop" trầm (thấp) | Lỗi - mã không hợp lệ | Khi mã sai format |
| "Beep beep beep" (3) | Cảnh báo - mã trùng lặp | Khi quét cùng mã |
| "Ding" (trong) | Đã lưu thành công | Khi nhấn Dừng |
| "Alarm" (liên tục) | Lỗi nghiêm trọng | Camera mất kết nối |
| Im lặng | Đang quay bình thường | Trong quá trình quay |

## Error Handling Patterns

### Camera Disconnect During Recording

```
Timeline:
  t=0    Đang quay video cho đơn SPX123
  t=15s  Camera bị ngắt (rút USB, Bluetooth mất, app bị iOS kill)
         |
         v
  [PHÁT HIỆN] (trong 500ms)
  App nhận event onCameraError / onDeviceDisconnected
         |
         v
  [XỬ LÝ NGAY LẬP TỨC]
  1. Lưu phần video đã quay (0-15 giây) -- KHÔNG ĐƯỢC MẤT DATA
     -> Finalize MP4 fragment đã có trong buffer
     -> Đánh dấu trong DB: status = 'partial', duration = 15s
  2. Phát âm ALARM
  3. Hiện thông báo toàn màn hình:
     ┌─────────────────────────────────────┐
     │   ⚠ CAMERA BỊ NGẮT KẾT NỐI         │
     │                                     │
     │   Đơn SPX123: Đã lưu 15 giây video  │
     │   (video không đầy đủ)              │
     │                                     │
     │   [Kết nối lại]  [Quay mới]  [Bỏ qua]│
     └─────────────────────────────────────┘
  4. Tự động thử kết nối lại camera mỗi 3 giây (tối đa 5 lần)
```

### Scanner Bluetooth Disconnect

```
[PHÁT HIỆN] (trong 1-2 giây)
Bluetooth HID device disconnected event
       |
       v
[XỬ LÝ]
1. Hiện icon "Scanner offline" trên status bar
2. TỰ ĐỘNG chuyển sang CAMERA SCAN MODE (dùng camera để quét mã)
3. Background: thử kết nối lại scanner mỗi 5 giây
       |
       v
[KHI SCANNER KẾT NỐI LẠI]
-> Hiện: "Scanner đã kết nối lại"
-> Tự động chuyển về Scanner mode
-> Tắt camera scan mode

NGUYÊN TẮC: Không bao giờ block workflow vì mất scanner.
Luôn có fallback sang camera scan hoặc nhập tay.
```

### Error Recovery Priority

| Lỗi | Mức Độ | Fallback | Auto Retry |
|-----|--------|----------|------------|
| Camera disconnect | Cao | Lưu video partial | Có (5 lần) |
| Camera bị app khác | Trung | Chờ tắt app kia | Có (foreground) |
| Scanner Bluetooth mất | Trung | Camera scan mode | Có (mỗi 5s) |
| Scanner USB không nhận | Thấp | Check focus + test | Manual |
| Mã bị mờ/hỏng | Thấp | Nhập tay | Không |
| Hết bộ nhớ thiết bị | Cao | Cảnh báo + auto clean | Không |

## Hands-Free Operation Models

### Model A: FULL HANDS-FREE (> 100 đơn/ngày)

```
Thiết bị: Scanner Bluetooth có giá đỡ + Camera cố định (webcam/IP cam)

    Nhân viên cầm đơn hàng
           |
           v
    Quét mã vận đơn qua scanner trên giá đỡ
    (chỉ cần đưa mã vạch qua scanner, không cần cầm scanner)
           |
           v
    [APP TỰ ĐỘNG] Bắt đầu quay video <-- KHÔNG CẦN CHẠM MÀN HÌNH
           |
           v
    Nhân viên đóng gói hàng trước camera
           |
           v
    Quét mã đơn TIẾP THEO
           |
           v
    [APP TỰ ĐỘNG] Dừng video cũ + Lưu + Bắt đầu video mới

    Tổng thao tác chạm màn hình: 0
```

### Model B: MINIMAL TOUCH (Điện thoại cá nhân)

```
Thiết bị: Điện thoại cá nhân, camera trước/sau

    Mở app -> Chọn "Đóng hàng" (1 tap)
           |
           v
    Quét mã bằng camera điện thoại
    (đưa phiếu gửi hàng vào camera)
           |
           v
    [APP TỰ ĐỘNG] Nhận diện mã -> Bắt đầu quay <-- KHÔNG CẦN TAP
           |
           v
    Đóng gói hàng trước camera
           |
           v
    Quét mã đơn TIẾP THEO (đưa phiếu tiếp theo vào camera)
           |
           v
    [APP TỰ ĐỘNG] Dừng + Lưu + Quay video mới

    Tổng thao tác chạm màn hình: 1 (chỉ lần đầu mở app)
```

### Model C: MANUAL (< 20 đơn/ngày)

```
    Mở app -> Chọn "Đóng hàng"
           |
           v
    Nhập tay mã vận đơn hoặc quét
           |
           v
    Nhấn nút "Bắt đầu quay"
           |
           v
    Đóng gói hàng
           |
           v
    Nhấn nút "Dừng & Lưu"

    Tổng thao tác: 3-4 tap
```

## Performance Targets

| Metric | Target | Critical |
|--------|--------|----------|
| Scan to Record Start | < 500ms | < 1000ms |
| Video Transition (continuous) | < 500ms | < 1000ms |
| Thumbnail Generation | < 1s | < 2s |
| SQLite Query (by order_code) | < 1ms | < 10ms |
| App Cold Start | < 3s | < 5s |
| Video Save | < 2s | < 5s |

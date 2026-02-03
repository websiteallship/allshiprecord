# BAO CAO TU VAN KIEN TRUC GIAI PHAP
## Ung dung quay video dong goi & doi soat don hang TMDT

**Vai tro:** Senior Solution Architect - Logistics & E-commerce
**Pham vi:** Phan tich ky thuat, Kien truc he thong, Workflow, Rui ro
**Ngay:** 2026-02-03

---

## MUC LUC

1. Phan tich ky thuat & Tech Stack
2. Kien truc he thong - Local vs Cloud
3. Logic & Workflow chi tiet
4. Tinh kha thi & Rui ro
5. Khuyen nghi tong the

---

## 1. PHAN TICH KY THUAT & TECH STACK

### 1.1 Danh gia Framework da nen tang

Danh gia dua tren yeu cau cot loi:
camera control + barcode scan + video encoding + ket noi phan cung ngoai vi.

#### Phuong an A: Flutter (Android + iOS + Desktop)

```
Uu diem:
  - Single codebase cho ca mobile va desktop
  - Impeller engine cho 60/120 FPS on dinh
  - Flutter Desktop ho tro Windows/macOS/Linux
  - Native bridge de viet hon React Native cho hardware APIs
  - Community lon, plugin camera mature

Nhuoc diem:
  - Camera plugin cho Desktop van chua mature bang mobile
  - Can viet platform channel rieng cho USB device tren desktop
  - File size app lon hon native (~15-20MB)
```

#### Phuong an B: React Native (Mobile) + Electron (Desktop)

```
Uu diem:
  - react-native-vision-camera: QUET MA + QUAY VIDEO dong thoi
    (1 thu vien lam ca 2 viec)
  - Electron: camera access qua Chromium WebRTC - cuc ky on dinh
  - Share logic layer bang JavaScript giua mobile va desktop
  - Electron co san desktopCapturer, getUserMedia out-of-the-box

Nhuoc diem:
  - Hai codebase rieng biet (React Native + Electron)
  - Electron rat nang (~150-300MB RAM, app size >100MB)
  - React Native performance kem hon Flutter duoi tai nang
    (benchmark: Flutter 60fps on dinh, RN drop 45-50fps khi render phuc tap)
  - Hermes engine cai thien startup nhung khong giai quyet camera overhead
```

#### Phuong an C: Native (Kotlin/Swift) + Desktop rieng

```
Uu diem:
  - Performance tot nhat, memory thap nhat
  - Full control hardware: camera, USB, Bluetooth
  - App size nho nhat

Nhuoc diem:
  - 3 codebase rieng: Android (Kotlin), iOS (Swift), Desktop (C#/.NET hoac Electron)
  - Chi phi phat trien cao nhat (x3 nhan luc)
  - Thoi gian ra mat lau nhat
```

#### KHUYEN NGHI: Hybrid Approach

```
KIEN TRUC DE XUAT
==================

MOBILE (Phase 1 - Uu tien)
  - Framework: Flutter
  - Camera: camera package + google_mlkit_barcode
  - Video: native MediaCodec (Android) / AVAssetWriter (iOS) qua platform channel
  - Scanner ngoai: Bluetooth HID qua TextField focus
  - Database: SQLite (sqflite package)

DESKTOP (Phase 2)
  - Framework: Electron
    (Ly do: camera WebRTC mature, multi-camera on dinh, MediaRecorder API co san)
  - Camera: getUserMedia + MediaRecorder
  - Scanner: Keyboard event listener (USB HID)
  - IP Camera: FFmpeg decode RTSP stream
  - Database: better-sqlite3 (Node.js)

SHARED LAYER
  - Business logic: Dart (mobile) / JS (desktop)
  - DB schema: dong nhat giua 2 nen tang
  - Video naming convention: thong nhat
```

**Ly do chon Flutter cho mobile thay vi React Native:**
- Yeu cau chinh la video recording + barcode scan. Flutter xu ly camera pipeline
  native hon, performance on dinh hon duoi tai
- react-native-vision-camera tuy scan+record cung luc nhung frame processing
  callback chay tren JS thread, co risk drop frame tren thiet bi cau hinh thap
- Flutter platform channel cho phep goi thang MediaCodec/AVAssetWriter,
  bypass hoan toan overhead framework

**Ly do chon Electron cho desktop thay vi Flutter Desktop:**
- Flutter Desktop camera support chua mature (thieu multi-camera, thieu USB camera hot-plug)
- Electron bundled Chromium = WebRTC camera hoat dong giong het Chrome browser
- FFmpeg integration qua Node.js child_process cho IP Camera RTSP decode

### 1.2 Video Processing Pipeline

```
VIDEO ENCODING PIPELINE
========================

Camera Stream (raw frames)
         |
         v
[Resolution Scaling]
  Input: Camera max
  Output: 1280x720 (hoac 1920x1080)
         |
         v
[Encoding Stage]
  Codec: H.264 (Main Profile)     <--- UU TIEN H.264, KHONG PHAI H.265
  Rate: VBR
  Target: 2-4 Mbps
  FPS: 20
  Keyframe interval: 2 giay

  Encoder Selection:
  - Mobile: Hardware MediaCodec (Android) / VideoToolbox (iOS)
  - Desktop: Hardware NVENC / QSV / AMF, fallback: libx264
         |
         v
[Container: Fragmented MP4]
  (khong mat data neu app crash giua chung)
         |
         v
  Local File System
```

#### Tai sao H.264 thay vi H.265 cho mobile?

Day la diem phan bac lai quan diem pho bien "H.265 tot hon":

| Tieu chi | H.264 | H.265 |
|---|---|---|
| **Encoding speed (ARM)** | Nhanh, toi uu tot cho ARM | **Cham gap 10-20 lan** tren ARM do thieu NEON optimization |
| **Hardware encoder support** | Moi thiet bi tu 2013+ | Chi thiet bi tu 2017+ |
| **Battery consumption** | Thap (hardware encode) | Cao hon 30-50% |
| **Playback compatibility** | Moi noi | Mot so browser/player cu khong ho tro |
| **File size (1080p, 20fps, VBR)** | ~8-12 MB/phut | ~4-6 MB/phut |
| **Upload len san TMDT** | 100% tuong thich | Mot so san chua accept |

**Ket luan:** Voi muc dich quay video dong goi (30-60 giay/video, can real-time,
chay tren da dang thiet bi), H.264 la lua chon an toan va thuc te hon.
Tiet kiem 50% dung luong cua H.265 khong dang voi rui ro compatibility va battery drain.

#### Thong so encoding khuyen nghi

```
PROFILE: "STANDARD" (mac dinh cho seller nho)
  - Resolution: 1280x720 (720p)
  - FPS: 20
  - Codec: H.264 Main Profile
  - Bitrate: VBR, target 2 Mbps, max 4 Mbps
  - Keyframe interval: 2 giay
  - Audio: AAC 64kbps mono
  - Ket qua: ~4-6 MB / 30 giay video

PROFILE: "HIGH QUALITY" (cho seller can bang chung chi tiet)
  - Resolution: 1920x1080 (1080p)
  - FPS: 24
  - Codec: H.264 High Profile
  - Bitrate: VBR, target 4 Mbps, max 8 Mbps
  - Keyframe interval: 2 giay
  - Audio: AAC 128kbps stereo
  - Ket qua: ~8-12 MB / 30 giay video
```

---

## 2. KIEN TRUC HE THONG - LOCAL vs CLOUD

### 2.1 Phan tich chi tiet 3 mo hinh

#### Mo hinh A: Pure Local Storage

```
[THIET BI NGUOI DUNG]
  Camera Module ---> App Engine ---> Local Storage
  Scanner Module     (Encoder)       /videos/
                     (SQLite)        /thumbs/
                                     /db/orders.db

Uu diem:                          Nhuoc diem:
  Chi phi = 0 (khong server)        Mat dien thoai = mat data
  Khong can internet                Khong truy xuat tu thiet bi khac
  Privacy tuyet doi                 Gioi han boi bo nho thiet bi
  Toc do truy xuat nhanh nhat       Khong backup tu dong
  Phu hop seller < 100 don/ngay     Kho scale khi co nhieu nhan vien
```

#### Mo hinh B: Pure Cloud Storage

```
[THIET BI]              [CLOUD SERVER]
  App (thin client) <--->  API Server
                           Object Storage (S3/GCS)
                           Database (PostgreSQL)

Uu diem:                          Nhuoc diem:
  Truy xuat tu bat ky dau          Chi phi server + storage hang thang
  Khong so mat data                Phu thuoc internet
  Multi-device, multi-user         Upload video ton bandwidth
  De scale                         Latency khi xem video
                                   Privacy concern
```

**Uoc tinh chi phi cloud cho 1 seller (300 don/ngay):**
```
Video storage: 300 don x 5MB x 30 ngay      = 45 GB/thang
S3 storage:    45 GB x $0.023/GB             = ~$1.04/thang
S3 transfer:   Upload mien phi, 10GB download = ~$0.90/thang
API Server:    t3.micro (shared)              = ~$3-5/thang
Database:      RDS PostgreSQL (shared)        = ~$5-10/thang
──────────────────────────────────────────────────────
Tong chi phi cho 1 seller:                    = ~$3-5/thang (~75-125K VND)
```

#### Mo hinh C: LOCAL-FIRST + OPTIONAL CLOUD SYNC (Khuyen nghi)

```
[THIET BI NGUOI DUNG]
  Camera + Scanner ---> App Engine ---> Local Storage (PRIMARY)
                          |               SQLite DB
                          |               Video Files
                          |               Thumbnails
                          |
                          v
                        Sync Engine (background, WiFi-only, optional)
                          |
                          v
                      [CLOUD (OPTIONAL)]
                        Tier 1: Metadata only (FREE)
                          - Sync order records
                          - Cross-device search
                        Tier 2: Metadata + Video ($)
                          - Full video backup
                          - CDN delivery
                          - Share link cho san TMDT
```

**Day la mo hinh khuyen nghi vi:**
1. **Seller nho (0 dong):** Dung pure local, khong can dang ky, khong can internet
2. **Seller vua (tier 1):** Sync metadata de tra cuu tu nhieu thiet bi
3. **Seller lon (tier 2):** Full cloud backup, chia se video cho san TMDT
4. **Monetization ro rang:** Free -> Paid tu nhien khi seller scale len

### 2.2 Database Schema (SQLite - Local)

```sql
-- BANG CHINH --

CREATE TABLE orders (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  order_code         TEXT NOT NULL,           -- ma van don (unique index)
  marketplace        TEXT,                    -- shopee/tiktok/lazada/tiki/other
  created_at         DATETIME DEFAULT CURRENT_TIMESTAMP,
  notes              TEXT
);

CREATE TABLE videos (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id           INTEGER REFERENCES orders(id),
  type               TEXT NOT NULL,           -- 'packing' | 'shipping' | 'return'
  file_path          TEXT NOT NULL,           -- relative path
  file_size_bytes    INTEGER,
  duration_ms        INTEGER,
  resolution         TEXT,                    -- '1280x720'
  codec              TEXT,                    -- 'h264'
  thumbnail_path     TEXT,
  recorded_at        DATETIME,
  device_name        TEXT,
  camera_source      TEXT,                    -- 'rear' | 'front' | 'webcam_0'
  synced_to_cloud    BOOLEAN DEFAULT 0,
  cloud_url          TEXT,
  return_status      TEXT,                    -- 'intact' | 'damaged' | 'wrong_item'
  notes              TEXT
);

-- INDEX --

CREATE UNIQUE INDEX idx_order_code ON orders(order_code);
CREATE INDEX idx_video_type ON videos(type);
CREATE INDEX idx_recorded_at ON videos(recorded_at);
CREATE INDEX idx_synced ON videos(synced_to_cloud);

-- QUERY PATTERNS --

-- Tra cuu video theo ma don (use case chinh, < 1ms voi index):
SELECT v.* FROM videos v
JOIN orders o ON v.order_id = o.id
WHERE o.order_code = 'SPX123456789';

-- Thong ke dung luong theo ngay:
SELECT DATE(recorded_at) as day,
       COUNT(*) as video_count,
       SUM(file_size_bytes) as total_bytes
FROM videos
GROUP BY DATE(recorded_at)
ORDER BY day DESC;

-- Tim video chua sync (cho cloud sync):
SELECT * FROM videos WHERE synced_to_cloud = 0
ORDER BY recorded_at ASC LIMIT 50;
```

### 2.3 Chien luoc quan ly dung luong

```
STORAGE MANAGEMENT STRATEGY
=============================

Cau hinh nguoi dung:
  max_storage_gb: 50 (default, configurable)
  retention_days: 90 (default, configurable)
  auto_cleanup: true

Logic cleanup (chay daily hoac khi dung luong > 80% max):

  IF total_video_size > max_storage_gb * 0.8:

    Buoc 1: Xoa video da sync len cloud + qua retention_days

    Buoc 2: Neu van thieu -> Xoa video chua sync nhung qua retention_days
            (CANH BAO user truoc khi xoa)

    Buoc 3: Neu van thieu -> Nen video cu xuong 480p
            (giu lai video nhung giam chat luong)

    Buoc 4: Neu van thieu -> Thong bao user can giai phong bo nho

  QUAN TRONG: KHONG BAO GIO tu dong xoa video co tag "dispute"
  (video dang dung cho khieu nai phai duoc protect vinh vien
   cho den khi user chu dong xoa)
```

---

## 3. LOGIC & WORKFLOW CHI TIET

### 3.1 User Flow: DONG HANG DI (Packing & Shipping)

```
USER                          APP                          SYSTEM

  Mo app, chon "Dong hang"
  --------------------------->
                              Khoi tao camera preview
                              Khoi tao scanner listener
                              ---------------------------->
                              <--- Camera ready -----------
  <-- Hien camera preview ---

  ============================================================
  BUOC 1: QUET MA VAN DON
  ============================================================

  Cach 1: Dua ma vach         Camera frame processing
  vao camera            ----> ML Kit Barcode Detection
                              ---------------------------->
  HOAC
  Cach 2: Quet bang           Nhan input tu HID keyboard
  scanner Bluetooth/USB ----> event (an TextField focus)

  HOAC
  Cach 3: Nhap tay      ----> Manual input field

                              Validate ma:
                              - Regex check format
                              - Duplicate check
                              - Length check

                              IF ma khong hop le:
  <-- Canh bao, retry ------  Hien thong bao loi

                              IF ma hop le:
                              - Tao record trong DB
                              - Hien thi ma tren UI (overlay)
                              -> CHUYEN SANG BUOC 2

  ============================================================
  BUOC 2: TU DONG BAT DAU QUAY VIDEO
  ============================================================

                              startRecording()
                              - Format: MP4 fragmented
                              - Path: /videos/YYYY/MM/DD/{order_code}...mp4
                              - Overlay: ma don + timestamp tren video
                              - Indicator: [REC]
                              ---------------------------->
  <-- Thay "Dang quay" -----

  Thuc hien dong goi          Recording continuously...
  hang hoa truoc camera       Timer hien thi tren UI

  ============================================================
  BUOC 3: KET THUC QUAY - 3 CACH
  ============================================================

  Cach A: Quet ma don         stopRecording(current)
  TIEP THEO           ------> saveVideo(current)
  (Continuous mode)            startRecording(next)
                               -> Quay lai BUOC 1 (seamless)

  Cach B: Nhan nut            stopRecording()
  "Hoan tat"          ------> saveVideo()
                               -> Ve man hinh cho quet

  Cach C: Auto-timeout        IF recording_time > 300s:
  (5 phut)                     stopRecording() + saveVideo()
                               ALERT: "Video da dung do qua thoi gian"

  ============================================================
  BUOC 4: POST-PROCESSING (Background)
  ============================================================

                              Background tasks:
                              - Finalize MP4 container
                              - Generate thumbnail (frame giay thu 2)
                              - Cap nhat SQLite
                              - Tinh dung luong con lai
                              - Queue cloud sync (neu co cau hinh)
                              ---------------------------->

  <-- "Da luu" -------------
      Hien thumbnail nho
      + thoi luong video
```

**Luu y quan trong ve Continuous Mode:**
Day la mode su dung nhieu nhat trong thuc te. Flow can seamless:
quet ma moi = tu dong ket thuc video cu + bat dau video moi,
khong co delay hoac buoc xac nhan nao o giua.
Thoi gian transition: stopRecording -> startRecording < 500ms.

### 3.2 User Flow: NHAN HANG HOAN VE (Return Processing)

```
USER                          APP                          SYSTEM

  Mo app, chon "Nhan hoan"
  --------------------------->
                              Khoi tao camera preview
                              Mode: RETURN
                              ---------------------------->

  ============================================================
  BUOC 1: QUET MA HANG HOAN
  ============================================================

  Quet ma van don
  (camera/scanner/nhap tay)
  --------------------------->
                              Validate + Tim trong DB:

                              CASE 1: Tim thay don cu (da co video packing)
  <-- Hien thong tin: ------  Hien thi:
  "Don SPX123456789"          - Ma don
  "Da dong: 03/02 10:30"      - Ngay dong goi goc
  "Video dong: 35 giay"       - Link xem video dong goc

                              CASE 2: Khong tim thay (don moi)
  <-- "Don moi. Tiep tuc    Tao record moi trong DB
       quay video?" --------

  ============================================================
  BUOC 2: QUAY VIDEO MO GOI
  ============================================================

                              startRecording()
                              type: 'return'
                              Overlay: ma don + "HOAN TRA" + timestamp
                              ---------------------------->

  Mo goi hang hoan             Recording...
  truoc camera
  - Tinh trang bao bi
  - San pham ben trong
  - Co dung hang khong
  - Hang co bi hu khong

  ============================================================
  BUOC 3: DANH GIA TINH TRANG (sau khi dung quay)
  ============================================================

  Nhan "Hoan tat"
  --------------------------->
                              stopRecording()

                              Hien popup danh gia:
  <-- Chon tinh trang: -----
  [ ] Hang nguyen ven
  [ ] Hang bi hu hong    ---> Gan tag vao video record
  [ ] Sai hang / thieu        return_status: 'damaged'
  [ ] Hang gia / trao

  Ghi chu: [___________] ---> notes: "Vo goc hop, thieu phu kien sac"

  ============================================================
  BUOC 4: LUU TRU & LIEN KET
  ============================================================

                              Luu video return
                              Lien ket voi video packing goc (neu co)

                              Record trong DB:
                              videos: {
                                order_id: 123,
                                type: 'return',
                                return_status: 'damaged',
                                notes: "Vo goc hop..."
                              }
                              ---------------------------->

  <-- "Da luu" -------------
  Hien tom tat:
  - Video dong goi goc
  - Video mo hoan tra
  - Tinh trang: Hu hong
  - [Xuat bao cao] --------> Tao PDF/anh tom tat
  - [Chia se]                 cho khieu nai san TMDT
```

**Diem khac biet quan trong so voi flow dong hang:**
1. **Lookup nguoc:** Quet ma hoan -> tim video dong goi goc de so sanh
2. **Tagging tinh trang:** Bat buoc danh gia tinh trang hang
3. **Khong co continuous mode:** Moi don hoan can xu ly can than
4. **Export evidence:** Xuat "bo bang chung" gom ca video dong + video hoan + metadata

### 3.3 State Machine tong the

```
                    APP STATES
                    ==========

                    [IDLE]
                       |
              +--------+--------+
              v        v        v
          [PACKING] [SEARCH] [RETURN]
          [MODE   ] [MODE  ] [MODE  ]
              |        |        |
              v        |        v
          [SCANNING]   |   [SCANNING]
          (cho ma)     |   (cho ma)
              |        |        |
              v        |        v
          [RECORDING]  |   [RECORDING]
          (dang quay)  |   (dang quay)
              |        |        |
              v        |        v
          [SAVING]     |   [TAGGING]  <-- Danh gia tinh trang
          (luu video)  |   (gan tag + luu)
              |        |        |
              v        v        v
                  [COMPLETED]
              (hien ket qua, quay lai
               IDLE hoac tiep tuc SCANNING)
```

---

## 4. TINH KHA THI & RUI RO

### 4.1 Ma tran rui ro ky thuat

```
                        TAC DONG
                 Thap    Trung binh    Cao
            +----------+----------+----------+
    Cao     |          |    R3    | R1  R2   |  <-- Can giai quyet ngay
            |          |         |          |
XAC SUAT   +----------+----------+----------+
  Trung     |    R6    | R4  R5  |    R7    |  <-- Can ke hoach mitigation
  binh      |          |         |          |
            +----------+----------+----------+
    Thap    |    R9    |    R8   |          |  <-- Monitor
            |          |         |          |
            +----------+----------+----------+
```

#### R1: iOS Background Recording Restriction (Cao x Cao)

**Van de:** iOS khong cho phep app tiep tuc quay video khi app chuyen sang background.
Neu user nhan cuoc goi, mo notification, hoac chuyen app -> video bi dung dot ngot.

**Mitigation:**
- Su dung fragmented MP4: video ghi theo segment 2-5 giay.
  Neu bi interrupt, chi mat segment cuoi cung
- Hien canh bao: "Khong chuyen app trong khi quay"
- Khi app quay lai foreground, detect video bi interrupt
  -> hoi user quay tiep hay quay video moi
- Dat che do Do Not Disturb suggestion

#### R2: Scanner Bluetooth HID tren iOS an ban phim ao (Cao x Cao)

**Van de:** Khi ket noi scanner Bluetooth HID, iOS an ban phim ao tren iPhone.
User khong the nhap lieu bang tay.

**Mitigation:**
- Thiet ke UI khong phu thuoc vao ban phim ao
- Nut "Nhap tay" se tam disconnect Bluetooth -> hien keyboard -> nhap -> reconnect
- Tren iPad: su dung option "Show keyboard" co san
- Ghi ro trong huong dan su dung

#### R3: Da dang thiet bi Android (Cao x Trung binh)

**Van de:** Hang nghin model Android voi camera behavior khac nhau.
Camera2 API hoat dong khac tren Samsung, Xiaomi, OPPO, v.v.

**Mitigation:**
- Su dung CameraX (Android Jetpack) thay vi Camera2 truc tiep
- Test tren 15-20 model pho bien o VN (Samsung A-series, Xiaomi Redmi, OPPO A, Vivo Y)
- Fallback resolution: 720p -> 640x480 -> default
- Build device compatibility database tu user reports

#### R4: Multi-camera tren Electron - USB hot-plug (Trung binh x Trung binh)

**Van de:** Electron enumerateDevices() co known bug: khong luon detect
USB camera duoc cam vao sau khi app da chay.

**Mitigation:**
- Them nut "Refresh camera list" manual
- Polling enumerateDevices() moi 5 giay khi o Settings
- Huong dan user cam camera truoc khi mo app
- Theo doi Electron issue #14743

#### R5: IP Camera (RTSP) latency va stability (Trung binh x Trung binh)

**Van de:** RTSP stream co the bi delay 1-3 giay, disconnect khi WiFi yeu.

**Mitigation:**
- IP Camera phu hop cho "giam sat tong the" hon recording per-order
- Voi per-order recording: uu tien USB webcam (latency < 100ms)
- Neu buoc dung IP Camera: pre-recording buffer 3 giay truoc khi quet ma
- Su dung GStreamer hoac FFmpeg cho RTSP decode

#### R6: Fragmented MP4 corruption khi app crash (Trung binh x Thap)

**Van de:** App crash hoac het pin trong luc quay, file MP4 co the corrupt.

**Mitigation:**
- Fragmented MP4: chi mat fragment cuoi
- MP4 repair routine khi app khoi dong
- Android: MediaMuxer voi MUXER_OUTPUT_MPEG_4 ho tro fMP4
- iOS: AVAssetWriter tu quan ly fragment

#### R7: Dung luong bo nho dien thoai voi seller lon (Trung binh x Cao)

**Van de:** Seller 500+ don/ngay: 2.5GB/ngay -> 75GB/thang.
Nhieu dien thoai tam trung VN chi co 64-128GB tong.

**Mitigation:**
- Dashboard hien ro: "Dung luong da dung: 12GB / Con trong: 25GB"
- Canh bao som khi storage < 20%
- Auto-cleanup policy configurable
- Khuyen nghi seller lon dung desktop hoac cloud storage
- Tuy chon giam quality tu dong khi storage thap

#### R8: Ma van don bi mo/nhan kho quet (Thap x Trung binh)

**Mitigation:**
- Luon co option nhap tay
- Tang scan tolerance: nhieu algorithm detect (ZXing -> ML Kit -> ZBar fallback)
- Ho tro ca 1D barcode va QR code
- Cho phep zoom camera khi scan

#### R9: Dong bo thoi gian giua scanner va camera (Thap x Thap)

**Mitigation:**
- Pre-recording buffer: app giu 2-3 giay video trong memory buffer.
  Khi nhan event quet -> gop buffer vao dau video.
  Video thuc te bat dau truoc luc quet 2 giay.

### 4.2 Tong ket rui ro theo nen tang

```
MOBILE (Android)
  Camera compatibility    8/10  - rat nhieu thiet bi
  Scanner Bluetooth       2/10  - HID mature
  Video encoding          3/10  - MediaCodec on
  Storage management      5/10  - bo nho han che
  Overall                 4.5/10

MOBILE (iOS)
  Camera compatibility    2/10  - it thiet bi
  Background restriction  8/10  - iOS strict
  Scanner Bluetooth       6/10  - an keyboard
  Video encoding          2/10  - VideoToolbox tot
  Overall                 4.5/10

DESKTOP (Electron)
  Camera/Webcam           3/10  - WebRTC mature
  Multi-camera            5/10  - hot-plug issue
  IP Camera RTSP          6/10  - can FFmpeg
  USB Scanner             1/10  - keyboard HID
  Storage management      1/10  - o cung lon
  Overall                 3.2/10
```

---

## 5. KHUYEN NGHI TONG THE

### 5.1 Chien luoc phat trien

```
PHASE 1 (MVP - Ra mat nhanh)
==============================
Target: Android app
Scope:
  - Quet ma bang camera dien thoai (ML Kit)
  - Quay video H.264, 720p, luu local
  - Tra cuu video theo ma don
  - SQLite database
  - Basic storage management
Tech: Flutter (Android only build)
Goal: Validate product-market fit


PHASE 2 (Mo rong nen tang)
==============================
Target: iOS + Bluetooth scanner
Scope:
  - iOS build tu cung Flutter codebase
  - Ket noi scanner Bluetooth HID
  - Continuous mode (quet lien tuc)
  - Return flow voi tagging
  - Export/share video
Tech: Flutter (iOS build) + Bluetooth HID integration


PHASE 3 (Desktop + Hardware)
==============================
Target: Windows/macOS desktop
Scope:
  - Electron app voi webcam support
  - Multi-camera management
  - USB scanner support
  - IP Camera RTSP (basic)
  - Cross-device search (metadata sync)
Tech: Electron + FFmpeg + better-sqlite3


PHASE 4 (Cloud + Scale)
==============================
Target: Seller lon, team nhieu nguoi
Scope:
  - Cloud backup (S3/GCS)
  - Multi-user, phan quyen
  - Dashboard analytics
  - API integration san TMDT
  - Share link video cho khieu nai
Tech: Cloud API (Node.js/Go) + PostgreSQL + S3
```

### 5.2 Decision Matrix tom tat

| Quyet dinh | Lua chon | Ly do chinh |
|---|---|---|
| Mobile framework | **Flutter** | Performance camera tot, single codebase Android+iOS |
| Desktop framework | **Electron** | Camera WebRTC mature, multi-camera on dinh |
| Video codec | **H.264** | Tuong thich 100%, encoding nhanh tren ARM |
| Storage mac dinh | **Local-first** | Zero cost, khong can internet, privacy |
| Database | **SQLite** | Nhe, nhanh, khong can server |
| Barcode SDK | **Google ML Kit** | Free, chinh xac, offline capable |
| Scanner protocol | **Bluetooth HID** | Universal, khong can SDK rieng |

---

> Ngay tao: 2026-02-03
> Phien phan tich: Solution Architecture Report

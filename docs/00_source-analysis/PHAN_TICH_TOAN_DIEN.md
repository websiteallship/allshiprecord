# Phan tich toan dien: Tool quay video dong hang & Quan ly don hang

---

## 1. Phan tich thi truong & Doi thu

### 1.1 Tong quan thi truong

Thi truong Viet Nam hien co nhieu giai phap tuong tu, tap trung vao viec
quay video dong goi de doi soat khieu nai voi san TMDT va don vi van chuyen.

### 1.2 Bang so sanh doi thu

| San pham | Dac diem | Gia | Nen tang |
|---|---|---|---|
| **Ecombox** (ecombox.vn) | App + Desktop + Hub phan cung, AI phat hien loi, cloud storage | 3 goi (Basic/Premium/Enterprise) | iOS, Android, Windows, macOS, Linux |
| **GHC** (goihangchuan.vn) | Da nen tang, tra cuu nhanh, ghi hinh tu dong | Chua cong bo | Da nen tang |
| **ECAM** (ghihinh.com) | Desktop, 2-16 camera/ban, hybrid cloud | 3,000,000 VND/nam | Windows |
| **ECAMPMCS** (pmcstech.net) | Desktop, 10-16 camera/may, ho tro Amazon S3 | Theo goi thiet bi | Windows |
| **EcomPMS** (ecompms.com) | Web-based, giam sat nhan vien | ~9,000-9,967 VND/ngay | Web |

### 1.3 Ecombox - Phan tich chi tiet doi thu chinh

**San pham:**
- **Ecombox App (Mobile):** iOS va Android, quet barcode/QR, quay video, dong bo cloud
- **Ecombox Desktop:** Windows, macOS, Linux, quan ly da camera, hoat dong 24/7
- **Ecombox Hub (Phan cung):** Camera FHD auto-focus, may quet barcode tich hop (99.9% do chinh xac, 0.1 giay quet), WiFi 6

**Tinh nang noi bat:**
- Luu tru video tren dam may de doi chieu tranh chap
- AI phat hien loi dong goi (thieu hang, sai ma san pham)
- Bao cao hieu suat nhan vien
- Tich hop Shopee, TikTok Shop, Lazada, Tiki
- Open API cho tich hop tuy chinh
- Dung thu 7 ngay mien phi

### 1.4 Co hoi khac biet

Hau het doi thu deu la SaaS tra phi hang thang/nam va yeu cau cloud.

| Diem | Doi thu hien tai | Giai phap cua ban (de xuat) |
|---|---|---|
| Chi phi | SaaS tra phi hang thang/nam | **Free local-first**, chi tra phi neu dung cloud |
| Luu tru | Bat buoc cloud (ton phi) | **Local-first**, cloud optional |
| Setup | Can dang ky tai khoan, cau hinh | **Cai app -> dung ngay** |
| Privacy | Video len server ben thu 3 | **Video o tren thiet bi nguoi dung** |
| Thiet bi | Thuong can mua phan cung rieng | **Dung dien thoai/laptop co san** |

---

## 2. Tinh nang cot loi - Phan tich chi tiet

### 2.1 Feature 1: Quet ma don hang (QR/Barcode)

**Cac loai ma can ho tro:**
- **1D Barcode:** Code 128, Code 39, EAN-13 (pho bien tren van don cac hang ship VN)
- **2D:** QR Code, Data Matrix
- **Ma van don dac thu:** Shopee, TikTok Shop, Lazada, Tiki thuong dung Code 128 hoac QR

**Nguon input quet ma:**

| Nguon | Cach hoat dong | Uu diem | Nhuoc diem |
|---|---|---|---|
| Camera dien thoai | Dung SDK quet truc tiep tu camera | Tien loi, khong can thiet bi them | Toc do cham hon scanner |
| Camera webcam (PC) | Stream tu webcam, xu ly frame de decode | Dung thiet bi co san | Phu thuoc chat luong webcam |
| May quet Bluetooth HID | Scanner gui du lieu nhu ban phim bluetooth | Nhanh (~0.1s), chinh xac 99.9% | Can mua thiet bi |
| May quet USB (PC/Android OTG) | Ket noi USB, hoat dong nhu keyboard input | Nhanh, on dinh | Chi dung tren PC hoac Android co OTG |

### 2.2 Feature 2: Quay & Luu video

**Workflow quay video:**
```
Quet ma van don -> Tu dong bat dau quay -> Dong goi hang ->
Quet ma lan 2 (hoac nhan nut) -> Dung quay -> Luu video gan voi ma don
```

**Thong so video khuyen nghi:**
- **Do phan giai:** 720p hoac 1080p (du ro de lam bang chung)
- **Codec:** H.264 uu tien (tuong thich cao, encoding nhanh tren ARM)
- **Container:** MP4
- **FPS:** 15-24fps (du muot, tiet kiem dung luong)
- **Bitrate:** VBR (Variable Bit Rate) - tu dong dieu chinh theo chuyen dong

**Uoc tinh dung luong (720p, H.264, 20fps, VBR):**
- 1 video ~30 giay: ~4-6 MB
- 100 don/ngay: ~400-600 MB/ngay
- 1 thang (3000 don): ~12-18 GB

### 2.3 Feature 3: Tra cuu & Truy xuat video

**Cach tra cuu:**
- Nhap/quet ma van don -> hien thi video tuong ung
- Tim theo ngay, khoang thoi gian
- Tim theo trang thai: dong hang / giao hang / hoan tra

**Du lieu metadata can luu cho moi video:**
```
{
  order_code:      "SPX123456789",     // ma van don
  video_path:      "/videos/2026/02/03/SPX123456789_packing_20260203_103052.mp4",
  recorded_at:     "2026-02-03T10:30:52",
  duration_seconds: 35,
  file_size_bytes:  6291456,
  type:            "packing",          // packing | shipping | return
  device_name:     "Samsung A54",
  camera_source:   "rear",
  thumbnail_path:  "/thumbs/SPX123456789_packing_20260203_103052_thumb.jpg"
}
```

---

## 3. Ket noi thiet bi ngoai

### 3.1 May quet ma vach Bluetooth

**Cach hoat dong:**
Scanner Bluetooth hoat dong o che do HID (Human Interface Device) - gia lap ban phim.
Khi quet, no "go" chuoi ma vach vao o input dang focus.

**Cach tich hop trong app:**
- Giu mot TextField (co the an) luon focus
- Scanner gui ky tu vao TextField
- Detect khi nhan duoc ky tu ket thuc (Enter/CR/LF) -> xu ly ma
- Khong can SDK dac biet - hoat dong nhu keyboard input

**Luu y iOS:**
Khi ket noi scanner Bluetooth HID, iOS nhan dien no nhu external keyboard
-> tu dong an ban phim ao tren iPhone. Can thiet ke UI khong phu thuoc keyboard ao.

**Luu y Android:**
Hau het Android va Windows chap nhan Bluetooth HID hoac USB scanner ngay lap tuc.
Ho tro USB OTG cho scanner USB tren Android.

### 3.2 Camera ngoai

**Tren PC (Electron/Desktop):**
- USB webcam: truy cap qua MediaDevices API (navigator.mediaDevices.getUserMedia)
- IP Camera: ket noi qua RTSP stream, decode bang FFmpeg hoac GStreamer
- Ho tro multi-camera: chon camera source tu danh sach thiet bi

**Tren Mobile:**
- Android: USB camera qua UVC (USB Video Class) - khong on dinh tren moi thiet bi
- iOS: Han che, chi ho tro camera built-in hoac camera MFi

### 3.3 May quet USB (tren PC)

- Hoat dong giong ban phim USB - gui keystroke
- App lang nghe keyboard event, detect pattern ma vach
- Phan biet input tu keyboard that vs scanner:
  dua vao toc do go (scanner gui toan bo chuoi trong < 50ms)

---

## 4. Chien luoc luu tru video

### 4.1 Local-first (khuyen nghi cho MVP)

| Khia canh | Chien luoc |
|---|---|
| **Codec** | H.264 Main Profile (tuong thich 100%, nhanh tren ARM) |
| **Encoding** | VBR (Variable Bit Rate) - tiet kiem khi it chuyen dong |
| **Phan giai** | 720p mac dinh, tuy chon 1080p |
| **FPS** | 20fps |
| **Cau truc thu muc** | /videos/YYYY/MM/DD/{order_code}_{type}_{datetime}.mp4 |
| **Thumbnail** | Trich 1 frame, luu JPEG 240px |
| **Auto-cleanup** | Tu xoa video cu hon X ngay (mac dinh 90 ngay) |
| **Database** | SQLite - nhe, khong can server, query nhanh |

### 4.2 Cloud (giai doan mo rong)

- Optional sync len Google Drive / OneDrive / S3
- Chi sync metadata truoc, video sync theo yeu cau hoac khi co WiFi
- Cho phep truy xuat tu nhieu thiet bi

---

## 5. Workflow chi tiet

### 5.1 Dong hang (Packing)

```
1. Mo app -> Chon che do "Dong hang"
2. Camera preview hien thi
3. Quet ma van don (camera hoac scanner ngoai)
   |-- Ma hop le -> Hien thi ma tren man hinh
   |               -> Tu dong BAT DAU quay video
   |-- Ma khong hop le -> Canh bao, yeu cau quet lai
4. Nguoi dung thuc hien dong goi (video ghi lai toan bo)
5. Ket thuc:
   |-- Cach 1: Quet ma van don TIEP THEO -> dung video hien tai, bat dau moi
   |-- Cach 2: Nhan nut "Hoan tat" -> dung va luu
   |-- Cach 3: Timeout (5 phut) -> tu dung
6. Video duoc luu -> Tao thumbnail -> Cap nhat DB
```

### 5.2 Giao hang cho shipper (Shipping out)

```
1. Chon che do "Giao hang"
2. Quet tung ma don giao cho shipper
3. Video ghi lai qua trinh ban giao (batch recording)
4. Tao danh sach don da giao kem timestamp
```

### 5.3 Nhan hang hoan tra (Return)

```
1. Chon che do "Nhan hoan"
2. Quet ma don hoan tra
3. Quay video mo goi, kiem tra tinh trang hang
4. Gan tag trang thai: "hang nguyen ven" / "hang bi hu" / "sai hang"
5. Luu video kem metadata trang thai
```

### 5.4 Tra cuu (Lookup)

```
1. Nhap ma don hang hoac quet ma
2. Hien thi tat ca video lien quan (dong hang + giao + hoan)
3. Xem video, tai ve, hoac chia se (gui cho san TMDT lam bang chung)
```

---

## 6. Lo trinh phat trien de xuat

### Phase 1 - MVP (Core)
- App mobile (Android truoc)
- Quet ma bang camera dien thoai
- Quay video, luu local
- Tra cuu video theo ma don
- SQLite luu metadata

### Phase 2 - Hardware Integration
- iOS support
- Ket noi scanner Bluetooth HID
- Continuous scan mode
- Return flow voi tagging

### Phase 3 - Desktop
- Desktop app (Electron) voi webcam
- Multi-camera support tren PC
- USB scanner support
- IP Camera RTSP (basic)

### Phase 4 - Mo rong
- Cloud backup (optional)
- Dashboard thong ke
- Multi-user / phan quyen
- Export video hang loat
- Tich hop API san TMDT

---

> Ngay tao: 2026-02-03
> Phien phan tich: Market Research & Feature Analysis

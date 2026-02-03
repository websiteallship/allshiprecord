# ALL SHIP ECOMBOX - Project Summary
## Tool quay video dong goi & doi soat don hang TMDT

> Tai lieu tong hop tu 3 phien phan tich: Market Research, Solution Architecture, Product Management

---

# PHAN I: PRODUCT MANAGER ANALYSIS
## Toi uu User Flow cho nhan vien dong goi

---

## 1. THIET KE HANDS-FREE WORKFLOW: QUET MA -> QUAY VIDEO

### 1.1 Nguyen tac thiet ke

Van de cot loi: Nhan vien dong goi xu ly 200-500 don/ngay, moi thao tac thua mat 3-5 giay = mat 25-40 phut/ngay. Workflow phai dat muc tieu **ZERO TAP** trong quy trinh lap (steady-state).

### 1.2 Ba mo hinh thao tac

```
MO HINH A: FULL HANDS-FREE (Khuyen nghi cho seller > 100 don/ngay)
=========================================================================

Thiet bi: Scanner Bluetooth co gia do + Camera co dinh (webcam/IP cam)

    Nhan vien cam don hang
           |
           v
    Quet ma van don qua scanner tren gia do
    (chi can dua ma vach qua scanner, khong can cam scanner)
           |
           v
    [APP TU DONG] Bat dau quay video <-- KHONG CAN CHAM MAN HINH
           |
           v
    Nhan vien dong goi hang truoc camera
           |
           v
    Quet ma don TIEP THEO
           |
           v
    [APP TU DONG] Dung video cu + Luu + Bat dau video moi
           |
           v
    ... LAP LAI ...

    Tong thao tac cham man hinh: 0
    Tong thao tac vat ly: CHI QUET MA (viec phai lam du co app hay khong)
```

```
MO HINH B: MINIMAL TOUCH (Cho seller dung dien thoai ca nhan)
=========================================================================

Thiet bi: Dien thoai ca nhan, camera truoc/sau

    Mo app -> Chon "Dong hang" (1 tap)
           |
           v
    Quet ma bang camera dien thoai
    (dua phieu gui hang vao camera)
           |
           v
    [APP TU DONG] Nhan dien ma -> Bat dau quay <-- KHONG CAN TAP
           |
           v
    Dong goi hang truoc camera
           |
           v
    Quet ma don TIEP THEO (dua phieu tiep theo vao camera)
           |
           v
    [APP TU DONG] Dung + Luu + Quay video moi
           |
           v
    ... LAP LAI ...

    Tong thao tac cham man hinh: 1 (chi lan dau mo app)
    Gioi han: Camera dien thoai vua quet ma vua quay video
              -> can vung quet ma rieng (goc tren) va vung quay (toan canh)
```

```
MO HINH C: MANUAL (Backup / seller < 20 don/ngay)
=========================================================================

    Mo app -> Chon "Dong hang"
           |
           v
    Nhap tay ma van don hoac quet
           |
           v
    Nhan nut "Bat dau quay"
           |
           v
    Dong goi hang
           |
           v
    Nhan nut "Dung & Luu"
           |
           v
    Tong thao tac: 3-4 tap
```

### 1.3 Continuous Scan Mode - Logic chi tiet

Day la tinh nang quan trong nhat cua app, quyet dinh trai nghiem nguoi dung:

```
CONTINUOUS SCAN MODE STATE MACHINE
====================================

State: READY (cho quet)
  |
  |-- [EVENT: Nhan ma barcode tu scanner hoac camera]
  |
  v
State: VALIDATING
  |
  |-- Ma hop le? --YES--> Tao order record trong DB
  |                       Chuyen sang RECORDING
  |
  |-- Ma hop le? --NO---> Phat am bao "beep loi"
  |                       Hien thong bao 2 giay
  |                       Quay lai READY
  v
State: RECORDING
  |
  |-- Video dang quay...
  |-- Timer hien thi tren man hinh
  |-- Overlay: ma don + thoi gian
  |
  |-- [EVENT: Nhan ma barcode MOI (ma khac)]
  |     |
  |     v
  |   TRANSITION (< 500ms):
  |     1. stopRecording(video_hien_tai)
  |     2. saveToFile() + generateThumbnail() [background]
  |     3. updateDatabase() [background]
  |     4. startRecording(video_moi) voi ma moi
  |     5. Phat am "beep thanh cong"
  |     --> Van o state RECORDING nhung cho don moi
  |
  |-- [EVENT: Nhan CUNG ma barcode (trung lap)]
  |     |
  |     v
  |   Phat am canh bao "da quet roi"
  |   Tiep tuc recording, khong lam gi
  |
  |-- [EVENT: Nhan nut "Dung"]
  |     |
  |     v
  |   stopRecording() + save + ve READY
  |
  |-- [EVENT: Timeout 5 phut]
  |     |
  |     v
  |   stopRecording() + save
  |   Hien canh bao "Video da tu dong dung"
  |   Ve READY
  |
  v
State: SAVING (background, khong block UI)
  |
  |-- Finalize MP4
  |-- Generate thumbnail (frame giay thu 2)
  |-- Update SQLite
  |-- Tinh dung luong con lai
  |-- (Optional) Queue cloud sync
  |
  v
State: READY (san sang quet don tiep)
```

### 1.4 Phan hoi am thanh (Audio Feedback) - rat quan trong

Nhan vien dong goi thuong KHONG NHIN man hinh khi lam viec. Am thanh la kenh phan hoi chinh:

```
AM THANH              | Y NGHIA                    | KHI NAO
---------------------|----------------------------|---------------------------
"Beep" ngan (cao)    | Quet thanh cong, bat dau   | Khi nhan ma hop le
                     | quay                        |
"Beep beep" (2 tieng)| Dung video cu, bat dau moi | Khi quet ma moi (continuous)
"Boop" tram (thap)   | Loi - ma khong hop le      | Khi ma sai format
"Beep beep beep" (3) | Canh bao - ma trung lap    | Khi quet cung ma
"Ding" (trong)       | Da luu thanh cong           | Khi nhan Dung
"Alarm" (lien tuc)   | Loi nghiem trong            | Camera mat ket noi
Im lang              | Dang quay binh thuong       | Trong qua trinh quay
```

---

## 2. LOGIC XU LY LOI: CAMERA & SCANNER

### 2.1 Camera bi mat ket noi

```
TINH HUONG 1: Camera disconnect TRONG KHI DANG QUAY
====================================================

Timeline:
  t=0    Dang quay video cho don SPX123
  t=15s  Camera bi ngat (rut USB, Bluetooth mat, app bi iOS kill)
         |
         v
  [PHAT HIEN] (trong 500ms)
  App nhan event onCameraError / onDeviceDisconnected
         |
         v
  [XU LY NGAY LAP TUC]
  1. Luu phan video da quay (0-15 giay) -- KHONG DUOC MAT DATA
     -> Finalize MP4 fragment da co trong buffer
     -> Danh dau trong DB: status = 'partial', duration = 15s
  2. Phat am ALARM
  3. Hien thong bao toan man hinh:
     ┌─────────────────────────────────────┐
     │   ⚠ CAMERA BI NGAT KET NOI         │
     │                                     │
     │   Don SPX123: Da luu 15 giay video  │
     │   (video khong day du)              │
     │                                     │
     │   [Ket noi lai]  [Quay moi]  [Bo qua]│
     └─────────────────────────────────────┘
  4. Tu dong thu ket noi lai camera moi 3 giay (toi da 5 lan)
         |
         v
  [NEU KET NOI LAI DUOC]
  -> Hien: "Camera da ket noi lai. Quay tiep don SPX123?"
  -> [Quay tiep] -> Tao video moi, lien ket voi cung order
  -> [Bo qua] -> Giu video partial, ve READY
         |
         v
  [NEU KHONG KET NOI LAI DUOC sau 15 giay]
  -> Hien: "Khong tim thay camera. Kiem tra ket noi."
  -> [Thu lai] -> Retry
  -> [Doi camera] -> Mo camera selection
  -> [Tiep tuc khong camera] -> Chi quet ma, khong quay (che do text-only)
```

```
TINH HUONG 2: Camera disconnect KHI KHONG QUAY (o man hinh READY)
==================================================================

  [PHAT HIEN]
  Camera preview mat hinh
         |
         v
  [XU LY]
  1. Hien icon canh bao tren camera preview
  2. Tu dong retry ket noi (background, moi 5 giay)
  3. Neu co nhieu camera -> tu dong chuyen sang camera khac
  4. Van cho phep quet ma (mode text-only)
         |
         v
  [KHI KET NOI LAI]
  -> Tu dong khoi phuc camera preview
  -> Phat am "beep" xac nhan
```

```
TINH HUONG 3: Camera bi chiem boi app khac (mobile)
====================================================

  [PHAT HIEN]
  Camera resource conflict error
         |
         v
  [XU LY]
  1. Hien: "Camera dang duoc su dung boi app khac"
  2. [Mo Settings] -> De user tat app kia
  3. Tu dong retry khi app quay lai foreground
```

### 2.2 May quet khong nhan ma

```
TINH HUONG 1: Quet nhung khong decode duoc ma
==============================================

  Scanner nhan barcorde nhung output la chuoi rong hoac ky tu la
         |
         v
  [APP PHAT HIEN]
  Input khong khop regex pattern ma van don
  (VD: SPX/VN/TK/LZ + 8-15 so)
         |
         v
  [XU LY]
  1. Phat am "boop" (loi)
  2. Hien: "Ma khong hop le: [hien chuoi da quet]"
  3. Goi y: "Thu quet lai hoac nhap tay"
  4. Hien input field de nhap tay (co nut "Paste" tu clipboard)
         |
         v
  [NEU LIEN TUC 3 LAN THAT BAI]
  -> Hien goi y chi tiet:
     "Ma bi mo? Thu:"
     "- Dieu chinh goc quet"
     "- Lam phang phieu gui hang"
     "- Dung den flash (mobile)"
     "- Nhap tay ma van don"
```

```
TINH HUONG 2: Scanner Bluetooth bi mat ket noi
================================================

  [PHAT HIEN] (trong 1-2 giay)
  Bluetooth HID device disconnected event
         |
         v
  [XU LY]
  1. Hien icon "Scanner offline" tren status bar
  2. Tu dong chuyen sang CAMERA SCAN MODE (dung camera de quet ma)
  3. Background: thu ket noi lai scanner moi 5 giay
         |
         v
  [KHI SCANNER KET NOI LAI]
  -> Hien: "Scanner da ket noi lai"
  -> Tu dong chuyen ve Scanner mode
  -> Tat camera scan mode

  QUAN TRONG: Khong bao gio block workflow vi mat scanner.
  Luon co fallback sang camera scan hoac nhap tay.
```

```
TINH HUONG 3: Scanner quet nhung app khong nhan (USB HID tren Desktop)
======================================================================

  Nguyen nhan thuong gap: App khong co focus, input di vao app khac
         |
         v
  [PHONG NGUA]
  1. App luon giu "Always on Top" khi o che do SCANNING/RECORDING
  2. An TextField luon co focus (invisible, bat moi keyboard input)
  3. Phan biet scanner vs keyboard:
     - Scanner gui toan bo chuoi trong < 50ms
     - Nguoi go tay: > 100ms giua cac ky tu
     -> Neu nhan chuoi > 6 ky tu trong < 100ms -> xac dinh la scanner input

  [NEU VAN KHONG NHAN]
  -> Hien nut "Test Scanner" trong Settings
  -> User quet thu -> App hien raw input de debug
```

### 2.3 Bang tom tat xu ly loi

```
LOI                    | MUC DO  | FALLBACK              | AUTO RETRY
-----------------------|---------|---------------------- |-----------
Camera disconnect      | Cao     | Luu video partial     | Co (5 lan)
Camera bi app khac     | Trung   | Cho tat app kia       | Co (foreground)
Scanner Bluetooth mat  | Trung   | Camera scan mode      | Co (moi 5s)
Scanner USB khong nhan | Thap    | Check focus + test    | Manual
Ma bi mo/hong          | Thap    | Nhap tay              | Khong
Het bo nho thiet bi    | Cao     | Canh bao + auto clean | Khong
```

---

## 3. CO CHE DAT TEN FILE & TO CHUC THU MUC

### 3.1 Cau truc dat ten file

```
QUY TAC DAT TEN:
================

{order_code}_{type}_{timestamp}.mp4

Vi du:
  SPX038294671_packing_20260203_103052.mp4
  VN72849301_return_20260203_143021.mp4
  TK9928374_shipping_20260203_160045.mp4

Giai thich:
  SPX038294671  -> Ma van don goc (giu nguyen, khong chinh sua)
  _packing      -> Loai video: packing | shipping | return
  _20260203     -> Ngay: YYYYMMDD (sap xep theo thu tu thoi gian)
  _103052       -> Gio: HHmmss
  .mp4          -> Dinh dang

TAI SAO KHONG DUNG ID SO HAY UUID:
  - Nhan vien khong the nho "video_00384.mp4" la don nao
  - Khi xem thu muc bang file explorer -> thay ngay ma don
  - Khi can gui video cho san TMDT -> ten file da chua ma don
  - Khi can tim bang terminal: ls | grep "SPX038294671" -> ra ngay

THUMBNAIL:
  {order_code}_{type}_{timestamp}_thumb.jpg
  SPX038294671_packing_20260203_103052_thumb.jpg
```

### 3.2 Cau truc thu muc

```
PHUONG AN A: PHAN THEO NGAY (Khuyen nghi)
==========================================

videos/
  2026/
    02/
      03/
        SPX038294671_packing_20260203_103052.mp4
        SPX038294671_packing_20260203_103052_thumb.jpg
        VN72849301_return_20260203_143021.mp4
        VN72849301_return_20260203_143021_thumb.jpg
      04/
        TK9928374_packing_20260204_091522.mp4
        ...
    03/
      ...

UU DIEM:
  + Xoa video cu theo thang rat de (xoa ca folder thang)
  + Backup theo ngay/tuan de dang
  + Moi folder khong qua nhieu file (500 don/ngay = 500-1500 file)
  + Truy cap nhanh khi biet "don nay dong khoang ngay nao"

NHUOC DIEM:
  - Tim 1 don cu thi TRA SQLITE roi moi biet ngay
    (nhung day la cach dung - khong ai luoi qua 10,000 file bang mat)
```

```
PHUONG AN B: PHAN THEO DON HANG
================================

videos/
  orders/
    SPX038294671/
      packing_20260203_103052.mp4
      packing_20260203_103052_thumb.jpg
      return_20260215_091200.mp4
      return_20260215_091200_thumb.jpg
    VN72849301/
      packing_20260203_143021.mp4
      ...

UU DIEM:
  + Tat ca video cua 1 don nam cung 1 cho (packing + return)
  + Tim don = mo folder

NHUOC DIEM:
  - 500 don/ngay x 30 ngay = 15,000 folder trong 1 thang -> CHAM
  - Xoa video cu theo thoi gian rat kho (phai quet tung folder)
  - File system performance giam khi qua nhieu folder
```

```
>>> QUYET DINH: PHUONG AN A (phan theo ngay)
    + Ket hop SQLite index de tra cuu theo ma don
    = Ket hop tot nhat giua performance va truy xuat
```

### 3.3 SQLite - Tang truy xuat nhanh

```
TRUY XUAT THEO MA DON (use case chinh):
========================================

User nhap: "SPX038294671"
  |
  v
App query SQLite:
  SELECT v.file_path, v.type, v.duration_ms, v.recorded_at, v.thumbnail_path
  FROM videos v
  JOIN orders o ON v.order_id = o.id
  WHERE o.order_code = 'SPX038294671'
  ORDER BY v.recorded_at ASC;
  |
  v
Ket qua (< 1ms voi index):
  1. packing  | 35s  | 2026-02-03 10:30 | /videos/2026/02/03/SPX...packing...mp4
  2. return   | 48s  | 2026-02-15 09:12 | /videos/2026/02/15/SPX...return...mp4
  |
  v
Hien thi card:
  ┌──────────────────────────────────────────────────┐
  │ Don: SPX038294671                                │
  │                                                  │
  │ ┌──────────────┐  ┌──────────────┐              │
  │ │ [thumbnail]  │  │ [thumbnail]  │              │
  │ │  DONG GOI    │  │  HOAN TRA    │              │
  │ │  03/02 10:30 │  │  15/02 09:12 │              │
  │ │  35 giay     │  │  48 giay     │              │
  │ └──────────────┘  └──────────────┘              │
  │                                                  │
  │ [Xem video dong]  [Xem video hoan]  [Chia se]  │
  └──────────────────────────────────────────────────┘
```

### 3.4 Tim kiem nang cao (khong can cloud)

```
TIM THEO NGAY:
  SELECT * FROM videos WHERE DATE(recorded_at) = '2026-02-03'

TIM THEO KHOANG THOI GIAN:
  SELECT * FROM videos WHERE recorded_at BETWEEN '2026-02-01' AND '2026-02-28'

TIM DON CO VIDEO HOAN TRA:
  SELECT o.order_code, v.* FROM orders o
  JOIN videos v ON v.order_id = o.id
  WHERE v.type = 'return'

TIM DON CHUA CO VIDEO (chi co record nhung chua quay):
  SELECT o.* FROM orders o
  LEFT JOIN videos v ON v.order_id = o.id
  WHERE v.id IS NULL

THONG KE DUNG LUONG:
  SELECT DATE(recorded_at) as ngay,
         COUNT(*) as so_video,
         SUM(file_size_bytes)/1024/1024 as mb
  FROM videos
  GROUP BY DATE(recorded_at)
  ORDER BY ngay DESC
```

---

## 4. PHAN TICH TINH KHA THI: DIEN THOAI vs MAY TINH BAN

### 4.1 So sanh chi tiet

```
TIEU CHI               | DIEN THOAI CA NHAN (BYOD)  | MAY TINH + WEBCAM
========================|============================|========================
CHI PHI BAN DAU         |                            |
  Thiet bi              | 0 VND (dung may co san)    | 5-15 trieu VND
                        |                            | (PC + webcam + scanner)
  Phan mem              | Mien phi (local storage)   | Mien phi (local storage)
                        |                            |
CHAT LUONG VIDEO        |                            |
  Camera                | 12-108MP (rat tot)         | Webcam 1-5MP (trung binh)
  Autofocus             | Co (nhanh)                 | Co the khong co
  Goc rong              | 70-120 do                  | 60-90 do
  Anh sang yeu          | Xu ly tot (ISP manh)       | Kem hon
  Ket luan              | ★★★★★ VUOT TROI            | ★★★☆☆ CHAP NHAN DUOC
                        |                            |
SU TIEN LOI            |                            |
  Setup                 | Cai app -> dung ngay       | Can lap dat, ke, day noi
  Di dong               | Mang di bat ky dau         | Co dinh tai 1 vi tri
  Da nhiem              | Kho (1 camera lam nhieu    | De (nhieu camera, man
                        | viec)                      | hinh lon)
  Ket luan              | ★★★★☆ LINH HOAT            | ★★★☆☆ CO DINH
                        |                            |
DO ON DINH             |                            |
  Pin/Nguon             | Can sac, co the het pin    | Luon co dien
  Nhiet do              | Quay lau -> nong -> giam   | Khong van de
                        | performance                |
  Gian doan             | Cuoc goi, thong bao, app   | Khong bi gian doan
                        | khac tranh camera          |
  Ket luan              | ★★☆☆☆ KHONG ON DINH        | ★★★★★ RAT ON DINH
                        |                            |
KHI NANG SCALE         |                            |
  100 don/ngay          | OK                         | OK
  500 don/ngay          | Nong may, het pin nhanh    | OK
  1000+ don/ngay        | KHONG PHU HOP              | OK (voi multi-cam)
  Nhieu nhan vien       | Moi nguoi 1 may (da co)    | Can them may/camera
  Ket luan              | ★★★☆☆ HAN CHE              | ★★★★☆ TOT
                        |                            |
LUU TRU                |                            |
  Dung luong            | 64-256GB (chung voi anh,   | 500GB - 2TB (rieng
                        | nhac, app khac)            | cho video)
  100 don/ngay x 5MB    | 500MB/ngay - OK 2-3 thang | OK > 1 nam
  500 don/ngay x 5MB    | 2.5GB/ngay - DAY sau 1     | OK 6+ thang
                        | thang                      |
  Ket luan              | ★★☆☆☆ HAN CHE              | ★★★★★ ROI RAO
                        |                            |
KET NOI THIET BI NGOAI |                            |
  Scanner Bluetooth     | Co (HID mode)              | Co
  Scanner USB           | Can OTG adapter            | Co (plug & play)
  Webcam ngoai          | Rat kho (Android UVC       | De (USB, nhieu cam)
                        | khong on dinh)             |
  IP Camera             | Kho                        | De (FFmpeg/RTSP)
  Ket luan              | ★★☆☆☆ HAN CHE              | ★★★★★ LINH HOAT
                        |                            |
QUAN LY (cho chu shop) |                            |
  Giam sat nhan vien    | Kho (may ca nhan)          | De (may cong ty)
  Dam bao quay du       | Kho kiem soat              | De kiem soat
  Bao mat data          | Video tren may nhan vien   | Video tren may cong ty
  Ket luan              | ★★☆☆☆ KHO QUAN LY          | ★★★★★ DE QUAN LY
```

### 4.2 Ma tran quyet dinh theo quy mo seller

```
SELLER NHO (1-2 nguoi, < 50 don/ngay)
======================================
>>> KHUYEN NGHI: DIEN THOAI CA NHAN <<<

Ly do:
- Khong dau tu them thiet bi
- Chat luong camera dien thoai thua du
- 50 don x 5MB = 250MB/ngay, bot nho
- Linh hoat: dong hang o ban, sofa, bat ky dau
- Can: Dien thoai + gia do dien thoai (50K VND)


SELLER VUA (3-5 nguoi, 50-300 don/ngay)
========================================
>>> KHUYEN NGHI: KET HOP (Mobile + 1 may tinh) <<<

Ly do:
- May tinh lam tram chinh (webcam co dinh, scanner USB)
- Dien thoai lam backup / cho di dong
- May tinh xu ly luong don chinh (on dinh, khong nong)
- Dien thoai cho truong hop nhan hang hoan, kiem hang tai kho
- Can: 1 PC (co san) + 1 webcam (300-500K) + 1 scanner USB (500K-1tr)


SELLER LON (5+ nguoi, 300+ don/ngay)
=====================================
>>> KHUYEN NGHI: MAY TINH BAN + MULTI-CAMERA <<<

Ly do:
- On dinh 8-12 tieng lien tuc
- Multi-camera: 1 cam toan canh + 1 cam can canh san pham
- O cung lon, khong lo dung luong
- Quan ly tap trung: biet nhan vien nao dong don nao
- IP Camera cho giam sat tong the kho
- Can: PC + 2 webcam/ban + scanner USB/ban + (optional) IP camera
```

### 4.3 Rui ro BYOD (Dung dien thoai ca nhan)

```
RUI RO                       | TAC DONG  | GIAI PHAP
------------------------------|-----------|----------------------------------
Nhan vien nghi viec, video    | CAO       | Sync metadata len cloud (free)
tren may ca nhan bi xoa       |           | Backup video hang tuan ra USB/PC
                              |           |
May cu, camera mo             | TRUNG     | App tu detect chat luong camera,
                              | BINH      | canh bao neu duoi nguong
                              |           |
Het bo nho vi anh/video       | CAO       | Storage quota rieng cho app,
ca nhan                       |           | canh bao som khi < 20%
                              |           |
Nhan vien khong muon cai      | TRUNG     | App nhe (< 30MB), khong can
app cong ty len may ca nhan   | BINH      | dang nhap, khong thu thap
                              |           | data ca nhan
                              |           |
iOS giet app nen,             | CAO       | Fragmented MP4, pre-recording
mat video giua chung          |           | buffer, audio alert khi bi
                              |           | interrupt
                              |           |
Da dang thiet bi Android      | TRUNG     | Test tren 15-20 model pho bien
(camera behavior khac nhau)   | BINH      | tai VN, fallback resolution
```

---

# PHAN II: TONG KET 3 PHIEN PHAN TICH

---

## PHIEN 1: NGHIEN CUU THI TRUONG & TINH NANG

### Tong quan du an
- **Muc tieu:** Xay dung tool giup seller luu tru video dong goi, xuat hang, nhan hoan tra
  de doi soat voi don vi van chuyen hoac san TMDT
- **Doi thu chinh:** Ecombox, GHC, ECAM, ECAMPMCS, EcomPMS
- **Diem khac biet:** Local-first storage (mien phi), khong bat buoc cloud,
  dung thiet bi co san

### Tinh nang cot loi
1. Quet ma van don (QR/Barcode) qua camera hoac scanner ngoai
2. Tu dong quay video gan voi ma don
3. Luu tru local, tra cuu nhanh theo ma don
4. Ho tro 3 workflow: Dong hang / Giao hang / Nhan hoan

### Ket noi thiet bi
- Camera: Built-in (mobile), Webcam USB (PC), IP Camera RTSP (PC)
- Scanner: Bluetooth HID (mobile + PC), USB HID (PC)
- Giao thuc: HID keyboard emulation (universal, khong can SDK rieng)

### Chien luoc luu tru
- Codec: H.264 (Main Profile), 720p, 20fps, VBR 2-4 Mbps
- ~4-6 MB / 30 giay video
- Container: Fragmented MP4
- Database: SQLite
- Auto-cleanup: configurable (mac dinh 90 ngay)

---

## PHIEN 2: KIEN TRUC GIAI PHAP (Solution Architecture)

### Tech Stack quyet dinh
| Thanh phan      | Lua chon               | Ly do                                    |
|-----------------|------------------------|------------------------------------------|
| Mobile          | Flutter                | Performance camera tot, single codebase   |
| Desktop         | Electron               | WebRTC camera mature, multi-cam on dinh   |
| Video codec     | H.264 (KHONG PHAI H.265)| Tuong thich 100%, encoding nhanh tren ARM|
| Database        | SQLite                 | Nhe, nhanh, offline, khong can server     |
| Barcode SDK     | Google ML Kit          | Free, chinh xac, offline                  |
| Scanner         | Bluetooth/USB HID      | Universal, khong can SDK rieng            |
| Luu tru         | Local-first            | Zero cost, privacy, khong can internet    |

### Kien truc Local-first + Optional Cloud
- **Tier mien phi:** Pure local, khong can dang ky
- **Tier 1 ($):** Sync metadata len cloud (tra cuu tu nhieu thiet bi)
- **Tier 2 ($$):** Full video backup + CDN + share link

### Video Processing Pipeline
```
Camera -> Resolution Scale (720p/1080p) -> H.264 Hardware Encoder
-> Fragmented MP4 -> Local File System -> SQLite metadata
```

### Phan tich rui ro ky thuat
| Rui ro                              | Muc do      | Giai phap                        |
|-------------------------------------|-------------|----------------------------------|
| iOS background recording            | Cao x Cao   | Fragmented MP4, canh bao user    |
| iOS scanner an ban phim ao          | Cao x Cao   | UI khong phu thuoc keyboard      |
| Android camera fragmentation        | Cao x TB    | CameraX + test 15-20 model       |
| Electron USB camera hot-plug        | TB x TB     | Manual refresh + polling         |
| IP Camera RTSP latency              | TB x TB     | Pre-recording buffer 3 giay      |
| Storage day tren mobile             | TB x Cao    | Auto-cleanup + canh bao som      |

### Lo trinh phat trien
- **Phase 1 (MVP):** Android app - quet camera + quay video + luu local
- **Phase 2:** iOS + Bluetooth scanner + continuous mode + return flow
- **Phase 3:** Desktop Electron + multi-camera + USB scanner
- **Phase 4:** Cloud backup + multi-user + API san TMDT

---

## PHIEN 3: PRODUCT MANAGEMENT - USER FLOW TOI UU

### Hands-free Workflow
- **Mo hinh A (Full hands-free):** Scanner Bluetooth co dinh + camera co dinh
  -> 0 lan cham man hinh trong quy trinh lap
- **Mo hinh B (Minimal touch):** Dien thoai ca nhan, camera quet + quay
  -> 1 lan cham (chi khi mo app)
- **Mo hinh C (Manual):** Nhap tay + nut bam -> 3-4 tap

### Continuous Scan Mode
- Quet ma moi = tu dong dung video cu + luu + bat dau video moi
- Transition time < 500ms
- Audio feedback la kenh phan hoi chinh (nhan vien khong nhin man hinh)

### Xu ly loi
- Camera disconnect khi dang quay: Luu video partial, retry 5 lan, fallback
- Scanner mat ket noi: Tu dong chuyen sang camera scan mode
- Ma bi mo: Retry 3 lan, goi y, fallback nhap tay
- NGUYEN TAC: Khong bao gio block workflow vi loi thiet bi

### Dat ten file & thu muc
```
Format:  {order_code}_{type}_{YYYYMMDD}_{HHmmss}.mp4
Thu muc: videos/YYYY/MM/DD/{file}.mp4
Tra cuu: SQLite index tren order_code (< 1ms)
```

### Phone vs Desktop
| Quy mo seller         | Khuyen nghi              | Ly do chinh                    |
|------------------------|--------------------------|--------------------------------|
| Nho (< 50 don/ngay)   | Dien thoai ca nhan       | 0 dong dau tu, du tot          |
| Vua (50-300 don/ngay)  | Ket hop PC + mobile      | PC chinh, mobile backup/di dong|
| Lon (300+ don/ngay)    | PC + multi-camera        | On dinh, quan ly tap trung     |

---

# PHAN III: QUYET DINH CUOI CUNG & NEXT STEPS

## Tom tat cac quyet dinh quan trong

| # | Quyet dinh                    | Ket luan                                  |
|---|-------------------------------|-------------------------------------------|
| 1 | Framework mobile              | Flutter                                   |
| 2 | Framework desktop             | Electron                                  |
| 3 | Video codec                   | H.264 (khong phai H.265)                  |
| 4 | Database                      | SQLite (local)                             |
| 5 | Luu tru mac dinh              | Local-first, cloud optional                |
| 6 | Barcode SDK                   | Google ML Kit                              |
| 7 | Scanner protocol              | Bluetooth/USB HID (keyboard emulation)     |
| 8 | Workflow chinh                | Continuous Scan Mode (hands-free)          |
| 9 | Dat ten file                  | {order_code}_{type}_{datetime}.mp4         |
| 10| To chuc thu muc               | /videos/YYYY/MM/DD/                        |
| 11| MVP platform                  | Android app                                |
| 12| Doi tuong MVP                 | Seller nho, dung dien thoai ca nhan        |

## MVP Feature List (Phase 1)

```
MUST HAVE (MVP):
  [x] Quet ma van don bang camera dien thoai
  [x] Tu dong quay video sau khi quet
  [x] Continuous scan mode (quet don moi = dung video cu)
  [x] Luu video local voi ten file co y nghia
  [x] Tra cuu video theo ma don (tim kiem)
  [x] Thumbnail preview
  [x] Audio feedback (beep thanh cong/that bai)
  [x] Thong ke dung luong da su dung
  [x] Auto-cleanup video cu

SHOULD HAVE (Phase 2):
  [ ] Ket noi scanner Bluetooth HID
  [ ] iOS support
  [ ] Return flow voi tagging tinh trang
  [ ] Export/share video (gui cho san TMDT)
  [ ] Nut quay nhanh (khong can quet ma)

COULD HAVE (Phase 3+):
  [ ] Desktop app (Electron)
  [ ] Multi-camera
  [ ] IP Camera RTSP
  [ ] Cloud backup
  [ ] Multi-user / phan quyen
  [ ] Dashboard thong ke
  [ ] API tich hop san TMDT
```

## Ky thuat can nghien cuu them

1. Flutter `camera` package + `google_mlkit_barcode_scanning`: test performance
   quay video + quet ma dong thoi tren thiet bi tam trung
2. Fragmented MP4 implementation tren Android MediaCodec: dam bao khong mat data
   khi app crash
3. Bluetooth HID integration tren Flutter: test voi cac scanner pho bien tai VN
   (Honeywell, Zebra, Tera, Netum)
4. SQLite performance voi 100,000+ records tren mobile

---

> Tai lieu nay duoc tong hop tu 3 phien phan tich lien tiep.
> Tac gia: AI Product & Architecture Consulting
> Ngay: 2026-02-03

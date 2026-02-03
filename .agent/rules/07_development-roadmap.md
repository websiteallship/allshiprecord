# Development Roadmap - ALL SHIP ECOMBOX

## Phase Overview

```
PHASE 1 (MVP)          PHASE 2               PHASE 3              PHASE 4
Android Mobile         iOS + Hardware        Desktop              Cloud + Scale
──────────────────────────────────────────────────────────────────────────────>
                                                                        TIME
```

## Phase 1: MVP (Android Mobile)

**Target:** Validate product-market fit  
**Platform:** Android only  
**Framework:** Flutter

### Must Have Features

- [x] Quét mã vận đơn bằng camera điện thoại (ML Kit)
- [x] Tự động quay video sau khi quét
- [x] Continuous scan mode (quét đơn mới = dừng video cũ)
- [x] Lưu video local với tên file có ý nghĩa
- [x] Tra cứu video theo mã đơn (tìm kiếm)
- [x] Thumbnail preview
- [x] Audio feedback (beep thành công/thất bại)
- [x] Thống kê dung lượng đã sử dụng
- [x] Auto-cleanup video cũ

### Tech Stack

```yaml
Framework: Flutter (Android only build)
Camera: camera package + google_mlkit_barcode
Video: Native MediaCodec via platform channel
Database: SQLite (sqflite)
```

### Skills Áp Dụng

| Skill | Mục Đích |
|-------|----------|
| `01_flutter-expert` | Core development |
| `02_mobile-design` | UI/UX |
| `17_video-encoding-mobile` | Video recording |
| `18_barcode-scanning-integration` | Order scanning |
| `04_database-design` | SQLite storage |
| `05_error-handling-patterns` | Robustness |
| `21_performance-optimization` | Performance |

---

## Phase 2: iOS + Hardware Integration

**Target:** Mở rộng thị trường, tăng năng suất  
**Platform:** iOS, Bluetooth scanner

### Should Have Features

- [ ] iOS support (cùng Flutter codebase)
- [ ] Kết nối scanner Bluetooth HID
- [ ] Continuous mode hoàn thiện
- [ ] Return flow với tagging tình trạng
- [ ] Export/share video (gửi cho sàn TMDT)
- [ ] Nút quay nhanh (không cần quét mã)

### Tech Stack

```yaml
Framework: Flutter (iOS build)
Scanner: Bluetooth HID integration
Video: VideoToolbox (iOS native)
```

### iOS-Specific Considerations

- Background recording restriction → Fragmented MP4
- Bluetooth HID ẩn keyboard → UI không phụ thuộc keyboard
- App Store review → Privacy compliance

### Skills Áp Dụng

| Skill | Mục Đích |
|-------|----------|
| `01_flutter-expert` | iOS platform |
| `17_video-encoding-mobile` | VideoToolbox |
| `19_bluetooth-hid-integration` | External scanners |
| `10_debugging-strategies` | iOS restrictions |
| `22_mobile-security` | App security |

---

## Phase 3: Desktop (Electron)

**Target:** Seller lớn, multi-camera, ổn định 8-12 tiếng  
**Platform:** Windows, macOS

### Could Have Features

- [ ] Desktop app (Electron)
- [ ] Multi-camera management
- [ ] USB scanner support
- [ ] IP Camera RTSP (basic)
- [ ] Cross-device search (metadata sync)

### Tech Stack

```yaml
Framework: Electron
Language: TypeScript
Camera: WebRTC (getUserMedia + MediaRecorder)
IP Camera: FFmpeg for RTSP decode
Database: better-sqlite3
Scanner: USB HID (keyboard event listener)
```

### Desktop Advantages

- Ổn định 8-12 tiếng liên tục
- Multi-camera: 1 cam toàn cảnh + 1 cam cận cảnh
- Ổ cứng lớn, không lo dung lượng
- Quản lý tập trung

### Skills Áp Dụng

| Skill | Mục Đích |
|-------|----------|
| `08_typescript-pro` | Electron app |
| `20_rtsp-ip-camera` | IP camera |
| `19_bluetooth-hid-integration` | USB scanners |

---

## Phase 4: Cloud + Scale

**Target:** Seller lớn, team nhiều người, enterprise  
**Platform:** All platforms + Cloud backend

### Future Features

- [ ] Cloud backup (S3/GCS)
- [ ] Multi-user / phân quyền
- [ ] Dashboard thống kê
- [ ] API tích hợp sàn TMDT
- [ ] Share link video cho khiếu nại

### Tech Stack

```yaml
Backend: Node.js hoặc Go
Database: PostgreSQL
Storage: S3/GCS
CDN: CloudFront/CloudFlare
Auth: JWT + OAuth
```

### Cloud Tiers

| Tier | Features | Target |
|------|----------|--------|
| Tier 0 (Free) | Pure local | Seller nhỏ |
| Tier 1 ($) | Metadata sync | Seller vừa, nhiều thiết bị |
| Tier 2 ($$) | Full video backup + CDN | Seller lớn, enterprise |

### Skills Áp Dụng

| Skill | Mục Đích |
|-------|----------|
| `09_api-design-principles` | REST API |
| `03_software-architecture` | Cloud integration |

---

## Kỹ Thuật Cần Nghiên Cứu Thêm

1. **Flutter `camera` + `google_mlkit_barcode_scanning`:**  
   Test performance quay video + quét mã đồng thời trên thiết bị tầm trung

2. **Fragmented MP4 trên Android MediaCodec:**  
   Đảm bảo không mất data khi app crash

3. **Bluetooth HID integration trên Flutter:**  
   Test với các scanner phổ biến (Honeywell, Zebra, Tera, Netum)

4. **SQLite performance:**  
   Test với 100,000+ records trên mobile

---

## Timeline Estimate

| Phase | Duration | Priority |
|-------|----------|----------|
| Phase 1 (MVP) | 4-6 tuần | 🔴 P0 |
| Phase 2 (iOS + Hardware) | 3-4 tuần | 🟠 P1 |
| Phase 3 (Desktop) | 4-6 tuần | 🟡 P2 |
| Phase 4 (Cloud) | 6-8 tuần | 🟢 P3 |

---

## Success Metrics

### Phase 1
- App có thể quay + lưu + tra cứu video
- Continuous scan mode hoạt động < 500ms transition
- Không mất video khi app crash
- Storage management hoạt động

### Phase 2
- iOS app hoạt động ổn định
- Bluetooth scanner kết nối thành công
- Return flow với tagging hoàn chỉnh

### Phase 3
- Desktop app ổn định 8h liên tục
- Multi-camera không conflict
- IP Camera stream không bị lag quá 2s

### Phase 4
- Cloud sync hoạt động reliable
- Share link video có thể xem trên web
- Dashboard thống kê hiển thị đúng

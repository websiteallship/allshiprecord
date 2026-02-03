# 📚 ALL SHIP ECOMBOX - Project Skills Registry

> Danh sách kỹ năng (skills) đã được cài đặt và tùy chỉnh cho dự án **Video Recording & Order Verification Tool**

**Cập nhật lần cuối:** 2026-02-03
**Tổng số skills:** 23

---

## 📋 Mục Lục

- [🏗️ Nhóm 1: Kiến Trúc & Thiết Kế](#-nhóm-1-kiến-trúc--thiết-kế)
- [📱 Nhóm 2: Phát Triển Mobile (Flutter)](#-nhóm-2-phát-triển-mobile-flutter)
- [💻 Nhóm 3: Phát Triển Desktop & Web](#-nhóm-3-phát-triển-desktop--web)
- [🎬 Nhóm 4: Video & Media Processing](#-nhóm-4-video--media-processing)
- [🔌 Nhóm 5: Hardware Integration](#-nhóm-5-hardware-integration)
- [🔧 Nhóm 6: API & Backend](#-nhóm-6-api--backend)
- [🧪 Nhóm 7: Testing & Quality](#-nhóm-7-testing--quality)
- [📝 Nhóm 8: Planning & Documentation](#-nhóm-8-planning--documentation)

---

## 🏗️ Nhóm 1: Kiến Trúc & Thiết Kế

### [03_software-architecture](.agent/skills/03_software-architecture/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 4 |
| **Mô tả** | Thiết kế kiến trúc Local-first + Optional Cloud, đảm bảo scalability |

### [04_database-design](.agent/skills/04_database-design/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP |
| **Mô tả** | SQLite schema design, indexing strategy cho video metadata |

### [11_architecture-decision-records](.agent/skills/11_architecture-decision-records/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | Ghi chép các quyết định quan trọng (Flutter vs RN, H.264 vs H.265...) |

---

## 📱 Nhóm 2: Phát Triển Mobile (Flutter)

### [01_flutter-expert](.agent/skills/01_flutter-expert/SKILL.md) ⭐ **QUAN TRỌNG NHẤT**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 2 |
| **Mô tả** | Framework chính cho mobile, Dart 3, state management, camera plugin, platform channels |

### [02_mobile-design](.agent/skills/02_mobile-design/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 2 |
| **Mô tả** | Mobile-first design, touch interaction, platform conventions (iOS/Android) |

---

## 💻 Nhóm 3: Phát Triển Desktop & Web

### [08_typescript-pro](.agent/skills/08_typescript-pro/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | Phase 3 |
| **Mô tả** | Electron app viết bằng TypeScript, async patterns |

### [16_browser-extension-builder](.agent/skills/16_browser-extension-builder/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐ |
| **Phase áp dụng** | Future |
| **Mô tả** | Chromium engine knowledge, WebRTC, MediaRecorder API |

---

## 🎬 Nhóm 4: Video & Media Processing

### [17_video-encoding-mobile](.agent/skills/17_video-encoding-mobile/SKILL.md) 🆕 **CUSTOM SKILL**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 3 |
| **Mô tả** | H.264/H.265 encoding, MediaCodec (Android), VideoToolbox (iOS), Fragmented MP4 |

**Nội dung chính:**
- Codec selection (H.264 Baseline Profile)
- Platform channels cho native encoding
- Fragmented MP4 cho crash-safe recording
- Recommended settings: 720p, 2-4 Mbps, Keyframe mỗi 2s

---

## 🔌 Nhóm 5: Hardware Integration

### [18_barcode-scanning-integration](.agent/skills/18_barcode-scanning-integration/SKILL.md) 🆕 **CUSTOM SKILL**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP |
| **Mô tả** | Google ML Kit integration, continuous scan mode, hybrid camera workflow |

**Nội dung chính:**
- ML Kit barcode scanning (QR, Code128, EAN-13)
- Continuous scan với duplicate detection
- Hybrid workflow: Scan + Record đồng thời
- Audio feedback integration

### [19_bluetooth-hid-integration](.agent/skills/19_bluetooth-hid-integration/SKILL.md) 🆕 **CUSTOM SKILL**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 3 |
| **Mô tả** | Bluetooth scanner pairing, HID keyboard mode, hidden TextField strategy |

**Nội dung chính:**
- Hidden TextField strategy cho Flutter
- RawKeyboardListener pattern
- Connection state management
- Recommended scanner models (Netum C750, Inateck BCST-70)

### [20_rtsp-ip-camera](.agent/skills/20_rtsp-ip-camera/SKILL.md) 🆕 **CUSTOM SKILL**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | Phase 3 |
| **Mô tả** | RTSP stream decoding, multi-camera management, FFmpeg/GStreamer |

**Nội dung chính:**
- FFmpeg integration cho Electron
- Multi-camera recording manager
- Camera discovery (ONVIF)
- Low-latency streaming với WebRTC

---

## 🔧 Nhóm 6: API & Backend

### [09_api-design-principles](.agent/skills/09_api-design-principles/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐ |
| **Phase áp dụng** | Phase 4 |
| **Mô tả** | REST API design cho cloud sync, metadata synchronization |

---

## 🧪 Nhóm 7: Testing & Quality

### [05_error-handling-patterns](.agent/skills/05_error-handling-patterns/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP |
| **Mô tả** | Hardware error handling, graceful degradation, camera/scanner disconnection |

### [06_testing-patterns](.agent/skills/06_testing-patterns/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | MVP |
| **Mô tả** | TDD workflow, unit tests cho business logic |

### [10_debugging-strategies](.agent/skills/10_debugging-strategies/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | Debug camera issues, iOS restrictions, Android compatibility |

### [15_clean-code](.agent/skills/15_clean-code/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | Coding standards, naming conventions |

### [21_performance-optimization](.agent/skills/21_performance-optimization/SKILL.md) 🆕 **CUSTOM SKILL**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 3 |
| **Mô tả** | Mobile performance optimization, profiling, memory management, battery optimization |

**Nội dung chính:**
- Flutter performance profiling (CPU, memory, frame rate)
- Camera preview optimization
- Video encoding efficiency
- Battery consumption monitoring
- SQLite query optimization
- Memory leak detection

### [22_mobile-security](.agent/skills/22_mobile-security/SKILL.md) 🆕 **INSTALLED**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 4 |
| **Mô tả** | Mobile security best practices, Flutter security, data protection, OWASP MASVS |

**Nội dung chính:**
- SQLite encryption và secure local storage
- Flutter platform channel security
- Biometric authentication (Touch ID, Face ID)
- Camera/sensor permission security
- Certificate pinning (cho Cloud Sync)
- Data protection và privacy compliance
- Screenshot protection
- Root/jailbreak detection

---

## 🎨 Nhóm 8: UI/UX Design

### [23_ui-ux-pro-max](.agent/skills/23_ui-ux-pro-max/SKILL.md) 🆕 **INSTALLED**
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | MVP → Phase 4 |
| **Mô tả** | 50+ styles, 97 color palettes, Flutter stack support, Material Design |

**Nội dung chính:**
- Color palettes cho mobile apps
- Typography và font pairings
- Dark mode implementation
- Accessibility (WCAG) guidelines
- Flutter-specific UI patterns
- Touch target sizing (44x44px minimum)
- Responsive layout principles

---

## 📝 Nhóm 9: Planning & Documentation

### [07_plan-writing](.agent/skills/07_plan-writing/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | Lập kế hoạch chi tiết cho từng Phase |

### [12_brainstorming](.agent/skills/12_brainstorming/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | Design thinking trước khi implement từng feature |

### [13_product-manager-toolkit](.agent/skills/13_product-manager-toolkit/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | PRD templates, RICE prioritization, feature backlog |

### [14_documentation-templates](.agent/skills/14_documentation-templates/SKILL.md)
| Thuộc tính | Giá trị |
|------------|---------|
| **Mức độ quan trọng** | ⭐⭐ |
| **Phase áp dụng** | Toàn bộ |
| **Mô tả** | README, API docs, user guides |

---

## 📊 Tổng Hợp Theo Phase

### Phase 1 - MVP (Android Mobile)

| # | Skill | Mục đích |
|---|-------|----------|
| 1 | `01_flutter-expert` | Core development |
| 2 | `02_mobile-design` | UI/UX |
| 3 | `17_video-encoding-mobile` | Video recording |
| 4 | `18_barcode-scanning-integration` | Order scanning |
| 5 | `19_bluetooth-hid-integration` | External scanners |
| 6 | `04_database-design` | SQLite storage |
| 7 | `05_error-handling-patterns` | Robustness |
| 8 | `06_testing-patterns` | Quality |
| 9 | `21_performance-optimization` | Performance profiling |

### Phase 2 - iOS Port

| # | Skill | Mục đích |
|---|-------|----------|
| 1 | `01_flutter-expert` | iOS platform |
| 2 | `17_video-encoding-mobile` | VideoToolbox |
| 3 | `10_debugging-strategies` | iOS restrictions |

### Phase 3 - Desktop (Electron)

| # | Skill | Mục đích |
|---|-------|----------|
| 1 | `08_typescript-pro` | Electron app |
| 2 | `20_rtsp-ip-camera` | IP camera |
| 3 | `19_bluetooth-hid-integration` | USB scanners |

### Phase 4 - Cloud Sync

| # | Skill | Mục đích |
|---|-------|----------|
| 1 | `09_api-design-principles` | REST API |
| 2 | `03_software-architecture` | Cloud integration |

---

## 🔧 Hướng Dẫn Sử Dụng

### Khi Bắt Đầu Feature Mới

1. Xem danh sách skills liên quan theo Phase
2. Đọc nội dung SKILL.md tương ứng
3. Áp dụng patterns và best practices
4. Tham khảo code examples trong skill

### Khi Gặp Vấn Đề

```
Camera issues → 17_video-encoding-mobile + 10_debugging-strategies
Scanner issues → 18_barcode-scanning + 19_bluetooth-hid-integration
Architecture → 03_software-architecture + 11_architecture-decision-records
Testing → 06_testing-patterns + 05_error-handling-patterns
```

### Thêm Skill Mới

1. Tạo folder: `XX_skill-name` (XX = số thứ tự tiếp theo)
2. Tạo file `SKILL.md` với YAML frontmatter
3. Cập nhật file này (PROJECT_SKILLS.md)

---

## 📁 Cấu Trúc Thư Mục

```
.agent/skills/
├── 01_flutter-expert/
│   └── SKILL.md
├── 02_mobile-design/
│   └── SKILL.md (+ examples/)
├── 03_software-architecture/
│   └── SKILL.md
├── 04_database-design/
│   └── SKILL.md (+ templates/)
├── 05_error-handling-patterns/
│   └── SKILL.md
├── 06_testing-patterns/
│   └── SKILL.md
├── 07_plan-writing/
│   └── SKILL.md
├── 08_typescript-pro/
│   └── SKILL.md
├── 09_api-design-principles/
│   └── SKILL.md
├── 10_debugging-strategies/
│   └── SKILL.md
├── 11_architecture-decision-records/
│   └── SKILL.md
├── 12_brainstorming/
│   └── SKILL.md
├── 13_product-manager-toolkit/
│   └── SKILL.md
├── 14_documentation-templates/
│   └── SKILL.md
├── 15_clean-code/
│   └── SKILL.md
├── 16_browser-extension-builder/
│   └── SKILL.md
├── 17_video-encoding-mobile/       🆕 CUSTOM
│   └── SKILL.md
├── 18_barcode-scanning-integration/ 🆕 CUSTOM
│   └── SKILL.md
├── 19_bluetooth-hid-integration/    🆕 CUSTOM
│   └── SKILL.md
├── 20_rtsp-ip-camera/               🆕 CUSTOM
│   └── SKILL.md
├── 21_performance-optimization/     🆕 CUSTOM
│   └── SKILL.md
├── 22_mobile-security/              🆕 INSTALLED
│   └── SKILL.md
└── 23_ui-ux-pro-max/                🆕 INSTALLED
    └── SKILL.md
```

---

> 💡 **Tip:** Sử dụng Ctrl+Click để mở trực tiếp các file SKILL.md trong VSCode/Cursor

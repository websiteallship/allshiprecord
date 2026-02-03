# Allship Record

> Video recording tool for e-commerce order packing evidence.

[![Flutter](https://img.shields.io/badge/Flutter-3.0+-blue.svg)](https://flutter.dev)
[![Dart](https://img.shields.io/badge/Dart-3.0+-blue.svg)](https://dart.dev)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)]()

---

## 📖 Mô tả

**Allship Record** là ứng dụng quay video đóng gói hàng hóa cho các shop bán hàng online. Video được gắn với mã vận đơn để làm bằng chứng giải quyết tranh chấp với khách hàng và đơn vị vận chuyển.

### Tính năng chính

- 📹 **Quay video đóng gói** - Ghi lại quá trình đóng hàng
- 🔍 **Quét mã vận đơn** - Tự động nhận diện và gắn với video
- 🔗 **Máy quét Bluetooth HID** - Hỗ trợ scanner không dây chuyên dụng
- 📂 **Tra cứu nhanh** - Tìm video theo mã đơn trong giây lát
- 💾 **Lưu trữ local-first** - Video lưu ngay trên thiết bị
- 📊 **Thống kê** - Dashboard tổng quan hoạt động

---

## 🚀 Getting Started

### Prerequisites

- Flutter SDK >= 3.0.0
- Dart SDK >= 3.0.0
- Android Studio / VS Code
- Android SDK (API 21+) cho Android
- Xcode (12+) cho iOS

### Installation

1. **Clone repository**

```bash
git clone https://github.com/allship/allship-record.git
cd allship-record
```

2. **Install dependencies**

```bash
flutter pub get
```

3. **Generate localization files**

```bash
flutter gen-l10n
```

4. **Run the app**

```bash
# Debug mode
flutter run

# Release mode
flutter run --release
```

---

## 📱 Platforms Supported

| Platform | Status | Min Version |
|---|---|---|
| Android | ✅ Supported | API 21 (Android 5.0) |
| iOS | ✅ Supported | iOS 12.0 |
| Web | ❌ Not planned | - |
| Desktop | ❌ Not planned | - |

---

## 🏗 Project Structure

```
lib/
├── main.dart                    # Entry point
├── app.dart                     # MaterialApp configuration
│
├── core/                        # Shared code
│   ├── constants/               # Constants
│   ├── extensions/              # Dart extensions
│   ├── theme/                   # Theme, colors, typography
│   ├── utils/                   # Utilities
│   └── widgets/                 # Reusable widgets
│
├── data/                        # Data layer
│   ├── datasources/             # Data sources
│   ├── models/                  # Data models
│   └── repositories/            # Repository implementations
│
├── domain/                      # Business logic
│   ├── entities/                # Domain entities
│   ├── repositories/            # Repository interfaces
│   └── usecases/                # Use cases
│
├── features/                    # Feature modules
│   ├── camera/                  # Recording feature
│   ├── history/                 # Video history
│   ├── scanner/                 # Barcode scanning
│   ├── settings/                # Settings
│   └── onboarding/              # First-time flow
│
└── l10n/                        # Localization
    └── intl_vi.arb              # Vietnamese strings
```

---

## 🧪 Running Tests

```bash
# Run all tests
flutter test

# Run with coverage
flutter test --coverage

# Run specific test
flutter test test/features/camera/camera_bloc_test.dart
```

---

## 📦 Build

### Android

```bash
# APK (debug)
flutter build apk --debug

# APK (release)
flutter build apk --release

# App Bundle (for Play Store)
flutter build appbundle --release
```

### iOS

```bash
# Build for iOS (release)
flutter build ios --release

# Open in Xcode for archive
open ios/Runner.xcworkspace
```

---

## 📚 Documentation

Tài liệu chi tiết tại thư mục `docs/`:

| Folder | Nội dung |
|---|---|
| `01_overview/` | Tổng quan dự án |
| `02_architecture/` | Kiến trúc, database, navigation |
| `03_features/` | Spec từng tính năng |
| `07_ui-ux/` | UI components, theme, localization |
| `08_error-handling/` | Mã lỗi và xử lý |
| `10_development/` | Folder structure, assets |

---

## 🛠 Development Workflows

Sử dụng các workflow có sẵn:

```bash
# Khởi tạo dự án mới
# Xem .agent/workflows/01_init-flutter.md

# Thêm tính năng mới
# Xem .agent/workflows/04_add-feature.md

# Sửa lỗi
# Xem .agent/workflows/05_fix-bug.md

# Build và release
# Xem .agent/workflows/06_release.md
```

---

## 📋 AI Development Rules

⚠️ **Quan trọng cho AI agents:**

Trước khi phát triển tính năng, **BẮT BUỘC** đọc:

1. `.ai/project_brief.md` - Hiểu dự án
2. `.ai/feature_backlog.md` - Feature ID
3. `docs/03_features/[feature].md` - Spec chi tiết
4. `docs/07_ui-ux/ui-components.md` - Components có sẵn
5. `.agent/rules/` - Rules liên quan

Xem chi tiết: `.agent/rules/00_ai-context-requirements.md`

---

## 🧠 AI Skills Installation

Dự án sử dụng **AI Skills** từ [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) để mở rộng khả năng của AI agents.

### Cài đặt Skills

**Bước 1:** Clone skills repository vào thư mục `.agent/skills/`

```bash
# Từ thư mục gốc của dự án
git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

**Bước 2:** Xóa thư mục `.git` của skills (để tránh embedded repo)

```bash
# Windows
Remove-Item -Recurse -Force .agent/skills/.git

# macOS/Linux
rm -rf .agent/skills/.git
```

**Bước 3:** Verify cài đặt

```bash
# Kiểm tra số lượng skills
ls .agent/skills
```

### Danh sách Skills đã cài đặt

Xem chi tiết tại: [`.agent/PROJECT_SKILLS.md`](.agent/PROJECT_SKILLS.md)

| Nhóm | Skills | Mô tả |
|---|---|---|
| 🏗️ Architecture | 3 skills | Software architecture, database design |
| 📱 Mobile | 2 skills | Flutter expert, mobile design |
| 🎬 Video | 1 skill | Video encoding (H.264, fMP4) |
| 🔌 Hardware | 3 skills | Barcode scanning, Bluetooth HID, RTSP |
| 🧪 Testing | 5 skills | Error handling, testing, debugging |
| 🎨 UI/UX | 1 skill | 50+ styles, 97 color palettes |
| 📝 Planning | 4 skills | Documentation, brainstorming |

**Tổng: 23 skills**

### Sử dụng Skills

AI agents sẽ tự động nhận diện và sử dụng skills khi:
- Phát triển tính năng mới
- Debug vấn đề
- Thiết kế kiến trúc
- Viết documentation

---

## 👥 Team

- **Project Owner**: Allship Team
- **Development**: AI-assisted development

---

## 📄 License

Proprietary - All rights reserved.

---

## 🔗 Links

- [Documentation](./docs/)
- [Changelog](./CHANGELOG.md)
- [Feature Backlog](./.ai/feature_backlog.md)

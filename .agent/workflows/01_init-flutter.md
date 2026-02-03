---
description: Khởi tạo dự án Flutter mới với cấu trúc chuẩn
---

# Khởi tạo Dự án Flutter

## Bước 1: Tạo Flutter App
// turbo
```bash
flutter create --org com.allship ecombox_app
```

## Bước 2: Tạo Cấu trúc Thư mục
Tạo cấu trúc feature-based:
```
lib/
├── core/
│   ├── constants/
│   ├── theme/
│   ├── utils/
│   └── widgets/
├── features/
│   ├── recording/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   ├── scanning/
│   └── history/
└── main.dart
```

## Bước 3: Thêm Dependencies
Sửa `pubspec.yaml`:
```yaml
dependencies:
  flutter_bloc: ^8.1.0
  sqflite: ^2.3.0
  camera: ^0.10.5
  google_mlkit_barcode_scanning: ^0.10.0
  path_provider: ^2.1.0

dev_dependencies:
  flutter_lints: ^3.0.0
  mockito: ^5.4.0
  build_runner: ^2.4.0
```

## Bước 4: Cài Packages
// turbo
```bash
flutter pub get
```

## Bước 5: Kiểm tra
// turbo
```bash
flutter doctor
flutter run
```

---
description: Build và chạy ứng dụng Flutter
---

# Build Ứng dụng Flutter

## Yêu cầu
- Flutter SDK đã cài và có trong PATH
- Thiết bị Android đã kết nối hoặc emulator đang chạy

## Bước 1: Kiểm tra Môi trường
// turbo
```bash
flutter doctor
```

## Bước 2: Cài Dependencies
// turbo
```bash
flutter pub get
```

## Bước 3: Chạy App (Debug)
```bash
flutter run
```

## Bước 4: Build APK Release (Tùy chọn)
```bash
flutter build apk --release
```
Output: `build/app/outputs/flutter-apk/app-release.apk`

## Bước 5: Cài lên Thiết bị (Tùy chọn)
```bash
flutter install
```

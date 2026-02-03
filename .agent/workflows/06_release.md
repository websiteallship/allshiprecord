---
description: Chuẩn bị phiên bản release mới
---

# Phát hành Phiên bản (Release)

## Bước 1: Kiểm tra Trước khi Release
1. Đảm bảo tất cả tests pass: `/03_run-tests`.
2. Review `CHANGELOG.md` - đã ghi đủ thay đổi chưa?
3. Tăng version trong `pubspec.yaml`.

## Bước 2: Cập nhật Changelog
1. Đổi `[Unreleased]` thành `[X.Y.Z] - YYYY-MM-DD`.
2. Thêm section `[Unreleased]` mới ở đầu file.

## Bước 3: Build Release
// turbo
```bash
flutter build apk --release
```

## Bước 4: Tag Git
```bash
git add .
git commit -m "Release vX.Y.Z"
git tag vX.Y.Z
git push origin main --tags
```

## Bước 5: Phân phối
- Upload APK lên kênh test nội bộ (Google Drive, Firebase).
- Thông báo cho testers.

## Bước 6: Cập nhật AI Context
1. Cập nhật `.ai/active_state.md` với mục tiêu mới.
2. Ghi log release vào `.ai/work_log.md`.

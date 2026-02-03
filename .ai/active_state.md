# Active State

## Current Phase: Phase 1 (MVP - Android)
**Goal:** Xây dựng Core App chạy trên Android để test thực tế tại shop nhỏ.

## Active Tasks
- [x] Thiết kế kiến trúc & Documentation (Done).
- [x] App Theme & Design System (Done).
- [x] Folder Structure & Navigation (Done).
- [x] State Management (BLoC) Architecture (Done).
- [x] Localization Strings (Vietnamese) (Done).
- [x] Assets Structure & Project Files (Done).
- [ ] **[NEXT]** Setup dự án Flutter (Init project).
- [ ] Implement: Camera Preview & Recording Logic (Basic).
- [ ] Implement: Barcode Scanning (ML Kit).
- [ ] Implement: Database (SQLite) & File Management.
- [ ] UI: Màn hình Scan & History.

## Known Issues / Blockers
- Chưa có source code Flutter.
- Cần verify performance `camera` + `google_mlkit_barcode_scanning` chạy đồng thời.

## Recent Context
- Đã hoàn thành toàn bộ documentation framework.
- Đã chốt Tech Stack: Flutter + H.264 + SQLite + BLoC.
- **Ready to init Flutter project!**

## Recent Updates (2024-02-04)
- ✅ Tạo `docs/07_ui-ux/app-theme.md` - Design System hoàn chỉnh.
- ✅ Tạo `docs/10_development/folder-structure.md` - lib/ structure.
- ✅ Tạo `docs/02_architecture/navigation.md` - Routes & deep links.
- ✅ Tạo `docs/02_architecture/state-management.md` - BLoC pattern.
- ✅ Tạo `docs/07_ui-ux/localization-strings.md` - ~151 strings tiếng Việt.
- ✅ Tạo `docs/10_development/assets-structure.md` - Fonts, sounds, images.
- ✅ Tạo `docs/10_development/environment-config.md` - Dev/Prod config.
- ✅ Tạo `.gitignore` - Flutter standard ignores.
- ✅ Tạo `README.md` - Project overview & setup guide.
- ✅ Tạo `.agent/rules/00_ai-context-requirements.md` - AI development rule.

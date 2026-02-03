---
description: Quy trình chuẩn để thêm tính năng mới
---

# Thêm Tính năng Mới

## Bước 0: Ghi nhận Feature
1. Kiểm tra `.ai/feature_backlog.md` - feature đã có ID chưa?
2. Nếu chưa có, thêm vào bảng Backlog với ID mới (F007, F008...).
3. Di chuyển feature sang bảng "In Progress".

## Bước 1: Xác định Yêu cầu
1. Đọc mô tả tính năng từ `docs/03_features/`.
2. Xác định workflow liên quan trong `docs/04_workflows/`.
3. Hỏi lại user nếu chưa rõ.

## Bước 2: Lập Kế hoạch
1. Cập nhật `.ai/active_state.md` với task mới.
2. Liệt kê các file cần tạo hoặc sửa.
3. Xác định dependencies (packages, APIs).

## Bước 3: Triển khai
1. Tạo thư mục feature: `lib/features/{tên_feature}/`
   - `data/` - Repositories, Data Sources
   - `domain/` - Entities, Use Cases
   - `presentation/` - BLoC, Widgets, Pages
2. Viết code theo `docs/10_development/coding-conventions.md`.
3. Thêm unit tests trong `test/features/{tên_feature}/`.

## Bước 4: Kiểm tra
1. Chạy `/03_run-tests`.
2. Test thủ công trên thiết bị.

## Bước 5: Ghi chép
1. Cập nhật `CHANGELOG.md` mục `[Unreleased]` -> `Added`.
2. Cập nhật `.ai/work_log.md`.
3. Chạy `/08_update-ai-context`.

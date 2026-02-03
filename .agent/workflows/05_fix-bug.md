---
description: Quy trình chuẩn để sửa lỗi
---

# Sửa Lỗi (Fix Bug)

## Bước 1: Tái hiện Lỗi
1. Lấy các bước để tái hiện lỗi.
2. Xác định component bị ảnh hưởng (Camera, Scanner, DB, UI).
3. Kiểm tra `docs/08_error-handling/` để tìm chiến lược xử lý.

## Bước 2: Điều tra
1. Dùng logging để trace vấn đề.
2. Kiểm tra các thay đổi gần đây trong `CHANGELOG.md`.
3. Review code trong thư mục feature liên quan.

## Bước 3: Sửa
1. Viết test case tái hiện bug (phải fail).
2. Sửa code.
3. Chạy test để xác nhận đã pass.

## Bước 4: Kiểm tra
1. Chạy `/03_run-tests` để đảm bảo không có regression.
2. Test thủ công trên thiết bị.

## Bước 5: Ghi chép
1. Cập nhật `CHANGELOG.md` mục `[Unreleased]` -> `Fixed`.
2. Thêm ghi chú vào `.ai/work_log.md`.
3. Nếu lỗi do thiếu docs, cập nhật tài liệu liên quan.

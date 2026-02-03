---
description: Cập nhật AI context và lịch sử dự án sau mỗi task
---

# Cập nhật AI Context

Chạy workflow này sau mỗi task hoặc phiên làm việc.

## Bước 1: Cập nhật Active State
1. Đọc `.ai/active_state.md`.
2. Đánh dấu `[x]` các task đã hoàn thành.
3. Thêm task mới phát hiện trong phiên làm việc.

## Bước 2: Cập nhật Changelog
1. Đọc `CHANGELOG.md`.
2. Thêm bullet point vào `[Unreleased]` mô tả công việc đã làm.
   - Ví dụ: `- Added continuous scan mode logic.`
3. Nếu là bản release, cập nhật version và ngày.

## Bước 3: Ghi Log Phiên làm việc
1. Đọc `.ai/work_log.md`.
2. Thêm entry mới với ngày/giờ hiện tại.
3. Tóm tắt:
   - **Context:** Tại sao bắt đầu phiên này?
   - **Actions:** Đã tạo/sửa file nào?
   - **Results:** Kết quả ra sao?
   - **Next:** Bước tiếp theo là gì?

## Bước 4: Kiểm tra
1. Xem `task.md` có cần cập nhật không.
2. Đảm bảo không có thông tin quan trọng bị bỏ sót.

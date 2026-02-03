---
description: Quy tắc cho Pre-recording Buffer
globs: ["**/features/recording/**", "**/camera/**"]
---

# Pre-recording Buffer Rules

## 1. Mục đích
Ghi trước 3-5 giây video để không bỏ lỡ khoảnh khắc đầu tiên khi cầm hàng lên.

## 2. Cấu hình Buffer

| Platform | Kích thước Buffer | Lý do |
|---|---|---|
| Mobile | 3 giây | Tiết kiệm RAM/pin |
| Desktop | 5 giây | Có nhiều tài nguyên hơn |

## 3. Kỹ thuật

### Mobile (Flutter)
- Sử dụng `camera` package.
- Ghi vào temp file liên tục.
- Khi scan → Copy buffer + tiếp tục quay.
- Xóa temp file sau mỗi session.

### Desktop (Electron)
- Sử dụng MediaRecorder với `timeslice: 1000` (1 chunk/giây).
- Giữ 5 chunks cuối trong memory.
- Khi scan → Concat chunks + tiếp tục.

## 4. Xử lý Memory

### PHẢI
- ✅ Giới hạn buffer size cố định.
- ✅ Xóa temp files khi app đóng.
- ✅ Fallback nếu không đủ RAM.

### KHÔNG
- ❌ Buffer vô hạn (memory leak).
- ❌ Ghi buffer khi app ở background (iOS sẽ kill).

## 5. User Control

Cho phép user tắt tính năng này trong Settings:
```
[ ] Ghi trước 3 giây (Pre-recording Buffer)
    Tốn thêm ~10MB RAM khi chờ quét.
```

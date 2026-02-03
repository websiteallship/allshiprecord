# Bảng Mã Lỗi (Error Codes)

Danh sách mã lỗi chuẩn để debug và support.

## Camera Errors (E1xx)

| Code | Tên | Mô tả | Giải pháp |
|---|---|---|---|
| E100 | CAMERA_NOT_FOUND | Không tìm thấy camera | Kiểm tra kết nối, cấp quyền |
| E101 | CAMERA_PERMISSION_DENIED | Chưa cấp quyền camera | Vào Settings → Cấp quyền |
| E102 | CAMERA_IN_USE | Camera đang được app khác sử dụng | Đóng app khác |
| E103 | CAMERA_DISCONNECTED | Mất kết nối camera khi đang quay | Kiểm tra cáp, retry |
| E104 | CAMERA_ENCODING_FAILED | Lỗi encode video | Giảm resolution, restart app |

## Scanner Errors (E2xx)

| Code | Tên | Mô tả | Giải pháp |
|---|---|---|---|
| E200 | SCANNER_NOT_PAIRED | Scanner chưa được pair | Vào Bluetooth Settings |
| E201 | SCANNER_DISCONNECTED | Mất kết nối scanner | Kiểm tra pin, khoảng cách |
| E202 | SCANNER_INVALID_INPUT | Mã quét không hợp lệ | Kiểm tra format mã |
| E203 | SCANNER_DUPLICATE | Quét trùng mã đang xử lý | Bỏ qua hoặc đổi đơn |

## Storage Errors (E3xx)

| Code | Tên | Mô tả | Giải pháp |
|---|---|---|---|
| E300 | STORAGE_FULL | Hết dung lượng | Dọn dẹp hoặc thêm storage |
| E301 | STORAGE_WRITE_FAILED | Không ghi được file | Kiểm tra quyền, dung lượng |
| E302 | STORAGE_READ_FAILED | Không đọc được file | File bị corrupt |
| E303 | STORAGE_FILE_NOT_FOUND | Không tìm thấy video | File đã bị xóa |

## Database Errors (E4xx)

| Code | Tên | Mô tả | Giải pháp |
|---|---|---|---|
| E400 | DB_CORRUPTED | Database bị hỏng | Restore từ backup |
| E401 | DB_QUERY_FAILED | Truy vấn thất bại | Restart app |
| E402 | DB_MIGRATION_FAILED | Upgrade DB thất bại | Clear data, reinstall |

## Network Errors (E5xx)

| Code | Tên | Mô tả | Giải pháp |
|---|---|---|---|
| E500 | NETWORK_OFFLINE | Không có mạng | Kiểm tra WiFi/4G |
| E501 | SYNC_FAILED | Sync cloud thất bại | Retry sau |
| E502 | API_TIMEOUT | API không phản hồi | Thử lại sau |

## Sử dụng trong Code

```dart
// Dart/Flutter
throw AppException(
  code: 'E103',
  message: 'Camera disconnected during recording',
  context: {'video_id': currentVideoId, 'duration': currentDuration},
);
```

```typescript
// TypeScript/Electron
throw new AppError('E301', 'Storage write failed', { path: filePath });
```

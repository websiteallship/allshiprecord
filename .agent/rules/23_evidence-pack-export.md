---
description: Quy tắc cho Evidence Pack Export
globs: ["**/features/export/**", "**/evidence/**"]
---

# Evidence Pack Export Rules

## 1. Cấu trúc ZIP bắt buộc

```
{ORDER_CODE}_evidence.zip
├── video_packing.mp4       # Video đóng gói (nếu có)
├── video_return.mp4        # Video hoàn hàng (nếu có)
├── thumbnail_packing.jpg   # Thumbnail
├── thumbnail_return.jpg
├── metadata.json           # Thông tin chi tiết
└── README.txt              # Hướng dẫn cho người nhận
```

## 2. Format metadata.json

```json
{
  "order_code": "VN987654321",
  "marketplace": "shopee",
  "seller_id": "shop_abc",
  "events": [
    {
      "type": "packing",
      "datetime_utc": "2026-02-01T03:30:00Z",
      "datetime_local": "2026-02-01T10:30:00+07:00",
      "duration_seconds": 45,
      "location": {"lat": 21.0285, "lng": 105.8542},
      "device": "Samsung Galaxy A54",
      "app_version": "1.0.0"
    }
  ],
  "exported_at": "2026-02-03T09:00:00Z",
  "checksum_sha256": "abc123..."
}
```

## 3. Tính toàn vẹn dữ liệu

### Checksum
- Tính SHA256 cho mỗi video file.
- Lưu trong metadata.json.
- Sàn TMĐT có thể verify file chưa bị sửa.

### Không chỉnh sửa
- ❌ KHÔNG re-encode video (giữ nguyên file gốc).
- ❌ KHÔNG crop/trim.
- ❌ KHÔNG thêm filter.

## 4. Kích thước tối ưu

### Nén video trước khi export (tùy chọn)
- Chỉ nén nếu user yêu cầu (checkbox).
- Target: 720p, ~1MB/phút.
- Giữ file gốc không nén.

## 5. Chia sẻ

### Hỗ trợ các kênh
- Share Sheet (Android/iOS native).
- Copy to clipboard (file path).
- Upload lên cloud (nếu đã setup).

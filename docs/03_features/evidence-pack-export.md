# Evidence Pack Export

## Mô tả
Xuất gói bằng chứng hoàn chỉnh (Evidence Pack) để gửi cho sàn TMĐT khi khiếu nại.

## Use Case
1. Khách hàng claim "Hàng hư hỏng khi nhận".
2. Seller cần gửi bằng chứng cho Shopee/Lazada support.
3. Thay vì gửi từng file, xuất 1 gói ZIP chứa tất cả.

## Cấu trúc Evidence Pack

```
VN987654321_evidence.zip
├── video_packing.mp4           # Video đóng gói
├── video_return.mp4            # Video nhận hoàn (nếu có)
├── thumbnail_packing.jpg       # Ảnh thumbnail
├── thumbnail_return.jpg
├── metadata.json               # Thông tin chi tiết
└── timeline.txt                # Mô tả timeline sự kiện
```

## Nội dung metadata.json

```json
{
  "order_code": "VN987654321",
  "marketplace": "shopee",
  "events": [
    {
      "type": "packing",
      "datetime": "2026-02-01T10:30:00+07:00",
      "duration_seconds": 45,
      "device": "Samsung Galaxy A54"
    },
    {
      "type": "return",
      "datetime": "2026-02-03T14:15:00+07:00",
      "duration_seconds": 120,
      "status": "damaged",
      "notes": "Vỡ góc hộp, sản phẩm bị trầy"
    }
  ],
  "exported_at": "2026-02-03T16:00:00+07:00",
  "app_version": "1.0.0"
}
```

## Ưu tiên
**P2** - Nice to have cho Phase 2-3.

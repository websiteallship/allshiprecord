# QR Code trên Video

## Mô tả
Tạo QR Code chứa link đến video bằng chứng, có thể in lên label/phiếu giao hàng để khách hàng hoặc shipper scan xem ngay.

## Use Cases

1. **In lên phiếu giao hàng**: Khách scan → Xem video đóng gói.
2. **Gửi cho sàn TMĐT**: QR link trong khiếu nại.
3. **Internal tracking**: Nhân viên scan kiểm tra nhanh.

## Cấu trúc QR Data

### Option A: Deep Link (Khuyến nghị)
```
allshiprecord://video/VN987654321
```
- App cài sẵn sẽ mở video.
- Không cần upload cloud.

### Option B: Cloud Link
```
https://allship.vn/v/abc123
```
- Cần upload video lên cloud.
- Ai cũng xem được (không cần app).

## Kỹ thuật triển khai

### Generate QR
```yaml
dependencies:
  qr_flutter: ^4.1.0
```

```dart
QrImageView(
  data: 'allshiprecord://video/$orderCode',
  version: QrVersions.auto,
  size: 100.0,
)
```

### In QR
- Export ảnh PNG.
- Tích hợp Bluetooth printer (ESC/POS).
- Hoặc share qua app khác để in.

## Ưu tiên
**P1** - Phase 2.

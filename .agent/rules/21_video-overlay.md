---
description: Quy tắc cho Video Overlay (Timestamp + Location)
globs: ["**/features/recording/**", "**/video/**"]
---

# Video Overlay Rules

## 1. Thông tin bắt buộc hiển thị

Mỗi video PHẢI có overlay chứa:
- **Timestamp**: Format `dd/MM/yyyy HH:mm:ss` (timezone local).
- **Mã đơn hàng**: Order code đang xử lý.

Thông tin **TÙY CHỌN** (user có thể tắt):
- **GPS Location**: `lat, lng` với 6 số thập phân.
- **App version**: `vX.Y.Z`.

## 2. Xử lý Location

### Khi lấy GPS
```dart
// LUÔN set timeout để tránh block UI
final position = await Geolocator.getCurrentPosition(
  desiredAccuracy: LocationAccuracy.high,
  timeLimit: Duration(seconds: 10), // QUAN TRỌNG
);
```

### Fallback Strategy
1. Thử GPS (high accuracy) - timeout 10s.
2. Nếu fail → Network location (lower accuracy).
3. Nếu fail → Last known location.
4. Nếu fail → Hiển thị "N/A".

### KHÔNG BAO GIỜ
- ❌ Block UI chờ GPS.
- ❌ Request background location (tốn pin).
- ❌ Track liên tục trong khi quay.

## 3. Quyền Location

### Giải thích cho User
Khi request quyền, PHẢI giải thích rõ:
> "Allship Record cần vị trí để gắn vào video làm bằng chứng. Vị trí chỉ được lấy 1 lần khi bắt đầu quay, không theo dõi liên tục."

### Khi User từ chối
- App vẫn hoạt động bình thường.
- Overlay hiển thị "📍 Không có vị trí".
- KHÔNG hỏi lại liên tục (chỉ hỏi lại khi user vào Settings).

## 4. Render Overlay

### Vị trí mặc định
- **Góc dưới trái** của video.
- Background bán trong suốt (black 50% opacity).
- Font: Roboto Mono, size 14-16pt.

### Không che nội dung quan trọng
- Overlay PHẢI nằm ngoài vùng center frame.
- User có thể thay đổi vị trí trong Settings.

## 5. Lưu trữ Metadata

Ngoài overlay visible, PHẢI lưu metadata vào:
- **Database**: Cột `gps_lat`, `gps_lng` trong bảng `videos`.
- **File**: Metadata JSON cùng thư mục với video.

```json
{
  "timestamp": "2026-02-04T10:35:47+07:00",
  "location": {
    "lat": 21.028511,
    "lng": 105.854167,
    "accuracy_meters": 10
  }
}
```

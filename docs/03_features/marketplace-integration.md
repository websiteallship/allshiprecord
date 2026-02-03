# Tích hợp API Sàn TMĐT (Marketplace Integration)

## Mô tả
Kết nối trực tiếp với API của Shopee, Lazada, TikTok Shop để:
1. Lấy danh sách đơn hàng cần đóng.
2. Tự động đối chiếu trạng thái đơn hàng.
3. Đẩy link video bằng chứng lên hệ thống khiếu nại.

## Lợi ích

| Tính năng | Không có API | Có API |
|---|---|---|
| Nhập mã đơn | Quét/Gõ tay | Chọn từ danh sách |
| Biết đơn nào cần đóng | Mở app sàn riêng | Xem ngay trong Allship |
| Khiếu nại | Upload video thủ công | 1-click gửi evidence |

## API cần tích hợp

### Shopee Open Platform
- `GET /orders/list` - Lấy danh sách đơn chờ xử lý.
- `GET /orders/detail` - Chi tiết đơn hàng.
- `POST /returns/dispute` - Tạo khiếu nại.

### Lazada Open Platform
- Tương tự Shopee, cần đăng ký Developer Account.

### TikTok Shop
- API còn hạn chế, ưu tiên thấp hơn.

## Yêu cầu kỹ thuật
- OAuth2 authentication.
- Rate limiting handling.
- Token refresh mechanism.
- Secure storage cho API keys.

## Ưu tiên
**P2** - Phase 4 (Enterprise features).

## Rủi ro
- API sàn có thể thay đổi bất cứ lúc nào.
- Cần maintain nhiều integration.
- Phải tuân thủ policy của từng sàn.

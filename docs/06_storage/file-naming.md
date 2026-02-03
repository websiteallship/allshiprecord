# Quy tắc Đặt tên File (Naming Convention)

Để dễ dàng quản lý thủ công (khi cần) và đảm bảo tính duy nhất, tên file video tuân thủ format sau:

```
{order_code}_{type}_{timestamp}_{extra}.mp4
```

## Giải thích thành phần

1.  `{order_code}`: **Mã vận đơn gốc**.
    -   Gữ nguyên các ký tự chữ và số.
    -   Loại bỏ các ký tự đặc biệt nếu hệ điều hành không cho phép (như `/`, `:`, `*`...).
    -   Ví dụ: `SPX038294671`, `VN12345678`.

2.  `{type}`: **Loại video**.
    -   `packing`: Đóng gói hàng đi.
    -   `shipping`: Giao hàng cho bưu tá.
    -   `return`: Nhận hàng hoàn và mở kiểm tra.

3.  `{timestamp}`: **Thời gian**.
    -   Format: `YYYYMMDD_HHmmss`.
    -   Ví dụ: `20260203_103052` (Ngày 03/02/2026, lúc 10 giờ 30 phút 52 giây).
    -   Giúp sắp xếp file theo tên sẽ đúng theo thứ tự thời gian.

4.  `{extra}`: **Thông tin phụ (Optional)**.
    -   Dùng trong trường hợp video bị chia cắt (fragmented) hoặc duplicate.
    -   Ví dụ: `part1`, `part2`.

5.  `.mp4`: **Định dạng file**.

## Các ví dụ chuẩn

-   **Đóng gói:** `SPX038294671_packing_20260203_103052.mp4`
-   **Hoàn trả:** `VN72849301_return_20260215_091200.mp4`
-   **Thumbnail:** `SPX038294671_packing_20260203_103052_thumb.jpg`

## Lợi ích
-   **Tra cứu thủ công:** Nhân viên có thể mở File Explorer, gõ mã đơn vào ô tìm kiếm là ra ngay file video mà không cần mở App.
-   **Chia sẻ:** Khi gửi file đi khiếu nại, tên file đã chứa đủ thông tin ngữ cảnh, không cần đổi tên lại.

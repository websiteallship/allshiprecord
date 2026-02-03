# Tính năng: Xử lý Hàng Hoàn (Return Processing)

Quy trình nhận hàng hoàn trả về kho, kiểm tra tình trạng và đối chiếu với video lúc đóng gói đi.

## 1. Workflow

1.  **Scan:** Quét mã vận đơn của gói hàng hoàn.
2.  **Lookup & Compare:**
    -   Hệ thống tìm kiếm trong Database xem đơn này đã từng được đóng gói đi chưa.
    -   **Nếu có:** Hiển thị thông tin đơn gốc (Ngày đóng, Người đóng) và nút "Xem video đóng gói" để nhân viên so sánh bao bì/quy cách đóng.
    -   **Nếu không:** Báo "Đơn mới/Không tìm thấy dữ liệu gốc" -> Vẫn cho phép quay video nhận hàng.
3.  **Record:** Quay video quá trình mở gói hàng (Unboxing).
    -   Quan trọng: Quay rõ tem niêm phong, tình trạng hộp, và sản phẩm bên trong.
4.  **Tagging (Đánh giá):** Sau khi dừng quay, bắt buộc nhân viên chọn trạng thái:
    -   `[ ] Hàng nguyên vẹn` -> Nhập kho lại.
    -   `[ ] Hàng hư hỏng` -> Chờ khiếu nại.
    -   `[ ] Sai hàng / Tráo hàng` -> Bằng chứng lừa đảo.
    -   `[ ] Thiếu phụ kiện`.
5.  **Save:** Lưu video với `type='return'` và metadata trạng thái.

## 2. Liên kết dữ liệu
Trong Database, video hoàn trả (Return Video) sẽ được link với đơn hàng (Order) đã có sẵn video đóng gói (Packing Video).

```json
// Cấu trúc logic
Order {
  id: "ORDER_123",
  code: "SPX987654321",
  videos: [
    {
      type: "packing",
      url: "/videos/.../packing.mp4",
      created_at: "2026-02-01"
    },
    {
      type: "return",
      url: "/videos/.../return.mp4",
      return_status: "damaged",
      created_at: "2026-02-10"
    }
  ]
}
```

## 3. Xuất bằng chứng (Export Logic)
Khi cần khiếu nại một đơn hàng hoàn bị tráo ruột:
-   Hệ thống cho phép xuất "Bộ bằng chứng" gồm:
    1.  Video đóng gói (Chứng minh lúc đi hàng đúng).
    2.  Video mở hàng hoàn (Chứng minh lúc về hàng sai).
    3.  Hình ảnh thumbnail + Metadata (Mã đơn, thời gian).
-   Tính năng này giúp Seller thắng khiếu nại trên sàn TMĐT với tỷ lệ cao hơn.

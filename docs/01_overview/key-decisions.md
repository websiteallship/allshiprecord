# Các Quyết định Quan trọng (Key Decisions)

Dưới đây là 12 quyết định cốt lõi định hình kiến trúc và sản phẩm:

| # | Quyết định | Lựa chọn | Lý do chính |
|---|---|---|---|
| 1 | **Framework Mobile** | **Flutter** | Performance camera tốt hơn React Native, single codebase cho Android & iOS, hỗ trợ Platform Channels mạnh mẽ để can thiệp sâu vào hardware. |
| 2 | **Framework Desktop** | **Electron** | Camera WebRTC rất mature, ổn định, hỗ trợ multi-camera tốt hơn Flutter Desktop hiện tại. Dễ dàng tích hợp các thư viện JS/Node.js. |
| 3 | **Video Codec** | **H.264** | Tối ưu hóa tuyệt vời cho phần cứng (Mobile & PC), tương thích 100% các trình phát và sàn TMĐT. Không chọn H.265 vì vấn đề bản quyền, hỗ trợ trình duyệt kém hơn và tốn pin hơn khi encoding bằng software fallback. |
| 4 | **Database** | **SQLite** | Nhẹ, nhanh, không cần server cài đặt, truy vấn SQL mạnh mẽ cho việc tra cứu local. Phù hợp hoàn hảo cho mô hình Local-first. |
| 5 | **Mô hình Lưu trữ** | **Local-first** | Giảm chi phí vận hành về 0 cho user cơ bản. Đảm bảo quyền riêng tư. Hoạt động offline 100%. Cloud chỉ dùng để sync metadata hoặc backup khi cần. |
| 6 | **Barcode SDK** | **Google ML Kit** | Miễn phí, độ chính xác cao, tốc độ nhanh, hoạt động offline trên thiết bị di động. |
| 7 | **Scanner Protocol** | **Bluetooth/USB HID** | Chế độ giả lập bàn phím (Keyboard Emulation). Universal, không cần SDK riêng của hãng máy quét, tương thích mọi loại máy quét giá rẻ. |
| 8 | **Workflow Chính** | **Continuous Scan Mode** | Chế độ quét liên tục "Hands-free". Quét mã mới = Tự động dừng video cũ + Lưu + Bắt đầu quay video mới. Giảm thao tác chạm màn hình xuống 0. |
| 9 | **Quy tắc Đặt tên File** | `{order_code}_{type}_{datetime}.mp4` | File tên chứa metadata giúp dễ dàng tìm kiếm, quản lý thủ công bằng File Explorer mà không cần qua App. Dễ dàng chia sẻ file bằng chứng. |
| 10 | **Tổ chức Thư mục** | `/videos/YYYY/MM/DD/` | Phân chia theo thời gian giúp dễ dàng quản lý backup và dọn dẹp (xóa cả tháng/ngày). Tránh việc một thư mục chứa quá nhiều file gây chậm hệ thống. |
| 11 | **MVP Platform** | **Android App** | Phổ biến nhất ở Việt Nam (đặc biệt là các shop vừa và nhỏ), dễ deploy và test hơn iOS. |
| 12 | **Đối tượng MVP** | **Seller nhỏ (BYOD)** | Nhóm khách hàng đông đảo nhất, nhu cầu đơn giản nhất, chấp nhận sử dụng điện thoại cá nhân để tiết kiệm chi phí đầu tư. |

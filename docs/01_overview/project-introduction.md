# Giới thiệu Dự án Allship Record

## Mục tiêu
Xây dựng công cụ chuyên dụng giúp nhà bán hàng (Seller) trên các sàn TMĐT:
1.  **Lưu trữ bằng chứng:** Quay video đóng gói, xuất hàng, và mở hàng hoàn trả để đối soát với đơn vị vận chuyển hoặc sàn TMĐT khi có tranh chấp.
2.  **Tối ưu quy trình:** Giúp nhân viên đóng gói thao tác nhanh, "hands-free" (không chạm màn hình), giảm sai sót.
3.  **Tiết kiệm chi phí:** Sử dụng thiết bị có sẵn (điện thoại cá nhân, PC), lưu trữ local không tốn phí cloud hàng tháng.

## Vấn đề cần giải quyết
-   Các giải pháp hiện tại thường yêu cầu mua phần cứng riêng hoặc trả phí thuê bao hàng tháng (SaaS).
-   Dữ liệu video đẩy lên cloud tốn băng thông và có rủi ro về quyền riêng tư.
-   Quy trình quay video thủ công tốn thời gian, làm chậm tốc độ đóng gói.

## Giải pháp cốt lõi
-   **Local-first:** Dữ liệu lưu trên thiết bị người dùng. Cloud chỉ là tùy chọn (optional).
-   **Hands-free:** Tương tác chủ yếu qua máy quét mã vạch (Barcode Scanner) và âm thanh phản hồi.
-   **Đa nền tảng:** Mobile App (Flutter) cho sự linh hoạt, Desktop App (Electron) cho sự ổn định và quản lý tập trung.

## Phạm vi dự án
-   **Đối tượng:** Seller nhỏ (cá nhân), vừa và lớn.
-   **Tính năng chính:** Quét mã vận đơn -> Tự động quay -> Lưu trữ & Tra cứu.
-   **Hỗ trợ:** Đóng hàng đi (Packing), Giao hàng cho bưu tá (Shipping), Xử lý hàng hoàn (Return).

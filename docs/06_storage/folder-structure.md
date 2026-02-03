# Cấu trúc Thư mục Lưu trữ

Hệ thống tổ chức file theo cấu trúc Cây thời gian (Time-based Tree) để tối ưu hiệu năng hệ thống tệp tin (File System Performance) và dễ dàng quản lý backup/xóa bỏ.

## Cấu trúc Cây

```
/videos/
├── 2026/                       # Năm (Year)
│   ├── 02/                     # Tháng (Month)
│   │   ├── 03/                 # Ngày (Day)
│   │   │   ├── SPX01_packing_20260203_100100.mp4
│   │   │   ├── SPX01_packing_20260203_100100_thumb.jpg
│   │   │   ├── VN02_return_20260203_140000.mp4
│   │   │   └── ...
│   │   ├── 04/
│   │   │   └── ...
│   │   └── ...
│   ├── 03/
│   │   └── ...
│   └── ...
└── ...
```

## Tại sao chọn cấu trúc này?

### 1. Hiệu năng (Performance)
Nếu dồn tất cả file vào 1 thư mục `videos/`, sau 1 năm có thể có tới 100,000 files. Việc liệt kê (listing) và ghi file sẽ rất chậm trên cả Windows (NTFS) và Android.
-> Chia nhỏ theo Ngày giúp mỗi thư mục chỉ chứa khoảng 100-500 files (với shop trung bình), đảm bảo truy xuất cực nhanh.

### 2. Dễ dàng Backup & Archive
Shop thường muốn backup dữ liệu theo tháng.
-> Chỉ cần copy folder `2026/02` ra ổ cứng rời là xong toàn bộ dữ liệu tháng 2.

### 3. Dễ dàng Dọn dẹp (Cleanup)
Nếu muốn xóa dữ liệu cũ hơn 3 tháng?
-> Chỉ cần xóa các folder tháng cũ (ví dụ `2025/11`, `2025/12`). Nhanh hơn nhiều so với việc quét từng file để check ngày tạo.

## Các phương án thay thế đã loại bỏ
-   *Phân theo Mã đơn (videos/SPX123/...):* Tạo ra quá nhiều thư mục con, khó quản lý thời gian.
-   *Phân theo Loại (videos/packing/...):* Vẫn gặp vấn đề số lượng file quá lớn trong 1 folder.

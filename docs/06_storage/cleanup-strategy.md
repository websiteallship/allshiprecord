# Chiến lược Dọn dẹp Lưu trữ (Storage Cleanup)

Vấn đề lớn nhất của hệ thống video là dung lượng. App cần cơ chế tự động dọn dẹp thông minh để đảm bảo thiết bị không bao giờ bị đầy bộ nhớ dẫn đến crash.

## Configuration (Người dùng cài đặt)
-   `retention_days`: Số ngày giữ video (Mặc định: **90 ngày**).
-   `min_free_space_mb`: Dung lượng trống tối thiểu cần duy trì (Mặc định: **2048 MB**).

## Thuật toán Dọn dẹp Tự động
Chạy định kỳ (Daily Background Job) hoặc mỗi lần khởi động App.

```mermaid
graph TD
    Start([Kiểm tra dung lượng]) --> CheckQuota{Còn trống > MinFreeSpace?}
    CheckQuota -- Yes --> CheckAge{Check file cũ > RetentionDays}
    
    CheckQuota -- No (Bộ nhớ đầy) --> Emergency[Kích hoạt chế độ Cấp cứu]
    
    CheckAge -- Có file hết hạn --> DeleteLegacy[Xóa file cũ nhất]
    DeleteLegacy --> End([Hoàn tất])
    
    Emergency --> DeleteSynced[Xóa Video đã Sync Cloud]
    DeleteSynced --> StillFull{Vẫn đầy?}
    
    StillFull -- Yes --> DeleteOldest[Xóa Video cũ nhất (Dù chưa hết hạn)]
    DeleteOldest --> Alert[Cảnh báo người dùng!]
```

## Các quy tắc an toàn
1.  **Ưu tiên giữ Video Return:** Video nhận hàng hoàn thường quan trọng để khiếu nại gian lận. Có thể set retention riêng dài hơn (ví dụ 180 ngày).
2.  **Không xóa Video đang "Dispute":** Cho phép user đánh dấu (Flag) các video đang tranh chấp. Các video này **KHÔNG BAO GIỜ** bị xóa tự động, trừ khi user tự tay xóa.
3.  **Cảnh báo sớm:** Khi bộ nhớ sử dụng > 80%, hiện thông báo nhắc nhở user backup hoặc cleanup.

## Manual Cleanup
Cung cấp công cụ cho user tự dọn dẹp:
-   "Xóa tất cả video trước ngày X".
-   "Xóa tất cả video đã sync lên Cloud".

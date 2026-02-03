# Auto-backup NAS

## Mô tả
Tự động backup video lên ổ cứng mạng nội bộ (NAS) qua giao thức SMB/CIFS hoặc NFS, không cần internet.

## Use Cases

- Shop có NAS (Synology, QNAP, TrueNAS).
- Muốn backup local, không upload cloud.
- Nhiều máy tính/điện thoại backup chung 1 chỗ.

## Giao thức hỗ trợ

| Protocol | Platform | Độ khó |
|---|---|---|
| SMB/CIFS | Windows, Android, Desktop | ⭐⭐ |
| NFS | Linux, macOS | ⭐⭐⭐ |
| FTP/SFTP | Cross-platform | ⭐⭐ |

## Cấu hình

```
+--------------------------------------------------+
|           AUTO-BACKUP NAS                        |
+--------------------------------------------------+
|                                                  |
|  Địa chỉ NAS:    [192.168.1.100        ]        |
|  Đường dẫn:      [/backup/allship      ]        |
|  Username:       [admin                ]        |
|  Password:       [••••••••             ]        |
|                                                  |
|  Backup khi:     [●] WiFi only                  |
|                  [ ] Cả 4G/LTE                  |
|                                                  |
|         [Test kết nối]  [Lưu cài đặt]           |
|                                                  |
+--------------------------------------------------+
```

## Package sử dụng

```yaml
# Desktop (Electron)
# Dùng native SMB client

# Mobile (Flutter)
dependencies:
  smb_connect: ^0.0.5  # Android only
```

## Ưu tiên
**P2** - Phase 3 (Desktop).

## Lưu ý
- Mobile hỗ trợ hạn chế (chủ yếu Android).
- Desktop (Electron) dễ implement hơn vì có file system access.

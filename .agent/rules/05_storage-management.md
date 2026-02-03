# Storage Management - ALL SHIP ECOMBOX

## Video Encoding Profiles

```yaml
STANDARD (default):
  Resolution: 1280x720
  FPS: 20
  Codec: H.264 Main Profile
  Bitrate: VBR 2-4 Mbps
  Audio: AAC 64kbps mono
  Container: Fragmented MP4
  Size: ~4-6 MB / 30 giây

HIGH QUALITY:
  Resolution: 1920x1080
  FPS: 24
  Codec: H.264 High Profile
  Bitrate: VBR 4-8 Mbps
  Audio: AAC 128kbps stereo
  Size: ~8-12 MB / 30 giây
```

## Tại Sao H.264?

| Tiêu chí | H.264 | H.265 |
|----------|-------|-------|
| Encoding speed | Nhanh | Chậm 10-20x trên ARM |
| Hardware support | 2013+ | 2017+ |
| Battery | Thấp | Cao hơn 30-50% |
| Compatibility | 100% | Một số sàn TMDT chưa hỗ trợ |

## File Organization

```
videos/
├── 2026/
│   └── 02/
│       └── 03/
│           ├── SPX038294671_packing_20260203_103052.mp4
│           └── SPX038294671_packing_20260203_103052_thumb.jpg

FORMAT: {order_code}_{type}_{YYYYMMDD}_{HHmmss}.mp4
```

## Database Schema (SQLite)

```sql
CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  order_code TEXT NOT NULL UNIQUE,
  marketplace TEXT,
  created_at DATETIME
);

CREATE TABLE videos (
  id INTEGER PRIMARY KEY,
  order_id INTEGER REFERENCES orders(id),
  type TEXT NOT NULL,        -- packing|shipping|return
  file_path TEXT NOT NULL,
  file_size_bytes INTEGER,
  duration_ms INTEGER,
  recorded_at DATETIME,
  synced_to_cloud BOOLEAN DEFAULT 0,
  return_status TEXT,        -- intact|damaged|wrong_item
  status TEXT DEFAULT 'complete'
);

CREATE INDEX idx_order_code ON orders(order_code);
CREATE INDEX idx_recorded_at ON videos(recorded_at);
```

## Auto-Cleanup Logic

```
Config mặc định:
  max_storage_gb: 50
  retention_days: 90
  auto_cleanup: true

Logic khi storage > 80%:
  1. Xóa video đã sync + quá retention_days
  2. Xóa video chưa sync + quá retention_days (cảnh báo user)
  3. Nén video cũ xuống 480p
  4. Thông báo user cần giải phóng bộ nhớ

⚠️ KHÔNG xóa video có tag "dispute" hoặc return_status='damaged'
```

## Storage Estimation

| Đơn/ngày | GB/tháng | 90 ngày |
|----------|---------|---------|
| 100 | 15 GB | 45 GB |
| 300 | 45 GB | 135 GB |
| 500 | 75 GB | 225 GB |

## Cloud Tiers (Phase 4)

- **Tier 0 (Free):** Pure local
- **Tier 1 ($):** Metadata sync only  
- **Tier 2 ($$):** Full video backup + CDN

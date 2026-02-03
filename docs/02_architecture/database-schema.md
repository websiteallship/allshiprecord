# Thiết kế Database Schema (SQLite)

Hệ thống sử dụng SQLite làm cơ sở dữ liệu chính lưu trữ metadata.

## 1. Tables

### orders (Đơn hàng)
Lưu trữ thông tin về đơn hàng được quét.

```sql
CREATE TABLE orders (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  order_code         TEXT NOT NULL,           -- Mã vận đơn (Unique)
  marketplace        TEXT,                    -- shopee/tiktok/lazada/tiki/other
  created_at         DATETIME DEFAULT CURRENT_TIMESTAMP,
  notes              TEXT
);

-- Index quan trọng cho việc tra cứu nhanh
CREATE UNIQUE INDEX idx_order_code ON orders(order_code);
```

### videos (Video ghi hình)
Lưu trữ thông tin về các video đã quay liên quan đến đơn hàng.

```sql
CREATE TABLE videos (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id           INTEGER REFERENCES orders(id),
  type               TEXT NOT NULL,           -- 'packing' | 'shipping' | 'return'
  file_path          TEXT NOT NULL,           -- Đường dẫn file (relative path)
  file_size_bytes    INTEGER,
  duration_ms        INTEGER,                 -- Thời lượng (ms)
  resolution         TEXT,                    -- Ví dụ: '1280x720'
  codec              TEXT,                    -- 'h264'
  thumbnail_path     TEXT,                    -- Đường dẫn thumbnail
  recorded_at        DATETIME,                -- Thời gian quay
  device_name        TEXT,                    -- Tên thiết bị quay (để trace)
  camera_source      TEXT,                    -- 'rear' | 'front' | 'webcam_0'
  synced_to_cloud    BOOLEAN DEFAULT 0,       -- Trạng thái sync
  cloud_url          TEXT,
  return_status      TEXT,                    -- 'intact' | 'damaged' | 'wrong_item' (cho type='return')
  notes              TEXT
);

-- Index phục vụ thống kê và tìm kiếm
CREATE INDEX idx_video_type ON videos(type);
CREATE INDEX idx_recorded_at ON videos(recorded_at);
CREATE INDEX idx_synced ON videos(synced_to_cloud);
```

## 2. Common Queries

### Tra cứu video theo mã vận đơn
Query này phải cực nhanh (< 1ms).

```sql
SELECT v.* 
FROM videos v
JOIN orders o ON v.order_id = o.id
WHERE o.order_code = 'SPX123456789'
ORDER BY v.recorded_at ASC;
```

### Thống kê dung lượng theo ngày

```sql
SELECT DATE(recorded_at) as day,
       COUNT(*) as video_count,
       SUM(file_size_bytes) as total_bytes
FROM videos
GROUP BY DATE(recorded_at)
ORDER BY day DESC;
```

### Tìm video cần sync (cho tính năng Cloud)

```sql
SELECT * FROM videos 
WHERE synced_to_cloud = 0 
ORDER BY recorded_at ASC 
LIMIT 50;
```

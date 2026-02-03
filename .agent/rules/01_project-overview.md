# Project Overview - ALL SHIP ECOMBOX

## Mô Tả Dự Án

Đây là dự án **Video Recording & Order Verification Tool** - công cụ quay video đóng gói và đối soát đơn hàng TMDT (Thương mại điện tử).

### Mục Tiêu Chính
- Hỗ trợ seller lưu trữ video đóng gói, xuất hàng, nhận hoàn trả
- Đối soát với đơn vị vận chuyển hoặc sàn TMDT (Shopee, TikTok Shop, Lazada, Tiki)
- Local-first storage - miễn phí, không bắt buộc cloud

## Tech Stack

| Component | Technology | Lý do |
|-----------|------------|-------|
| **Mobile** | Flutter (Dart) | Performance camera tốt, single codebase Android+iOS |
| **Desktop** | Electron (TypeScript) | WebRTC camera mature, multi-camera ổn định |
| **Video Codec** | H.264 (KHÔNG phải H.265) | Tương thích 100%, encoding nhanh trên ARM |
| **Database** | SQLite | Nhẹ, nhanh, offline, không cần server |
| **Barcode SDK** | Google ML Kit | Free, chính xác, offline capable |
| **Scanner Protocol** | Bluetooth/USB HID | Universal, không cần SDK riêng |
| **Storage** | Local-first + Optional Cloud | Zero cost, privacy |

## Architecture Pattern

```
LOCAL-FIRST + OPTIONAL CLOUD SYNC
==================================

[THIẾT BỊ NGƯỜI DÙNG]
  Camera + Scanner --> App Engine --> Local Storage (PRIMARY)
                          |              SQLite DB
                          |              Video Files  
                          |              Thumbnails
                          |
                          v
                        Sync Engine (background, WiFi-only, optional)
                          |
                          v
                      [CLOUD (OPTIONAL)]
                        Tier 1: Metadata only (FREE)
                        Tier 2: Metadata + Video ($)
```

## Database Schema

```sql
-- Bảng chính
CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_code TEXT NOT NULL,           -- mã vận đơn (unique index)
  marketplace TEXT,                   -- shopee/tiktok/lazada/tiki/other
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  notes TEXT
);

CREATE TABLE videos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id INTEGER REFERENCES orders(id),
  type TEXT NOT NULL,                 -- 'packing' | 'shipping' | 'return'
  file_path TEXT NOT NULL,            -- relative path
  file_size_bytes INTEGER,
  duration_ms INTEGER,
  resolution TEXT,                    -- '1280x720'
  codec TEXT,                         -- 'h264'
  thumbnail_path TEXT,
  recorded_at DATETIME,
  device_name TEXT,
  camera_source TEXT,                 -- 'rear' | 'front' | 'webcam_0'
  synced_to_cloud BOOLEAN DEFAULT 0,
  cloud_url TEXT,
  return_status TEXT,                 -- 'intact' | 'damaged' | 'wrong_item'
  notes TEXT
);
```

## Development Phases

1. **Phase 1 (MVP):** Android app - quét camera + quay video + lưu local
2. **Phase 2:** iOS + Bluetooth scanner + continuous mode + return flow
3. **Phase 3:** Desktop Electron + multi-camera + USB scanner + IP Camera RTSP
4. **Phase 4:** Cloud backup + multi-user + API sàn TMDT

## Đối Tượng Người Dùng

| Quy mô | Khuyến nghị | Lý do |
|--------|-------------|-------|
| Nhỏ (<50 đơn/ngày) | Điện thoại cá nhân | 0 đồng đầu tư, đủ tốt |
| Vừa (50-300 đơn/ngày) | Kết hợp PC + mobile | PC chính, mobile backup/di động |
| Lớn (300+ đơn/ngày) | PC + multi-camera | Ổn định, quản lý tập trung |

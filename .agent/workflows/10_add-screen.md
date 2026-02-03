---
description: Quy trình thêm màn hình mới vào ứng dụng
---

# Add Screen Workflow

Quy trình chuẩn để thêm một màn hình (screen/page) mới vào ứng dụng Allship Record.

---

## Step 1: Xác định thông tin

Trước khi code, xác định:
- **Screen name**: Tên màn hình (ví dụ: `VideoDetail`)
- **Feature folder**: Thuộc feature nào (`history`, `settings`, etc.)
- **Route path**: URL path (ví dụ: `/history/video/:id`)
- **Cần BLoC không?**: Có state phức tạp → Cần BLoC

---

## Step 2: Tạo file structure

```bash
# Ví dụ: Thêm VideoDetailPage vào feature history

lib/features/history/
├── bloc/
│   └── (nếu cần BLoC mới, xem workflow 11_add-bloc.md)
├── pages/
│   └── video_detail_page.dart    # ← TẠO FILE NÀY
└── widgets/
    └── video_info_card.dart       # ← Widgets riêng nếu cần
```

---

## Step 3: Tạo Page file

```dart
// lib/features/history/pages/video_detail_page.dart

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:allship_record/core/theme/app_theme.dart';
import 'package:allship_record/core/widgets/index.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class VideoDetailPage extends StatelessWidget {
  final String videoId;

  const VideoDetailPage({
    required this.videoId,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(S.of(context).videoDetailTitle),
      ),
      body: _buildBody(context),
    );
  }

  Widget _buildBody(BuildContext context) {
    // TODO: Implement UI
    return const Center(
      child: Text('Video Detail'),
    );
  }
}
```

---

## Step 4: Thêm Route

```dart
// lib/core/constants/route_names.dart

class RouteNames {
  // ... existing routes
  
  // Thêm route mới
  static const String videoDetail = '/history/video/:id';
  
  // Helper method
  static String videoDetailPath(String id) => '/history/video/$id';
}
```

```dart
// lib/core/router/app_router.dart

GoRoute(
  path: 'video/:id',
  builder: (context, state) => VideoDetailPage(
    videoId: state.pathParameters['id']!,
  ),
),
```

---

## Step 5: Thêm Localization strings

```json
// lib/l10n/intl_vi.arb

{
  "videoDetailTitle": "Chi tiết video",
  "videoDetailPlay": "Phát video",
  "videoDetailShare": "Chia sẻ"
}
```

```bash
// turbo
flutter gen-l10n
```

---

## Step 6: Verify

- [ ] Page render không có lỗi
- [ ] Route hoạt động đúng
- [ ] Localization strings hiển thị đúng
- [ ] Theme colors/typography đúng
- [ ] Back navigation hoạt động

---

## 📋 Checklist

| Step | Task |
|---|---|
| 1 | Xác định screen name, feature, route |
| 2 | Tạo file trong `lib/features/{feature}/pages/` |
| 3 | Implement page với proper imports |
| 4 | Thêm route vào `route_names.dart` và `app_router.dart` |
| 5 | Thêm l10n strings và chạy `gen-l10n` |
| 6 | Test navigation và UI |

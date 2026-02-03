# Remote Config

## Mô tả
Sử dụng Firebase Remote Config để thay đổi cài đặt app mà không cần user update từ Play Store.

## Use Cases

1. **Feature Flags**: Bật/tắt tính năng cho nhóm user test.
2. **Thay đổi default settings**: Video duration, resolution.
3. **A/B Testing**: Test UI variants.
4. **Kill Switch**: Tắt feature có bug ngay lập tức.

## Config Keys

| Key | Type | Default | Mô tả |
|---|---|---|---|
| `max_video_duration_seconds` | int | 300 | Thời lượng tối đa |
| `enable_voice_commands` | bool | false | Bật voice control |
| `enable_cloud_sync` | bool | true | Cho phép cloud sync |
| `force_update_version` | string | "" | Force update nếu < version này |
| `maintenance_mode` | bool | false | Hiển thị thông báo bảo trì |

## Setup

```yaml
dependencies:
  firebase_remote_config: ^4.3.0
```

```dart
final remoteConfig = FirebaseRemoteConfig.instance;

// Set defaults
await remoteConfig.setDefaults({
  'max_video_duration_seconds': 300,
  'enable_voice_commands': false,
});

// Fetch & activate
await remoteConfig.fetchAndActivate();

// Use config
final maxDuration = remoteConfig.getInt('max_video_duration_seconds');
```

## Fetch Strategy

- Fetch khi app start.
- Fetch mỗi 12 giờ (background).
- Minimum fetch interval: 1 giờ (avoid quota).

## Ưu tiên
**P2** - Phase 4.

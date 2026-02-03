# Localization Strings - Allship Record

Tất cả chuỗi UI tiếng Việt cho ứng dụng Allship Record.

---

## 1. Cấu trúc file ARB

```
lib/l10n/
├── intl_vi.arb         # Vietnamese (default)
└── intl_en.arb         # English (optional)
```

---

## 2. Vietnamese Strings (intl_vi.arb)

```json
{
  "@@locale": "vi",
  "@@last_modified": "2024-02-04",
  
  "_comment_app": "=== APP GENERAL ===",
  "appName": "Allship Record",
  "appTagline": "Quay video đóng hàng",
  
  "_comment_common": "=== COMMON ===",
  "btnCancel": "Hủy",
  "btnConfirm": "Xác nhận",
  "btnSave": "Lưu",
  "btnDelete": "Xóa",
  "btnClose": "Đóng",
  "btnRetry": "Thử lại",
  "btnBack": "Quay lại",
  "btnNext": "Tiếp tục",
  "btnDone": "Hoàn thành",
  "btnSettings": "Cài đặt",
  "btnShare": "Chia sẻ",
  "btnExport": "Xuất",
  "loading": "Đang tải...",
  "noData": "Không có dữ liệu",
  "error": "Lỗi",
  "success": "Thành công",
  "warning": "Cảnh báo",
  "today": "Hôm nay",
  "yesterday": "Hôm qua",
  
  "_comment_tabs": "=== BOTTOM NAVIGATION ===",
  "tabRecord": "Quay",
  "tabHistory": "Lịch sử",
  "tabDashboard": "Tổng quan",
  "tabSettings": "Cài đặt",
  
  "_comment_onboarding": "=== ONBOARDING ===",
  "onboardingTitle1": "Quay video đóng hàng",
  "onboardingDesc1": "Ghi lại quá trình đóng gói để bảo vệ shop khỏi tranh chấp",
  "onboardingTitle2": "Quét mã tự động",
  "onboardingDesc2": "Quét mã vận đơn để tự động gắn video với đơn hàng",
  "onboardingTitle3": "Tra cứu nhanh chóng",
  "onboardingDesc3": "Tìm video theo mã đơn khi cần giải quyết khiếu nại",
  "onboardingBtnStart": "Bắt đầu sử dụng",
  "onboardingBtnSkip": "Bỏ qua",
  
  "_comment_permissions": "=== PERMISSIONS ===",
  "permissionCameraTitle": "Quyền Camera",
  "permissionCameraDesc": "Cần để quay video đóng hàng",
  "permissionMicTitle": "Quyền Microphone",
  "permissionMicDesc": "Cần để ghi âm thanh trong video",
  "permissionStorageTitle": "Quyền Bộ nhớ",
  "permissionStorageDesc": "Cần để lưu video vào thiết bị",
  "permissionLocationTitle": "Quyền Vị trí",
  "permissionLocationDesc": "Gắn địa điểm vào video (tùy chọn)",
  "permissionDenied": "Quyền bị từ chối",
  "permissionDeniedDesc": "Vui lòng cấp quyền trong Cài đặt để sử dụng tính năng này",
  "permissionGrant": "Cấp quyền",
  "permissionOpenSettings": "Mở Cài đặt",
  
  "_comment_camera": "=== CAMERA / RECORDING ===",
  "cameraTitle": "Quay video",
  "cameraScanHint": "Quét hoặc nhập mã vận đơn",
  "cameraScanPlaceholder": "Nhập mã đơn...",
  "cameraStartRecording": "Bắt đầu quay",
  "cameraStopRecording": "Dừng quay",
  "cameraPauseRecording": "Tạm dừng",
  "cameraResumeRecording": "Tiếp tục",
  "cameraRecording": "Đang quay",
  "cameraPaused": "Đã tạm dừng",
  "cameraSaving": "Đang lưu...",
  "cameraSaved": "Đã lưu video",
  "cameraOrderCode": "Mã đơn: {code}",
  "@cameraOrderCode": {
    "placeholders": {
      "code": {"type": "String"}
    }
  },
  "cameraTimeRemaining": "Còn {seconds}s",
  "@cameraTimeRemaining": {
    "placeholders": {
      "seconds": {"type": "int"}
    }
  },
  "cameraAutoStopped": "Video tự động dừng khi đạt giới hạn",
  
  "_comment_order_types": "=== ORDER TYPES ===",
  "orderTypePacking": "Đóng gói",
  "orderTypeShipping": "Giao hàng",
  "orderTypeReturn": "Hàng hoàn",
  "orderTypeSelect": "Chọn loại đơn",
  
  "_comment_history": "=== HISTORY ===",
  "historyTitle": "Lịch sử video",
  "historySearch": "Tìm theo mã đơn",
  "historyEmpty": "Chưa có video nào",
  "historyEmptyDesc": "Video đóng gói sẽ xuất hiện ở đây",
  "historyVideoCount": "{count} video",
  "@historyVideoCount": {
    "placeholders": {
      "count": {"type": "int"}
    }
  },
  "historyDeleteConfirm": "Xóa video này?",
  "historyDeleteDesc": "Video sẽ bị xóa vĩnh viễn và không thể khôi phục",
  "historyDeleted": "Đã xóa video",
  "historyFilterAll": "Tất cả",
  "historyFilterToday": "Hôm nay",
  "historyFilterWeek": "Tuần này",
  "historyFilterMonth": "Tháng này",
  
  "_comment_video_detail": "=== VIDEO DETAIL ===",
  "videoDetailTitle": "Chi tiết video",
  "videoDetailDate": "Ngày quay",
  "videoDetailDuration": "Thời lượng",
  "videoDetailSize": "Dung lượng",
  "videoDetailResolution": "Độ phân giải",
  "videoDetailLocation": "Địa điểm",
  "videoDetailNoLocation": "Không có thông tin",
  "videoDetailPlay": "Phát video",
  "videoDetailShare": "Chia sẻ",
  "videoDetailExport": "Xuất bằng chứng",
  "videoDetailDelete": "Xóa video",
  
  "_comment_dashboard": "=== DASHBOARD ===",
  "dashboardTitle": "Tổng quan",
  "dashboardToday": "Hôm nay",
  "dashboardWeek": "Tuần này",
  "dashboardMonth": "Tháng này",
  "dashboardTotal": "Tổng",
  "dashboardVideosCount": "Video đã quay",
  "dashboardStorageUsed": "Dung lượng đã dùng",
  "dashboardAvgDuration": "Thời lượng TB",
  "dashboardByType": "Theo loại đơn",
  
  "_comment_settings": "=== SETTINGS ===",
  "settingsTitle": "Cài đặt",
  "settingsCameraSection": "Camera",
  "settingsStorageSection": "Bộ nhớ",
  "settingsScannerSection": "Máy quét",
  "settingsAppSection": "Ứng dụng",
  
  "settingsCameraQuality": "Chất lượng video",
  "settingsCameraQualityHigh": "Cao (1080p)",
  "settingsCameraQualityMedium": "Trung bình (720p)",
  "settingsCameraQualityLow": "Tiết kiệm (480p)",
  
  "settingsMaxDuration": "Thời lượng tối đa",
  "settingsMaxDurationValue": "{minutes} phút",
  "@settingsMaxDurationValue": {
    "placeholders": {
      "minutes": {"type": "int"}
    }
  },
  
  "settingsAudioRecord": "Ghi âm thanh",
  "settingsAudioRecordDesc": "Ghi âm thanh trong video",
  
  "settingsLocationOverlay": "Hiển thị vị trí",
  "settingsLocationOverlayDesc": "Gắn địa điểm trên video",
  
  "settingsTimestampOverlay": "Hiển thị thời gian",
  "settingsTimestampOverlayDesc": "Gắn ngày giờ trên video",
  
  "settingsStorageLocation": "Vị trí lưu",
  "settingsStorageInternal": "Bộ nhớ trong",
  "settingsStorageExternal": "Thẻ SD",
  
  "settingsStorageUsage": "Dung lượng đã dùng",
  "settingsStorageUsageValue": "{used} / {total}",
  "@settingsStorageUsageValue": {
    "placeholders": {
      "used": {"type": "String"},
      "total": {"type": "String"}
    }
  },
  
  "settingsAutoDelete": "Tự động xóa",
  "settingsAutoDeleteDesc": "Xóa video cũ hơn {days} ngày",
  "@settingsAutoDeleteDesc": {
    "placeholders": {
      "days": {"type": "int"}
    }
  },
  
  "settingsClearCache": "Xóa cache",
  "settingsClearCacheDesc": "Giải phóng dung lượng tạm",
  "settingsClearCacheConfirm": "Xóa cache ứng dụng?",
  "settingsCacheCleared": "Đã xóa cache",
  
  "settingsBluetoothScanner": "Máy quét Bluetooth",
  "settingsBluetoothScannerDesc": "Kết nối máy quét HID không dây",
  "settingsBluetoothConnected": "Đã kết nối: {name}",
  "@settingsBluetoothConnected": {
    "placeholders": {
      "name": {"type": "String"}
    }
  },
  "settingsBluetoothDisconnected": "Chưa kết nối",
  "settingsBluetoothSearching": "Đang tìm...",
  
  "settingsTheme": "Giao diện",
  "settingsThemeLight": "Sáng",
  "settingsThemeDark": "Tối",
  "settingsThemeSystem": "Theo hệ thống",
  
  "settingsLanguage": "Ngôn ngữ",
  "settingsLanguageVi": "Tiếng Việt",
  "settingsLanguageEn": "English",
  
  "settingsAbout": "Về ứng dụng",
  "settingsVersion": "Phiên bản {version}",
  "@settingsVersion": {
    "placeholders": {
      "version": {"type": "String"}
    }
  },
  "settingsPrivacy": "Chính sách bảo mật",
  "settingsTerms": "Điều khoản sử dụng",
  "settingsLicenses": "Giấy phép",
  "settingsRateApp": "Đánh giá ứng dụng",
  "settingsFeedback": "Gửi phản hồi",
  
  "_comment_errors": "=== ERRORS ===",
  "errorCameraInit": "Không thể khởi tạo camera",
  "errorCameraAccess": "Không thể truy cập camera",
  "errorRecordingFailed": "Không thể quay video",
  "errorSaveFailed": "Không thể lưu video",
  "errorStorageFull": "Bộ nhớ đầy",
  "errorStorageFullDesc": "Giải phóng dung lượng để tiếp tục quay",
  "errorInvalidBarcode": "Mã vận đơn không hợp lệ",
  "errorNetworkFailed": "Lỗi kết nối mạng",
  "errorUnknown": "Đã xảy ra lỗi",
  "errorTryAgain": "Vui lòng thử lại sau",
  
  "_comment_status": "=== STATUS BADGES ===",
  "statusIntact": "Nguyên vẹn",
  "statusDamaged": "Hư hỏng",
  "statusSwapped": "Tráo hàng",
  "statusConnected": "Đã kết nối",
  "statusDisconnected": "Chưa kết nối",
  "statusConnecting": "Đang kết nối...",
  
  "_comment_time": "=== TIME FORMATS ===",
  "timeMinutes": "{count} phút",
  "@timeMinutes": {
    "placeholders": {
      "count": {"type": "int"}
    }
  },
  "timeSeconds": "{count} giây",
  "@timeSeconds": {
    "placeholders": {
      "count": {"type": "int"}
    }
  },
  "timeDaysAgo": "{count} ngày trước",
  "@timeDaysAgo": {
    "placeholders": {
      "count": {"type": "int"}
    }
  },
  
  "_comment_storage": "=== STORAGE UNITS ===",
  "storageBytes": "{size} B",
  "@storageBytes": {
    "placeholders": {
      "size": {"type": "int"}
    }
  },
  "storageKB": "{size} KB",
  "@storageKB": {
    "placeholders": {
      "size": {"type": "String"}
    }
  },
  "storageMB": "{size} MB",
  "@storageMB": {
    "placeholders": {
      "size": {"type": "String"}
    }
  },
  "storageGB": "{size} GB",
  "@storageGB": {
    "placeholders": {
      "size": {"type": "String"}
    }
  }
}
```

---

## 3. Usage in Flutter

### 3.1 pubspec.yaml

```yaml
dependencies:
  flutter_localizations:
    sdk: flutter
  intl: ^0.18.1

flutter:
  generate: true
```

### 3.2 l10n.yaml

```yaml
arb-dir: lib/l10n
template-arb-file: intl_vi.arb
output-localization-file: app_localizations.dart
output-class: S
```

### 3.3 Usage in Widgets

```dart
// Import
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

// Usage
Text(S.of(context).appName)
Text(S.of(context).cameraOrderCode(orderCode))
Text(S.of(context).historyVideoCount(videos.length))
```

---

## 4. String Categories

| Category | Prefix | Count |
|---|---|---|
| Common | `btn*`, `loading`, etc. | 20 |
| Navigation | `tab*` | 4 |
| Onboarding | `onboarding*` | 7 |
| Permissions | `permission*` | 10 |
| Camera/Recording | `camera*` | 15 |
| Order Types | `orderType*` | 4 |
| History | `history*` | 12 |
| Video Detail | `videoDetail*` | 12 |
| Dashboard | `dashboard*` | 8 |
| Settings | `settings*` | 35 |
| Errors | `error*` | 10 |
| Status | `status*` | 6 |
| Time/Storage | `time*`, `storage*` | 8 |
| **Total** | | **~151 strings** |

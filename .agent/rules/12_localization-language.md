# Localization & Language - ALL SHIP ECOMBOX

## Ngôn Ngữ Mặc Định

**Tiếng Việt (vi-VN)** là ngôn ngữ mặc định của ứng dụng.

## String Resources

### Cấu Trúc

```dart
// lib/core/l10n/app_strings.dart

class AppStrings {
  // ============================================
  // NAVIGATION & TABS
  // ============================================
  static const navPacking = 'Đóng hàng';
  static const navReturn = 'Nhận hoàn';
  static const navSearch = 'Tra cứu';
  static const navSettings = 'Cài đặt';

  // ============================================
  // RECORDING SCREEN
  // ============================================
  static const recordingTitle = 'Quay video đóng gói';
  static const recordingStart = 'Bắt đầu quay';
  static const recordingStop = 'Hoàn tất';
  static const recordingCancel = 'Hủy';
  static const recordingInProgress = 'Đang quay...';
  static const recordingSaved = 'Đã lưu video';
  
  static const scanPrompt = 'Quét mã vận đơn để bắt đầu';
  static const scanManual = 'Nhập tay';
  static const scanSuccess = 'Đã nhận mã';
  static const scanDuplicate = 'Mã này đã quét rồi';
  static const scanInvalid = 'Mã không hợp lệ';

  // ============================================
  // RETURN SCREEN
  // ============================================
  static const returnTitle = 'Nhận hàng hoàn trả';
  static const returnScanPrompt = 'Quét mã đơn hàng hoàn';
  static const returnFoundOrder = 'Tìm thấy đơn hàng';
  static const returnNewOrder = 'Đơn mới - Tiếp tục quay?';
  static const returnEvaluate = 'Đánh giá tình trạng';
  
  // Return status options
  static const returnIntact = 'Hàng nguyên vẹn';
  static const returnDamaged = 'Hàng bị hư hỏng';
  static const returnWrongItem = 'Sai hàng / thiếu hàng';
  static const returnSwapped = 'Hàng bị tráo';

  // ============================================
  // SEARCH SCREEN
  // ============================================
  static const searchTitle = 'Tra cứu video';
  static const searchHint = 'Nhập mã vận đơn...';
  static const searchNoResults = 'Không tìm thấy video';
  static const searchResults = 'Kết quả tìm kiếm';

  // ============================================
  // SETTINGS SCREEN
  // ============================================
  static const settingsTitle = 'Cài đặt';
  static const settingsVideoQuality = 'Chất lượng video';
  static const settingsStorage = 'Dung lượng lưu trữ';
  static const settingsRetention = 'Thời gian giữ video';
  static const settingsScanner = 'Máy quét';
  static const settingsCamera = 'Camera';
  static const settingsAbout = 'Về ứng dụng';
  
  // Quality options
  static const qualityStandard = 'Tiêu chuẩn (720p)';
  static const qualityHigh = 'Cao (1080p)';

  // ============================================
  // VIDEO TYPES
  // ============================================
  static const videoPacking = 'Đóng gói';
  static const videoShipping = 'Giao hàng';
  static const videoReturn = 'Hoàn trả';

  // ============================================
  // ERRORS & WARNINGS
  // ============================================
  static const errorGeneric = 'Đã xảy ra lỗi';
  static const errorCamera = 'Không thể mở camera';
  static const errorCameraDisconnected = 'Camera bị ngắt kết nối';
  static const errorStorage = 'Không đủ dung lượng';
  static const errorPermission = 'Cần cấp quyền truy cập';
  
  static const warningLowStorage = 'Dung lượng sắp hết';
  static const warningScannerOffline = 'Máy quét đã ngắt kết nối';

  // ============================================
  // CONFIRMATIONS
  // ============================================
  static const confirmDelete = 'Xác nhận xóa';
  static const confirmDeleteMessage = 'Bạn có chắc muốn xóa video này?';
  static const confirmYes = 'Xóa';
  static const confirmNo = 'Hủy';

  // ============================================
  // BUTTONS
  // ============================================
  static const btnOk = 'Đồng ý';
  static const btnCancel = 'Hủy';
  static const btnRetry = 'Thử lại';
  static const btnShare = 'Chia sẻ';
  static const btnDelete = 'Xóa';
  static const btnPlay = 'Phát';
  static const btnSave = 'Lưu';

  // ============================================
  // DATE & TIME
  // ============================================
  static const today = 'Hôm nay';
  static const yesterday = 'Hôm qua';
  static const daysAgo = 'ngày trước';
  
  // Duration format helper
  static String formatDuration(Duration d) {
    final minutes = d.inMinutes;
    final seconds = d.inSeconds % 60;
    return '${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';
  }
  
  // File size format helper
  static String formatFileSize(int bytes) {
    if (bytes < 1024) return '$bytes B';
    if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(1)} KB';
    if (bytes < 1024 * 1024 * 1024) {
      return '${(bytes / 1024 / 1024).toStringAsFixed(1)} MB';
    }
    return '${(bytes / 1024 / 1024 / 1024).toStringAsFixed(2)} GB';
  }
}
```

## Quy Tắc Viết Text

### Tone of Voice

```yaml
GIỌNG ĐIỆU:
  - Thân thiện, dễ hiểu
  - Ngắn gọn, súc tích
  - Tránh thuật ngữ kỹ thuật
  - Dùng ngôn ngữ hàng ngày

VÍ DỤ TỐT:
  - "Đã lưu video" ✓
  - "Quét mã để bắt đầu" ✓
  - "Không đủ chỗ trống" ✓

VÍ DỤ XẤU:
  - "Video đã được persist vào storage" ✗
  - "Scan barcode để initiate recording" ✗
  - "Storage capacity exceeded" ✗
```

### Viết Hoa

```yaml
QUY TẮC VIẾT HOA:
  1. Tiêu đề màn hình: Viết hoa chữ cái đầu
     "Đóng hàng", "Tra cứu video"
  
  2. Nút bấm: Viết hoa chữ cái đầu
     "Hoàn tất", "Hủy", "Chia sẻ"
  
  3. Thông báo: Viết hoa chữ cái đầu câu
     "Đã lưu video thành công"
  
  4. Placeholder: Viết thường
     "Nhập mã vận đơn..."
```

### Độ Dài Text

```yaml
QUY TẮC ĐỘ DÀI:
  - Tiêu đề: ≤ 20 ký tự
  - Nút bấm: ≤ 10 ký tự
  - Thông báo toast: ≤ 40 ký tự
  - Mô tả: ≤ 80 ký tự
  - Error message: ≤ 60 ký tự
```

## Date & Number Formatting

### Date Format

```dart
// Định dạng ngày tháng theo chuẩn Việt Nam
import 'package:intl/intl.dart';

class DateFormatter {
  static final _locale = 'vi_VN';
  
  /// 03/02/2026
  static String shortDate(DateTime date) {
    return DateFormat('dd/MM/yyyy', _locale).format(date);
  }
  
  /// 03/02/2026 10:30
  static String dateTime(DateTime date) {
    return DateFormat('dd/MM/yyyy HH:mm', _locale).format(date);
  }
  
  /// Thứ Hai, 03 tháng 02, 2026
  static String fullDate(DateTime date) {
    return DateFormat('EEEE, dd MMMM, yyyy', _locale).format(date);
  }
  
  /// 10:30:45
  static String time(DateTime date) {
    return DateFormat('HH:mm:ss', _locale).format(date);
  }
  
  /// Hôm nay, Hôm qua, hoặc 03/02
  static String relativeDate(DateTime date) {
    final now = DateTime.now();
    final diff = now.difference(date);
    
    if (diff.inDays == 0) return 'Hôm nay';
    if (diff.inDays == 1) return 'Hôm qua';
    if (diff.inDays < 7) return '${diff.inDays} ngày trước';
    return DateFormat('dd/MM', _locale).format(date);
  }
}
```

### Number Format

```dart
class NumberFormatter {
  static final _locale = 'vi_VN';
  
  /// 1.234.567
  static String number(int value) {
    return NumberFormat('#,###', _locale).format(value);
  }
  
  /// 1.234.567 đ
  static String currency(int value) {
    return NumberFormat.currency(
      locale: _locale,
      symbol: 'đ',
      decimalDigits: 0,
    ).format(value);
  }
}
```

## Pluralization (Số Nhiều)

```dart
// Tiếng Việt thường không phân biệt số ít/số nhiều
// Nhưng có thể thêm "các" hoặc số đếm

class PluralizationHelper {
  static String videos(int count) {
    if (count == 0) return 'Không có video nào';
    if (count == 1) return '1 video';
    return '$count video';
  }
  
  static String orders(int count) {
    if (count == 0) return 'Không có đơn hàng nào';
    if (count == 1) return '1 đơn hàng';
    return '$count đơn hàng';
  }
  
  static String daysAgo(int days) {
    if (days == 0) return 'Hôm nay';
    if (days == 1) return 'Hôm qua';
    return '$days ngày trước';
  }
}
```

## Future: Multi-language Support

```dart
// lib/core/l10n/app_localizations.dart
// Chuẩn bị cho Phase sau nếu cần hỗ trợ tiếng Anh

// pubspec.yaml
// flutter_localizations:
//   sdk: flutter
// intl: ^0.18.0

// Supported locales
const supportedLocales = [
  Locale('vi', 'VN'), // Vietnamese (default)
  Locale('en', 'US'), // English (future)
];
```

## Audio Feedback Messages

```dart
// Audio cues (beep sounds) cũng cần "localize"
// Không phải text, nhưng cần nhất quán

class AudioCues {
  /// Beep cao: Thành công
  static const success = 'assets/audio/beep_success.mp3';
  
  /// Beep thấp: Lỗi
  static const error = 'assets/audio/beep_error.mp3';
  
  /// 2 beep: Chuyển video
  static const transition = 'assets/audio/beep_transition.mp3';
  
  /// 3 beep: Cảnh báo trùng
  static const warning = 'assets/audio/beep_warning.mp3';
  
  /// Ding: Đã lưu
  static const saved = 'assets/audio/ding_saved.mp3';
  
  /// Alarm: Lỗi nghiêm trọng
  static const alarm = 'assets/audio/alarm.mp3';
}
```

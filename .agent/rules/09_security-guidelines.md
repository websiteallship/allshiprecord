# Security Guidelines - ALL SHIP ECOMBOX

## Nguyên Tắc Bảo Mật

### Data Protection

```yaml
LOẠI DỮ LIỆU CẦN BẢO VỆ:
  - Video files: Chứa hình ảnh sản phẩm, quy trình đóng gói
  - Order data: Mã vận đơn, thông tin đơn hàng
  - User preferences: Cài đặt app
  - Device info: Camera, scanner configuration
```

### Local Storage Security

```dart
// SQLite DB encryption (optional, khi cần bảo mật cao)
import 'package:sqflite_sqlcipher/sqflite.dart';

final db = await openDatabase(
  path,
  password: secureKey, // Lưu trong Secure Storage
);
```

#### Secure Storage cho Sensitive Data

```dart
// Sử dụng flutter_secure_storage
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecurePreferences {
  static const _storage = FlutterSecureStorage();
  
  // Android: EncryptedSharedPreferences
  // iOS: Keychain
  
  Future<void> saveApiKey(String key) async {
    await _storage.write(key: 'api_key', value: key);
  }
  
  Future<String?> getApiKey() async {
    return await _storage.read(key: 'api_key');
  }
}
```

### Video File Protection

```dart
/// Video files KHÔNG được encrypt (performance)
/// Nhưng cần:
/// 1. Lưu trong app-private directory
/// 2. Không expose qua Content Provider công khai
/// 3. Xóa secure khi cần (overwrite trước khi delete)

// Android: getExternalFilesDir() - private to app
// iOS: Documents directory with .nobackup suffix
```

### Permission Security

```dart
/// Chỉ request permissions khi cần thiết
/// Giải thích rõ lý do cho user

class PermissionHandler {
  Future<bool> requestCamera() async {
    // Hiện dialog giải thích trước
    final shouldRequest = await showExplanationDialog(
      'Ứng dụng cần quyền Camera để quay video đóng gói.',
    );
    
    if (!shouldRequest) return false;
    
    final status = await Permission.camera.request();
    return status.isGranted;
  }
}
```

### Network Security (Phase 4 - Cloud)

```dart
/// Certificate Pinning cho Cloud Sync
class SecureHttpClient {
  static final client = HttpClient()
    ..badCertificateCallback = (cert, host, port) {
      // Verify certificate fingerprint
      return _verifyPinnedCertificate(cert);
    };
}

/// API Authentication
class ApiAuth {
  // JWT với short expiry + refresh token
  static const accessTokenExpiry = Duration(minutes: 15);
  static const refreshTokenExpiry = Duration(days: 7);
}
```

### Input Validation

```dart
/// Validate tất cả input từ scanner/user
class InputValidator {
  /// Sanitize order code - chỉ cho phép alphanumeric
  static String sanitizeOrderCode(String input) {
    return input.replaceAll(RegExp(r'[^A-Z0-9]'), '').toUpperCase();
  }
  
  /// Validate file path - ngăn path traversal
  static bool isValidFilePath(String path) {
    if (path.contains('..')) return false;
    if (path.contains('//')) return false;
    return true;
  }
}
```

### Biometric Authentication (Optional)

```dart
/// Cho seller muốn bảo vệ app
import 'package:local_auth/local_auth.dart';

class BiometricAuth {
  final _localAuth = LocalAuthentication();
  
  Future<bool> authenticate() async {
    final canCheck = await _localAuth.canCheckBiometrics;
    if (!canCheck) return true; // Skip if not available
    
    return await _localAuth.authenticate(
      localizedReason: 'Xác thực để mở ứng dụng',
      options: AuthenticationOptions(
        biometricOnly: true,
        stickyAuth: true,
      ),
    );
  }
}
```

### Screenshot Protection

```dart
/// Ngăn screenshot trong màn hình nhạy cảm (nếu cần)
// Android: FLAG_SECURE
// iOS: Không hỗ trợ native, cần workaround

// Thường KHÔNG cần cho app này vì video cần chia sẻ
```

### Root/Jailbreak Detection

```dart
/// Cảnh báo (không block) trên thiết bị đã root/jailbreak
import 'package:flutter_jailbreak_detection/flutter_jailbreak_detection.dart';

class SecurityCheck {
  Future<void> checkDevice() async {
    final isJailbroken = await FlutterJailbreakDetection.jailbroken;
    
    if (isJailbroken) {
      // Hiện cảnh báo, không block
      showWarningDialog(
        'Thiết bị đã jailbreak/root. '
        'Video có thể bị truy cập bởi app khác.',
      );
    }
  }
}
```

### Privacy Compliance

```yaml
NGUYÊN TẮC PRIVACY:
  1. Không thu thập data không cần thiết
  2. Video chỉ lưu local (mặc định)
  3. Cloud sync là optional, user chọn
  4. Không gửi analytics về server (nếu có, phải xin phép)
  5. Cung cấp tính năng "Xóa tất cả data"
```

### Secure Coding Checklist

```markdown
[ ] Không hardcode secrets trong code
[ ] Không log sensitive data
[ ] Validate tất cả input
[ ] Sanitize file paths
[ ] Sử dụng Secure Storage cho credentials
[ ] Timeout sessions (nếu có auth)
[ ] Encrypt network traffic (HTTPS only)
[ ] Handle errors không expose internal info
```

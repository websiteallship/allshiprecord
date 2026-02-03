# Crash Analytics

## Mô tả
Tích hợp Firebase Crashlytics để theo dõi và phân tích crash, giúp fix bug nhanh hơn.

## Lợi ích

- Biết app crash ở đâu, device nào.
- Nhận alert khi có crash mới.
- Priority bug theo số user bị ảnh hưởng.

## Setup

### 1. Thêm Firebase
```yaml
dependencies:
  firebase_core: ^2.24.0
  firebase_crashlytics: ^3.4.0
```

### 2. Initialize
```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  
  // Catch Flutter errors
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterFatalError;
  
  // Catch async errors
  PlatformDispatcher.instance.onError = (error, stack) {
    FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);
    return true;
  };
  
  runApp(MyApp());
}
```

### 3. Custom Logging
```dart
// Log custom events
FirebaseCrashlytics.instance.log('User started recording');

// Set user ID (anonymous)
FirebaseCrashlytics.instance.setUserIdentifier('shop_abc');

// Log errors không crash
FirebaseCrashlytics.instance.recordError(exception, stackTrace);
```

## Privacy

- **Không gửi video** lên Firebase.
- Chỉ gửi crash logs + device info.
- Có thể tắt trong Settings (opt-out).

## Ưu tiên
**P2** - Phase 4.

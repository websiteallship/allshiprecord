# Error Handling & Logging - ALL SHIP ECOMBOX

## Error Handling Strategy

### Error Types

```dart
// lib/core/errors/app_exception.dart
sealed class AppException implements Exception {
  final String message;
  final String? code;
  final dynamic originalError;
  
  const AppException(this.message, {this.code, this.originalError});
}

class CameraException extends AppException {
  const CameraException(super.message, {super.code});
}

class StorageException extends AppException {
  const StorageException(super.message, {super.code});
}

class ScannerException extends AppException {
  const ScannerException(super.message, {super.code});
}

class DatabaseException extends AppException {
  const DatabaseException(super.message, {super.code});
}

class NetworkException extends AppException {
  const NetworkException(super.message, {super.code});
}
```

### Result Pattern

```dart
// lib/core/utils/result.dart
sealed class Result<T> {
  const Result();
}

class Success<T> extends Result<T> {
  final T data;
  const Success(this.data);
}

class Failure<T> extends Result<T> {
  final AppException exception;
  const Failure(this.exception);
}

// Usage
Future<Result<Video>> saveVideo(Video video) async {
  try {
    await _repository.save(video);
    return Success(video);
  } on IOException catch (e) {
    return Failure(StorageException('Không thể lưu video', originalError: e));
  }
}

// Handling
final result = await saveVideo(video);
switch (result) {
  case Success(:final data):
    showSuccess('Đã lưu ${data.filename}');
  case Failure(:final exception):
    showError(exception.message);
}
```

### Try-Catch Guidelines

```dart
// ✅ ĐÚNG: Catch specific exceptions
try {
  await camera.startRecording();
} on CameraException catch (e) {
  _handleCameraError(e);
} on StorageException catch (e) {
  _handleStorageError(e);
}

// ❌ SAI: Catch generic Exception
try {
  await camera.startRecording();
} catch (e) {
  print(e); // Lost context
}
```

## Logging

### Log Levels

| Level | Use Case | Production |
|-------|----------|------------|
| `debug` | Development only | ❌ Hidden |
| `info` | Important events | ❌ Hidden |
| `warning` | Recoverable issues | ✅ Visible |
| `error` | Failures | ✅ Visible + Report |

### Logger Implementation

```dart
// lib/core/logging/app_logger.dart
enum LogLevel { debug, info, warning, error }

class AppLogger {
  static LogLevel minLevel = EnvConfig.isDev ? LogLevel.debug : LogLevel.warning;
  
  static void debug(String message, [Map<String, dynamic>? data]) {
    _log(LogLevel.debug, message, data);
  }
  
  static void info(String message, [Map<String, dynamic>? data]) {
    _log(LogLevel.info, message, data);
  }
  
  static void warning(String message, [Map<String, dynamic>? data]) {
    _log(LogLevel.warning, message, data);
  }
  
  static void error(String message, {dynamic error, StackTrace? stack}) {
    _log(LogLevel.error, message, {'error': error.toString()});
    if (EnvConfig.isProd) {
      _reportToCrashlytics(message, error, stack);
    }
  }
  
  static void _log(LogLevel level, String message, Map<String, dynamic>? data) {
    if (level.index >= minLevel.index) {
      final timestamp = DateTime.now().toIso8601String();
      print('[$timestamp][${level.name.toUpperCase()}] $message');
      if (data != null) print('  Data: $data');
    }
  }
}
```

### Usage Examples

```dart
// Recording flow
AppLogger.info('Recording started', {'orderCode': code});
AppLogger.debug('Frame processed', {'fps': currentFps});
AppLogger.warning('Low storage', {'remaining': '500MB'});
AppLogger.error('Recording failed', error: e, stack: stackTrace);
```

## Crash Reporting

### Sentry Setup

```dart
// lib/main_prod.dart
Future<void> main() async {
  await SentryFlutter.init(
    (options) {
      options.dsn = dotenv.env['SENTRY_DSN'];
      options.environment = 'production';
      options.tracesSampleRate = 0.2;
    },
    appRunner: () => runApp(const MyApp()),
  );
}
```

### Manual Reporting

```dart
try {
  await riskyOperation();
} catch (e, stack) {
  Sentry.captureException(e, stackTrace: stack);
  // Also show user-friendly message
}
```

## User-Facing Errors

```dart
// lib/core/errors/error_messages.dart
class ErrorMessages {
  static String forException(AppException e) {
    return switch (e) {
      CameraException _ => 'Không thể mở camera. Vui lòng thử lại.',
      StorageException _ => 'Không đủ dung lượng. Hãy xóa bớt video cũ.',
      ScannerException _ => 'Máy quét ngắt kết nối. Kiểm tra Bluetooth.',
      DatabaseException _ => 'Lỗi dữ liệu. Khởi động lại ứng dụng.',
      NetworkException _ => 'Không có kết nối mạng.',
      _ => 'Đã xảy ra lỗi. Vui lòng thử lại.',
    };
  }
}
```

## Graceful Degradation

```dart
// ✅ Fallback khi feature fail
Future<void> saveWithFallback(Video video) async {
  try {
    await primaryStorage.save(video);
  } catch (e) {
    AppLogger.warning('Primary storage failed, using fallback');
    await fallbackStorage.save(video);
  }
}

// ✅ Partial success
Future<SaveResult> saveMultiple(List<Video> videos) async {
  final succeeded = <Video>[];
  final failed = <Video>[];
  
  for (final video in videos) {
    try {
      await save(video);
      succeeded.add(video);
    } catch (e) {
      failed.add(video);
    }
  }
  
  return SaveResult(succeeded: succeeded, failed: failed);
}
```

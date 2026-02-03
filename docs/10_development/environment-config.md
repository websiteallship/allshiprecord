# Environment Configuration - Allship Record

Hướng dẫn cấu hình môi trường cho các giai đoạn phát triển.

---

## 1. Tổng quan

Ứng dụng Allship Record sử dụng cấu hình môi trường để phân biệt giữa các giai đoạn:

| Environment | Use Case |
|---|---|
| **Development** | Phát triển local, debug |
| **Staging** | Testing trước khi release |
| **Production** | Bản release cho end-user |

---

## 2. Environment Variables

### 2.1 File .env (local development)

```env
# .env.development

# App Info
APP_NAME=Allship Record Dev
APP_FLAVOR=development

# Debug Settings
DEBUG_MODE=true
LOG_LEVEL=debug
SHOW_DEBUG_BANNER=true

# Storage
MAX_VIDEO_DURATION_SECONDS=180
DEFAULT_VIDEO_QUALITY=medium
AUTO_DELETE_DAYS=30

# Feature Flags
ENABLE_CLOUD_SYNC=false
ENABLE_ANALYTICS=false
ENABLE_CRASH_REPORTING=false
ENABLE_VOICE_COMMANDS=false

# API (Future)
API_BASE_URL=https://api-dev.allship.com
API_TIMEOUT_SECONDS=30
```

### 2.2 File .env.production

```env
# .env.production

# App Info
APP_NAME=Allship Record
APP_FLAVOR=production

# Debug Settings
DEBUG_MODE=false
LOG_LEVEL=error
SHOW_DEBUG_BANNER=false

# Storage
MAX_VIDEO_DURATION_SECONDS=180
DEFAULT_VIDEO_QUALITY=high
AUTO_DELETE_DAYS=90

# Feature Flags
ENABLE_CLOUD_SYNC=true
ENABLE_ANALYTICS=true
ENABLE_CRASH_REPORTING=true
ENABLE_VOICE_COMMANDS=true

# API (Future)
API_BASE_URL=https://api.allship.com
API_TIMEOUT_SECONDS=30
```

---

## 3. Flutter Implementation

### 3.1 Environment Config Class

```dart
// lib/core/config/environment.dart

enum Flavor { development, staging, production }

class Environment {
  static late Flavor flavor;
  static late EnvironmentConfig config;
  
  static void init(Flavor f) {
    flavor = f;
    config = _getConfig(f);
  }
  
  static EnvironmentConfig _getConfig(Flavor flavor) {
    return switch (flavor) {
      Flavor.development => EnvironmentConfig.development(),
      Flavor.staging => EnvironmentConfig.staging(),
      Flavor.production => EnvironmentConfig.production(),
    };
  }
  
  static bool get isDevelopment => flavor == Flavor.development;
  static bool get isProduction => flavor == Flavor.production;
}

class EnvironmentConfig {
  final String appName;
  final bool debugMode;
  final String logLevel;
  final bool showDebugBanner;
  
  final int maxVideoDurationSeconds;
  final String defaultVideoQuality;
  final int autoDeleteDays;
  
  final bool enableCloudSync;
  final bool enableAnalytics;
  final bool enableCrashReporting;
  final bool enableVoiceCommands;
  
  final String? apiBaseUrl;
  final int apiTimeoutSeconds;
  
  const EnvironmentConfig({
    required this.appName,
    required this.debugMode,
    required this.logLevel,
    required this.showDebugBanner,
    required this.maxVideoDurationSeconds,
    required this.defaultVideoQuality,
    required this.autoDeleteDays,
    required this.enableCloudSync,
    required this.enableAnalytics,
    required this.enableCrashReporting,
    required this.enableVoiceCommands,
    this.apiBaseUrl,
    this.apiTimeoutSeconds = 30,
  });
  
  // Development config
  factory EnvironmentConfig.development() => const EnvironmentConfig(
    appName: 'Allship Record Dev',
    debugMode: true,
    logLevel: 'debug',
    showDebugBanner: true,
    maxVideoDurationSeconds: 180,
    defaultVideoQuality: 'medium',
    autoDeleteDays: 30,
    enableCloudSync: false,
    enableAnalytics: false,
    enableCrashReporting: false,
    enableVoiceCommands: false,
    apiBaseUrl: 'https://api-dev.allship.com',
  );
  
  // Staging config
  factory EnvironmentConfig.staging() => const EnvironmentConfig(
    appName: 'Allship Record Staging',
    debugMode: true,
    logLevel: 'info',
    showDebugBanner: true,
    maxVideoDurationSeconds: 180,
    defaultVideoQuality: 'high',
    autoDeleteDays: 60,
    enableCloudSync: true,
    enableAnalytics: true,
    enableCrashReporting: true,
    enableVoiceCommands: true,
    apiBaseUrl: 'https://api-staging.allship.com',
  );
  
  // Production config
  factory EnvironmentConfig.production() => const EnvironmentConfig(
    appName: 'Allship Record',
    debugMode: false,
    logLevel: 'error',
    showDebugBanner: false,
    maxVideoDurationSeconds: 180,
    defaultVideoQuality: 'high',
    autoDeleteDays: 90,
    enableCloudSync: true,
    enableAnalytics: true,
    enableCrashReporting: true,
    enableVoiceCommands: true,
    apiBaseUrl: 'https://api.allship.com',
  );
}
```

### 3.2 Entry Points

```dart
// lib/main_development.dart
import 'main.dart' as app;
import 'core/config/environment.dart';

void main() {
  Environment.init(Flavor.development);
  app.main();
}
```

```dart
// lib/main_staging.dart
import 'main.dart' as app;
import 'core/config/environment.dart';

void main() {
  Environment.init(Flavor.staging);
  app.main();
}
```

```dart
// lib/main_production.dart
import 'main.dart' as app;
import 'core/config/environment.dart';

void main() {
  Environment.init(Flavor.production);
  app.main();
}
```

### 3.3 Run with Flavor

```bash
# Development
flutter run -t lib/main_development.dart

# Staging
flutter run -t lib/main_staging.dart

# Production
flutter run -t lib/main_production.dart --release
```

---

## 4. Feature Flags

### 4.1 Available Flags

| Flag | Description | Dev | Staging | Prod |
|---|---|---|---|---|
| `ENABLE_CLOUD_SYNC` | Cloud backup feature | ❌ | ✅ | ✅ |
| `ENABLE_ANALYTICS` | Firebase Analytics | ❌ | ✅ | ✅ |
| `ENABLE_CRASH_REPORTING` | Firebase Crashlytics | ❌ | ✅ | ✅ |
| `ENABLE_VOICE_COMMANDS` | Voice control feature | ❌ | ✅ | ✅ |
| `ENABLE_NAS_BACKUP` | NAS backup feature | ❌ | ✅ | ✅ |
| `ENABLE_DEBUG_OVERLAY` | Debug info overlay | ✅ | ✅ | ❌ |

### 4.2 Usage in Code

```dart
// Check feature flag
if (Environment.config.enableVoiceCommands) {
  // Initialize voice commands
}

// Conditional widget
Widget build(BuildContext context) {
  return Column(
    children: [
      // Always show
      RecordingControls(),
      
      // Only in development
      if (Environment.isDevelopment)
        DebugOverlay(),
      
      // Feature flag
      if (Environment.config.enableVoiceCommands)
        VoiceCommandButton(),
    ],
  );
}
```

---

## 5. Video Settings

### 5.1 Quality Presets

| Quality | Resolution | Bitrate | FPS |
|---|---|---|---|
| `low` | 480p | 1 Mbps | 24 |
| `medium` | 720p | 2.5 Mbps | 30 |
| `high` | 1080p | 5 Mbps | 30 |

### 5.2 Configuration

```dart
class VideoSettings {
  static VideoQuality get defaultQuality {
    return switch (Environment.config.defaultVideoQuality) {
      'low' => VideoQuality.low,
      'medium' => VideoQuality.medium,
      'high' => VideoQuality.high,
      _ => VideoQuality.medium,
    };
  }
  
  static Duration get maxDuration {
    return Duration(
      seconds: Environment.config.maxVideoDurationSeconds,
    );
  }
}
```

---

## 6. Storage Settings

### 6.1 Paths

```dart
class StoragePaths {
  // Base directory for app data
  static Future<Directory> get appDirectory async {
    if (Platform.isAndroid) {
      return await getExternalStorageDirectory() 
        ?? await getApplicationDocumentsDirectory();
    }
    return await getApplicationDocumentsDirectory();
  }
  
  // Videos directory
  static Future<Directory> get videosDirectory async {
    final base = await appDirectory;
    final dir = Directory('${base.path}/videos');
    if (!await dir.exists()) {
      await dir.create(recursive: true);
    }
    return dir;
  }
  
  // Thumbnails directory
  static Future<Directory> get thumbnailsDirectory async {
    final base = await appDirectory;
    final dir = Directory('${base.path}/thumbnails');
    if (!await dir.exists()) {
      await dir.create(recursive: true);
    }
    return dir;
  }
  
  // Database path
  static Future<String> get databasePath async {
    final base = await appDirectory;
    return '${base.path}/allship_record.db';
  }
}
```

### 6.2 Auto Delete Policy

```dart
class AutoDeleteService {
  Future<void> cleanupOldVideos() async {
    final days = Environment.config.autoDeleteDays;
    final cutoff = DateTime.now().subtract(Duration(days: days));
    
    final videos = await _videoRepository.getVideosBefore(cutoff);
    for (final video in videos) {
      await _videoRepository.delete(video.id);
    }
  }
}
```

---

## 7. Android Configuration

### 7.1 Build Types (android/app/build.gradle)

```groovy
android {
    buildTypes {
        debug {
            applicationIdSuffix ".dev"
            versionNameSuffix "-dev"
            resValue "string", "app_name", "Allship Record Dev"
        }
        
        release {
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.release
            resValue "string", "app_name", "Allship Record"
        }
    }
    
    flavorDimensions "default"
    productFlavors {
        development {
            dimension "default"
            applicationIdSuffix ".dev"
        }
        staging {
            dimension "default"
            applicationIdSuffix ".staging"
        }
        production {
            dimension "default"
        }
    }
}
```

---

## 8. iOS Configuration

### 8.1 Schemes

Create Xcode schemes for each environment:

- `Runner-Development`
- `Runner-Staging`
- `Runner-Production`

### 8.2 Info.plist per Scheme

```
ios/
├── Runner/
│   ├── Info.plist                    # Base
│   ├── Info-Development.plist       # Development overrides
│   ├── Info-Staging.plist           # Staging overrides
│   └── Info-Production.plist        # Production overrides
```

---

## 9. Logging

### 9.1 Log Levels

| Level | Description | Dev | Staging | Prod |
|---|---|---|---|---|
| `debug` | Detailed debug info | ✅ | ❌ | ❌ |
| `info` | General information | ✅ | ✅ | ❌ |
| `warning` | Warnings | ✅ | ✅ | ✅ |
| `error` | Errors only | ✅ | ✅ | ✅ |

### 9.2 Logger Implementation

```dart
class AppLogger {
  static void init() {
    final level = Environment.config.logLevel;
    // Initialize logger with appropriate level
  }
  
  static void debug(String message) {
    if (Environment.config.debugMode) {
      print('[DEBUG] $message');
    }
  }
  
  static void info(String message) {
    if (['debug', 'info'].contains(Environment.config.logLevel)) {
      print('[INFO] $message');
    }
  }
  
  static void error(String message, [Object? error, StackTrace? stack]) {
    print('[ERROR] $message');
    if (Environment.config.enableCrashReporting) {
      // Send to Crashlytics
    }
  }
}
```

---

## 10. Summary

| Environment | Debug | Analytics | Cloud Sync | Auto Delete |
|---|---|---|---|---|
| Development | ✅ | ❌ | ❌ | 30 days |
| Staging | ✅ | ✅ | ✅ | 60 days |
| Production | ❌ | ✅ | ✅ | 90 days |

# Environment & Configuration - ALL SHIP ECOMBOX

## Môi Trường

### Environment Types

| Env | Mục Đích | Config |
|-----|----------|--------|
| `development` | Local dev | Debug mode, verbose logs |
| `staging` | Testing trước release | Production-like, test APIs |
| `production` | Live users | Optimized, minimal logs |

### Flutter Environment Setup

```dart
// lib/core/config/environment.dart
enum Environment { development, staging, production }

class EnvConfig {
  static late Environment current;
  
  static void init(Environment env) {
    current = env;
  }
  
  static bool get isDev => current == Environment.development;
  static bool get isProd => current == Environment.production;
  
  static String get apiBaseUrl => switch (current) {
    Environment.development => 'http://localhost:3000',
    Environment.staging => 'https://staging-api.allship.vn',
    Environment.production => 'https://api.allship.vn',
  };
  
  static bool get enableLogging => current != Environment.production;
  static bool get enableCrashReporting => current == Environment.production;
}
```

### Entry Points

```dart
// lib/main_dev.dart
void main() {
  EnvConfig.init(Environment.development);
  runApp(const MyApp());
}

// lib/main_staging.dart
void main() {
  EnvConfig.init(Environment.staging);
  runApp(const MyApp());
}

// lib/main_prod.dart
void main() {
  EnvConfig.init(Environment.production);
  runApp(const MyApp());
}
```

### Build Flavors (Android)

```groovy
// android/app/build.gradle
android {
    flavorDimensions "environment"
    productFlavors {
        dev {
            dimension "environment"
            applicationIdSuffix ".dev"
            versionNameSuffix "-dev"
        }
        staging {
            dimension "environment"
            applicationIdSuffix ".staging"
            versionNameSuffix "-staging"
        }
        prod {
            dimension "environment"
        }
    }
}
```

### Build Commands

```bash
# Development
flutter run --flavor dev -t lib/main_dev.dart

# Staging
flutter run --flavor staging -t lib/main_staging.dart

# Production
flutter build apk --flavor prod -t lib/main_prod.dart --release
flutter build appbundle --flavor prod -t lib/main_prod.dart --release
```

## Secrets Management

```yaml
KHÔNG BAO GIỜ:
  - Commit secrets vào Git
  - Hardcode API keys trong code
  - Log sensitive data

SỬ DỤNG:
  - .env files (gitignore)
  - flutter_dotenv package
  - CI/CD secret variables
```

### .env Example

```
# .env.dev (gitignored)
API_BASE_URL=http://localhost:3000
SENTRY_DSN=

# .env.prod (gitignored)
API_BASE_URL=https://api.allship.vn
SENTRY_DSN=https://xxx@sentry.io/xxx
```

### Loading Secrets

```dart
import 'package:flutter_dotenv/flutter_dotenv.dart';

Future<void> main() async {
  await dotenv.load(fileName: '.env.${EnvConfig.current.name}');
  runApp(const MyApp());
}

// Usage
final apiUrl = dotenv.env['API_BASE_URL'];
```

## Feature Flags

```dart
class FeatureFlags {
  // Runtime toggles
  static bool cloudSyncEnabled = false;
  static bool newRecordingUIEnabled = false;
  static bool betaFeaturesEnabled = false;
  
  // Environment-based
  static bool get debugToolsEnabled => EnvConfig.isDev;
  static bool get mockDataEnabled => EnvConfig.isDev;
}
```

## Logging

```dart
class AppLogger {
  static void debug(String message, [dynamic error]) {
    if (EnvConfig.enableLogging) {
      print('[DEBUG] $message');
      if (error != null) print(error);
    }
  }
  
  static void info(String message) {
    if (EnvConfig.enableLogging) {
      print('[INFO] $message');
    }
  }
  
  static void error(String message, [dynamic error, StackTrace? stack]) {
    print('[ERROR] $message');
    if (error != null) print(error);
    if (EnvConfig.enableCrashReporting) {
      // Send to Sentry/Firebase Crashlytics
    }
  }
}
```

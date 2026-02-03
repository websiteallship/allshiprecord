# Folder Structure - Allship Record

Cấu trúc thư mục chuẩn cho ứng dụng Flutter Allship Record.

---

## 1. Tổng quan kiến trúc

```
lib/
├── main.dart                    # Entry point
├── app.dart                     # MaterialApp configuration
│
├── core/                        # Shared code across features
│   ├── constants/               # App-wide constants
│   ├── extensions/              # Dart extensions
│   ├── theme/                   # Theme, colors, typography
│   ├── utils/                   # Utility functions
│   └── widgets/                 # Reusable widgets
│
├── data/                        # Data layer
│   ├── datasources/            # Local & remote data sources
│   ├── models/                 # Data models / entities
│   └── repositories/           # Repository implementations
│
├── domain/                      # Business logic
│   ├── entities/               # Domain entities
│   ├── repositories/           # Repository interfaces
│   └── usecases/               # Use cases
│
├── features/                    # Feature modules
│   ├── camera/                 # Camera & recording
│   ├── history/                # Video history
│   ├── scanner/                # Barcode scanning
│   ├── settings/               # App settings
│   └── onboarding/             # First-time user flow
│
└── l10n/                        # Localization
    └── intl_vi.arb             # Vietnamese strings
```

---

## 2. Chi tiết từng thư mục

### 2.1 Core (`lib/core/`)

```
core/
├── constants/
│   ├── app_constants.dart       # App-wide constants
│   ├── api_constants.dart       # API endpoints (if any)
│   ├── storage_keys.dart        # SharedPreferences keys
│   └── route_names.dart         # Route path constants
│
├── extensions/
│   ├── context_extensions.dart  # BuildContext extensions
│   ├── datetime_extensions.dart # DateTime helpers
│   ├── string_extensions.dart   # String helpers
│   └── duration_extensions.dart # Duration formatters
│
├── theme/
│   ├── app_theme.dart           # ThemeData (light/dark)
│   ├── app_colors.dart          # Color definitions
│   ├── app_typography.dart      # Text styles
│   ├── app_spacing.dart         # Spacing constants
│   └── app_sizing.dart          # Sizing constants
│
├── utils/
│   ├── file_utils.dart          # File operations
│   ├── permission_utils.dart    # Permission handling
│   ├── date_utils.dart          # Date formatting
│   ├── vibration_utils.dart     # Haptic feedback
│   └── logger.dart              # Logging utility
│
└── widgets/
    ├── app_button.dart
    ├── order_card.dart
    ├── status_badge.dart
    ├── video_overlay_info.dart
    ├── video_thumbnail.dart
    ├── scanner_input.dart
    ├── storage_indicator.dart
    ├── connection_status.dart
    ├── recording_timer.dart
    ├── date_group_header.dart
    ├── confirm_dialog.dart
    ├── stat_card.dart
    ├── empty_state.dart
    ├── settings_tile.dart
    ├── loading_indicator.dart
    └── index.dart               # Export all widgets
```

### 2.2 Data Layer (`lib/data/`)

```
data/
├── datasources/
│   ├── local/
│   │   ├── database_helper.dart     # SQLite helper
│   │   ├── video_local_datasource.dart
│   │   └── settings_local_datasource.dart
│   └── remote/                      # (Future: cloud sync)
│       └── cloud_datasource.dart
│
├── models/
│   ├── video_record_model.dart      # Video record DTO
│   ├── settings_model.dart          # Settings DTO
│   ├── scan_result_model.dart       # Barcode scan result
│   └── device_info_model.dart       # Device information
│
└── repositories/
    ├── video_repository_impl.dart
    ├── settings_repository_impl.dart
    └── scanner_repository_impl.dart
```

### 2.3 Domain Layer (`lib/domain/`)

```
domain/
├── entities/
│   ├── video_record.dart            # Video record entity
│   ├── order_type.dart              # Enum: packing, shipping, return
│   ├── settings.dart                # Settings entity
│   └── scan_result.dart             # Scan result entity
│
├── repositories/
│   ├── video_repository.dart        # Abstract interface
│   ├── settings_repository.dart
│   └── scanner_repository.dart
│
└── usecases/
    ├── video/
    │   ├── start_recording.dart
    │   ├── stop_recording.dart
    │   ├── get_video_history.dart
    │   ├── delete_video.dart
    │   └── export_video.dart
    ├── scanner/
    │   ├── process_barcode.dart
    │   └── validate_order_code.dart
    └── settings/
        ├── get_settings.dart
        └── update_settings.dart
```

### 2.4 Features (`lib/features/`)

Mỗi feature là một module độc lập:

```
features/
├── camera/
│   ├── bloc/
│   │   ├── camera_bloc.dart
│   │   ├── camera_event.dart
│   │   └── camera_state.dart
│   ├── widgets/
│   │   ├── camera_preview.dart
│   │   ├── recording_controls.dart
│   │   └── overlay_layer.dart
│   └── pages/
│       └── camera_page.dart
│
├── history/
│   ├── bloc/
│   │   ├── history_bloc.dart
│   │   ├── history_event.dart
│   │   └── history_state.dart
│   ├── widgets/
│   │   ├── video_list.dart
│   │   ├── video_list_item.dart
│   │   └── search_bar.dart
│   └── pages/
│       ├── history_page.dart
│       └── video_detail_page.dart
│
├── scanner/
│   ├── bloc/
│   │   ├── scanner_bloc.dart
│   │   ├── scanner_event.dart
│   │   └── scanner_state.dart
│   ├── widgets/
│   │   └── scanner_overlay.dart
│   └── pages/
│       └── scanner_page.dart
│
├── settings/
│   ├── bloc/
│   │   ├── settings_bloc.dart
│   │   ├── settings_event.dart
│   │   └── settings_state.dart
│   ├── widgets/
│   │   └── settings_section.dart
│   └── pages/
│       ├── settings_page.dart
│       ├── camera_settings_page.dart
│       ├── storage_settings_page.dart
│       └── about_page.dart
│
└── onboarding/
    ├── widgets/
    │   ├── permission_card.dart
    │   └── onboarding_step.dart
    └── pages/
        └── onboarding_page.dart
```

### 2.5 Localization (`lib/l10n/`)

```
l10n/
├── intl_vi.arb                  # Vietnamese (default)
└── intl_en.arb                  # English (optional)
```

---

## 3. Entry Files

### 3.1 main.dart

```dart
// lib/main.dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'app.dart';
import 'core/utils/logger.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Lock orientation to portrait
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
  ]);
  
  // Initialize logging
  AppLogger.init();
  
  // Run app
  runApp(const AllshipRecordApp());
}
```

### 3.2 app.dart

```dart
// lib/app.dart
import 'package:flutter/material.dart';
import 'core/theme/app_theme.dart';
import 'core/constants/route_names.dart';

class AllshipRecordApp extends StatelessWidget {
  const AllshipRecordApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Allship Record',
      debugShowCheckedModeBanner: false,
      
      // Theming
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.system,
      
      // Routing
      initialRoute: RouteNames.splash,
      onGenerateRoute: AppRouter.generateRoute,
      
      // Localization
      locale: const Locale('vi', 'VN'),
      supportedLocales: const [
        Locale('vi', 'VN'),
      ],
    );
  }
}
```

---

## 4. Naming Conventions

### 4.1 Files

| Type | Convention | Example |
|---|---|---|
| Pages | `*_page.dart` | `camera_page.dart` |
| Widgets | `*_widget.dart` hoặc tên component | `order_card.dart` |
| BLoC | `*_bloc.dart`, `*_event.dart`, `*_state.dart` | `camera_bloc.dart` |
| Models | `*_model.dart` | `video_record_model.dart` |
| Entities | Tên entity | `video_record.dart` |
| Repositories | `*_repository.dart` / `*_repository_impl.dart` | `video_repository.dart` |
| Use Cases | Verb phrase | `start_recording.dart` |
| Utils | `*_utils.dart` | `file_utils.dart` |
| Constants | `*_constants.dart` | `app_constants.dart` |

### 4.2 Classes

| Type | Convention | Example |
|---|---|---|
| Pages | `*Page` | `CameraPage` |
| Widgets | PascalCase | `OrderCard` |
| BLoC | `*Bloc`, `*Event`, `*State` | `CameraBloc` |
| Models | `*Model` | `VideoRecordModel` |
| Entities | PascalCase | `VideoRecord` |
| Repositories | `*Repository`, `*RepositoryImpl` | `VideoRepository` |
| Use Cases | PascalCase | `StartRecording` |

---

## 5. Import Order

Thứ tự import trong mỗi file:

```dart
// 1. Dart SDK
import 'dart:async';
import 'dart:io';

// 2. Flutter SDK
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

// 3. Third-party packages
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:iconsax_flutter/iconsax_flutter.dart';

// 4. Project imports - absolute path
import 'package:allship_record/core/theme/app_theme.dart';
import 'package:allship_record/core/widgets/index.dart';
import 'package:allship_record/features/camera/bloc/camera_bloc.dart';

// 5. Relative imports (same feature only)
import '../widgets/camera_preview.dart';
import 'camera_state.dart';
```

---

## 6. Assets Structure

```
assets/
├── fonts/
│   ├── Rubik-Regular.ttf
│   ├── Rubik-Medium.ttf
│   ├── Rubik-SemiBold.ttf
│   ├── Rubik-Bold.ttf
│   ├── NunitoSans-Regular.ttf
│   ├── NunitoSans-Medium.ttf
│   ├── NunitoSans-SemiBold.ttf
│   ├── NunitoSans-Bold.ttf
│   ├── RobotoMono-Regular.ttf
│   └── RobotoMono-Medium.ttf
│
├── images/
│   ├── logo.png
│   ├── logo_dark.png
│   ├── onboarding_1.png
│   ├── onboarding_2.png
│   ├── onboarding_3.png
│   └── empty_state.png
│
└── sounds/
    ├── scan_success.mp3
    ├── scan_error.mp3
    ├── recording_start.mp3
    └── recording_stop.mp3
```

---

## 7. Quick Reference

### File Location by Type

| Tìm gì? | Ở đâu? |
|---|---|
| Colors, Typography | `lib/core/theme/` |
| Reusable widgets | `lib/core/widgets/` |
| Feature UI | `lib/features/{feature}/pages/` |
| Feature widgets | `lib/features/{feature}/widgets/` |
| BLoC | `lib/features/{feature}/bloc/` |
| Database | `lib/data/datasources/local/` |
| Data models | `lib/data/models/` |
| Business logic | `lib/domain/usecases/` |
| Routes | `lib/core/constants/route_names.dart` |
| Localization | `lib/l10n/` |

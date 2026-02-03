# Project Architecture - ALL SHIP ECOMBOX

## Kiến Trúc Tổng Quan

### Clean Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│  (UI, Widgets, Screens, ViewModels/BLoCs)                   │
├─────────────────────────────────────────────────────────────┤
│                      DOMAIN LAYER                            │
│  (Entities, Use Cases, Repository Interfaces)               │
├─────────────────────────────────────────────────────────────┤
│                       DATA LAYER                             │
│  (Repository Implementations, Data Sources, Models)         │
├─────────────────────────────────────────────────────────────┤
│                     PLATFORM LAYER                           │
│  (Native code: Camera, Video Encoding, Bluetooth)           │
└─────────────────────────────────────────────────────────────┘
```

## Module Structure

### Flutter Project Structure

```
lib/
├── main.dart                 # Entry point
├── app/
│   ├── app.dart              # App widget, routing
│   └── di.dart               # Dependency injection setup
│
├── core/                     # Shared utilities
│   ├── constants/
│   │   ├── app_constants.dart
│   │   └── video_constants.dart
│   ├── extensions/
│   │   ├── datetime_ext.dart
│   │   └── string_ext.dart
│   ├── errors/
│   │   ├── app_error.dart
│   │   └── failures.dart
│   ├── utils/
│   │   ├── file_utils.dart
│   │   └── validators.dart
│   └── theme/
│       ├── app_theme.dart
│       ├── colors.dart
│       └── typography.dart
│
├── data/                     # Data layer
│   ├── datasources/
│   │   ├── local/
│   │   │   ├── database.dart
│   │   │   └── preferences.dart
│   │   └── remote/           # Phase 4
│   │       └── api_client.dart
│   ├── models/
│   │   ├── order_model.dart
│   │   └── video_model.dart
│   └── repositories/
│       ├── order_repository_impl.dart
│       └── video_repository_impl.dart
│
├── domain/                   # Business logic
│   ├── entities/
│   │   ├── order.dart
│   │   └── video.dart
│   ├── repositories/         # Interfaces
│   │   ├── order_repository.dart
│   │   └── video_repository.dart
│   └── usecases/
│       ├── create_order.dart
│       ├── start_recording.dart
│       ├── stop_recording.dart
│       └── search_videos.dart
│
├── presentation/             # UI layer
│   ├── common/
│   │   ├── widgets/
│   │   │   ├── app_button.dart
│   │   │   ├── order_card.dart
│   │   │   └── video_thumbnail.dart
│   │   └── dialogs/
│   │       └── error_dialog.dart
│   ├── recording/
│   │   ├── recording_screen.dart
│   │   ├── recording_bloc.dart
│   │   └── widgets/
│   │       ├── camera_preview.dart
│   │       ├── recording_indicator.dart
│   │       └── order_overlay.dart
│   ├── return/
│   │   ├── return_screen.dart
│   │   └── return_bloc.dart
│   ├── search/
│   │   ├── search_screen.dart
│   │   └── search_bloc.dart
│   └── settings/
│       ├── settings_screen.dart
│       └── settings_bloc.dart
│
└── services/                 # Platform services
    ├── camera/
    │   ├── camera_service.dart
    │   └── camera_service_impl.dart
    ├── scanner/
    │   ├── scanner_service.dart
    │   └── bluetooth_scanner.dart
    ├── video/
    │   ├── video_encoder.dart
    │   └── thumbnail_generator.dart
    ├── audio/
    │   └── feedback_audio.dart
    └── storage/
        └── storage_manager.dart
```

## Module Dependencies

### Dependency Flow

```
presentation → domain → data
     ↓           ↓        ↓
  services ←←←←←←←←←←←←←←←┘

RULE: Dependencies flow INWARD only
  - presentation có thể depend on domain
  - domain KHÔNG depend on presentation
  - data implement domain interfaces
```

### Module Responsibilities

| Module | Trách Nhiệm |
|--------|-------------|
| `core/` | Constants, utilities, theme - shared across all modules |
| `domain/` | Business logic thuần, không UI, không framework |
| `data/` | Data access, caching, API calls |
| `presentation/` | UI widgets, screens, state management |
| `services/` | Platform-specific code, native integration |

## Feature Modules

### Recording Module

```dart
// lib/presentation/recording/

recording/
├── recording_screen.dart       # Main screen
├── recording_bloc.dart         # State management
├── recording_event.dart        # BLoC events
├── recording_state.dart        # BLoC states
└── widgets/
    ├── camera_preview.dart     # Camera view
    ├── recording_indicator.dart # REC indicator
    ├── order_overlay.dart      # Order code overlay
    └── action_buttons.dart     # Start/Stop buttons
```

### Search Module

```dart
// lib/presentation/search/

search/
├── search_screen.dart
├── search_bloc.dart
└── widgets/
    ├── search_bar.dart
    ├── video_list.dart
    └── video_player_dialog.dart
```

## State Management

### BLoC Pattern (Recommended)

```dart
// Events
abstract class RecordingEvent {}
class StartRecording extends RecordingEvent {
  final String orderCode;
}
class StopRecording extends RecordingEvent {}
class BarcodeScanned extends RecordingEvent {
  final String barcode;
}

// States
abstract class RecordingState {}
class RecordingInitial extends RecordingState {}
class RecordingInProgress extends RecordingState {
  final String orderCode;
  final Duration elapsed;
}
class RecordingSaved extends RecordingState {
  final Video video;
}
class RecordingError extends RecordingState {
  final String message;
}

// BLoC
class RecordingBloc extends Bloc<RecordingEvent, RecordingState> {
  final StartRecordingUseCase startRecording;
  final StopRecordingUseCase stopRecording;
  
  RecordingBloc({
    required this.startRecording,
    required this.stopRecording,
  }) : super(RecordingInitial()) {
    on<StartRecording>(_onStartRecording);
    on<StopRecording>(_onStopRecording);
    on<BarcodeScanned>(_onBarcodeScanned);
  }
}
```

## Dependency Injection

### GetIt Setup

```dart
// lib/app/di.dart
import 'package:get_it/get_it.dart';

final getIt = GetIt.instance;

Future<void> setupDependencies() async {
  // Services
  getIt.registerLazySingleton<CameraService>(
    () => CameraServiceImpl(),
  );
  getIt.registerLazySingleton<ScannerService>(
    () => BluetoothScannerService(),
  );
  
  // Data sources
  getIt.registerLazySingleton<Database>(
    () => AppDatabase(),
  );
  
  // Repositories
  getIt.registerLazySingleton<OrderRepository>(
    () => OrderRepositoryImpl(getIt()),
  );
  getIt.registerLazySingleton<VideoRepository>(
    () => VideoRepositoryImpl(getIt()),
  );
  
  // Use cases
  getIt.registerFactory(
    () => StartRecordingUseCase(getIt(), getIt()),
  );
  
  // BLoCs
  getIt.registerFactory(
    () => RecordingBloc(
      startRecording: getIt(),
      stopRecording: getIt(),
    ),
  );
}
```

## Platform Channels

### Native Code Structure

```
android/
├── app/src/main/kotlin/com/allship/ecombox/
│   ├── MainActivity.kt
│   └── channels/
│       ├── VideoEncoderChannel.kt    # MediaCodec
│       └── BluetoothScannerChannel.kt

ios/
├── Runner/
│   ├── AppDelegate.swift
│   └── Channels/
│       ├── VideoEncoderChannel.swift  # VideoToolbox
│       └── BluetoothScannerChannel.swift
```

### Channel Definition

```dart
// lib/services/video/video_encoder.dart
class VideoEncoderChannel {
  static const _channel = MethodChannel('com.allship.ecombox/video_encoder');
  
  Future<void> startEncoding({
    required String outputPath,
    required int width,
    required int height,
    required int bitrate,
    required int fps,
  }) async {
    await _channel.invokeMethod('startEncoding', {
      'outputPath': outputPath,
      'width': width,
      'height': height,
      'bitrate': bitrate,
      'fps': fps,
    });
  }
  
  Future<void> stopEncoding() async {
    await _channel.invokeMethod('stopEncoding');
  }
}
```

## Error Handling Architecture

### Error Types

```dart
// lib/core/errors/failures.dart
sealed class Failure {
  final String message;
  const Failure(this.message);
}

class CameraFailure extends Failure {
  const CameraFailure(super.message);
}

class StorageFailure extends Failure {
  const StorageFailure(super.message);
}

class ScannerFailure extends Failure {
  const ScannerFailure(super.message);
}

class DatabaseFailure extends Failure {
  const DatabaseFailure(super.message);
}
```

### Result Type

```dart
// lib/core/utils/result.dart
sealed class Result<T> {}

class Success<T> extends Result<T> {
  final T data;
  const Success(this.data);
}

class Error<T> extends Result<T> {
  final Failure failure;
  const Error(this.failure);
}

// Usage in use case
class StartRecordingUseCase {
  Future<Result<void>> call(String orderCode) async {
    try {
      await cameraService.startRecording(orderCode);
      return Success(null);
    } on CameraException catch (e) {
      return Error(CameraFailure(e.message));
    }
  }
}
```

## Configuration

### Environment Config

```dart
// lib/core/config/env_config.dart
enum Environment { development, staging, production }

class EnvConfig {
  static Environment get current => Environment.development;
  
  static String get apiBaseUrl {
    switch (current) {
      case Environment.development:
        return 'http://localhost:3000';
      case Environment.staging:
        return 'https://staging-api.allship.vn';
      case Environment.production:
        return 'https://api.allship.vn';
    }
  }
}
```

### Feature Flags

```dart
// lib/core/config/feature_flags.dart
class FeatureFlags {
  static const cloudSyncEnabled = false;  // Phase 4
  static const ipCameraEnabled = false;   // Phase 3
  static const multiUserEnabled = false;  // Phase 4
  static const darkModeEnabled = true;
  static const biometricAuthEnabled = false;
}
```

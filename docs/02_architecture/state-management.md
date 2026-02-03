# State Management Architecture - Allship Record

Kiến trúc State Management sử dụng BLoC pattern.

---

## 1. Tổng quan

### 1.1 Pattern đã chọn: BLoC

| Tiêu chí | BLoC |
|---|---|
| **Scalability** | ✅ Tốt cho app lớn |
| **Testability** | ✅ Dễ test |
| **Separation** | ✅ Tách biệt rõ ràng |
| **Learning Curve** | ⚠️ Trung bình |
| **Boilerplate** | ⚠️ Nhiều hơn Riverpod |

### 1.2 Dependencies

```yaml
dependencies:
  flutter_bloc: ^8.1.3
  equatable: ^2.0.5
  bloc_concurrency: ^0.2.2  # Optional: for event debouncing
```

---

## 2. BLoC Architecture

### 2.1 Sơ đồ tổng quan

```
┌─────────────────────────────────────────────────────────────────┐
│                           UI Layer                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  CameraPage │  │ HistoryPage │  │ SettingsPage│              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                      │
│         ▼                ▼                ▼                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ BlocBuilder │  │ BlocBuilder │  │ BlocBuilder │              │
│  │ BlocListener│  │ BlocListener│  │ BlocListener│              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                          BLoC Layer                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ CameraBloc  │  │HistoryBloc │  │SettingsBloc │              │
│  │             │  │             │  │             │              │
│  │ Event→State │  │ Event→State │  │ Event→State │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Domain Layer                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │StartRecording│ │GetVideoList│  │GetSettings  │              │
│  │StopRecording │ │DeleteVideo │  │UpdateSettings│             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                         Data Layer                               │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                     Repositories                         │    │
│  │  VideoRepository  │  SettingsRepository  │  ScannerRepo  │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. BLoC Structure

### 3.1 Event

```dart
// lib/features/camera/bloc/camera_event.dart

import 'package:equatable/equatable.dart';

abstract class CameraEvent extends Equatable {
  const CameraEvent();
  
  @override
  List<Object?> get props => [];
}

/// Initialize camera
class CameraInitialized extends CameraEvent {}

/// Barcode scanned
class BarcodeScanned extends CameraEvent {
  final String orderCode;
  
  const BarcodeScanned(this.orderCode);
  
  @override
  List<Object?> get props => [orderCode];
}

/// Start recording
class RecordingStarted extends CameraEvent {
  final String orderCode;
  final String orderType; // 'packing', 'shipping', 'return'
  
  const RecordingStarted({
    required this.orderCode,
    required this.orderType,
  });
  
  @override
  List<Object?> get props => [orderCode, orderType];
}

/// Stop recording
class RecordingStopped extends CameraEvent {}

/// Pause recording
class RecordingPaused extends CameraEvent {}

/// Resume recording
class RecordingResumed extends CameraEvent {}

/// Recording timer tick
class RecordingTicked extends CameraEvent {
  final Duration elapsed;
  
  const RecordingTicked(this.elapsed);
  
  @override
  List<Object?> get props => [elapsed];
}

/// Camera error
class CameraErrorOccurred extends CameraEvent {
  final String error;
  
  const CameraErrorOccurred(this.error);
  
  @override
  List<Object?> get props => [error];
}
```

### 3.2 State

```dart
// lib/features/camera/bloc/camera_state.dart

import 'package:equatable/equatable.dart';

enum CameraStatus {
  initial,
  loading,
  ready,
  scanning,
  recording,
  paused,
  saving,
  saved,
  error,
}

class CameraState extends Equatable {
  final CameraStatus status;
  final String? orderCode;
  final String? orderType;
  final Duration elapsed;
  final Duration maxDuration;
  final String? videoPath;
  final String? errorMessage;
  
  const CameraState({
    this.status = CameraStatus.initial,
    this.orderCode,
    this.orderType,
    this.elapsed = Duration.zero,
    this.maxDuration = const Duration(minutes: 3),
    this.videoPath,
    this.errorMessage,
  });
  
  /// Copy with new values
  CameraState copyWith({
    CameraStatus? status,
    String? orderCode,
    String? orderType,
    Duration? elapsed,
    Duration? maxDuration,
    String? videoPath,
    String? errorMessage,
  }) {
    return CameraState(
      status: status ?? this.status,
      orderCode: orderCode ?? this.orderCode,
      orderType: orderType ?? this.orderType,
      elapsed: elapsed ?? this.elapsed,
      maxDuration: maxDuration ?? this.maxDuration,
      videoPath: videoPath ?? this.videoPath,
      errorMessage: errorMessage ?? this.errorMessage,
    );
  }
  
  /// Convenience getters
  bool get isRecording => status == CameraStatus.recording;
  bool get isPaused => status == CameraStatus.paused;
  bool get isReady => status == CameraStatus.ready;
  bool get hasError => status == CameraStatus.error;
  
  double get progress => elapsed.inSeconds / maxDuration.inSeconds;
  bool get isNearLimit => progress > 0.9;
  
  @override
  List<Object?> get props => [
    status,
    orderCode,
    orderType,
    elapsed,
    maxDuration,
    videoPath,
    errorMessage,
  ];
}
```

### 3.3 BLoC

```dart
// lib/features/camera/bloc/camera_bloc.dart

import 'dart:async';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'camera_event.dart';
import 'camera_state.dart';

class CameraBloc extends Bloc<CameraEvent, CameraState> {
  final StartRecordingUseCase _startRecording;
  final StopRecordingUseCase _stopRecording;
  final ProcessBarcodeUseCase _processBarcode;
  
  StreamSubscription<Duration>? _timerSubscription;
  
  CameraBloc({
    required StartRecordingUseCase startRecording,
    required StopRecordingUseCase stopRecording,
    required ProcessBarcodeUseCase processBarcode,
  })  : _startRecording = startRecording,
        _stopRecording = stopRecording,
        _processBarcode = processBarcode,
        super(const CameraState()) {
    // Register event handlers
    on<CameraInitialized>(_onCameraInitialized);
    on<BarcodeScanned>(_onBarcodeScanned);
    on<RecordingStarted>(_onRecordingStarted);
    on<RecordingStopped>(_onRecordingStopped);
    on<RecordingPaused>(_onRecordingPaused);
    on<RecordingResumed>(_onRecordingResumed);
    on<RecordingTicked>(_onRecordingTicked);
    on<CameraErrorOccurred>(_onCameraError);
  }
  
  // ═══════════════════════════════════════════════════════════════
  // EVENT HANDLERS
  // ═══════════════════════════════════════════════════════════════
  
  Future<void> _onCameraInitialized(
    CameraInitialized event,
    Emitter<CameraState> emit,
  ) async {
    emit(state.copyWith(status: CameraStatus.loading));
    
    try {
      // Initialize camera
      await _initializeCamera();
      emit(state.copyWith(status: CameraStatus.ready));
    } catch (e) {
      emit(state.copyWith(
        status: CameraStatus.error,
        errorMessage: e.toString(),
      ));
    }
  }
  
  Future<void> _onBarcodeScanned(
    BarcodeScanned event,
    Emitter<CameraState> emit,
  ) async {
    emit(state.copyWith(status: CameraStatus.scanning));
    
    try {
      final result = await _processBarcode(event.orderCode);
      
      if (result.isValid) {
        emit(state.copyWith(
          status: CameraStatus.ready,
          orderCode: event.orderCode,
          orderType: result.orderType,
        ));
      } else {
        emit(state.copyWith(
          status: CameraStatus.error,
          errorMessage: 'Mã vận đơn không hợp lệ',
        ));
      }
    } catch (e) {
      emit(state.copyWith(
        status: CameraStatus.error,
        errorMessage: e.toString(),
      ));
    }
  }
  
  Future<void> _onRecordingStarted(
    RecordingStarted event,
    Emitter<CameraState> emit,
  ) async {
    try {
      await _startRecording(
        orderCode: event.orderCode,
        orderType: event.orderType,
      );
      
      emit(state.copyWith(
        status: CameraStatus.recording,
        orderCode: event.orderCode,
        orderType: event.orderType,
        elapsed: Duration.zero,
      ));
      
      // Start timer
      _startTimer();
    } catch (e) {
      emit(state.copyWith(
        status: CameraStatus.error,
        errorMessage: e.toString(),
      ));
    }
  }
  
  Future<void> _onRecordingStopped(
    RecordingStopped event,
    Emitter<CameraState> emit,
  ) async {
    _timerSubscription?.cancel();
    emit(state.copyWith(status: CameraStatus.saving));
    
    try {
      final videoPath = await _stopRecording();
      
      emit(state.copyWith(
        status: CameraStatus.saved,
        videoPath: videoPath,
      ));
    } catch (e) {
      emit(state.copyWith(
        status: CameraStatus.error,
        errorMessage: e.toString(),
      ));
    }
  }
  
  void _onRecordingPaused(
    RecordingPaused event,
    Emitter<CameraState> emit,
  ) {
    _timerSubscription?.pause();
    emit(state.copyWith(status: CameraStatus.paused));
  }
  
  void _onRecordingResumed(
    RecordingResumed event,
    Emitter<CameraState> emit,
  ) {
    _timerSubscription?.resume();
    emit(state.copyWith(status: CameraStatus.recording));
  }
  
  void _onRecordingTicked(
    RecordingTicked event,
    Emitter<CameraState> emit,
  ) {
    emit(state.copyWith(elapsed: event.elapsed));
    
    // Auto-stop when reaching max duration
    if (event.elapsed >= state.maxDuration) {
      add(RecordingStopped());
    }
  }
  
  void _onCameraError(
    CameraErrorOccurred event,
    Emitter<CameraState> emit,
  ) {
    emit(state.copyWith(
      status: CameraStatus.error,
      errorMessage: event.error,
    ));
  }
  
  // ═══════════════════════════════════════════════════════════════
  // PRIVATE METHODS
  // ═══════════════════════════════════════════════════════════════
  
  void _startTimer() {
    _timerSubscription?.cancel();
    _timerSubscription = Stream.periodic(
      const Duration(seconds: 1),
      (tick) => Duration(seconds: tick + 1),
    ).listen((elapsed) {
      add(RecordingTicked(elapsed));
    });
  }
  
  Future<void> _initializeCamera() async {
    // Camera initialization logic
  }
  
  @override
  Future<void> close() {
    _timerSubscription?.cancel();
    return super.close();
  }
}
```

---

## 4. BLoC Provider Setup

### 4.1 App-level Providers

```dart
// lib/app.dart

class AllshipRecordApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiRepositoryProvider(
      providers: [
        RepositoryProvider<VideoRepository>(
          create: (_) => VideoRepositoryImpl(),
        ),
        RepositoryProvider<SettingsRepository>(
          create: (_) => SettingsRepositoryImpl(),
        ),
        RepositoryProvider<ScannerRepository>(
          create: (_) => ScannerRepositoryImpl(),
        ),
      ],
      child: MultiBlocProvider(
        providers: [
          // Global BLoCs
          BlocProvider<SettingsBloc>(
            create: (context) => SettingsBloc(
              repository: context.read<SettingsRepository>(),
            )..add(SettingsLoaded()),
          ),
        ],
        child: MaterialApp.router(
          // ...
        ),
      ),
    );
  }
}
```

### 4.2 Feature-level Providers

```dart
// lib/features/camera/pages/camera_page.dart

class CameraPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => CameraBloc(
        startRecording: StartRecordingUseCase(
          repository: context.read<VideoRepository>(),
        ),
        stopRecording: StopRecordingUseCase(
          repository: context.read<VideoRepository>(),
        ),
        processBarcode: ProcessBarcodeUseCase(
          repository: context.read<ScannerRepository>(),
        ),
      )..add(CameraInitialized()),
      child: const CameraView(),
    );
  }
}
```

---

## 5. Usage in Widgets

### 5.1 BlocBuilder

```dart
// Rebuild when state changes
BlocBuilder<CameraBloc, CameraState>(
  builder: (context, state) {
    if (state.status == CameraStatus.loading) {
      return LoadingIndicator();
    }
    
    if (state.status == CameraStatus.recording) {
      return RecordingTimer(
        elapsed: state.elapsed,
        maxDuration: state.maxDuration,
      );
    }
    
    return CameraPreview();
  },
)

// Only rebuild for specific state changes
BlocBuilder<CameraBloc, CameraState>(
  buildWhen: (previous, current) => 
    previous.elapsed != current.elapsed,
  builder: (context, state) {
    return Text('${state.elapsed.inSeconds}s');
  },
)
```

### 5.2 BlocListener

```dart
// Side effects (navigation, snackbar, etc.)
BlocListener<CameraBloc, CameraState>(
  listenWhen: (previous, current) =>
    previous.status != current.status,
  listener: (context, state) {
    if (state.status == CameraStatus.saved) {
      // Navigate to preview
      context.push(
        RouteNames.recordingPreview,
        extra: state.videoPath,
      );
    }
    
    if (state.status == CameraStatus.error) {
      // Show error snackbar
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(state.errorMessage!)),
      );
    }
  },
  child: childWidget,
)
```

### 5.3 BlocConsumer

```dart
// Both build and listen
BlocConsumer<CameraBloc, CameraState>(
  listenWhen: (previous, current) =>
    current.status == CameraStatus.error,
  listener: (context, state) {
    showErrorDialog(context, state.errorMessage!);
  },
  buildWhen: (previous, current) =>
    previous.status != current.status,
  builder: (context, state) {
    return switch (state.status) {
      CameraStatus.recording => RecordingView(),
      CameraStatus.ready => ReadyView(),
      _ => LoadingView(),
    };
  },
)
```

### 5.4 Dispatching Events

```dart
// From widget
ElevatedButton(
  onPressed: () {
    context.read<CameraBloc>().add(
      RecordingStarted(
        orderCode: 'ORD123',
        orderType: 'packing',
      ),
    );
  },
  child: Text('Bắt đầu quay'),
)

// Using extension
extension BlocExt on BuildContext {
  void startRecording(String orderCode, String type) {
    read<CameraBloc>().add(
      RecordingStarted(orderCode: orderCode, orderType: type),
    );
  }
}

// Usage
context.startRecording('ORD123', 'packing');
```

---

## 6. All BLoCs in Project

| BLoC | Feature | Responsibilities |
|---|---|---|
| `CameraBloc` | Camera | Recording, scanning, timer |
| `HistoryBloc` | History | Video list, search, delete |
| `VideoPlayerBloc` | History | Playback control |
| `SettingsBloc` | Settings | App preferences |
| `StorageBloc` | Settings | Storage management |
| `ScannerBloc` | Scanner | Bluetooth HID devices |
| `DashboardBloc` | Dashboard | Statistics |
| `OnboardingBloc` | Onboarding | Permissions, setup |

---

## 7. Testing BLoCs

### 7.1 Unit Test

```dart
// test/features/camera/bloc/camera_bloc_test.dart

import 'package:bloc_test/bloc_test.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';

void main() {
  late CameraBloc cameraBloc;
  late MockStartRecordingUseCase mockStartRecording;
  
  setUp(() {
    mockStartRecording = MockStartRecordingUseCase();
    cameraBloc = CameraBloc(
      startRecording: mockStartRecording,
      // ...
    );
  });
  
  tearDown(() {
    cameraBloc.close();
  });
  
  blocTest<CameraBloc, CameraState>(
    'emits [loading, ready] when CameraInitialized is added',
    build: () => cameraBloc,
    act: (bloc) => bloc.add(CameraInitialized()),
    expect: () => [
      const CameraState(status: CameraStatus.loading),
      const CameraState(status: CameraStatus.ready),
    ],
  );
  
  blocTest<CameraBloc, CameraState>(
    'emits [recording] when RecordingStarted is added',
    build: () {
      when(mockStartRecording.call(any)).thenAnswer((_) async => {});
      return cameraBloc;
    },
    seed: () => const CameraState(status: CameraStatus.ready),
    act: (bloc) => bloc.add(
      const RecordingStarted(orderCode: 'ORD123', orderType: 'packing'),
    ),
    expect: () => [
      const CameraState(
        status: CameraStatus.recording,
        orderCode: 'ORD123',
        orderType: 'packing',
      ),
    ],
  );
}
```

---

## 8. Best Practices

### 8.1 Event Naming

| Pattern | Example |
|---|---|
| Past tense for triggers | `BarcodeScanned`, `RecordingStarted` |
| Present tense for actions | `SaveVideo`, `DeleteVideo` |
| Suffix with context | `CameraInitialized`, `HistoryLoaded` |

### 8.2 State Design

- ✅ Use `Equatable` for proper comparison
- ✅ Use `copyWith` for immutability
- ✅ Add convenience getters (`isLoading`, `hasError`)
- ✅ Keep state flat, avoid deep nesting

### 8.3 Performance

- ✅ Use `buildWhen` to reduce rebuilds
- ✅ Use `listenWhen` to filter side effects
- ✅ Close BLoCs in `dispose`
- ✅ Cancel subscriptions in BLoC `close()`

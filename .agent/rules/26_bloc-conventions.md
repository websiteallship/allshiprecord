# BLoC Conventions

Quy tắc đặt tên và cấu trúc BLoC trong dự án Allship Record.

---

## 📁 Cấu trúc thư mục

```
lib/features/{feature}/
├── bloc/
│   ├── {feature}_bloc.dart      # BLoC class
│   ├── {feature}_event.dart     # Events
│   └── {feature}_state.dart     # State
├── pages/
│   └── {feature}_page.dart
└── widgets/
    └── ...
```

---

## 📝 Naming Conventions

### Events

| Pattern | Khi nào dùng | Ví dụ |
|---|---|---|
| `{Noun}{PastTense}` | Triggered by user/system | `BarcodeScanned`, `RecordingStarted` |
| `{Feature}Loaded` | Initial load | `HistoryLoaded`, `SettingsLoaded` |
| `{Action}Requested` | User action | `DeleteRequested`, `ExportRequested` |

```dart
// ✅ ĐÚNG
class BarcodeScanned extends CameraEvent {}
class RecordingStarted extends CameraEvent {}
class VideoDeleted extends HistoryEvent {}

// ❌ SAI
class ScanBarcode extends CameraEvent {}  // Không dùng imperative
class StartRecording extends CameraEvent {}  // Dùng past tense
```

### States

```dart
// ✅ ĐÚNG - Single state class với status enum
enum CameraStatus { initial, loading, ready, recording, error }

class CameraState extends Equatable {
  final CameraStatus status;
  final String? errorMessage;
  // ...
}

// ❌ SAI - Multiple state classes (quá nhiều boilerplate)
class CameraInitial extends CameraState {}
class CameraLoading extends CameraState {}
class CameraReady extends CameraState {}
```

### BLoC Class

```dart
class {Feature}Bloc extends Bloc<{Feature}Event, {Feature}State> {
  // Dependencies via constructor
  final VideoRepository _videoRepository;
  
  {Feature}Bloc({required VideoRepository videoRepository})
    : _videoRepository = videoRepository,
      super(const {Feature}State()) {
    // Register handlers
    on<{Feature}Loaded>(_onLoaded);
    on<VideoDeleted>(_onVideoDeleted);
  }
  
  // Handler naming: _on{EventName}
  Future<void> _onLoaded(
    {Feature}Loaded event,
    Emitter<{Feature}State> emit,
  ) async {
    // Implementation
  }
}
```

---

## 🎯 Best Practices

### 1. State immutability

```dart
// ✅ ĐÚNG - Sử dụng copyWith
emit(state.copyWith(status: CameraStatus.loading));

// ❌ SAI - Mutate state
state.status = CameraStatus.loading;  // KHÔNG!
```

### 2. Error handling

```dart
Future<void> _onRecordingStarted(...) async {
  emit(state.copyWith(status: CameraStatus.loading));
  
  try {
    await _startRecording();
    emit(state.copyWith(status: CameraStatus.recording));
  } catch (e) {
    emit(state.copyWith(
      status: CameraStatus.error,
      errorMessage: e.toString(),
    ));
  }
}
```

### 3. Convenience getters trong State

```dart
class CameraState extends Equatable {
  final CameraStatus status;
  
  // ✅ Thêm convenience getters
  bool get isLoading => status == CameraStatus.loading;
  bool get isRecording => status == CameraStatus.recording;
  bool get hasError => status == CameraStatus.error;
}
```

### 4. Cleanup resources

```dart
@override
Future<void> close() {
  _subscription?.cancel();
  _controller?.dispose();
  return super.close();
}
```

---

## 📋 Checklist

- [ ] Event names là past tense hoặc `*Loaded`/`*Requested`
- [ ] State sử dụng status enum, không tạo nhiều class
- [ ] State extends Equatable với đầy đủ props
- [ ] State có copyWith method
- [ ] BLoC cleanup resources trong close()
- [ ] Handler methods đặt tên `_on{EventName}`

---

## 🔗 Tài liệu liên quan

- `docs/02_architecture/state-management.md` - Chi tiết BLoC architecture

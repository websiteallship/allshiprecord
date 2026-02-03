---
description: Quy trình tạo BLoC mới theo chuẩn dự án
---

# Add BLoC Workflow

Quy trình chuẩn để tạo BLoC mới trong ứng dụng Allship Record.

---

## Step 1: Xác định thông tin

- **BLoC name**: Tên BLoC (ví dụ: `VideoPlayer`)
- **Feature folder**: Thuộc feature nào
- **Events**: Các sự kiện BLoC cần xử lý
- **State fields**: Các field trong state

---

## Step 2: Tạo file structure

```bash
lib/features/{feature}/bloc/
├── {name}_bloc.dart
├── {name}_event.dart
└── {name}_state.dart
```

---

## Step 3: Tạo Event file

```dart
// lib/features/history/bloc/video_player_event.dart

import 'package:equatable/equatable.dart';

abstract class VideoPlayerEvent extends Equatable {
  const VideoPlayerEvent();

  @override
  List<Object?> get props => [];
}

/// Video được load
class VideoLoaded extends VideoPlayerEvent {
  final String videoId;

  const VideoLoaded(this.videoId);

  @override
  List<Object?> get props => [videoId];
}

/// Play/Pause toggle
class PlayPauseToggled extends VideoPlayerEvent {}

/// Seek đến vị trí
class VideoSeeked extends VideoPlayerEvent {
  final Duration position;

  const VideoSeeked(this.position);

  @override
  List<Object?> get props => [position];
}
```

---

## Step 4: Tạo State file

```dart
// lib/features/history/bloc/video_player_state.dart

import 'package:equatable/equatable.dart';

enum VideoPlayerStatus { initial, loading, ready, playing, paused, error }

class VideoPlayerState extends Equatable {
  final VideoPlayerStatus status;
  final String? videoPath;
  final Duration position;
  final Duration duration;
  final String? errorMessage;

  const VideoPlayerState({
    this.status = VideoPlayerStatus.initial,
    this.videoPath,
    this.position = Duration.zero,
    this.duration = Duration.zero,
    this.errorMessage,
  });

  // Convenience getters
  bool get isPlaying => status == VideoPlayerStatus.playing;
  bool get isLoading => status == VideoPlayerStatus.loading;
  bool get hasError => status == VideoPlayerStatus.error;
  double get progress => duration.inMilliseconds > 0
      ? position.inMilliseconds / duration.inMilliseconds
      : 0;

  // CopyWith method
  VideoPlayerState copyWith({
    VideoPlayerStatus? status,
    String? videoPath,
    Duration? position,
    Duration? duration,
    String? errorMessage,
  }) {
    return VideoPlayerState(
      status: status ?? this.status,
      videoPath: videoPath ?? this.videoPath,
      position: position ?? this.position,
      duration: duration ?? this.duration,
      errorMessage: errorMessage ?? this.errorMessage,
    );
  }

  @override
  List<Object?> get props => [
    status,
    videoPath,
    position,
    duration,
    errorMessage,
  ];
}
```

---

## Step 5: Tạo BLoC file

```dart
// lib/features/history/bloc/video_player_bloc.dart

import 'dart:async';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'video_player_event.dart';
import 'video_player_state.dart';

class VideoPlayerBloc extends Bloc<VideoPlayerEvent, VideoPlayerState> {
  final VideoRepository _videoRepository;
  StreamSubscription<Duration>? _positionSubscription;

  VideoPlayerBloc({
    required VideoRepository videoRepository,
  })  : _videoRepository = videoRepository,
        super(const VideoPlayerState()) {
    // Register event handlers
    on<VideoLoaded>(_onVideoLoaded);
    on<PlayPauseToggled>(_onPlayPauseToggled);
    on<VideoSeeked>(_onVideoSeeked);
  }

  Future<void> _onVideoLoaded(
    VideoLoaded event,
    Emitter<VideoPlayerState> emit,
  ) async {
    emit(state.copyWith(status: VideoPlayerStatus.loading));

    try {
      final video = await _videoRepository.getById(event.videoId);
      emit(state.copyWith(
        status: VideoPlayerStatus.ready,
        videoPath: video.path,
        duration: video.duration,
      ));
    } catch (e) {
      emit(state.copyWith(
        status: VideoPlayerStatus.error,
        errorMessage: e.toString(),
      ));
    }
  }

  Future<void> _onPlayPauseToggled(
    PlayPauseToggled event,
    Emitter<VideoPlayerState> emit,
  ) async {
    if (state.isPlaying) {
      emit(state.copyWith(status: VideoPlayerStatus.paused));
    } else {
      emit(state.copyWith(status: VideoPlayerStatus.playing));
    }
  }

  Future<void> _onVideoSeeked(
    VideoSeeked event,
    Emitter<VideoPlayerState> emit,
  ) async {
    emit(state.copyWith(position: event.position));
  }

  @override
  Future<void> close() {
    _positionSubscription?.cancel();
    return super.close();
  }
}
```

---

## Step 6: Sử dụng trong Page

```dart
// Trong page file

class VideoPlayerPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => VideoPlayerBloc(
        videoRepository: context.read<VideoRepository>(),
      )..add(VideoLoaded(videoId)),
      child: const VideoPlayerView(),
    );
  }
}

class VideoPlayerView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocBuilder<VideoPlayerBloc, VideoPlayerState>(
      builder: (context, state) {
        if (state.isLoading) {
          return const LoadingIndicator();
        }
        // ... rest of UI
      },
    );
  }
}
```

---

## 📋 Checklist

| Step | Task |
|---|---|
| 1 | Xác định events và state fields |
| 2 | Tạo 3 files trong `bloc/` folder |
| 3 | Event: extends Equatable, có props |
| 4 | State: có status enum, copyWith, convenience getters |
| 5 | BLoC: register handlers, cleanup trong close() |
| 6 | Wrap page với BlocProvider |

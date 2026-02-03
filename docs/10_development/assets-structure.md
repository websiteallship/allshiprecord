# Assets Structure - Allship Record

Cấu trúc và quy tắc cho thư mục assets.

---

## 1. Folder Structure

```
assets/
├── fonts/                    # Custom fonts
│   ├── Rubik/
│   │   ├── Rubik-Regular.ttf
│   │   ├── Rubik-Medium.ttf
│   │   ├── Rubik-SemiBold.ttf
│   │   └── Rubik-Bold.ttf
│   ├── NunitoSans/
│   │   ├── NunitoSans-Regular.ttf
│   │   ├── NunitoSans-Medium.ttf
│   │   ├── NunitoSans-SemiBold.ttf
│   │   └── NunitoSans-Bold.ttf
│   └── RobotoMono/
│       ├── RobotoMono-Regular.ttf
│       └── RobotoMono-Medium.ttf
│
├── images/                   # Static images
│   ├── logo/
│   │   ├── logo.png
│   │   ├── logo_dark.png
│   │   └── logo_mono.png
│   ├── onboarding/
│   │   ├── onboarding_1.png
│   │   ├── onboarding_2.png
│   │   └── onboarding_3.png
│   ├── empty_states/
│   │   ├── no_videos.png
│   │   ├── no_results.png
│   │   └── error.png
│   └── icons/
│       └── app_icon.png
│
├── sounds/                   # Audio feedback
│   ├── scan_success.mp3
│   ├── scan_error.mp3
│   ├── recording_start.mp3
│   ├── recording_stop.mp3
│   ├── recording_warning.mp3
│   └── button_click.mp3
│
└── animations/               # Lottie animations (optional)
    ├── loading.json
    ├── success.json
    └── recording.json
```

---

## 2. Assets Declaration (pubspec.yaml)

```yaml
flutter:
  assets:
    # Images
    - assets/images/logo/
    - assets/images/onboarding/
    - assets/images/empty_states/
    - assets/images/icons/
    
    # Sounds
    - assets/sounds/
    
    # Animations (if using Lottie)
    - assets/animations/

  fonts:
    # Heading font
    - family: Rubik
      fonts:
        - asset: assets/fonts/Rubik/Rubik-Regular.ttf
        - asset: assets/fonts/Rubik/Rubik-Medium.ttf
          weight: 500
        - asset: assets/fonts/Rubik/Rubik-SemiBold.ttf
          weight: 600
        - asset: assets/fonts/Rubik/Rubik-Bold.ttf
          weight: 700
    
    # Body font
    - family: NunitoSans
      fonts:
        - asset: assets/fonts/NunitoSans/NunitoSans-Regular.ttf
        - asset: assets/fonts/NunitoSans/NunitoSans-Medium.ttf
          weight: 500
        - asset: assets/fonts/NunitoSans/NunitoSans-SemiBold.ttf
          weight: 600
        - asset: assets/fonts/NunitoSans/NunitoSans-Bold.ttf
          weight: 700
    
    # Monospace font
    - family: RobotoMono
      fonts:
        - asset: assets/fonts/RobotoMono/RobotoMono-Regular.ttf
        - asset: assets/fonts/RobotoMono/RobotoMono-Medium.ttf
          weight: 500
```

---

## 3. Asset Constants

```dart
// lib/core/constants/assets.dart

class Assets {
  Assets._();
  
  // ═══════════════════════════════════════════════════════════════
  // LOGOS
  // ═══════════════════════════════════════════════════════════════
  
  static const String logo = 'assets/images/logo/logo.png';
  static const String logoDark = 'assets/images/logo/logo_dark.png';
  static const String logoMono = 'assets/images/logo/logo_mono.png';
  
  // ═══════════════════════════════════════════════════════════════
  // ONBOARDING
  // ═══════════════════════════════════════════════════════════════
  
  static const String onboarding1 = 'assets/images/onboarding/onboarding_1.png';
  static const String onboarding2 = 'assets/images/onboarding/onboarding_2.png';
  static const String onboarding3 = 'assets/images/onboarding/onboarding_3.png';
  
  // ═══════════════════════════════════════════════════════════════
  // EMPTY STATES
  // ═══════════════════════════════════════════════════════════════
  
  static const String emptyVideos = 'assets/images/empty_states/no_videos.png';
  static const String emptyResults = 'assets/images/empty_states/no_results.png';
  static const String errorImage = 'assets/images/empty_states/error.png';
  
  // ═══════════════════════════════════════════════════════════════
  // SOUNDS
  // ═══════════════════════════════════════════════════════════════
  
  static const String soundScanSuccess = 'assets/sounds/scan_success.mp3';
  static const String soundScanError = 'assets/sounds/scan_error.mp3';
  static const String soundRecordStart = 'assets/sounds/recording_start.mp3';
  static const String soundRecordStop = 'assets/sounds/recording_stop.mp3';
  static const String soundRecordWarning = 'assets/sounds/recording_warning.mp3';
  static const String soundButtonClick = 'assets/sounds/button_click.mp3';
  
  // ═══════════════════════════════════════════════════════════════
  // ANIMATIONS (Lottie)
  // ═══════════════════════════════════════════════════════════════
  
  static const String animLoading = 'assets/animations/loading.json';
  static const String animSuccess = 'assets/animations/success.json';
  static const String animRecording = 'assets/animations/recording.json';
}
```

---

## 4. Image Specifications

### 4.1 Logo

| Asset | Size | Format | Notes |
|---|---|---|---|
| `logo.png` | 512x512 | PNG | With background |
| `logo_dark.png` | 512x512 | PNG | For dark mode |
| `logo_mono.png` | 512x512 | PNG | White/monochrome |

### 4.2 Onboarding

| Asset | Size | Format | Notes |
|---|---|---|---|
| `onboarding_*.png` | 400x400 | PNG | Transparent background |

### 4.3 Empty States

| Asset | Size | Format | Notes |
|---|---|---|---|
| `no_videos.png` | 300x300 | PNG | Transparent |
| `no_results.png` | 300x300 | PNG | Transparent |
| `error.png` | 300x300 | PNG | Transparent |

### 4.4 App Icon

| Platform | Size | Notes |
|---|---|---|
| Android | mdpi: 48x48, hdpi: 72x72, xhdpi: 96x96, xxhdpi: 144x144, xxxhdpi: 192x192 | Adaptive icon |
| iOS | 1024x1024 (App Store), 180x180 (@3x), 120x120 (@2x), 60x60 (@1x) | No transparency |

---

## 5. Sound Specifications

| Sound | Duration | Format | Use Case |
|---|---|---|---|
| `scan_success.mp3` | < 0.5s | MP3 | Barcode scanned OK |
| `scan_error.mp3` | < 0.5s | MP3 | Invalid barcode |
| `recording_start.mp3` | < 0.3s | MP3 | Recording started |
| `recording_stop.mp3` | < 0.3s | MP3 | Recording stopped |
| `recording_warning.mp3` | < 0.3s | MP3 | Near time limit |
| `button_click.mp3` | < 0.1s | MP3 | Button feedback |

### Sound Requirements

- **Format**: MP3 (smallest size, good compatibility)
- **Sample Rate**: 44.1 kHz
- **Bit Rate**: 128 kbps
- **Channels**: Mono
- **Max Duration**: 0.5 seconds

---

## 6. Font Specifications

### 6.1 Rubik (Headings)

- **Source**: [Google Fonts](https://fonts.google.com/specimen/Rubik)
- **Weights**: Regular (400), Medium (500), SemiBold (600), Bold (700)
- **Format**: TTF
- **License**: Open Font License

### 6.2 Nunito Sans (Body)

- **Source**: [Google Fonts](https://fonts.google.com/specimen/Nunito+Sans)
- **Weights**: Regular (400), Medium (500), SemiBold (600), Bold (700)
- **Format**: TTF
- **License**: Open Font License

### 6.3 Roboto Mono (Code/Timer)

- **Source**: [Google Fonts](https://fonts.google.com/specimen/Roboto+Mono)
- **Weights**: Regular (400), Medium (500)
- **Format**: TTF
- **License**: Apache 2.0

---

## 7. Naming Conventions

### 7.1 Files

| Type | Convention | Example |
|---|---|---|
| Images | `snake_case.png` | `empty_state.png` |
| Sounds | `snake_case.mp3` | `scan_success.mp3` |
| Animations | `snake_case.json` | `loading.json` |
| Fonts | `FontName-Weight.ttf` | `Rubik-Bold.ttf` |

### 7.2 Resolution Variants (Images)

```
images/
├── logo.png        # 1x (base)
├── 2.0x/
│   └── logo.png    # 2x
└── 3.0x/
    └── logo.png    # 3x
```

Flutter auto-selects based on device pixel ratio.

---

## 8. Usage Examples

### 8.1 Images

```dart
// Using constant
Image.asset(Assets.logo)

// With size
Image.asset(
  Assets.logo,
  width: 120,
  height: 120,
)

// In dark mode
Image.asset(
  Theme.of(context).brightness == Brightness.dark
    ? Assets.logoDark
    : Assets.logo,
)
```

### 8.2 Sounds

```dart
import 'package:audioplayers/audioplayers.dart';

class SoundService {
  final AudioPlayer _player = AudioPlayer();
  
  Future<void> playScanSuccess() async {
    await _player.play(AssetSource('sounds/scan_success.mp3'));
  }
  
  Future<void> playScanError() async {
    await _player.play(AssetSource('sounds/scan_error.mp3'));
  }
}
```

### 8.3 Fonts

```dart
// Already defined in ThemeData
Text(
  'Order Code',
  style: TextStyle(
    fontFamily: 'RobotoMono',
    fontSize: 18,
    fontWeight: FontWeight.w600,
  ),
)

// Using AppTextStyles
Text(
  'Order Code',
  style: AppTextStyles.orderCode,
)
```

---

## 9. Optimization Tips

### 9.1 Images

- ✅ Use WebP for better compression (if targeting Android 4.0+)
- ✅ Compress PNG with tools like TinyPNG
- ✅ Provide @2x and @3x variants for sharp display
- ✅ Use SVG (via flutter_svg) for icons if possible

### 9.2 Sounds

- ✅ Keep sounds short (< 0.5s)
- ✅ Use MP3 for smallest size
- ✅ Preload sounds for instant playback

### 9.3 Fonts

- ✅ Only include weights you actually use
- ✅ Use variable fonts if available (smaller size)
- ✅ Consider Google Fonts package for on-demand loading

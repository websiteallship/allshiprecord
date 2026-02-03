# UI/UX Design Guidelines - ALL SHIP ECOMBOX

## Design Principles

### 1. Hands-Free First

```yaml
NGUYÊN TẮC CORE:
  - Nhân viên đóng gói KHÔNG NHÌN màn hình khi làm việc
  - Audio feedback là kênh phản hồi CHÍNH
  - Touch targets phải LỚN (minimum 48x48dp)
  - Gestures phải ĐƠN GIẢN (tap, không swipe phức tạp)
```

### 2. One-Handed Operation

```
Thiết kế cho thao tác 1 tay:
  - Các nút quan trọng ở phần DƯỚI màn hình
  - Thumb zone: vùng dễ với ngón cái
  - Không cần kéo/scroll khi đang quay video
```

### 3. High Visibility

```yaml
TEXT:
  - Font size tối thiểu: 16sp
  - Order code: 24sp+ (phải nhìn rõ từ xa)
  - Contrast ratio: ≥ 4.5:1

COLORS:
  - Recording indicator: Đỏ sáng, nhấp nháy
  - Success: Xanh lá đậm
  - Error: Đỏ đậm
  - Warning: Vàng cam
```

## Color Palette

### Primary Colors

```css
/* Material Design 3 inspired */

/* Primary - Blue (Trust, Professional) */
--primary-50: #E3F2FD;
--primary-100: #BBDEFB;
--primary-500: #2196F3;
--primary-700: #1976D2;
--primary-900: #0D47A1;

/* Secondary - Teal (Success, Completion) */
--secondary-500: #009688;
--secondary-700: #00796B;

/* Error - Red */
--error-500: #F44336;
--error-700: #D32F2F;

/* Warning - Orange */
--warning-500: #FF9800;
--warning-700: #F57C00;

/* Surface */
--surface-light: #FFFFFF;
--surface-dark: #121212;
--on-surface-light: #1C1B1F;
--on-surface-dark: #E6E1E5;
```

### Dark Mode (Recommended Default)

```yaml
LÝ DO DÙNG DARK MODE:
  - Giảm mỏi mắt khi dùng lâu
  - Tiết kiệm pin (OLED)
  - Camera preview nổi bật hơn
  - Recording indicator dễ thấy
```

## Typography

### Font Family

```dart
// Google Fonts - Roboto (default cho Android Material)
// SF Pro (iOS system font)

// Fallback hierarchy
fontFamily: 'Roboto, SF Pro, system-ui, sans-serif';
```

### Type Scale

```dart
class AppTypography {
  // Display - Order code on camera overlay
  static const displayLarge = TextStyle(
    fontSize: 32,
    fontWeight: FontWeight.bold,
    letterSpacing: 0,
  );
  
  // Headline - Screen titles
  static const headlineMedium = TextStyle(
    fontSize: 24,
    fontWeight: FontWeight.w500,
  );
  
  // Title - Section headers
  static const titleLarge = TextStyle(
    fontSize: 20,
    fontWeight: FontWeight.w500,
  );
  
  // Body - Normal text
  static const bodyLarge = TextStyle(
    fontSize: 16,
    fontWeight: FontWeight.normal,
  );
  
  // Label - Buttons, chips
  static const labelLarge = TextStyle(
    fontSize: 14,
    fontWeight: FontWeight.w500,
    letterSpacing: 0.1,
  );
}
```

## Layout Structure

### Screen Zones

```
┌─────────────────────────────────┐
│         STATUS BAR              │ ← System status, scanner status
├─────────────────────────────────┤
│                                 │
│                                 │
│       CAMERA PREVIEW            │ ← 60-70% màn hình
│       (Main content)            │
│                                 │
│   ┌───────────────────────┐     │
│   │  ORDER CODE OVERLAY   │     │ ← Luôn hiện khi đang quay
│   │  SPX123456789         │     │
│   │  ● REC  00:35         │     │
│   └───────────────────────┘     │
│                                 │
├─────────────────────────────────┤
│                                 │
│     ACTION BUTTONS              │ ← Thumb zone, 30% màn hình
│     [Hoàn tất]  [Hủy]           │
│                                 │
└─────────────────────────────────┘
```

### Bottom Navigation

```dart
// 3-4 tabs maximum
BottomNavigationBar(
  items: [
    BottomNavigationBarItem(
      icon: Icon(Icons.video_camera_back),
      label: 'Đóng hàng',
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.assignment_return),
      label: 'Nhận hoàn',
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.search),
      label: 'Tra cứu',
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.settings),
      label: 'Cài đặt',
    ),
  ],
);
```

## Component Patterns

### Primary Button

```dart
ElevatedButton(
  style: ElevatedButton.styleFrom(
    minimumSize: Size(double.infinity, 56), // Full width, 56dp height
    backgroundColor: Theme.of(context).colorScheme.primary,
    foregroundColor: Theme.of(context).colorScheme.onPrimary,
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
  ),
  onPressed: () {},
  child: Text('Hoàn tất', style: TextStyle(fontSize: 18)),
);
```

### Recording Indicator

```dart
class RecordingIndicator extends StatefulWidget {
  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        // Blinking red dot
        AnimatedOpacity(
          opacity: _isVisible ? 1.0 : 0.3,
          duration: Duration(milliseconds: 500),
          child: Container(
            width: 12,
            height: 12,
            decoration: BoxDecoration(
              color: Colors.red,
              shape: BoxShape.circle,
            ),
          ),
        ),
        SizedBox(width: 8),
        Text('REC', style: TextStyle(
          color: Colors.red,
          fontWeight: FontWeight.bold,
        )),
        SizedBox(width: 8),
        Text(_formatDuration(duration)),
      ],
    );
  }
}
```

### Order Card

```dart
Card(
  child: Padding(
    padding: EdgeInsets.all(16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Order code - LARGE
        Text(
          'SPX123456789',
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            fontFamily: 'monospace', // Dễ đọc mã
          ),
        ),
        SizedBox(height: 8),
        // Thumbnail row
        Row(
          children: [
            _buildVideoThumbnail('Đóng gói', packingVideo),
            SizedBox(width: 12),
            _buildVideoThumbnail('Hoàn trả', returnVideo),
          ],
        ),
      ],
    ),
  ),
);
```

## Touch Targets

```dart
/// Minimum touch target: 48x48 dp
/// Recommended: 56x56 dp cho action chính

// GOOD
IconButton(
  iconSize: 24,
  padding: EdgeInsets.all(16), // Total: 56x56
  onPressed: () {},
  icon: Icon(Icons.close),
);

// BAD - quá nhỏ
IconButton(
  iconSize: 16,
  padding: EdgeInsets.all(4), // Total: 24x24 ❌
  onPressed: () {},
  icon: Icon(Icons.close),
);
```

## Accessibility

### Screen Reader Support

```dart
Semantics(
  label: 'Nút bắt đầu quay video',
  button: true,
  child: RecordButton(),
);
```

### Color Contrast

```yaml
WCAG AA Compliance:
  - Text nhỏ (< 18sp): contrast ratio ≥ 4.5:1
  - Text lớn (≥ 18sp): contrast ratio ≥ 3:1
  - UI components: contrast ratio ≥ 3:1
```

### Motion Sensitivity

```dart
// Respect reduced motion preference
final reduceMotion = MediaQuery.of(context).disableAnimations;

AnimatedContainer(
  duration: reduceMotion ? Duration.zero : Duration(milliseconds: 300),
  // ...
);
```

## Responsive Design

### Breakpoints

```dart
class Breakpoints {
  static const mobile = 600.0;    // < 600
  static const tablet = 840.0;    // 600 - 840
  static const desktop = 1200.0;  // > 840
}

// Usage
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth < Breakpoints.mobile) {
      return MobileLayout();
    } else if (constraints.maxWidth < Breakpoints.desktop) {
      return TabletLayout();
    } else {
      return DesktopLayout();
    }
  },
);
```

### Orientation

```dart
// Camera preview nên LUÔN landscape aspect ratio
// App có thể dùng portrait hoặc landscape

OrientationBuilder(
  builder: (context, orientation) {
    if (orientation == Orientation.landscape) {
      return LandscapeRecordingLayout();
    }
    return PortraitRecordingLayout();
  },
);
```

## Loading & Empty States

### Loading

```dart
// Skeleton loading cho lists
Shimmer.fromColors(
  baseColor: Colors.grey[300]!,
  highlightColor: Colors.grey[100]!,
  child: VideoCardSkeleton(),
);
```

### Empty State

```dart
EmptyState(
  icon: Icons.video_library_outlined,
  title: 'Chưa có video nào',
  subtitle: 'Quét mã vận đơn để bắt đầu quay video đóng gói',
  action: ElevatedButton(
    onPressed: () => navigateToRecording(),
    child: Text('Bắt đầu quay'),
  ),
);
```

## Animation Guidelines

```yaml
DURATION:
  - Micro-interactions: 100-200ms
  - Page transitions: 250-350ms
  - Complex animations: 300-500ms

CURVES:
  - Standard: Curves.easeInOut
  - Entering: Curves.easeOut
  - Exiting: Curves.easeIn
  - Emphasized: Curves.easeInOutCubicEmphasized

KHÔNG NÊN:
  - Animation quá lâu (> 500ms)
  - Animation block user interaction
  - Animation trong recording screen (distraction)
```

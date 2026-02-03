# Dark Mode

## Mô tả
Chế độ giao diện tối, giảm mỏi mắt khi làm việc trong môi trường thiếu sáng.

## Color Palette

### Light Theme
| Element | Color |
|---|---|
| Background | #FFFFFF |
| Surface | #F5F5F5 |
| Primary | #1976D2 |
| Text | #212121 |
| Text Secondary | #757575 |

### Dark Theme
| Element | Color |
|---|---|
| Background | #121212 |
| Surface | #1E1E1E |
| Primary | #90CAF9 |
| Text | #FFFFFF |
| Text Secondary | #B0B0B0 |

## Implementation

```dart
// theme.dart
class AppTheme {
  static ThemeData light = ThemeData(
    brightness: Brightness.light,
    primaryColor: Color(0xFF1976D2),
    // ...
  );
  
  static ThemeData dark = ThemeData(
    brightness: Brightness.dark,
    primaryColor: Color(0xFF90CAF9),
    scaffoldBackgroundColor: Color(0xFF121212),
    // ...
  );
}

// main.dart
MaterialApp(
  theme: AppTheme.light,
  darkTheme: AppTheme.dark,
  themeMode: ThemeMode.system, // Follow system setting
)
```

## User Control

```
Giao diện:
  ( ) Sáng
  ( ) Tối
  (●) Theo hệ thống
```

## Ưu tiên
**P2** - Phase 5.

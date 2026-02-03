# App Theme - Allship Record

Design System cho ứng dụng Allship Record, được tạo dựa trên UI/UX Pro Max guidelines.

---

## 1. Design Philosophy

### 1.1 Nguyên tắc thiết kế

| Nguyên tắc | Mô tả |
|---|---|
| **Professional** | Hình ảnh chuyên nghiệp, đáng tin cậy cho business |
| **Functional** | Ưu tiên chức năng, dễ sử dụng trong môi trường kho |
| **High Contrast** | Dễ đọc trong mọi điều kiện ánh sáng |
| **One-Handed** | Tối ưu cho thao tác một tay khi đóng hàng |

### 1.2 Style Direction

- **Style**: Professional + Dark Mode friendly
- **Mood**: E-commerce, warehouse, productivity, trust
- **Best For**: B2B service, logistics, warehouse operations

---

## 2. Color Palette

### 2.1 Core Colors

```dart
// lib/core/theme/app_colors.dart

class AppColors {
  // ═══════════════════════════════════════════════════════════════
  // PRIMARY PALETTE
  // ═══════════════════════════════════════════════════════════════
  
  /// Primary brand color - Navy blue
  static const Color primary = Color(0xFF0F172A);
  
  /// Secondary color - Slate
  static const Color secondary = Color(0xFF334155);
  
  /// CTA/Accent color - Professional blue
  static const Color accent = Color(0xFF0369A1);
  
  // ═══════════════════════════════════════════════════════════════
  // SEMANTIC COLORS
  // ═══════════════════════════════════════════════════════════════
  
  /// Success - Video saved, scan success
  static const Color success = Color(0xFF10B981);
  
  /// Warning - Low storage, approaching limit
  static const Color warning = Color(0xFFF59E0B);
  
  /// Error - Recording failed, permission denied
  static const Color error = Color(0xFFEF4444);
  
  /// Info - Hints, tips
  static const Color info = Color(0xFF3B82F6);
  
  // ═══════════════════════════════════════════════════════════════
  // RECORDING COLORS
  // ═══════════════════════════════════════════════════════════════
  
  /// Recording active indicator
  static const Color recording = Color(0xFFDC2626);
  
  /// Recording paused
  static const Color recordingPaused = Color(0xFF6B7280);
  
  // ═══════════════════════════════════════════════════════════════
  // ORDER TYPE COLORS
  // ═══════════════════════════════════════════════════════════════
  
  /// Packing order - Blue
  static const Color orderPacking = Color(0xFF3B82F6);
  
  /// Shipping order - Green
  static const Color orderShipping = Color(0xFF22C55E);
  
  /// Return order - Orange
  static const Color orderReturn = Color(0xFFF97316);
}
```

### 2.2 Light Theme Colors

```dart
class LightThemeColors {
  // Background
  static const Color background = Color(0xFFF8FAFC);
  static const Color surface = Color(0xFFFFFFFF);
  static const Color surfaceVariant = Color(0xFFF1F5F9);
  
  // Text
  static const Color textPrimary = Color(0xFF020617);
  static const Color textSecondary = Color(0xFF475569);
  static const Color textTertiary = Color(0xFF94A3B8);
  static const Color textOnPrimary = Color(0xFFFFFFFF);
  
  // Border & Divider
  static const Color border = Color(0xFFE2E8F0);
  static const Color divider = Color(0xFFE2E8F0);
  
  // Input
  static const Color inputBackground = Color(0xFFF8FAFC);
  static const Color inputBorder = Color(0xFFCBD5E1);
  static const Color inputFocusBorder = Color(0xFF0369A1);
  
  // Card
  static const Color cardBackground = Color(0xFFFFFFFF);
  static const Color cardShadow = Color(0x1A000000);
}
```

### 2.3 Dark Theme Colors

```dart
class DarkThemeColors {
  // Background
  static const Color background = Color(0xFF0F172A);
  static const Color surface = Color(0xFF1E293B);
  static const Color surfaceVariant = Color(0xFF334155);
  
  // Text
  static const Color textPrimary = Color(0xFFF8FAFC);
  static const Color textSecondary = Color(0xFFCBD5E1);
  static const Color textTertiary = Color(0xFF64748B);
  static const Color textOnPrimary = Color(0xFFFFFFFF);
  
  // Border & Divider
  static const Color border = Color(0xFF334155);
  static const Color divider = Color(0xFF334155);
  
  // Input
  static const Color inputBackground = Color(0xFF1E293B);
  static const Color inputBorder = Color(0xFF475569);
  static const Color inputFocusBorder = Color(0xFF0EA5E9);
  
  // Card
  static const Color cardBackground = Color(0xFF1E293B);
  static const Color cardShadow = Color(0x33000000);
}
```

### 2.4 Color Usage Guidelines

| Component | Light Mode | Dark Mode |
|---|---|---|
| App Bar | `primary` | `surface` |
| Background | `background` | `background` |
| Card | `cardBackground` | `cardBackground` |
| Primary Button | `accent` | `accent` |
| Text | `textPrimary` | `textPrimary` |
| Secondary Text | `textSecondary` | `textSecondary` |
| Border | `border` | `border` |
| Success Badge | `success` | `success` |
| Error Badge | `error` | `error` |

---

## 3. Typography

### 3.1 Font Families

```dart
// lib/core/theme/app_typography.dart

class AppTypography {
  /// Heading font - Rubik (Google Fonts)
  static const String headingFont = 'Rubik';
  
  /// Body font - Nunito Sans (Google Fonts)
  static const String bodyFont = 'NunitoSans';
  
  /// Monospace font - For order codes, timestamps
  static const String monoFont = 'RobotoMono';
}
```

### 3.2 Text Styles

```dart
class AppTextStyles {
  // ═══════════════════════════════════════════════════════════════
  // HEADINGS (Rubik)
  // ═══════════════════════════════════════════════════════════════
  
  /// H1 - Screen titles
  static const TextStyle h1 = TextStyle(
    fontFamily: 'Rubik',
    fontSize: 28,
    fontWeight: FontWeight.w700,
    height: 1.3,
    letterSpacing: -0.5,
  );
  
  /// H2 - Section titles
  static const TextStyle h2 = TextStyle(
    fontFamily: 'Rubik',
    fontSize: 24,
    fontWeight: FontWeight.w600,
    height: 1.35,
  );
  
  /// H3 - Card titles
  static const TextStyle h3 = TextStyle(
    fontFamily: 'Rubik',
    fontSize: 20,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  /// H4 - Subsection titles
  static const TextStyle h4 = TextStyle(
    fontFamily: 'Rubik',
    fontSize: 18,
    fontWeight: FontWeight.w600,
    height: 1.4,
  );
  
  // ═══════════════════════════════════════════════════════════════
  // BODY (Nunito Sans)
  // ═══════════════════════════════════════════════════════════════
  
  /// Body Large - Important information
  static const TextStyle bodyLarge = TextStyle(
    fontFamily: 'NunitoSans',
    fontSize: 16,
    fontWeight: FontWeight.w400,
    height: 1.6,
  );
  
  /// Body Medium - Default text (16px minimum for mobile)
  static const TextStyle bodyMedium = TextStyle(
    fontFamily: 'NunitoSans',
    fontSize: 16,
    fontWeight: FontWeight.w400,
    height: 1.5,
  );
  
  /// Body Small - Secondary information
  static const TextStyle bodySmall = TextStyle(
    fontFamily: 'NunitoSans',
    fontSize: 14,
    fontWeight: FontWeight.w400,
    height: 1.5,
  );
  
  // ═══════════════════════════════════════════════════════════════
  // LABELS & BUTTONS
  // ═══════════════════════════════════════════════════════════════
  
  /// Button text
  static const TextStyle button = TextStyle(
    fontFamily: 'NunitoSans',
    fontSize: 16,
    fontWeight: FontWeight.w600,
    height: 1.25,
    letterSpacing: 0.5,
  );
  
  /// Label
  static const TextStyle label = TextStyle(
    fontFamily: 'NunitoSans',
    fontSize: 12,
    fontWeight: FontWeight.w500,
    height: 1.4,
    letterSpacing: 0.5,
  );
  
  /// Caption
  static const TextStyle caption = TextStyle(
    fontFamily: 'NunitoSans',
    fontSize: 12,
    fontWeight: FontWeight.w400,
    height: 1.4,
  );
  
  // ═══════════════════════════════════════════════════════════════
  // SPECIAL (RobotoMono)
  // ═══════════════════════════════════════════════════════════════
  
  /// Order code display
  static const TextStyle orderCode = TextStyle(
    fontFamily: 'RobotoMono',
    fontSize: 18,
    fontWeight: FontWeight.w600,
    height: 1.4,
    letterSpacing: 1,
  );
  
  /// Timer display
  static const TextStyle timer = TextStyle(
    fontFamily: 'RobotoMono',
    fontSize: 24,
    fontWeight: FontWeight.w700,
    height: 1.2,
  );
  
  /// Timestamp on video overlay
  static const TextStyle overlay = TextStyle(
    fontFamily: 'RobotoMono',
    fontSize: 14,
    fontWeight: FontWeight.w500,
    height: 1.3,
  );
}
```

### 3.3 Typography Scale

| Style | Size | Weight | Line Height | Use Case |
|---|---|---|---|---|
| H1 | 28px | 700 | 1.3 | Screen titles |
| H2 | 24px | 600 | 1.35 | Section titles |
| H3 | 20px | 600 | 1.4 | Card titles |
| H4 | 18px | 600 | 1.4 | Subsections |
| Body Large | 16px | 400 | 1.6 | Important text |
| Body Medium | 16px | 400 | 1.5 | Default text |
| Body Small | 14px | 400 | 1.5 | Secondary info |
| Button | 16px | 600 | 1.25 | Button labels |
| Label | 12px | 500 | 1.4 | Form labels |
| Caption | 12px | 400 | 1.4 | Hints, timestamps |
| Order Code | 18px | 600 | 1.4 | Mã vận đơn |
| Timer | 24px | 700 | 1.2 | Recording timer |

---

## 4. Spacing & Sizing

### 4.1 Spacing Scale

```dart
class AppSpacing {
  /// 4px - Minimal spacing
  static const double xs = 4;
  
  /// 8px - Tight spacing
  static const double sm = 8;
  
  /// 12px - Compact spacing
  static const double md = 12;
  
  /// 16px - Default spacing
  static const double lg = 16;
  
  /// 24px - Comfortable spacing
  static const double xl = 24;
  
  /// 32px - Section spacing
  static const double xxl = 32;
  
  /// 48px - Large section spacing
  static const double xxxl = 48;
  
  // Screen padding
  static const double screenPadding = 16;
  
  // Card padding
  static const double cardPadding = 16;
  
  // Bottom navigation height
  static const double bottomNavHeight = 80;
}
```

### 4.2 Sizing

```dart
class AppSizing {
  // ═══════════════════════════════════════════════════════════════
  // TOUCH TARGETS (Minimum 44x44 for accessibility)
  // ═══════════════════════════════════════════════════════════════
  
  /// Minimum touch target size
  static const double touchTarget = 48;
  
  /// Button height
  static const double buttonHeight = 48;
  
  /// Large button height
  static const double buttonHeightLarge = 56;
  
  /// Icon button size
  static const double iconButton = 48;
  
  // ═══════════════════════════════════════════════════════════════
  // ICONS
  // ═══════════════════════════════════════════════════════════════
  
  /// Small icon
  static const double iconSm = 16;
  
  /// Default icon
  static const double iconMd = 24;
  
  /// Large icon
  static const double iconLg = 32;
  
  /// Extra large icon
  static const double iconXl = 48;
  
  // ═══════════════════════════════════════════════════════════════
  // BORDERS
  // ═══════════════════════════════════════════════════════════════
  
  /// Default border radius
  static const double radiusSm = 4;
  static const double radiusMd = 8;
  static const double radiusLg = 12;
  static const double radiusXl = 16;
  static const double radiusFull = 999;
  
  /// Border width
  static const double borderWidth = 1;
  static const double borderWidthMedium = 2;
  
  // ═══════════════════════════════════════════════════════════════
  // COMPONENTS
  // ═══════════════════════════════════════════════════════════════
  
  /// App bar height
  static const double appBarHeight = 56;
  
  /// Bottom nav height
  static const double bottomNavHeight = 80;
  
  /// Card minimum height
  static const double cardMinHeight = 72;
  
  /// Thumbnail size (list)
  static const double thumbnailSm = 56;
  static const double thumbnailMd = 80;
  static const double thumbnailLg = 120;
  
  /// Avatar size
  static const double avatarSm = 32;
  static const double avatarMd = 48;
  static const double avatarLg = 64;
}
```

---

## 5. Shadows & Elevation

```dart
class AppShadows {
  /// Elevation 1 - Cards, buttons
  static BoxShadow elevation1(Color shadowColor) => BoxShadow(
    color: shadowColor,
    offset: Offset(0, 1),
    blurRadius: 3,
    spreadRadius: 0,
  );
  
  /// Elevation 2 - Floating elements
  static BoxShadow elevation2(Color shadowColor) => BoxShadow(
    color: shadowColor,
    offset: Offset(0, 4),
    blurRadius: 6,
    spreadRadius: -1,
  );
  
  /// Elevation 3 - Modals, dialogs
  static BoxShadow elevation3(Color shadowColor) => BoxShadow(
    color: shadowColor,
    offset: Offset(0, 10),
    blurRadius: 15,
    spreadRadius: -3,
  );
  
  /// Elevation 4 - Popovers, dropdowns
  static BoxShadow elevation4(Color shadowColor) => BoxShadow(
    color: shadowColor,
    offset: Offset(0, 20),
    blurRadius: 25,
    spreadRadius: -5,
  );
}
```

---

## 6. Animation

```dart
class AppAnimation {
  // ═══════════════════════════════════════════════════════════════
  // DURATIONS (150-300ms for micro-interactions)
  // ═══════════════════════════════════════════════════════════════
  
  /// Fast - Button press, hover
  static const Duration fast = Duration(milliseconds: 150);
  
  /// Normal - Card interactions
  static const Duration normal = Duration(milliseconds: 200);
  
  /// Slow - Page transitions
  static const Duration slow = Duration(milliseconds: 300);
  
  /// Very slow - Complex animations
  static const Duration verySlow = Duration(milliseconds: 500);
  
  // ═══════════════════════════════════════════════════════════════
  // CURVES
  // ═══════════════════════════════════════════════════════════════
  
  /// Default curve
  static const Curve defaultCurve = Curves.easeInOut;
  
  /// Enter curve
  static const Curve enterCurve = Curves.easeOut;
  
  /// Exit curve
  static const Curve exitCurve = Curves.easeIn;
  
  /// Bounce curve
  static const Curve bounceCurve = Curves.elasticOut;
}
```

---

## 7. Theme Data

```dart
// lib/core/theme/app_theme.dart

import 'package:flutter/material.dart';
import 'app_colors.dart';
import 'app_typography.dart';
import 'app_sizing.dart';

class AppTheme {
  static ThemeData get lightTheme => ThemeData(
    useMaterial3: true,
    brightness: Brightness.light,
    
    // Colors
    colorScheme: ColorScheme.light(
      primary: AppColors.primary,
      secondary: AppColors.secondary,
      tertiary: AppColors.accent,
      surface: LightThemeColors.surface,
      background: LightThemeColors.background,
      error: AppColors.error,
      onPrimary: LightThemeColors.textOnPrimary,
      onSecondary: LightThemeColors.textOnPrimary,
      onSurface: LightThemeColors.textPrimary,
      onBackground: LightThemeColors.textPrimary,
      onError: LightThemeColors.textOnPrimary,
    ),
    
    // Typography
    fontFamily: AppTypography.bodyFont,
    textTheme: TextTheme(
      headlineLarge: AppTextStyles.h1.copyWith(color: LightThemeColors.textPrimary),
      headlineMedium: AppTextStyles.h2.copyWith(color: LightThemeColors.textPrimary),
      headlineSmall: AppTextStyles.h3.copyWith(color: LightThemeColors.textPrimary),
      titleLarge: AppTextStyles.h4.copyWith(color: LightThemeColors.textPrimary),
      bodyLarge: AppTextStyles.bodyLarge.copyWith(color: LightThemeColors.textPrimary),
      bodyMedium: AppTextStyles.bodyMedium.copyWith(color: LightThemeColors.textPrimary),
      bodySmall: AppTextStyles.bodySmall.copyWith(color: LightThemeColors.textSecondary),
      labelLarge: AppTextStyles.button.copyWith(color: LightThemeColors.textPrimary),
      labelMedium: AppTextStyles.label.copyWith(color: LightThemeColors.textSecondary),
      labelSmall: AppTextStyles.caption.copyWith(color: LightThemeColors.textTertiary),
    ),
    
    // App Bar
    appBarTheme: AppBarTheme(
      backgroundColor: AppColors.primary,
      foregroundColor: LightThemeColors.textOnPrimary,
      elevation: 0,
      centerTitle: true,
      titleTextStyle: AppTextStyles.h4.copyWith(color: LightThemeColors.textOnPrimary),
    ),
    
    // Buttons
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.accent,
        foregroundColor: Colors.white,
        minimumSize: Size(double.infinity, AppSizing.buttonHeight),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppSizing.radiusMd),
        ),
        textStyle: AppTextStyles.button,
      ),
    ),
    
    // Cards
    cardTheme: CardTheme(
      color: LightThemeColors.cardBackground,
      elevation: 1,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppSizing.radiusLg),
      ),
    ),
    
    // Input
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: LightThemeColors.inputBackground,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppSizing.radiusMd),
        borderSide: BorderSide(color: LightThemeColors.inputBorder),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppSizing.radiusMd),
        borderSide: BorderSide(color: LightThemeColors.inputFocusBorder, width: 2),
      ),
      contentPadding: EdgeInsets.symmetric(horizontal: 16, vertical: 14),
    ),
    
    // Divider
    dividerTheme: DividerThemeData(
      color: LightThemeColors.divider,
      thickness: 1,
    ),
    
    // Bottom Navigation
    bottomNavigationBarTheme: BottomNavigationBarThemeData(
      backgroundColor: LightThemeColors.surface,
      selectedItemColor: AppColors.accent,
      unselectedItemColor: LightThemeColors.textTertiary,
      type: BottomNavigationBarType.fixed,
      elevation: 8,
    ),
  );
  
  static ThemeData get darkTheme => ThemeData(
    useMaterial3: true,
    brightness: Brightness.dark,
    
    // Colors
    colorScheme: ColorScheme.dark(
      primary: AppColors.accent,
      secondary: AppColors.secondary,
      tertiary: AppColors.accent,
      surface: DarkThemeColors.surface,
      background: DarkThemeColors.background,
      error: AppColors.error,
      onPrimary: DarkThemeColors.textOnPrimary,
      onSecondary: DarkThemeColors.textOnPrimary,
      onSurface: DarkThemeColors.textPrimary,
      onBackground: DarkThemeColors.textPrimary,
      onError: DarkThemeColors.textOnPrimary,
    ),
    
    // Typography
    fontFamily: AppTypography.bodyFont,
    textTheme: TextTheme(
      headlineLarge: AppTextStyles.h1.copyWith(color: DarkThemeColors.textPrimary),
      headlineMedium: AppTextStyles.h2.copyWith(color: DarkThemeColors.textPrimary),
      headlineSmall: AppTextStyles.h3.copyWith(color: DarkThemeColors.textPrimary),
      titleLarge: AppTextStyles.h4.copyWith(color: DarkThemeColors.textPrimary),
      bodyLarge: AppTextStyles.bodyLarge.copyWith(color: DarkThemeColors.textPrimary),
      bodyMedium: AppTextStyles.bodyMedium.copyWith(color: DarkThemeColors.textPrimary),
      bodySmall: AppTextStyles.bodySmall.copyWith(color: DarkThemeColors.textSecondary),
      labelLarge: AppTextStyles.button.copyWith(color: DarkThemeColors.textPrimary),
      labelMedium: AppTextStyles.label.copyWith(color: DarkThemeColors.textSecondary),
      labelSmall: AppTextStyles.caption.copyWith(color: DarkThemeColors.textTertiary),
    ),
    
    // App Bar
    appBarTheme: AppBarTheme(
      backgroundColor: DarkThemeColors.surface,
      foregroundColor: DarkThemeColors.textPrimary,
      elevation: 0,
      centerTitle: true,
      titleTextStyle: AppTextStyles.h4.copyWith(color: DarkThemeColors.textPrimary),
    ),
    
    // Buttons
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.accent,
        foregroundColor: Colors.white,
        minimumSize: Size(double.infinity, AppSizing.buttonHeight),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppSizing.radiusMd),
        ),
        textStyle: AppTextStyles.button,
      ),
    ),
    
    // Cards
    cardTheme: CardTheme(
      color: DarkThemeColors.cardBackground,
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppSizing.radiusLg),
        side: BorderSide(color: DarkThemeColors.border),
      ),
    ),
    
    // Input
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: DarkThemeColors.inputBackground,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppSizing.radiusMd),
        borderSide: BorderSide(color: DarkThemeColors.inputBorder),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppSizing.radiusMd),
        borderSide: BorderSide(color: DarkThemeColors.inputFocusBorder, width: 2),
      ),
      contentPadding: EdgeInsets.symmetric(horizontal: 16, vertical: 14),
    ),
    
    // Divider
    dividerTheme: DividerThemeData(
      color: DarkThemeColors.divider,
      thickness: 1,
    ),
    
    // Bottom Navigation
    bottomNavigationBarTheme: BottomNavigationBarThemeData(
      backgroundColor: DarkThemeColors.surface,
      selectedItemColor: AppColors.accent,
      unselectedItemColor: DarkThemeColors.textTertiary,
      type: BottomNavigationBarType.fixed,
      elevation: 0,
    ),
  );
}
```

---

## 8. Accessibility Guidelines

### 8.1 Color Contrast

| Element | Minimum Ratio | Target Ratio |
|---|---|---|
| Body Text | 4.5:1 | 7:1 |
| Large Text (>18px) | 3:1 | 4.5:1 |
| Icons | 3:1 | 4.5:1 |
| Focus Ring | 3:1 | 4.5:1 |

### 8.2 Touch Targets

- **Minimum size**: 48x48px
- **Spacing between targets**: 8px minimum
- **Edge spacing**: 16px from screen edge

### 8.3 Motion

```dart
// Check user preference
final reduceMotion = MediaQuery.of(context).disableAnimations;

// Use appropriately
AnimatedContainer(
  duration: reduceMotion ? Duration.zero : AppAnimation.normal,
  // ...
);
```

---

## 9. Pre-Delivery Checklist

Trước khi ship UI, verify:

### Visual Quality
- [ ] No emojis used as icons (use Iconsax)
- [ ] All icons consistent size (24x24)
- [ ] Hover states don't cause layout shift
- [ ] Use theme colors, not hardcoded values

### Interaction
- [ ] All clickable elements have InkWell/GestureDetector
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard/TV navigation

### Light/Dark Mode
- [ ] Text contrast 4.5:1 minimum
- [ ] Tested in both modes
- [ ] Borders visible in both modes

### Accessibility
- [ ] Touch targets >= 48px
- [ ] Form inputs have labels
- [ ] `prefers-reduced-motion` respected
- [ ] Screen reader semantics (Semantics widget)

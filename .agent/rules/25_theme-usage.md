# Theme Usage Rules

Quy tắc sử dụng Theme, Colors, Typography trong dự án Allship Record.

---

## ⚠️ BẮT BUỘC

### 1. Sử dụng Theme Colors

```dart
// ✅ ĐÚNG - Sử dụng AppColors hoặc Theme
Container(
  color: AppColors.primary,
)
Container(
  color: Theme.of(context).colorScheme.primary,
)

// ❌ SAI - Hardcode màu
Container(
  color: Color(0xFF0F172A),  // KHÔNG hardcode!
)
Container(
  color: Colors.blue,  // KHÔNG dùng Colors trực tiếp!
)
```

### 2. Sử dụng Typography

```dart
// ✅ ĐÚNG - Sử dụng AppTextStyles hoặc Theme
Text(
  'Title',
  style: AppTextStyles.h1,
)
Text(
  'Body',
  style: Theme.of(context).textTheme.bodyMedium,
)

// ❌ SAI - Tự định nghĩa style
Text(
  'Title',
  style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),  // KHÔNG!
)
```

### 3. Sử dụng Spacing

```dart
// ✅ ĐÚNG - Sử dụng AppSpacing
Padding(
  padding: EdgeInsets.all(AppSpacing.lg),  // 16px
)
SizedBox(height: AppSpacing.md),  // 12px

// ❌ SAI - Hardcode số
Padding(
  padding: EdgeInsets.all(16),  // KHÔNG hardcode!
)
```

### 4. Sử dụng Sizing

```dart
// ✅ ĐÚNG - Sử dụng AppSizing
Icon(
  Iconsax.home,
  size: AppSizing.iconMd,  // 24px
)
Container(
  height: AppSizing.buttonHeight,  // 48px
)

// ❌ SAI - Magic numbers
Icon(
  Iconsax.home,
  size: 24,  // Không rõ ràng
)
```

---

## 📁 Tham chiếu

| Cần gì? | Import từ đâu? |
|---|---|
| Colors | `package:allship_record/core/theme/app_colors.dart` |
| Typography | `package:allship_record/core/theme/app_typography.dart` |
| Spacing | `package:allship_record/core/theme/app_spacing.dart` |
| Sizing | `package:allship_record/core/theme/app_sizing.dart` |
| Full theme | `package:allship_record/core/theme/app_theme.dart` |

---

## 📋 Checklist trước khi commit

- [ ] Không có hardcoded colors (0xFF..., Colors.*)
- [ ] Không có hardcoded font sizes
- [ ] Không có magic numbers cho padding/margin
- [ ] Sử dụng semantic colors (success, error, warning)
- [ ] Test cả Light mode và Dark mode

---

## 🔗 Tài liệu liên quan

- `docs/07_ui-ux/app-theme.md` - Định nghĩa đầy đủ
- `docs/07_ui-ux/ui-components.md` - Reusable components

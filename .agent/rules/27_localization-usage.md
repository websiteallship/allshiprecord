# Localization Usage Rules

Quy tắc sử dụng Localization (l10n) trong dự án Allship Record.

---

## ⚠️ BẮT BUỘC

### 1. KHÔNG hardcode strings

```dart
// ✅ ĐÚNG - Sử dụng l10n
Text(S.of(context).appName)
Text(S.of(context).btnSave)

// ❌ SAI - Hardcode string
Text('Allship Record')  // KHÔNG!
Text('Lưu')  // KHÔNG!
```

### 2. Sử dụng placeholders cho dynamic values

```dart
// ✅ ĐÚNG - Placeholder trong ARB
// intl_vi.arb:
// "cameraOrderCode": "Mã đơn: {code}"

Text(S.of(context).cameraOrderCode(orderCode))

// ❌ SAI - String interpolation
Text('Mã đơn: $orderCode')  // KHÔNG!
```

### 3. Error messages cũng phải l10n

```dart
// ✅ ĐÚNG
showSnackBar(S.of(context).errorSaveFailed)

// ❌ SAI
showSnackBar('Không thể lưu video')  // KHÔNG!
```

---

## 📁 Cấu trúc file

```
lib/l10n/
├── intl_vi.arb     # Vietnamese (default)
└── intl_en.arb     # English (optional)
```

---

## 📝 ARB Naming Convention

| Prefix | Dùng cho | Ví dụ |
|---|---|---|
| `btn*` | Button labels | `btnSave`, `btnCancel` |
| `tab*` | Tab labels | `tabRecord`, `tabHistory` |
| `error*` | Error messages | `errorSaveFailed` |
| `{screen}*` | Screen-specific | `cameraStartRecording` |
| `settings*` | Settings items | `settingsTheme` |

### Ví dụ ARB entry

```json
{
  "cameraOrderCode": "Mã đơn: {code}",
  "@cameraOrderCode": {
    "placeholders": {
      "code": {"type": "String"}
    }
  }
}
```

---

## 🔧 Quy trình thêm string mới

### Step 1: Thêm vào ARB
```json
// lib/l10n/intl_vi.arb
{
  "newFeatureTitle": "Tiêu đề mới"
}
```

### Step 2: Generate
```bash
flutter gen-l10n
```

### Step 3: Sử dụng
```dart
Text(S.of(context).newFeatureTitle)
```

---

## 📋 Checklist

- [ ] Không có hardcoded string trong UI
- [ ] Error messages sử dụng l10n
- [ ] Dynamic values dùng placeholders
- [ ] Key names theo convention (screen prefix)
- [ ] Đã chạy `flutter gen-l10n` sau khi thêm string

---

## 🚫 Exceptions (có thể hardcode)

| Loại | Ví dụ | Lý do |
|---|---|---|
| Log messages | `print('Debug: ...')` | Chỉ cho dev |
| Technical strings | `'video/mp4'` | MIME types, formats |
| Package names | `'allship_record'` | Technical identifiers |

---

## 🔗 Tài liệu liên quan

- `docs/07_ui-ux/localization-strings.md` - Tất cả strings (~151)
- `.agent/rules/12_localization-language.md` - Localization guidelines

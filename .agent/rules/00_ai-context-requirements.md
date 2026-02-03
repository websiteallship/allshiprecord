---
description: Quy tắc bắt buộc AI phải đọc context trước khi phát triển tính năng
globs: ["**/*"]
alwaysApply: true
---

# AI Context Reading Requirements

## ⚠️ QUAN TRỌNG - BẮT BUỘC THỰC HIỆN

Trước khi phát triển **BẤT KỲ** tính năng nào, AI agent **PHẢI** đọc qua các tài liệu sau để hiểu đầy đủ context của dự án.

---

## 1. Thứ tự đọc bắt buộc

### Bước 1: Đọc AI Context (`.ai/`)
```
.ai/
├── project_brief.md      ⬅️ Đọc TRƯỚC TIÊN - Hiểu dự án làm gì
├── active_state.md       ⬅️ Biết đang ở phase nào
├── feature_backlog.md    ⬅️ Xem feature này đã có chưa, ID là gì
├── coding_patterns.md    ⬅️ Patterns cần tuân theo
└── work_log.md           ⬅️ Bối cảnh gần đây
```

### Bước 2: Đọc Docs liên quan
```
docs/
├── 01_overview/          ⬅️ Nếu cần context business
├── 02_architecture/      ⬅️ Nếu liên quan kiến trúc
├── 03_features/          ⬅️ LUÔN đọc spec của feature cần dev
├── 07_ui-ux/             ⬅️ Nếu liên quan UI
└── 08_error-handling/    ⬅️ Nếu cần xử lý lỗi
```

### Bước 3: Đọc Rules liên quan
```
.agent/rules/
├── 02_coding-conventions.md    ⬅️ Quy tắc code
├── 10_ui-ux-design.md          ⬅️ Quy tắc UI
└── [rule liên quan feature]    ⬅️ Rule cụ thể nếu có
```

---

## 2. Checklist trước khi code

AI agent PHẢI xác nhận đã đọc:

- [ ] `.ai/project_brief.md` - Hiểu mục tiêu dự án
- [ ] `.ai/feature_backlog.md` - Xác định Feature ID
- [ ] `docs/03_features/[feature].md` - Đọc spec chi tiết
- [ ] `docs/07_ui-ux/ui-components.md` - Biết components có sẵn
- [ ] `.agent/rules/` - Đọc rules liên quan

---

## 3. Quy tắc cụ thể

### 3.1 Sử dụng Components có sẵn
- **PHẢI** kiểm tra `docs/07_ui-ux/ui-components.md` trước khi tạo widget mới.
- Nếu component đã có → SỬ DỤNG, không tạo mới.
- Nếu cần component mới → Thêm vào docs trước, rồi implement.

### 3.2 Tuân theo Feature Spec
- Nếu `docs/03_features/[feature].md` tồn tại → **PHẢI** tuân theo spec.
- Nếu chưa có spec → Tạo spec trước, xin approval, rồi mới code.

### 3.3 Cập nhật sau khi hoàn thành
- Đánh dấu feature là "Done" trong `.ai/feature_backlog.md`.
- Ghi log vào `.ai/work_log.md`.
- Cập nhật `CHANGELOG.md` nếu là thay đổi đáng kể.

---

## 4. Ví dụ workflow

```
User: "Thêm tính năng Voice Commands"

AI phải:
1. Đọc .ai/project_brief.md → Hiểu đây là app quay video đóng hàng
2. Đọc .ai/feature_backlog.md → Feature F022, Phase 2
3. Đọc docs/03_features/voice-commands.md → Có spec chi tiết
4. Đọc docs/07_ui-ux/ui-components.md → Biết components có sẵn
5. Đọc .agent/rules/02_coding-conventions.md → Code style
6. BẮT ĐẦU CODE theo spec
7. Cập nhật backlog, work_log sau khi xong
```

---

## 5. Cảnh báo

### ❌ KHÔNG ĐƯỢC
- Bắt đầu code mà chưa đọc context.
- Tạo component mới khi đã có sẵn.
- Tự ý thay đổi spec mà không hỏi user.
- Bỏ qua error handling rules.

### ✅ PHẢI
- Luôn bắt đầu bằng việc đọc `.ai/project_brief.md`.
- Tham chiếu Feature ID khi làm việc.
- Sử dụng Iconsax icons (không dùng emoji trong code).
- Tuân theo coding conventions.

---

## 6. Tham chiếu nhanh

| Cần biết gì? | Đọc file nào? |
|---|---|
| Dự án làm gì | `.ai/project_brief.md` |
| Đang ở phase nào | `.ai/active_state.md` |
| Feature list | `.ai/feature_backlog.md` |
| Feature spec | `docs/03_features/[name].md` |
| UI components | `docs/07_ui-ux/ui-components.md` |
| Screen layouts | `docs/07_ui-ux/screen-layouts.md` |
| Code style | `.agent/rules/02_coding-conventions.md` |
| Database schema | `docs/02_architecture/database-schema.md` |
| Error codes | `docs/08_error-handling/error-codes.md` |

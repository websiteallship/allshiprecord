---
description: Quy tắc quản lý tính năng và cập nhật AI context
globs: ["**/*"]
---

# Feature & AI Context Management Rules

Quy tắc này định nghĩa cách AI agent quản lý tính năng mới và cập nhật context trong suốt vòng đời dự án.

---

## 1. Khi có TÍNH NĂNG MỚI được đề xuất

### Bước 1: Ghi nhận vào Backlog
Thêm feature mới vào `.ai/feature_backlog.md`:
- Tạo ID mới (F001, F002...).
- Mô tả ngắn gọn.
- Đặt mức ưu tiên (P0/P1/P2).

### Bước 2: Tạo tài liệu chi tiết (nếu cần)
Nếu feature phức tạp, tạo file mới: `docs/03_features/{tên-feature}.md`
- Mô tả use case.
- Flow diagram (Mermaid).
- Yêu cầu kỹ thuật.

### Bước 3: Cập nhật UI (nếu cần)
Nếu feature có giao diện, cập nhật: `docs/07_ui-ux/screen-layouts.md`
- Thêm wireframe ASCII cho màn hình mới.

---

## 2. Khi BẮT ĐẦU phát triển tính năng

### Files cần cập nhật:
1. **`.ai/feature_backlog.md`**: Di chuyển feature từ Backlog → In Progress.
2. **`.ai/active_state.md`**: Thêm task vào Active Tasks.
3. **`CHANGELOG.md`**: Thêm dòng vào `[Unreleased]` → `Added`.

---

## 3. Khi HOÀN THÀNH tính năng

### Files cần cập nhật:
1. **`.ai/feature_backlog.md`**: Di chuyển từ In Progress → Done.
2. **`.ai/active_state.md`**: Đánh dấu `[x]` task đã hoàn thành.
3. **`.ai/work_log.md`**: Ghi lại session summary.
4. **`CHANGELOG.md`**: Đảm bảo đã có entry trong `[Unreleased]`.

---

## 4. Sơ đồ Lưu trữ Tính năng

```
Tính năng mới
    │
    ├──► .ai/feature_backlog.md     (Tracking ID, Priority, Status)
    │
    ├──► docs/03_features/*.md      (Chi tiết kỹ thuật, Use cases)
    │
    ├──► docs/07_ui-ux/screen-layouts.md  (Wireframes UI)
    │
    ├──► .ai/active_state.md        (Task đang làm)
    │
    └──► CHANGELOG.md               (Lịch sử thay đổi)
```

---

## 5. AI Agent PHẢI tự động làm

Mỗi khi kết thúc một phiên làm việc liên quan đến feature:

1. **Check Backlog**: Feature đã được ghi nhận chưa? Nếu chưa → Thêm vào.
2. **Check Active State**: Task hiện tại đã được mark đúng chưa?
3. **Check Changelog**: Thay đổi đã được log chưa?
4. **Check Work Log**: Đã ghi nhật ký phiên làm việc chưa?

> ⚠️ **QUAN TRỌNG**: Nếu thiếu bất kỳ bước nào, AI phải tự động bổ sung TRƯỚC KHI kết thúc phiên.

---

## 6. Workflow liên quan

- `/04_add-feature` - Quy trình thêm tính năng mới
- `/08_update-ai-context` - Cập nhật AI context sau mỗi task

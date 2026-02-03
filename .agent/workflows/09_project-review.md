---
description: Review toàn bộ dự án và xác định trạng thái hiện tại
---

# Review Dự Án (Project Health Check)

Workflow này giúp AI agent (hoặc developer mới) nhanh chóng hiểu được trạng thái dự án và biết cần làm gì tiếp theo.

## Bước 1: Đọc AI Context Files

Đọc các file trong thứ tự sau:

```
1. .ai/project_brief.md     → Hiểu dự án làm gì
2. .ai/active_state.md      → Biết đang ở phase nào
3. .ai/feature_backlog.md   → Xem danh sách features
4. .ai/work_log.md          → Xem lịch sử làm việc gần đây
5. CHANGELOG.md             → Xem những gì đã hoàn thành
```

## Bước 2: Kiểm tra Source Code

### 2a. Có source code Flutter chưa?
```bash
# Kiểm tra thư mục lib/
ls lib/
```

**Nếu KHÔNG có `lib/`**: Dự án chưa được init code → Chạy `/01_init-flutter`.

**Nếu CÓ `lib/`**: Tiếp tục bước 2b.

### 2b. Đếm features đã implement
```bash
# Đếm số file trong features/
ls -la lib/features/
```

So sánh với `.ai/feature_backlog.md` để biết:
- Số features đã Done.
- Số features đang In Progress.
- Số features còn Backlog.

## Bước 3: Chạy Tests (nếu có code)

```bash
flutter test
```

Ghi nhận:
- Số tests pass/fail.
- Coverage %.

## Bước 4: Tạo Báo cáo Trạng thái

Tạo/cập nhật file `.ai/project_status_report.md`:

```markdown
# Báo cáo Trạng thái Dự án

**Ngày review:** YYYY-MM-DD HH:mm
**Reviewer:** AI Agent / [Tên người]

## 1. Tổng quan

| Metric | Giá trị |
|---|---|
| Phase hiện tại | [Phase 1/2/3/4] |
| Features đã hoàn thành | X / Y |
| Features đang làm | Z |
| Test coverage | XX% |
| Lỗi chưa fix | N |

## 2. Đang ở đâu?

[Mô tả ngắn gọn trạng thái hiện tại]

## 3. Cần làm gì?

| Ưu tiên | Task | Lý do |
|---|---|---|
| P0 | [Task 1] | [Giải thích] |
| P0 | [Task 2] | [Giải thích] |
| P1 | [Task 3] | [Giải thích] |

## 4. Blockers / Rủi ro

- [Liệt kê các vấn đề đang block progress]

## 5. Đề xuất hành động tiếp theo

1. [Action 1]
2. [Action 2]
```

## Bước 5: Cập nhật Active State

Dựa trên kết quả review, cập nhật `.ai/active_state.md`:
- Current Phase.
- Active Tasks.
- Known Issues.

## Bước 6: Thông báo cho User

Tóm tắt kết quả cho user biết:
- Dự án đang ở đâu.
- Việc tiếp theo nên làm.
- Có blocker gì không.

---

## Mẫu Output

```
📊 PROJECT STATUS REPORT
========================

📍 ĐANG Ở ĐÂU:
   Phase 1 (MVP) - Chưa có source code

📋 CẦN LÀM GÌ:
   1. [P0] Init Flutter project → Chưa có thư mục lib/
   2. [P0] Implement Camera Preview → Core feature MVP
   3. [P0] Implement Barcode Scan → Core feature MVP

⚠️ BLOCKERS:
   - Không có

💡 ĐỀ XUẤT:
   Chạy /01_init-flutter để khởi tạo project structure.
```

---

## Khi nào chạy workflow này?

- ✅ Khi bắt đầu session mới sau thời gian dài.
- ✅ Khi có người mới join dự án.
- ✅ Khi cảm thấy "lạc" không biết làm gì tiếp.
- ✅ Trước mỗi sprint planning.
- ✅ Khi user hỏi "dự án đang ở đâu?".

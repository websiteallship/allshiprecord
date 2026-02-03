# AI Coding Patterns

## 1. Principles
-   **No Over-engineering:** Viết code đơn giản nhất có thể chạy được.
-   **Defensive Programming:** Luôn check `null`, check `mounted` (Flutter), try-catch các IO operation.
-   **Optimization:** Tránh rebuild widget không cần thiết.

## 2. Flutter Specifics
-   State Management: **BLoC** (Sử dụng `flutter_bloc`).
-   Folder Structure: Feature-based (`/features/name/{data,domain,presentation}`).
-   Async: Dùng `Future`/`Stream` cẩn thận. Tất cả file IO phải chạy background isolate hoặc async thread.

## 3. Database Interactions
-   Luôn dùng **Prepared Statements**.
-   Index các cột `where`.
-   Không query quá 50 record một lúc lên UI (Pagination).

## 4. UI Rules
-   Tuân thủ `docs/07_ui-ux/design-principles.md`.
-   Màu sắc: Dùng constants từ `AppColors`.
-   Font size: Luôn to hơn bình thường (+20%).

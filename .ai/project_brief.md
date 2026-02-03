# Project Brief (AI Context)

## Identity
**Project:** Allship Record
**Type:** Cross-platform Tool (Mobile/Desktop) for E-commerce Sellers.
**Core Value:** Quay video đóng gói/hoàn hàng làm bằng chứng đối soát "Hands-free".

## Critical Constraints
1.  **Local-First:** Dữ liệu video & DB nằm trên thiết bị user. Offline 100%.
2.  **Performance:** App phải chạy mượt trên Android tầm trung (Snapdragon 6xx). Video encoding H.264 Hardware.
3.  **Stack:** Flutter (Mobile), Electron (Desktop), SQLite (DB).
4.  **Workflow:** Ưu tiên tốc độ. Không block UI. Thao tác < 500ms.

## Key References
-   Full Docs: `docs/README.md`
-   Architecture: `docs/02_architecture/system-overview.md`
-   Database: `docs/02_architecture/database-schema.md`

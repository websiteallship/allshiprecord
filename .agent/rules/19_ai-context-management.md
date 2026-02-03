---
description: Rules for maintaining AI context and project history
globs: ["**/*"]
---
# AI Context Management Rules

This rule ensures that the project's AI context (`.ai/` folder) and history (`CHANGELOG.md`) remain up-to-date, allowing any AI agent to immediately understand the project state.

## 1. When to Update
You MUST update the context files when:
-   A task in `task.md` is marked as completed.
-   A major feature is implemented.
-   A critical bug is fixed.
-   The project architecture or tech stack changes.
-   A working session ends (update work log).

## 2. Files to Maintain

### A. `.ai/active_state.md`
-   **Purpose:** Tracks the current phase and immediate to-do list.
-   **Action:**
    -   Move completed items from `Active Tasks` to a `Completed` section (if exists) or just mark as `[x]`.
    -   Add new items to `Active Tasks` as they are discovered.
    -   Update `Current Phase` if the project milestone changes.

### B. `.ai/project_brief.md`
-   **Purpose:** High-level overview and constraints.
-   **Action:** Update ONLY if there is a fundamental change in:
    -   Tech Stack (e.g., switching from SQLite to Realm).
    -   Core Constraints (e.g., switching from Local-first to Cloud-first).

### C. `.ai/coding_patterns.md`
-   **Purpose:** Shared coding standards.
-   **Action:** Update if you establish a new pattern (e.g., "Always use `runZonedGuarded` for error handling") that future agents should follow.

### D. `CHANGELOG.md`
-   **Purpose:** User-facing project history.
-   **Action:** Add a line under the `[Unreleased]` section for every meaningful change.
    -   `Added`: New features.
    -   `Changed`: Changes in existing functionality.
    -   `Fixed`: Bug fixes.

### E. `.ai/work_log.md`
-   **Purpose:** Session diary.
-   **Action:** Append a new entry at the end of every session summarizing what was done.

## 3. Workflow
To automate this, run the workflow:
`agent run workflow update-ai-context` (or follow the steps in `.agent/workflows/update-ai-context.md`).

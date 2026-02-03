# Coding Conventions

## 1. General Principles
-   **KISS (Keep It Simple, Stupid):** Code đơn giản, dễ đọc là ưu tiên số 1.
-   **Local-first mindset:** Luôn giả định app đang offline.
-   **Comment:** Comment "Tại sao" (Why), không comment "Cái gì" (What).

## 2. Flutter (Dart)
Tuân thủ [Effective Dart](https://dart.dev/effective-dart) và [Flutter Lints](https://pub.dev/packages/flutter_lints).

-   **Naming:**
    -   Classes/Enums: `PascalCase` (`VideoRecorder`)
    -   Variables/Functions: `camelCase` (`startRecording`)
    -   Files: `snake_case` (`video_recorder.dart`)
-   **Project Structure:** Feature-first.
    ```
    lib/
      features/
        recording/
          presentation/
          domain/
          data/
        scanning/
      core/
    ```

## 3. Electron (TypeScript)
Sử dụng ESLint + Prettier.

-   **Naming:**
    -   Files: `kebab-case` (`scanner-service.ts`)
-   **IPC:**
    -   Luôn dùng `ipcRenderer.invoke` (Promise) thay vì `send/on` để tránh callback hell.
    -   Type-safe channels definition.

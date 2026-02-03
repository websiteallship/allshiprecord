# CI/CD Pipeline

Sử dụng GitHub Actions hoặc GitLab CI.

## 1. Workflow Mobile (Flutter)
Trigger: Push to `main` hoặc Tag `v*`

1.  **Check:** `flutter analyze`, `flutter format --set-exit-if-changed`.
2.  **Test:** `flutter test`.
3.  **Build Android:** `flutter build apk --release`.
4.  **Artifact:** Upload APK lên GitHub Releases.

## 2. Workflow Desktop (Electron)
Trigger: Push to `main`.

1.  **Check:** `eslint`.
2.  **Build:** `electron-builder`.
    -   Target: Windows (nsis), macOS (dmg).
3.  **Artifact:** Upload installer lên GitHub Releases.

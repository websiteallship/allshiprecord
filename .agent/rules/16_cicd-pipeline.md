# CI/CD Pipeline - ALL SHIP ECOMBOX

## Pipeline Overview

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Push   │───▶│  Build  │───▶│  Test   │───▶│ Deploy  │
│         │    │         │    │         │    │         │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
  Trigger      Compile +      Unit +        Staging /
              Lint Check   Integration     Production
```

## GitHub Actions

### Main Workflow

```yaml
# .github/workflows/main.yml
name: CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # ============================================
  # ANALYZE & LINT
  # ============================================
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.x'
          channel: 'stable'
      - run: flutter pub get
      - run: flutter analyze
      - run: dart format --set-exit-if-changed .

  # ============================================
  # UNIT TESTS
  # ============================================
  test:
    runs-on: ubuntu-latest
    needs: analyze
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
      - run: flutter pub get
      - run: flutter test --coverage
      - uses: codecov/codecov-action@v3
        with:
          file: coverage/lcov.info

  # ============================================
  # BUILD ANDROID
  # ============================================
  build-android:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      
      - name: Build APK
        run: |
          flutter build apk --flavor prod -t lib/main_prod.dart --release
      
      - name: Upload APK
        uses: actions/upload-artifact@v3
        with:
          name: app-release
          path: build/app/outputs/flutter-apk/app-prod-release.apk

  # ============================================
  # BUILD iOS
  # ============================================
  build-ios:
    runs-on: macos-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
      
      - name: Build iOS
        run: |
          flutter build ios --flavor prod -t lib/main_prod.dart --release --no-codesign
```

### Release Workflow

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release-android:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
      
      - name: Decode Keystore
        run: echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > android/keystore.jks
      
      - name: Build AAB
        env:
          KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}
        run: |
          flutter build appbundle --flavor prod -t lib/main_prod.dart --release
      
      - name: Upload to Play Store
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJsonPlainText: ${{ secrets.PLAY_STORE_JSON }}
          packageName: com.allship.ecombox
          releaseFiles: build/app/outputs/bundle/prodRelease/app-prod-release.aab
          track: internal
```

## Branch Strategy

```
main (production)
  │
  ├── develop (staging)
  │     │
  │     ├── feature/scan-improvement
  │     ├── feature/cloud-sync
  │     └── bugfix/camera-crash
  │
  └── hotfix/critical-bug
```

| Branch | Triggers | Deploys To |
|--------|----------|------------|
| `feature/*` | PR only | - |
| `develop` | Push | Staging |
| `main` | Push | Production |
| `v*` tags | Push | Play Store / App Store |

## Secrets Configuration

```yaml
# GitHub Secrets cần thiết:
KEYSTORE_BASE64        # Android signing keystore
KEYSTORE_PASSWORD      # Keystore password
KEY_ALIAS              # Key alias
KEY_PASSWORD           # Key password
PLAY_STORE_JSON        # Google Play service account
CODECOV_TOKEN          # Codecov upload token
SENTRY_DSN             # Sentry error tracking
```

## Version Management

```yaml
# pubspec.yaml
version: 1.0.0+1
# format: MAJOR.MINOR.PATCH+BUILD_NUMBER

# Auto-increment build number in CI:
- name: Increment Build Number
  run: |
    BUILD_NUMBER=${{ github.run_number }}
    sed -i "s/version: \(.*\)+.*/version: \1+$BUILD_NUMBER/" pubspec.yaml
```

## Quality Gates

```yaml
MERGE REQUEST yêu cầu:
  ✓ flutter analyze: 0 issues
  ✓ dart format: no changes
  ✓ flutter test: 100% pass
  ✓ Code coverage: ≥80%
  ✓ At least 1 approval
```

## Monitoring Post-Deploy

```yaml
TOOLS:
  - Sentry: Error tracking
  - Firebase Crashlytics: Crash reports
  - Firebase Analytics: Usage metrics (Phase 4)
  - Play Console: ANR, crashes, reviews
```

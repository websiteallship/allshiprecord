# Navigation Architecture - Allship Record

Kiến trúc điều hướng cho ứng dụng Allship Record.

---

## 1. Tổng quan Navigation

### 1.1 Navigation Pattern

- **Bottom Navigation**: 4 tabs chính
- **Modal Pages**: Full-screen cho quay video
- **Nested Navigation**: Trong mỗi tab
- **Deep Links**: Hỗ trợ mở trực tiếp màn hình

### 1.2 Sơ đồ Navigation

```
┌─────────────────────────────────────────────────────────────┐
│                        App Shell                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                     Content Area                       │   │
│  │  (Hiển thị page tương ứng với tab được chọn)          │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  [🎥 Quay]    [📋 Lịch sử]    [📊 Tổng quan]    [⚙️ Cài đặt] │
│     Tab 0         Tab 1          Tab 2           Tab 3      │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Route Definitions

### 2.1 Route Names

```dart
// lib/core/constants/route_names.dart

class RouteNames {
  RouteNames._();
  
  // ═══════════════════════════════════════════════════════════════
  // ROOT ROUTES
  // ═══════════════════════════════════════════════════════════════
  
  /// Splash screen
  static const String splash = '/';
  
  /// Onboarding flow
  static const String onboarding = '/onboarding';
  
  /// Main shell (bottom navigation)
  static const String main = '/main';
  
  // ═══════════════════════════════════════════════════════════════
  // CAMERA TAB (/camera)
  // ═══════════════════════════════════════════════════════════════
  
  /// Camera home - scan barcode
  static const String camera = '/camera';
  
  /// Active recording screen (modal full-screen)
  static const String recording = '/camera/recording';
  
  /// Recording preview after stop
  static const String recordingPreview = '/camera/preview';
  
  // ═══════════════════════════════════════════════════════════════
  // HISTORY TAB (/history)
  // ═══════════════════════════════════════════════════════════════
  
  /// History list
  static const String history = '/history';
  
  /// Video detail
  static const String videoDetail = '/history/video/:id';
  
  /// Video player (full screen)
  static const String videoPlayer = '/history/video/:id/player';
  
  /// Search videos
  static const String search = '/history/search';
  
  // ═══════════════════════════════════════════════════════════════
  // DASHBOARD TAB (/dashboard)
  // ═══════════════════════════════════════════════════════════════
  
  /// Dashboard overview
  static const String dashboard = '/dashboard';
  
  /// Statistics detail
  static const String statistics = '/dashboard/statistics';
  
  // ═══════════════════════════════════════════════════════════════
  // SETTINGS TAB (/settings)
  // ═══════════════════════════════════════════════════════════════
  
  /// Settings home
  static const String settings = '/settings';
  
  /// Camera settings
  static const String cameraSettings = '/settings/camera';
  
  /// Storage settings
  static const String storageSettings = '/settings/storage';
  
  /// Scanner settings (Bluetooth HID)
  static const String scannerSettings = '/settings/scanner';
  
  /// About app
  static const String about = '/settings/about';
  
  /// Licenses
  static const String licenses = '/settings/licenses';
  
  // ═══════════════════════════════════════════════════════════════
  // HELPER METHODS
  // ═══════════════════════════════════════════════════════════════
  
  /// Generate video detail path
  static String videoDetailPath(String videoId) => '/history/video/$videoId';
  
  /// Generate video player path
  static String videoPlayerPath(String videoId) => '/history/video/$videoId/player';
}
```

### 2.2 Route Table

| Route | Page | Description |
|---|---|---|
| `/` | `SplashPage` | App loading |
| `/onboarding` | `OnboardingPage` | First-time setup |
| `/main` | `MainShell` | Bottom nav container |
| `/camera` | `CameraPage` | Scanner + camera preview |
| `/camera/recording` | `RecordingPage` | Active recording (modal) |
| `/camera/preview` | `RecordingPreviewPage` | Review before save |
| `/history` | `HistoryPage` | Video list |
| `/history/video/:id` | `VideoDetailPage` | Video info + actions |
| `/history/video/:id/player` | `VideoPlayerPage` | Full-screen playback |
| `/history/search` | `SearchPage` | Search by order code |
| `/dashboard` | `DashboardPage` | Statistics overview |
| `/settings` | `SettingsPage` | Settings menu |
| `/settings/camera` | `CameraSettingsPage` | Camera options |
| `/settings/storage` | `StorageSettingsPage` | Storage management |
| `/settings/scanner` | `ScannerSettingsPage` | Bluetooth scanner |
| `/settings/about` | `AboutPage` | App info |

---

## 3. Router Implementation

### 3.1 App Router

```dart
// lib/core/router/app_router.dart

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../constants/route_names.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: RouteNames.splash,
    debugLogDiagnostics: true,
    routes: [
      // Splash
      GoRoute(
        path: RouteNames.splash,
        builder: (context, state) => const SplashPage(),
      ),
      
      // Onboarding
      GoRoute(
        path: RouteNames.onboarding,
        builder: (context, state) => const OnboardingPage(),
      ),
      
      // Main Shell with Bottom Navigation
      ShellRoute(
        builder: (context, state, child) => MainShell(child: child),
        routes: [
          // Camera Tab
          GoRoute(
            path: RouteNames.camera,
            pageBuilder: (context, state) => const NoTransitionPage(
              child: CameraPage(),
            ),
            routes: [
              GoRoute(
                path: 'recording',
                pageBuilder: (context, state) => MaterialPage(
                  fullscreenDialog: true,
                  child: RecordingPage(
                    orderCode: state.extra as String,
                  ),
                ),
              ),
              GoRoute(
                path: 'preview',
                builder: (context, state) => RecordingPreviewPage(
                  videoPath: state.extra as String,
                ),
              ),
            ],
          ),
          
          // History Tab
          GoRoute(
            path: RouteNames.history,
            pageBuilder: (context, state) => const NoTransitionPage(
              child: HistoryPage(),
            ),
            routes: [
              GoRoute(
                path: 'video/:id',
                builder: (context, state) => VideoDetailPage(
                  videoId: state.pathParameters['id']!,
                ),
                routes: [
                  GoRoute(
                    path: 'player',
                    pageBuilder: (context, state) => MaterialPage(
                      fullscreenDialog: true,
                      child: VideoPlayerPage(
                        videoId: state.pathParameters['id']!,
                      ),
                    ),
                  ),
                ],
              ),
              GoRoute(
                path: 'search',
                builder: (context, state) => const SearchPage(),
              ),
            ],
          ),
          
          // Dashboard Tab
          GoRoute(
            path: RouteNames.dashboard,
            pageBuilder: (context, state) => const NoTransitionPage(
              child: DashboardPage(),
            ),
            routes: [
              GoRoute(
                path: 'statistics',
                builder: (context, state) => const StatisticsPage(),
              ),
            ],
          ),
          
          // Settings Tab
          GoRoute(
            path: RouteNames.settings,
            pageBuilder: (context, state) => const NoTransitionPage(
              child: SettingsPage(),
            ),
            routes: [
              GoRoute(
                path: 'camera',
                builder: (context, state) => const CameraSettingsPage(),
              ),
              GoRoute(
                path: 'storage',
                builder: (context, state) => const StorageSettingsPage(),
              ),
              GoRoute(
                path: 'scanner',
                builder: (context, state) => const ScannerSettingsPage(),
              ),
              GoRoute(
                path: 'about',
                builder: (context, state) => const AboutPage(),
              ),
              GoRoute(
                path: 'licenses',
                builder: (context, state) => const LicensesPage(),
              ),
            ],
          ),
        ],
      ),
    ],
    
    // Error page
    errorBuilder: (context, state) => ErrorPage(error: state.error),
    
    // Redirect logic
    redirect: (context, state) async {
      final isFirstLaunch = await AppPreferences.isFirstLaunch();
      
      if (isFirstLaunch && state.uri.path == RouteNames.splash) {
        return RouteNames.onboarding;
      }
      
      return null;
    },
  );
}
```

### 3.2 Main Shell (Bottom Navigation)

```dart
// lib/features/shell/pages/main_shell.dart

class MainShell extends StatefulWidget {
  final Widget child;
  
  const MainShell({required this.child, super.key});
  
  @override
  State<MainShell> createState() => _MainShellState();
}

class _MainShellState extends State<MainShell> {
  int _currentIndex = 0;
  
  static const List<String> _tabRoutes = [
    RouteNames.camera,
    RouteNames.history,
    RouteNames.dashboard,
    RouteNames.settings,
  ];
  
  void _onTabTapped(int index) {
    if (index != _currentIndex) {
      setState(() => _currentIndex = index);
      context.go(_tabRoutes[index]);
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: widget.child,
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: _onTabTapped,
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Iconsax.video),
            activeIcon: Icon(Iconsax.video5),
            label: 'Quay',
          ),
          BottomNavigationBarItem(
            icon: Icon(Iconsax.clock),
            activeIcon: Icon(Iconsax.clock5),
            label: 'Lịch sử',
          ),
          BottomNavigationBarItem(
            icon: Icon(Iconsax.chart_2),
            activeIcon: Icon(Iconsax.chart_21),
            label: 'Tổng quan',
          ),
          BottomNavigationBarItem(
            icon: Icon(Iconsax.setting_2),
            activeIcon: Icon(Iconsax.setting5),
            label: 'Cài đặt',
          ),
        ],
      ),
    );
  }
}
```

---

## 4. Navigation Patterns

### 4.1 Push (Navigate Forward)

```dart
// Navigate to a new page
context.push(RouteNames.cameraSettings);

// With path parameters
context.push(RouteNames.videoDetailPath('video_123'));

// With extra data
context.push(
  RouteNames.recording,
  extra: orderCode,
);
```

### 4.2 Go (Replace)

```dart
// Replace current page
context.go(RouteNames.camera);

// After onboarding, replace with main
context.go(RouteNames.main);
```

### 4.3 Pop (Go Back)

```dart
// Go back
context.pop();

// Pop with result
context.pop(result);

// Check if can pop
if (context.canPop()) {
  context.pop();
}
```

### 4.4 Pop Until

```dart
// Pop to root of current tab
Navigator.of(context).popUntil((route) => route.isFirst);

// Pop to specific route
while (context.canPop()) {
  context.pop();
}
context.go(RouteNames.history);
```

---

## 5. Deep Links

### 5.1 Supported Deep Links

| Deep Link | Route | Use Case |
|---|---|---|
| `allship://camera` | `/camera` | Open camera |
| `allship://history` | `/history` | Open history |
| `allship://video/123` | `/history/video/123` | Open specific video |
| `allship://settings` | `/settings` | Open settings |

### 5.2 Android Configuration

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="allship" />
</intent-filter>
```

### 5.3 iOS Configuration

```xml
<!-- ios/Runner/Info.plist -->
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>allship</string>
    </array>
  </dict>
</array>
```

---

## 6. Navigation Guards

### 6.1 Permission Guard

```dart
// Check permissions before entering recording
redirect: (context, state) async {
  if (state.uri.path == RouteNames.recording) {
    final hasPermission = await PermissionUtils.hasCameraPermission();
    if (!hasPermission) {
      return RouteNames.camera; // Return to camera to request permission
    }
  }
  return null;
},
```

### 6.2 Auth Guard (Future)

```dart
// For authenticated routes (cloud sync, etc.)
redirect: (context, state) async {
  final isLoggedIn = await AuthService.isLoggedIn();
  final protectedRoutes = ['/settings/cloud', '/settings/account'];
  
  if (protectedRoutes.contains(state.uri.path) && !isLoggedIn) {
    return '/settings/login';
  }
  return null;
},
```

---

## 7. Page Transitions

### 7.1 Default Transitions

| Transition Type | When Used |
|---|---|
| `NoTransition` | Tab switching |
| `MaterialPage` | Standard navigation |
| `fullscreenDialog` | Modal overlays (Recording, Video Player) |
| `CupertinoPage` | iOS-style slide (optional) |

### 7.2 Custom Transitions

```dart
// Fade transition
CustomTransitionPage(
  child: page,
  transitionsBuilder: (context, animation, secondaryAnimation, child) {
    return FadeTransition(opacity: animation, child: child);
  },
)

// Slide up transition (for modals)
CustomTransitionPage(
  child: page,
  transitionsBuilder: (context, animation, secondaryAnimation, child) {
    return SlideTransition(
      position: Tween<Offset>(
        begin: const Offset(0, 1),
        end: Offset.zero,
      ).animate(animation),
      child: child,
    );
  },
)
```

---

## 8. pubspec.yaml Dependency

```yaml
dependencies:
  go_router: ^13.0.0
```

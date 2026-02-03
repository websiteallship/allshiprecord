# Scalability & Extensibility - ALL SHIP ECOMBOX

## Nguyên Tắc Core

> **LUÔN CODE ĐỂ CÓ THỂ MỞ RỘNG VỀ SAU**

```yaml
MINDSET:
  - MVP là nền tảng, KHÔNG phải sản phẩm cuối cùng
  - Mọi tính năng phải có "điểm mở rộng" (extension points)
  - Interface trước, implementation sau
  - Configuration > Hardcode
```

## Tính Năng Cần Chuẩn Bị Mở Rộng

### 1. Cloud Storage (Phase 4)

```dart
// ❌ SAI: Hardcode local storage
class VideoService {
  Future<void> saveVideo(Video video) async {
    final file = File('/videos/${video.filename}');
    await file.writeAsBytes(video.data);
  }
}

// ✅ ĐÚNG: Interface cho storage
abstract class StorageProvider {
  Future<String> save(String filename, Uint8List data);
  Future<Uint8List?> load(String filename);
  Future<void> delete(String filename);
  Future<bool> exists(String filename);
}

class LocalStorageProvider implements StorageProvider {
  @override
  Future<String> save(String filename, Uint8List data) async {
    final file = File('${_basePath}/$filename');
    await file.writeAsBytes(data);
    return file.path;
  }
}

// Phase 4: Thêm cloud mà KHÔNG đổi code cũ
class S3StorageProvider implements StorageProvider {
  @override
  Future<String> save(String filename, Uint8List data) async {
    // Upload to S3
  }
}

class HybridStorageProvider implements StorageProvider {
  final LocalStorageProvider local;
  final S3StorageProvider cloud;
  
  @override
  Future<String> save(String filename, Uint8List data) async {
    // Save local first
    final localPath = await local.save(filename, data);
    // Queue for cloud sync (background)
    _syncQueue.add(SyncJob(filename, data));
    return localPath;
  }
}
```

### 2. Multi-User / Team (Phase 4)

```dart
// ❌ SAI: Không có khái niệm user
class Order {
  final String code;
  final DateTime createdAt;
}

// ✅ ĐÚNG: Chuẩn bị cho multi-user
class Order {
  final String code;
  final DateTime createdAt;
  final String? userId;      // Null = single user mode
  final String? teamId;      // Null = no team
  final String? deviceId;    // Để sync across devices
}

// User context (nullable cho MVP)
class UserContext {
  static String? currentUserId;
  static String? currentTeamId;
  static String get deviceId => _getDeviceId();
}
```

### 3. API Integration (Phase 4)

```dart
// ❌ SAI: Hardcode marketplace logic
String getMarketplace(String code) {
  if (code.startsWith('SPX')) return 'Shopee';
  if (code.startsWith('GHN')) return 'GHN';
  return 'Unknown';
}

// ✅ ĐÚNG: Configurable marketplace rules
class MarketplaceConfig {
  final String name;
  final String prefix;
  final RegExp pattern;
  final String? apiEndpoint;  // Phase 4
  final String? apiKey;       // Phase 4
  
  static List<MarketplaceConfig> all = [
    MarketplaceConfig(name: 'Shopee', prefix: 'SPX', pattern: RegExp(r'^SPX\d{9,12}$')),
    MarketplaceConfig(name: 'GHN', prefix: 'GHN', pattern: RegExp(r'^GHN\d+')),
    // Dễ dàng thêm marketplace mới
  ];
}
```

### 4. Subscription / Commercialization

```dart
// ✅ Chuẩn bị tiers từ đầu
enum SubscriptionTier {
  free,       // Local only, 1 device
  basic,      // Metadata sync, 3 devices
  pro,        // Full sync, unlimited devices
  enterprise, // API access, team features
}

class FeatureFlags {
  final SubscriptionTier tier;
  
  bool get cloudSyncEnabled => tier.index >= SubscriptionTier.basic.index;
  bool get multiDeviceEnabled => tier.index >= SubscriptionTier.basic.index;
  bool get fullBackupEnabled => tier.index >= SubscriptionTier.pro.index;
  bool get apiAccessEnabled => tier == SubscriptionTier.enterprise;
  bool get teamFeaturesEnabled => tier == SubscriptionTier.enterprise;
  
  int get maxDevices => switch (tier) {
    SubscriptionTier.free => 1,
    SubscriptionTier.basic => 3,
    SubscriptionTier.pro => 10,
    SubscriptionTier.enterprise => 999,
  };
}

// MVP: Hardcode free tier
final features = FeatureFlags(tier: SubscriptionTier.free);
```

### 5. Analytics & Reporting

```dart
// ✅ Event tracking interface (implement sau)
abstract class AnalyticsProvider {
  void trackEvent(String name, Map<String, dynamic> params);
  void setUserProperty(String name, String value);
}

class NoOpAnalytics implements AnalyticsProvider {
  @override
  void trackEvent(String name, Map<String, dynamic> params) {}
  @override
  void setUserProperty(String name, String value) {}
}

// Phase 4: Firebase, Mixpanel, etc.
class FirebaseAnalyticsProvider implements AnalyticsProvider {
  @override
  void trackEvent(String name, Map<String, dynamic> params) {
    FirebaseAnalytics.instance.logEvent(name: name, parameters: params);
  }
}
```

## Design Patterns Bắt Buộc

### 1. Repository Pattern

```dart
// Interface
abstract class OrderRepository {
  Future<Order?> findByCode(String code);
  Future<List<Order>> findAll({DateTime? from, DateTime? to});
  Future<void> save(Order order);
  Future<void> delete(String id);
}

// Local implementation (MVP)
class LocalOrderRepository implements OrderRepository { ... }

// Remote implementation (Phase 4)
class RemoteOrderRepository implements OrderRepository { ... }

// Hybrid (Phase 4)
class HybridOrderRepository implements OrderRepository {
  final LocalOrderRepository local;
  final RemoteOrderRepository remote;
  
  @override
  Future<void> save(Order order) async {
    await local.save(order);
    if (features.cloudSyncEnabled) {
      await remote.save(order);
    }
  }
}
```

### 2. Service Abstraction

```dart
// Interface cho mọi service
abstract class VideoRecordingService {
  Future<void> startRecording(RecordingConfig config);
  Future<Video> stopRecording();
  Stream<RecordingState> get stateStream;
}

// Implementation có thể swap
class NativeVideoRecordingService implements VideoRecordingService { ... }
class FFmpegVideoRecordingService implements VideoRecordingService { ... }
```

### 3. Event-Driven Architecture

```dart
// Events cho decoupling
abstract class AppEvent {}

class OrderScannedEvent extends AppEvent {
  final String orderCode;
  final DateTime scannedAt;
}

class VideoSavedEvent extends AppEvent {
  final Video video;
}

// Listeners có thể thêm sau
class EventBus {
  final _controller = StreamController<AppEvent>.broadcast();
  
  void emit(AppEvent event) => _controller.add(event);
  Stream<T> on<T extends AppEvent>() => _controller.stream.whereType<T>();
}

// Phase 4: Thêm analytics listener
eventBus.on<VideoSavedEvent>().listen((e) {
  analytics.trackEvent('video_saved', {'duration': e.video.duration});
});
```

## Database Schema Extensible

```sql
-- ✅ Dùng nullable columns cho future fields
CREATE TABLE orders (
  id TEXT PRIMARY KEY,
  code TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  -- Future fields (nullable)
  user_id TEXT,
  team_id TEXT,
  synced_at INTEGER,
  cloud_url TEXT
);

-- ✅ Metadata table cho flexibility
CREATE TABLE metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

-- ✅ Separate sync status
CREATE TABLE sync_queue (
  id TEXT PRIMARY KEY,
  entity_type TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  action TEXT NOT NULL,  -- 'create', 'update', 'delete'
  created_at INTEGER NOT NULL,
  status TEXT DEFAULT 'pending'
);
```

## Configuration Over Hardcode

```dart
// ✅ Centralized config
class AppConfig {
  // Video
  static const defaultResolution = '1280x720';
  static const maxRecordingDuration = Duration(minutes: 5);
  static const defaultBitrate = 2000000;
  
  // Storage
  static const retentionDays = 90;
  static const storageWarningThreshold = 0.8;
  static const autoCleanupEnabled = true;
  
  // Feature flags (swap at runtime)
  static bool cloudSyncEnabled = false;
  static bool analyticsEnabled = false;
  static bool crashReportingEnabled = false;
}
```

## Checklist Khi Viết Code

```markdown
[ ] Có interface/abstract class cho service này không?
[ ] Có thể swap implementation khác không?
[ ] Config có hardcode không? Nên chuyển sang AppConfig
[ ] Database schema có nullable fields cho future không?
[ ] Có event nào cần emit cho listeners không?
[ ] Code có phụ thuộc vào 1 provider cụ thể không?
[ ] Có chuẩn bị cho multi-user scenario không?
```

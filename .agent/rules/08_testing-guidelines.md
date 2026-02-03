# Testing Guidelines - ALL SHIP ECOMBOX

## Chiến Lược Testing

### Pyramid Testing

```
                 /\
                /  \
               / E2E\        ← Ít nhất, chậm nhất, đắt nhất
              /──────\
             /        \
            / INTEGRATION\   ← Vừa phải
           /──────────────\
          /                \
         /    UNIT TESTS    \  ← Nhiều nhất, nhanh nhất
        /────────────────────\
```

## Unit Tests

### Coverage Target: 80%+ cho Business Logic

```dart
// Ví dụ: Test OrderCodeValidator
group('OrderCodeValidator', () {
  test('validates Shopee order code', () {
    final result = OrderCodeValidator.validate('SPX038294671');
    expect(result.isValid, true);
    expect(result.marketplace, 'shopee');
  });

  test('validates TikTok order code', () {
    final result = OrderCodeValidator.validate('TK1234567890');
    expect(result.isValid, true);
    expect(result.marketplace, 'tiktok');
  });

  test('rejects invalid code', () {
    final result = OrderCodeValidator.validate('ABC');
    expect(result.isValid, false);
    expect(result.message, contains('quá ngắn'));
  });

  test('handles empty input', () {
    final result = OrderCodeValidator.validate('');
    expect(result.isValid, false);
  });
});
```

### Mocking Patterns

```dart
// Mock repository
class MockOrderRepository extends Mock implements OrderRepository {}

// Mock camera service
class MockCameraService extends Mock implements CameraService {}

// Usage
void main() {
  late MockOrderRepository mockRepo;
  late OrderService orderService;

  setUp(() {
    mockRepo = MockOrderRepository();
    orderService = OrderService(mockRepo);
  });

  test('creates order when code is valid', () async {
    when(() => mockRepo.findByCode(any()))
        .thenAnswer((_) async => null);
    when(() => mockRepo.create(any()))
        .thenAnswer((_) async => Order(id: 1, code: 'SPX123'));

    final result = await orderService.createOrder('SPX123');
    
    expect(result.isSuccess, true);
    verify(() => mockRepo.create(any())).called(1);
  });
});
```

## Integration Tests

### Camera + Recording Flow

```dart
testWidgets('records video when barcode scanned', (tester) async {
  await tester.pumpWidget(MaterialApp(
    home: RecordingScreen(),
  ));

  // Simulate barcode scan
  final controller = tester.state<RecordingScreenState>(
    find.byType(RecordingScreen),
  );
  controller.onBarcodeScanned('SPX123456789');

  await tester.pumpAndSettle();

  // Verify recording started
  expect(find.byIcon(Icons.fiber_manual_record), findsOneWidget);
  expect(find.text('SPX123456789'), findsOneWidget);
});
```

### Database Operations

```dart
test('saves and retrieves video record', () async {
  final db = await openDatabase(':memory:');
  await initializeSchema(db);
  
  final repo = VideoRepository(db);
  
  // Save
  await repo.save(Video(
    orderCode: 'SPX123',
    filePath: '/videos/2026/02/03/SPX123_packing.mp4',
    type: 'packing',
    recordedAt: DateTime.now(),
  ));
  
  // Retrieve
  final videos = await repo.findByOrderCode('SPX123');
  
  expect(videos.length, 1);
  expect(videos.first.type, 'packing');
});
```

## Device Testing Matrix

### Android (Test trên 15-20 model phổ biến tại VN)

| Brand | Model | Priority | Notes |
|-------|-------|----------|-------|
| Samsung | Galaxy A54 | P0 | Phổ biến nhất |
| Samsung | Galaxy A34 | P0 | Tầm trung |
| Samsung | Galaxy A14 | P1 | Entry level |
| Xiaomi | Redmi Note 12 | P0 | Phổ biến |
| Xiaomi | Redmi 12 | P1 | Budget |
| OPPO | A78 | P0 | Phổ biến |
| OPPO | A17 | P1 | Budget |
| Vivo | Y36 | P1 | Budget |
| Realme | C55 | P1 | Budget |

### iOS

| Device | Priority | Notes |
|--------|----------|-------|
| iPhone 12 | P0 | Minimum supported |
| iPhone 13 | P0 | Common |
| iPhone 14 | P0 | Latest |
| iPad Air | P1 | Tablet support |

### Desktop

| OS | Version | Priority |
|----|---------|----------|
| Windows 11 | Latest | P0 |
| Windows 10 | Latest | P0 |
| macOS 13 (Ventura) | Latest | P1 |
| macOS 12 (Monterey) | Latest | P1 |

## Test Scenarios

### Critical Paths

1. **Happy Path: Quét → Quay → Lưu**
   - Mở app, chọn "Đóng hàng"
   - Quét mã vận đơn
   - Video bắt đầu tự động
   - Quét mã mới → video cũ dừng, video mới bắt đầu
   - Nhấn "Hoàn tất" → video lưu thành công

2. **Search Flow**
   - Nhập mã đơn → hiện video tương ứng
   - Nhấn video → phát lại
   - Chia sẻ video

3. **Return Flow**
   - Mở app, chọn "Nhận hoàn"
   - Quét mã → hiện thông tin đơn cũ
   - Quay video mở gói
   - Đánh giá tình trạng → lưu

### Edge Cases

1. **Camera disconnect during recording**
   - Verify: Video partial được lưu
   - Verify: User được thông báo
   - Verify: App không crash

2. **Scanner Bluetooth disconnect**
   - Verify: Tự động chuyển camera scan mode
   - Verify: Thông báo "Scanner offline"
   - Verify: Reconnect tự động

3. **Storage full**
   - Verify: Cảnh báo hiện trước khi hết
   - Verify: Auto-cleanup chạy đúng
   - Verify: Video mới vẫn có thể quay (cleanup xong)

4. **App crash và resume**
   - Verify: Partial video được lưu (fMP4)
   - Verify: App khởi động lại bình thường
   - Verify: Database không corrupt

5. **Duplicate barcode scan**
   - Verify: Phát âm cảnh báo "đã quét rồi"
   - Verify: Không tạo video mới
   - Verify: Recording vẫn tiếp tục

## Performance Benchmarks

| Metric | Target | Critical |
|--------|--------|----------|
| App cold start | < 3s | < 5s |
| Scan to record | < 500ms | < 1000ms |
| Video transition | < 500ms | < 1000ms |
| Thumbnail generation | < 1s | < 2s |
| SQLite query (by order) | < 1ms | < 10ms |
| Video save | < 2s | < 5s |
| FPS during recording | ≥ 20 | ≥ 15 |
| Memory usage | < 200MB | < 300MB |

## Automated Testing

### CI/CD Pipeline

```yaml
# .github/workflows/test.yml
name: Test
on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: subosito/flutter-action@v2
      - run: flutter pub get
      - run: flutter test --coverage
      - uses: codecov/codecov-action@v3

  integration-tests:
    runs-on: macos-latest # iOS simulator
    steps:
      - uses: actions/checkout@v3
      - uses: subosito/flutter-action@v2
      - run: flutter pub get
      - run: flutter test integration_test/
```

### Manual Test Checklist (Pre-release)

```
[ ] Camera recording works on 3+ Android devices
[ ] Camera recording works on iPhone
[ ] Bluetooth scanner pairing works
[ ] Continuous scan mode transitions < 500ms
[ ] Audio feedback plays correctly
[ ] Video thumbnail generates correctly
[ ] Search by order code works
[ ] Storage cleanup runs correctly
[ ] App survives crash/force close
[ ] App works offline
```

## Bug Reporting Template

```markdown
## Bug Report

**Severity:** Critical / High / Medium / Low

**Device:** [Model, OS version]

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. ...

**Expected Behavior:**

**Actual Behavior:**

**Screenshots/Videos:**

**Logs:**
```

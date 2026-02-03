---
description: Chạy unit test và integration test
---

# Chạy Tests

## Bước 1: Chạy Unit Tests
// turbo
```bash
flutter test
```

## Bước 2: Chạy với Coverage (Tùy chọn)
```bash
flutter test --coverage
```

## Bước 3: Xem Báo cáo Coverage
```bash
genhtml coverage/lcov.info -o coverage/html
start coverage/html/index.html
```

## Bước 4: Chạy Integration Tests (Trên thiết bị)
```bash
flutter test integration_test/
```

## Ghi chú
- Unit tests nằm trong thư mục `test/`.
- Integration tests nằm trong `integration_test/`.
- Cần Mock phần cứng (Camera, Scanner) khi test.

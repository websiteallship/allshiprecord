# Pre-recording Buffer

## Mô tả
Tính năng ghi hình "trước" khi user quét mã, giúp không bỏ lỡ khoảnh khắc đầu tiên khi cầm hàng lên.

## Vấn đề cần giải quyết
- iOS có thể kill app background bất cứ lúc nào.
- User quét mã **SAU** khi đã cầm hàng lên → Video bắt đầu từ giữa chừng.
- Mất bằng chứng "hàng đang ở đâu trước khi đóng".

## Giải pháp: Rolling Buffer
Camera liên tục ghi vào buffer xoay vòng (circular buffer) 3-5 giây.

```
Thời gian: |---5s---|---5s---|---5s---|
Buffer:    [Buffer A][Buffer B][Buffer C] → Xoay vòng
                                    ↑
                              User quét mã
                                    ↓
           [Lưu Buffer C + Tiếp tục quay]
```

## Kỹ thuật triển khai

### Mobile (Flutter)
- Sử dụng `camera` package với `startVideoRecording()`.
- Ghi vào file tạm (temp file).
- Khi quét mã: Copy 5s cuối từ temp file → Prepend vào video chính.
- Xóa temp file định kỳ.

### Desktop (Electron)
- Sử dụng MediaRecorder với `timeslice` để ghi từng chunk.
- Giữ 2-3 chunks cuối trong memory.
- Khi quét mã: Concat chunks + tiếp tục quay.

## Ưu tiên
**P1** - Should have cho Phase 2.

## Tham chiếu
- [MediaRecorder API](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder)

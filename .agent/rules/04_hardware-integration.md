# Hardware Integration - ALL SHIP ECOMBOX

## Barcode Scanner Integration

### Supported Scanner Types

| Loại | Kết Nối | Platform | Ưu Điểm | Nhược Điểm |
|------|---------|----------|---------|------------|
| Bluetooth HID | Bluetooth | Mobile, Desktop | Nhanh (~0.1s), chính xác 99.9% | Cần mua thiết bị |
| USB HID | USB | Desktop, Android OTG | Nhanh, ổn định | Chỉ dùng trên PC hoặc Android có OTG |
| Camera Built-in | N/A | Mobile | Tiện lợi, không cần thiết bị thêm | Tốc độ chậm hơn scanner |
| Webcam | USB | Desktop | Dùng thiết bị có sẵn | Phụ thuộc chất lượng webcam |

### Bluetooth HID Integration Pattern

```dart
// Flutter: Hidden TextField Strategy
class ScannerInputHandler extends StatefulWidget {
  @override
  _ScannerInputHandlerState createState() => _ScannerInputHandlerState();
}

class _ScannerInputHandlerState extends State<ScannerInputHandler> {
  final _textController = TextEditingController();
  final _focusNode = FocusNode();
  String _buffer = '';
  Timer? _inputTimer;

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // Hidden TextField - always focused for scanner input
        Positioned(
          left: -1000,
          child: TextField(
            controller: _textController,
            focusNode: _focusNode,
            autofocus: true,
            onChanged: _onInputReceived,
          ),
        ),
        // Actual UI content
        YourMainContent(),
      ],
    );
  }

  void _onInputReceived(String value) {
    _buffer = value;
    _inputTimer?.cancel();
    
    // Scanner sends all characters within 50ms
    // Human typing: > 100ms between keystrokes
    _inputTimer = Timer(Duration(milliseconds: 50), () {
      if (_buffer.length >= 6) {  // Valid barcode minimum length
        _processBarcode(_buffer);
        _textController.clear();
        _buffer = '';
      }
    });
  }

  void _processBarcode(String code) {
    // Validate and process barcode
    if (_isValidOrderCode(code)) {
      widget.onBarcodeScanned(code);
    }
  }
}
```

### iOS Keyboard Issue Workaround

> **Vấn đề:** Khi kết nối scanner Bluetooth HID, iOS nhận diện nó như external keyboard → tự động ẩn bàn phím ảo trên iPhone.

**Giải pháp:**
1. Thiết kế UI không phụ thuộc vào bàn phím ảo
2. Nút "Nhập tay" sẽ tạm disconnect Bluetooth → hiện keyboard → nhập → reconnect
3. Trên iPad: sử dụng option "Show keyboard" có sẵn
4. Ghi rõ trong hướng dẫn sử dụng

### Recommended Scanner Models

| Model | Giá | Loại | Tương thích |
|-------|-----|------|-------------|
| Netum C750 | ~300K | Bluetooth | iOS, Android, Windows |
| Inateck BCST-70 | ~500K | Bluetooth | iOS, Android, Windows |
| Honeywell Voyager 1202g | ~2M | Bluetooth | All platforms |
| Zebra DS2278 | ~3M | Bluetooth | Enterprise grade |

## Camera Integration

### Mobile (Flutter)

```dart
// Platform channels for native encoding
class NativeVideoEncoder {
  static const _channel = MethodChannel('video_encoder');
  
  Future<void> startRecording({
    required String outputPath,
    required VideoProfile profile,
  }) async {
    await _channel.invokeMethod('startRecording', {
      'outputPath': outputPath,
      'resolution': profile.resolution,
      'bitrate': profile.bitrate,
      'fps': profile.fps,
      'codec': 'h264',
      'useHardwareEncoder': true,
    });
  }
  
  Future<void> stopRecording() async {
    await _channel.invokeMethod('stopRecording');
  }
}

// Android: MediaCodec
// iOS: VideoToolbox (AVAssetWriter)
```

### Desktop (Electron)

```typescript
// WebRTC camera access
async function initializeCamera(): Promise<MediaStream> {
  const devices = await navigator.mediaDevices.enumerateDevices();
  const videoDevices = devices.filter(d => d.kind === 'videoinput');
  
  // Allow user to select camera
  const selectedDeviceId = await showCameraSelector(videoDevices);
  
  return navigator.mediaDevices.getUserMedia({
    video: {
      deviceId: { exact: selectedDeviceId },
      width: { ideal: 1280 },
      height: { ideal: 720 },
      frameRate: { ideal: 20 },
    },
    audio: true,
  });
}

// MediaRecorder for recording
class VideoRecorder {
  private mediaRecorder: MediaRecorder;
  private chunks: Blob[] = [];
  
  start(stream: MediaStream) {
    this.mediaRecorder = new MediaRecorder(stream, {
      mimeType: 'video/webm; codecs=vp8,opus',
    });
    
    this.mediaRecorder.ondataavailable = (e) => {
      this.chunks.push(e.data);
    };
    
    this.mediaRecorder.start(1000); // Callback every 1 second (fragmented)
  }
  
  async stop(): Promise<Blob> {
    return new Promise((resolve) => {
      this.mediaRecorder.onstop = () => {
        resolve(new Blob(this.chunks, { type: 'video/webm' }));
      };
      this.mediaRecorder.stop();
    });
  }
}
```

### IP Camera (RTSP) - Phase 3

```javascript
// FFmpeg for RTSP stream decoding (Electron)
const { spawn } = require('child_process');

class RTSPCameraStream {
  private ffmpegProcess: ChildProcess;
  
  async connect(rtspUrl: string): Promise<void> {
    // FFmpeg decode RTSP to raw frames
    this.ffmpegProcess = spawn('ffmpeg', [
      '-rtsp_transport', 'tcp',
      '-i', rtspUrl,
      '-f', 'rawvideo',
      '-pix_fmt', 'rgb24',
      '-vf', 'fps=20,scale=1280:720',
      '-'
    ]);
    
    this.ffmpegProcess.stdout.on('data', (data) => {
      this.onFrame(data);
    });
  }
  
  startRecording(outputPath: string): void {
    // Record RTSP stream directly to file
    spawn('ffmpeg', [
      '-rtsp_transport', 'tcp',
      '-i', this.rtspUrl,
      '-c:v', 'libx264',
      '-preset', 'fast',
      '-crf', '23',
      '-f', 'mp4',
      '-movflags', '+frag_keyframe+empty_moov',
      outputPath
    ]);
  }
}
```

## Multi-Camera Management (Desktop)

```typescript
interface CameraDevice {
  id: string;
  name: string;
  type: 'usb' | 'ip' | 'builtin';
  status: 'online' | 'offline' | 'error';
}

class MultiCameraManager {
  private cameras: Map<string, CameraDevice> = new Map();
  private activeCamera: string | null = null;
  
  async discoverCameras(): Promise<CameraDevice[]> {
    const usbCameras = await this.discoverUSBCameras();
    const ipCameras = await this.discoverIPCameras(); // ONVIF discovery
    
    return [...usbCameras, ...ipCameras];
  }
  
  // Handle USB camera hot-plug (known Electron issue #14743)
  startHotPlugMonitoring(): void {
    // Polling every 5 seconds in Settings screen
    setInterval(async () => {
      const currentDevices = await navigator.mediaDevices.enumerateDevices();
      this.detectChanges(currentDevices);
    }, 5000);
    
    // Also provide manual "Refresh camera list" button
  }
  
  async switchCamera(deviceId: string): Promise<void> {
    // Stop current camera
    if (this.activeCamera) {
      await this.stopCamera(this.activeCamera);
    }
    
    // Start new camera
    await this.startCamera(deviceId);
    this.activeCamera = deviceId;
  }
}
```

## Barcode Format Support

### Supported Formats

| Format | Sử Dụng | Ví Dụ |
|--------|---------|-------|
| Code 128 | Vận đơn (phổ biến nhất) | SPX123456789 |
| Code 39 | Vận đơn cũ | VN12345678 |
| EAN-13 | Sản phẩm | 4901234567890 |
| QR Code | Đa dạng (URL, data) | https://track.shopee.vn/SPX123 |
| Data Matrix | Compact data | Binary data |

### Order Code Validation

```dart
class OrderCodeValidator {
  // Regex patterns for Vietnamese e-commerce platforms
  static final patterns = {
    'shopee': RegExp(r'^SPX?\d{10,15}$'),
    'tiktok': RegExp(r'^TK\d{10,15}$'),
    'lazada': RegExp(r'^LZ\d{10,15}$'),
    'tiki': RegExp(r'^(TI|TIKI)\d{8,12}$'),
    'vnpost': RegExp(r'^VN\d{9,13}$'),
    'general': RegExp(r'^[A-Z]{2,4}\d{8,15}$'),
  };
  
  static ValidationResult validate(String code) {
    code = code.trim().toUpperCase();
    
    // Check minimum length
    if (code.length < 8) {
      return ValidationResult.invalid('Mã quá ngắn');
    }
    
    // Check against known patterns
    for (final entry in patterns.entries) {
      if (entry.value.hasMatch(code)) {
        return ValidationResult.valid(
          marketplace: entry.key,
          normalizedCode: code,
        );
      }
    }
    
    // Allow unknown format but warn
    if (RegExp(r'^[A-Z0-9]{8,20}$').hasMatch(code)) {
      return ValidationResult.warning(
        message: 'Định dạng mã không nhận diện được',
        normalizedCode: code,
      );
    }
    
    return ValidationResult.invalid('Mã không hợp lệ');
  }
}
```

## Hardware Error Codes

| Code | Description | Recovery |
|------|-------------|----------|
| `CAMERA_NOT_FOUND` | Không tìm thấy camera | Check connections, show camera selector |
| `CAMERA_IN_USE` | Camera đang được app khác sử dụng | Notify user to close other app |
| `CAMERA_PERMISSION_DENIED` | Không có quyền camera | Open app settings |
| `SCANNER_DISCONNECTED` | Scanner Bluetooth mất kết nối | Auto reconnect, fallback to camera scan |
| `SCANNER_PAIRING_FAILED` | Không thể ghép nối scanner | Show pairing instructions |
| `STORAGE_FULL` | Hết bộ nhớ | Auto-cleanup, notify user |
| `ENCODING_ERROR` | Lỗi encode video | Save partial, retry with lower quality |

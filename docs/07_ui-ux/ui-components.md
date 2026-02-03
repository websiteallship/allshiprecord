# UI Components Library

Tài liệu về các thư viện UI và reusable components cho dự án Allship Record.

---

## 1. Thư viện UI Được Sử Dụng

### 1.1 Core Libraries

| Package | Version | Mục đích |
|---|---|---|
| `flutter_platform_widgets` | ^6.1.0 | Auto-switch Material/Cupertino theo platform |
| `getwidget` | ^4.0.0 | 1000+ pre-built components |
| `styled_widget` | ^0.4.1 | CSS-like styling, code gọn hơn |
| `nb_utils` | ^6.1.5 | Utilities và helper methods |
| `iconsax_flutter` | ^1.0.0 | Icon library hiện đại, 1500+ icons |

### 1.2 Khi nào dùng thư viện nào?

| Use Case | Dùng |
|---|---|
| Button, Card, ListTile cơ bản | Material (built-in) |
| Cần adaptive iOS/Android | `flutter_platform_widgets` |
| Cần component phức tạp (Avatar, Rating, Accordion) | `getwidget` |
| Styling phức tạp, chain methods | `styled_widget` |
| Extension methods (`.isEmptyOrNull`, `.toInt()`) | `nb_utils` |

---

## 2. Reusable Components Tự Tạo

Đặt trong `lib/core/widgets/`.

### 2.1 AppButton

```dart
// lib/core/widgets/app_button.dart
import 'package:flutter/material.dart';

class AppButton extends StatelessWidget {
  final String label;
  final VoidCallback? onPressed;
  final bool isLoading;
  final IconData? icon;
  final AppButtonType type;

  const AppButton({
    required this.label,
    this.onPressed,
    this.isLoading = false,
    this.icon,
    this.type = AppButtonType.primary,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: isLoading ? null : onPressed,
      style: _getStyle(),
      child: isLoading
          ? SizedBox(
              width: 20,
              height: 20,
              child: CircularProgressIndicator(strokeWidth: 2),
            )
          : Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                if (icon != null) Icon(icon, size: 20),
                if (icon != null) SizedBox(width: 8),
                Text(label),
              ],
            ),
    );
  }

  ButtonStyle _getStyle() {
    switch (type) {
      case AppButtonType.primary:
        return ElevatedButton.styleFrom(
          backgroundColor: Colors.blue,
          foregroundColor: Colors.white,
          minimumSize: Size(double.infinity, 48),
        );
      case AppButtonType.secondary:
        return ElevatedButton.styleFrom(
          backgroundColor: Colors.grey[200],
          foregroundColor: Colors.black87,
        );
      case AppButtonType.danger:
        return ElevatedButton.styleFrom(
          backgroundColor: Colors.red,
          foregroundColor: Colors.white,
        );
    }
  }
}

enum AppButtonType { primary, secondary, danger }
```

### 2.2 OrderCard

```dart
// lib/core/widgets/order_card.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class OrderCard extends StatelessWidget {
  final String orderCode;
  final String type; // 'packing', 'shipping', 'return'
  final DateTime recordedAt;
  final int durationSeconds;
  final String? thumbnailPath;
  final VoidCallback? onTap;

  const OrderCard({
    required this.orderCode,
    required this.type,
    required this.recordedAt,
    required this.durationSeconds,
    this.thumbnailPath,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        leading: _buildThumbnail(),
        title: Text(orderCode, style: TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Row(
          children: [
            Icon(_getTypeIcon(), size: 14, color: _getTypeColor()),
            SizedBox(width: 4),
            Text('${_getTypeLabel()} | ${_formatTime()} | ${_formatDuration()}'),
          ],
        ),
        trailing: Icon(Iconsax.arrow_right_3),
        onTap: onTap,
      ),
    );
  }

  Widget _buildThumbnail() {
    if (thumbnailPath != null) {
      return ClipRRect(
        borderRadius: BorderRadius.circular(4),
        child: Image.file(File(thumbnailPath!), width: 56, height: 56, fit: BoxFit.cover),
      );
    }
    return Container(
      width: 56,
      height: 56,
      color: Colors.grey[300],
      child: Icon(Iconsax.video, color: Colors.grey[600]),
    );
  }

  IconData _getTypeIcon() {
    switch (type) {
      case 'packing': return Iconsax.box;
      case 'shipping': return Iconsax.truck;
      case 'return': return Iconsax.receive_square;
      default: return Iconsax.document;
    }
  }

  Color _getTypeColor() {
    switch (type) {
      case 'packing': return Colors.blue;
      case 'shipping': return Colors.green;
      case 'return': return Colors.orange;
      default: return Colors.grey;
    }
  }

  String _getTypeLabel() {
    switch (type) {
      case 'packing': return 'Đóng gói';
      case 'shipping': return 'Giao hàng';
      case 'return': return 'Hàng hoàn';
      default: return type;
    }
  }

  String _formatTime() => DateFormat('HH:mm').format(recordedAt);
  String _formatDuration() => '${durationSeconds}s';
}
```

### 2.3 StatusBadge

```dart
// lib/core/widgets/status_badge.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class StatusBadge extends StatelessWidget {
  final String status;

  const StatusBadge({required this.status});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: _getColor().withOpacity(0.2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(_getIcon(), size: 14, color: _getColor()),
          SizedBox(width: 4),
          Text(
            _getLabel(),
            style: TextStyle(
              color: _getColor(),
              fontSize: 12,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }

  IconData _getIcon() {
    switch (status) {
      case 'intact': return Iconsax.tick_circle;
      case 'damaged': return Iconsax.close_circle;
      case 'swapped': return Iconsax.warning_2;
      default: return Iconsax.info_circle;
    }
  }

  Color _getColor() {
    switch (status) {
      case 'intact': return Colors.green;
      case 'damaged': return Colors.red;
      case 'swapped': return Colors.orange;
      default: return Colors.grey;
    }
  }

  String _getLabel() {
    switch (status) {
      case 'intact': return 'Nguyên vẹn';
      case 'damaged': return 'Hư hỏng';
      case 'swapped': return 'Tráo hàng';
      default: return status;
    }
  }
}
```

### 2.4 VideoOverlayInfo

```dart
// lib/core/widgets/video_overlay_info.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class VideoOverlayInfo extends StatelessWidget {
  final String orderCode;
  final Duration elapsed;
  final Duration maxDuration;
  final String? location;

  const VideoOverlayInfo({
    required this.orderCode,
    required this.elapsed,
    required this.maxDuration,
    this.location,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(8),
      decoration: BoxDecoration(
        color: Colors.black.withOpacity(0.5),
        borderRadius: BorderRadius.circular(4),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            'MÃ ĐƠN: $orderCode',
            style: TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.bold,
              fontFamily: 'RobotoMono',
            ),
          ),
          SizedBox(height: 4),
          Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Iconsax.timer_1, size: 14, color: Colors.white),
              SizedBox(width: 4),
              Text(
                '${_formatDuration(elapsed)} / ${_formatDuration(maxDuration)}',
                style: TextStyle(color: Colors.white, fontSize: 14),
              ),
            ],
          ),
          if (location != null)
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Iconsax.location, size: 12, color: Colors.white70),
                SizedBox(width: 4),
                Text(
                  location!,
                  style: TextStyle(color: Colors.white70, fontSize: 12),
                ),
              ],
            ),
        ],
      ),
    );
  }

  String _formatDuration(Duration d) {
    return '${d.inMinutes.toString().padLeft(2, '0')}:${(d.inSeconds % 60).toString().padLeft(2, '0')}';
  }
}
```

### 2.5 EmptyState

```dart
// lib/core/widgets/empty_state.dart
class EmptyState extends StatelessWidget {
  final IconData icon;
  final String title;
  final String? subtitle;
  final Widget? action;

  const EmptyState({
    required this.icon,
    required this.title,
    this.subtitle,
    this.action,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 64, color: Colors.grey[400]),
          SizedBox(height: 16),
          Text(
            title,
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
          ),
          if (subtitle != null) ...[
            SizedBox(height: 8),
            Text(
              subtitle!,
              style: TextStyle(color: Colors.grey[600]),
              textAlign: TextAlign.center,
            ),
          ],
          if (action != null) ...[
            SizedBox(height: 24),
            action!,
          ],
        ],
      ),
    );
  }
}

// Usage:
// EmptyState(
//   icon: Icons.videocam_off,
//   title: 'Chưa có video nào',
//   subtitle: 'Quét mã vận đơn để bắt đầu quay',
//   action: AppButton(label: 'Quay video', onPressed: () {}),
// )
```

### 2.6 SettingsTile

```dart
// lib/core/widgets/settings_tile.dart
class SettingsTile extends StatelessWidget {
  final IconData icon;
  final String title;
  final String? subtitle;
  final Widget? trailing;
  final VoidCallback? onTap;

  const SettingsTile({
    required this.icon,
    required this.title,
    this.subtitle,
    this.trailing,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Container(
        padding: EdgeInsets.all(8),
        decoration: BoxDecoration(
          color: Theme.of(context).primaryColor.withOpacity(0.1),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Icon(icon, color: Theme.of(context).primaryColor),
      ),
      title: Text(title),
      subtitle: subtitle != null ? Text(subtitle!) : null,
      trailing: trailing ?? Icon(Icons.chevron_right),
      onTap: onTap,
    );
  }
}
```

### 2.7 ScannerInput

```dart
// lib/core/widgets/scanner_input.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class ScannerInput extends StatefulWidget {
  final Function(String) onScanned;
  final String? hintText;
  final bool autoFocus;

  const ScannerInput({
    required this.onScanned,
    this.hintText = 'Quét hoặc nhập mã đơn...',
    this.autoFocus = true,
  });

  @override
  State<ScannerInput> createState() => _ScannerInputState();
}

class _ScannerInputState extends State<ScannerInput> {
  final _controller = TextEditingController();
  final _focusNode = FocusNode();

  @override
  void initState() {
    super.initState();
    if (widget.autoFocus) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _focusNode.requestFocus();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _controller,
      focusNode: _focusNode,
      decoration: InputDecoration(
        hintText: widget.hintText,
        prefixIcon: Icon(Iconsax.scan_barcode),
        suffixIcon: _controller.text.isNotEmpty
            ? IconButton(
                icon: Icon(Iconsax.close_circle),
                onPressed: () {
                  _controller.clear();
                  setState(() {});
                },
              )
            : null,
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
        filled: true,
      ),
      onSubmitted: (value) {
        if (value.isNotEmpty) {
          widget.onScanned(value);
          _controller.clear();
        }
      },
      onChanged: (_) => setState(() {}),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    _focusNode.dispose();
    super.dispose();
  }
}
```

### 2.8 VideoThumbnail

```dart
// lib/core/widgets/video_thumbnail.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class VideoThumbnail extends StatelessWidget {
  final String? imagePath;
  final int durationSeconds;
  final VoidCallback? onTap;
  final double width;
  final double height;

  const VideoThumbnail({
    this.imagePath,
    required this.durationSeconds,
    this.onTap,
    this.width = 120,
    this.height = 80,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: width,
        height: height,
        decoration: BoxDecoration(
          color: Colors.grey[300],
          borderRadius: BorderRadius.circular(8),
          image: imagePath != null
              ? DecorationImage(
                  image: FileImage(File(imagePath!)),
                  fit: BoxFit.cover,
                )
              : null,
        ),
        child: Stack(
          children: [
            // Play button overlay
            Center(
              child: Container(
                padding: EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.black54,
                  shape: BoxShape.circle,
                ),
                child: Icon(Iconsax.play, color: Colors.white, size: 20),
              ),
            ),
            // Duration badge
            Positioned(
              bottom: 4,
              right: 4,
              child: Container(
                padding: EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                decoration: BoxDecoration(
                  color: Colors.black87,
                  borderRadius: BorderRadius.circular(4),
                ),
                child: Text(
                  _formatDuration(),
                  style: TextStyle(color: Colors.white, fontSize: 10),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  String _formatDuration() {
    final minutes = durationSeconds ~/ 60;
    final seconds = durationSeconds % 60;
    return '${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';
  }
}
```

### 2.9 StorageIndicator

```dart
// lib/core/widgets/storage_indicator.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class StorageIndicator extends StatelessWidget {
  final int usedBytes;
  final int totalBytes;
  final VoidCallback? onTap;

  const StorageIndicator({
    required this.usedBytes,
    required this.totalBytes,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final percentage = (usedBytes / totalBytes).clamp(0.0, 1.0);
    final isLow = percentage > 0.9;

    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: isLow ? Colors.red.withOpacity(0.1) : Colors.grey.withOpacity(0.1),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Row(
          children: [
            Icon(
              Iconsax.folder,
              color: isLow ? Colors.red : Colors.grey[600],
            ),
            SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    '${_formatBytes(usedBytes)} / ${_formatBytes(totalBytes)}',
                    style: TextStyle(fontWeight: FontWeight.w600),
                  ),
                  SizedBox(height: 4),
                  LinearProgressIndicator(
                    value: percentage,
                    backgroundColor: Colors.grey[300],
                    color: isLow ? Colors.red : Colors.blue,
                  ),
                ],
              ),
            ),
            if (isLow)
              Padding(
                padding: EdgeInsets.only(left: 8),
                child: Icon(Iconsax.warning_2, color: Colors.red),
              ),
          ],
        ),
      ),
    );
  }

  String _formatBytes(int bytes) {
    if (bytes < 1024) return '$bytes B';
    if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(1)} KB';
    if (bytes < 1024 * 1024 * 1024) return '${(bytes / 1024 / 1024).toStringAsFixed(1)} MB';
    return '${(bytes / 1024 / 1024 / 1024).toStringAsFixed(1)} GB';
  }
}
```

### 2.10 ConnectionStatus

```dart
// lib/core/widgets/connection_status.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

enum ConnectionType { bluetooth, camera, wifi }
enum ConnectionState { connected, disconnected, connecting }

class ConnectionStatus extends StatelessWidget {
  final ConnectionType type;
  final ConnectionState state;
  final String? deviceName;
  final VoidCallback? onTap;

  const ConnectionStatus({
    required this.type,
    required this.state,
    this.deviceName,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        decoration: BoxDecoration(
          color: _getBackgroundColor(),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: _getBorderColor()),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            if (state == ConnectionState.connecting)
              SizedBox(
                width: 14,
                height: 14,
                child: CircularProgressIndicator(strokeWidth: 2),
              )
            else
              Icon(_getIcon(), size: 16, color: _getIconColor()),
            SizedBox(width: 6),
            Text(
              deviceName ?? _getDefaultLabel(),
              style: TextStyle(
                fontSize: 12,
                color: _getTextColor(),
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }

  IconData _getIcon() {
    switch (type) {
      case ConnectionType.bluetooth: return Iconsax.bluetooth;
      case ConnectionType.camera: return Iconsax.camera;
      case ConnectionType.wifi: return Iconsax.wifi;
    }
  }

  String _getDefaultLabel() {
    switch (state) {
      case ConnectionState.connected: return 'Đã kết nối';
      case ConnectionState.disconnected: return 'Chưa kết nối';
      case ConnectionState.connecting: return 'Đang kết nối...';
    }
  }

  Color _getIconColor() => state == ConnectionState.connected ? Colors.green : Colors.grey;
  Color _getTextColor() => state == ConnectionState.connected ? Colors.green[700]! : Colors.grey[600]!;
  Color _getBackgroundColor() => state == ConnectionState.connected 
      ? Colors.green.withOpacity(0.1) 
      : Colors.grey.withOpacity(0.1);
  Color _getBorderColor() => state == ConnectionState.connected 
      ? Colors.green.withOpacity(0.3) 
      : Colors.grey.withOpacity(0.3);
}
```

### 2.11 RecordingTimer

```dart
// lib/core/widgets/recording_timer.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class RecordingTimer extends StatelessWidget {
  final Duration elapsed;
  final Duration? maxDuration;
  final bool isRecording;

  const RecordingTimer({
    required this.elapsed,
    this.maxDuration,
    this.isRecording = true,
  });

  @override
  Widget build(BuildContext context) {
    final isNearLimit = maxDuration != null && 
        elapsed.inSeconds > maxDuration!.inSeconds * 0.9;

    return Container(
      padding: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      decoration: BoxDecoration(
        color: isRecording ? Colors.red : Colors.grey[800],
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (isRecording)
            _BlinkingDot()
          else
            Icon(Iconsax.pause, size: 14, color: Colors.white),
          SizedBox(width: 8),
          Text(
            _formatDuration(elapsed),
            style: TextStyle(
              color: Colors.white,
              fontSize: 18,
              fontWeight: FontWeight.bold,
              fontFamily: 'RobotoMono',
            ),
          ),
          if (maxDuration != null) ...[
            Text(
              ' / ${_formatDuration(maxDuration!)}',
              style: TextStyle(
                color: isNearLimit ? Colors.yellow : Colors.white70,
                fontSize: 14,
              ),
            ),
          ],
        ],
      ),
    );
  }

  String _formatDuration(Duration d) {
    final minutes = d.inMinutes.toString().padLeft(2, '0');
    final seconds = (d.inSeconds % 60).toString().padLeft(2, '0');
    return '$minutes:$seconds';
  }
}

class _BlinkingDot extends StatefulWidget {
  @override
  State<_BlinkingDot> createState() => _BlinkingDotState();
}

class _BlinkingDotState extends State<_BlinkingDot> 
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(milliseconds: 800),
      vsync: this,
    )..repeat(reverse: true);
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _controller,
      child: Container(
        width: 10,
        height: 10,
        decoration: BoxDecoration(
          color: Colors.white,
          shape: BoxShape.circle,
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

### 2.12 DateGroupHeader

```dart
// lib/core/widgets/date_group_header.dart
class DateGroupHeader extends StatelessWidget {
  final DateTime date;
  final int videoCount;

  const DateGroupHeader({
    required this.date,
    required this.videoCount,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      color: Colors.grey[100],
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            _formatDate(),
            style: TextStyle(
              fontWeight: FontWeight.w600,
              color: Colors.grey[700],
            ),
          ),
          Text(
            '$videoCount video',
            style: TextStyle(
              color: Colors.grey[500],
              fontSize: 12,
            ),
          ),
        ],
      ),
    );
  }

  String _formatDate() {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final yesterday = today.subtract(Duration(days: 1));
    final dateOnly = DateTime(date.year, date.month, date.day);

    if (dateOnly == today) return 'Hôm nay';
    if (dateOnly == yesterday) return 'Hôm qua';
    return DateFormat('EEEE, dd/MM/yyyy', 'vi').format(date);
  }
}
```

### 2.13 ConfirmDialog

```dart
// lib/core/widgets/confirm_dialog.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class ConfirmDialog extends StatelessWidget {
  final String title;
  final String message;
  final String confirmLabel;
  final String cancelLabel;
  final IconData? icon;
  final Color? confirmColor;

  const ConfirmDialog({
    required this.title,
    required this.message,
    this.confirmLabel = 'Xác nhận',
    this.cancelLabel = 'Hủy',
    this.icon,
    this.confirmColor,
  });

  static Future<bool?> show(
    BuildContext context, {
    required String title,
    required String message,
    String confirmLabel = 'Xác nhận',
    String cancelLabel = 'Hủy',
    IconData? icon,
    Color? confirmColor,
  }) {
    return showDialog<bool>(
      context: context,
      builder: (_) => ConfirmDialog(
        title: title,
        message: message,
        confirmLabel: confirmLabel,
        cancelLabel: cancelLabel,
        icon: icon,
        confirmColor: confirmColor,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      icon: icon != null ? Icon(icon, size: 48, color: confirmColor) : null,
      title: Text(title, textAlign: TextAlign.center),
      content: Text(message, textAlign: TextAlign.center),
      actionsAlignment: MainAxisAlignment.spaceEvenly,
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, false),
          child: Text(cancelLabel),
        ),
        ElevatedButton(
          onPressed: () => Navigator.pop(context, true),
          style: ElevatedButton.styleFrom(
            backgroundColor: confirmColor ?? Theme.of(context).primaryColor,
          ),
          child: Text(confirmLabel),
        ),
      ],
    );
  }
}

// Usage:
// final confirmed = await ConfirmDialog.show(
//   context,
//   title: 'Xóa video?',
//   message: 'Video sẽ bị xóa vĩnh viễn và không thể khôi phục.',
//   confirmLabel: 'Xóa',
//   icon: Iconsax.trash,
//   confirmColor: Colors.red,
// );
```

### 2.14 StatCard

```dart
// lib/core/widgets/stat_card.dart
import 'package:iconsax_flutter/iconsax_flutter.dart';

class StatCard extends StatelessWidget {
  final String label;
  final String value;
  final IconData icon;
  final Color? color;
  final String? trend; // e.g., "+12%"
  final bool? trendUp;

  const StatCard({
    required this.label,
    required this.value,
    required this.icon,
    this.color,
    this.trend,
    this.trendUp,
  });

  @override
  Widget build(BuildContext context) {
    final cardColor = color ?? Theme.of(context).primaryColor;

    return Container(
      padding: EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: cardColor.withOpacity(0.1),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: cardColor.withOpacity(0.2)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, color: cardColor, size: 20),
              Spacer(),
              if (trend != null)
                Container(
                  padding: EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                  decoration: BoxDecoration(
                    color: (trendUp ?? true) ? Colors.green : Colors.red,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(
                    trend!,
                    style: TextStyle(color: Colors.white, fontSize: 10),
                  ),
                ),
            ],
          ),
          SizedBox(height: 12),
          Text(
            value,
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: cardColor,
            ),
          ),
          SizedBox(height: 4),
          Text(
            label,
            style: TextStyle(
              color: Colors.grey[600],
              fontSize: 12,
            ),
          ),
        ],
      ),
    );
  }
}

// Usage:
// StatCard(
//   label: 'Đơn hôm nay',
//   value: '156',
//   icon: Iconsax.box,
//   color: Colors.blue,
//   trend: '+12%',
//   trendUp: true,
// )
```

---

## 3. Cấu trúc Thư mục Components

```
lib/
├── core/
│   ├── widgets/
│   │   ├── app_button.dart
│   │   ├── order_card.dart
│   │   ├── status_badge.dart
│   │   ├── video_overlay_info.dart
│   │   ├── video_thumbnail.dart
│   │   ├── scanner_input.dart
│   │   ├── empty_state.dart
│   │   ├── loading_indicator.dart
│   │   ├── settings_tile.dart
│   │   └── index.dart  ← Export all widgets
│   ├── theme/
│   │   ├── app_theme.dart
│   │   ├── app_colors.dart
│   │   └── app_text_styles.dart
│   └── constants/
│       └── app_constants.dart
```

---

## 4. Export Index

```dart
// lib/core/widgets/index.dart
export 'app_button.dart';
export 'order_card.dart';
export 'status_badge.dart';
export 'video_overlay_info.dart';
export 'empty_state.dart';
export 'settings_tile.dart';
// ... export all widgets
```

Usage:
```dart
import 'package:allship_record/core/widgets/index.dart';
```

---

## 5. Theming với GetWidget

```dart
// Sử dụng GetWidget components
import 'package:getwidget/getwidget.dart';

// Button
GFButton(
  onPressed: () {},
  text: 'Đóng hàng',
  icon: Icon(Icons.camera_alt, color: Colors.white),
  size: GFSize.LARGE,
  fullWidthButton: true,
)

// Avatar
GFAvatar(
  backgroundImage: AssetImage('assets/logo.png'),
  shape: GFAvatarShape.standard,
)

// Badge
GFBadge(
  text: '5',
  color: Colors.red,
)

// Toast
GFToast.showToast(
  'Video đã lưu thành công!',
  context,
  toastPosition: GFToastPosition.BOTTOM,
)
```

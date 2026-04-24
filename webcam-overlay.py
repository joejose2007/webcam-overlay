import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QWidgetAction, QSlider, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QColor, QPainterPath

class WebcamOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam Overlay")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.size = 300
        self.shape = "circle"
        self.rect_width_ratio = 1.33
        self.fixed = False
        self.opacity = 1.0
        self.update_widget_size()
        self.move(200, 200)

        self.cap = cv2.VideoCapture(0)
        self.flip = True

        self.dragging = False
        self.drag_start_pos = QPoint()
        self.drag_start_geom = QPoint()
        self.frame = None

        # Close button
        self.close_btn = QPushButton("✕", self)
        self.close_btn.setFixedSize(24, 24)
        self.close_btn.setStyleSheet(
            "QPushButton{background:rgba(255,0,0,0.8);color:white;border:none;"
            "border-radius:12px;font-weight:bold;font-size:14px;}"
            "QPushButton:hover{background:rgba(255,50,50,0.9);}"
        )
        self.close_btn.clicked.connect(self.close_app)

        # Settings button
        self.settings_btn = QPushButton("⚙", self)
        self.settings_btn.setFixedSize(24, 24)
        self.settings_btn.setStyleSheet(
            "QPushButton{background:rgba(80,80,80,0.8);color:white;border:none;"
            "border-radius:12px;font-size:14px;}"
            "QPushButton:hover{background:rgba(100,100,100,0.9);}"
        )
        self.settings_btn.clicked.connect(self.show_settings_menu)

        self.update_buttons_position()
        self.setWindowOpacity(self.opacity)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_widget_size(self):
        if self.shape == "circle":
            w = h = self.size + 30
        else:
            w = int(self.size * self.rect_width_ratio) + 30
            h = self.size + 30
        self.resize(w, h)

    def update_buttons_position(self):
        bw = 24
        gap = 4
        total_w = bw * 2 + gap
        x_start = self.width() - total_w
        self.settings_btn.move(x_start, 0)
        self.close_btn.move(x_start + bw + gap, 0)
        self.close_btn.setVisible(not self.fixed)
        self.settings_btn.setVisible(not self.fixed)

    def set_opacity(self, value):
        self.opacity = value / 100.0
        self.setWindowOpacity(self.opacity)

    def show_settings_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet(
            "QMenu{background-color:rgba(40,40,40,0.95);color:white;"
            "border:1px solid rgba(80,80,80,0.8);border-radius:8px;padding:8px;}"
            "QMenu::item{padding:8px 16px;border-radius:4px;}"
            "QMenu::item:selected{background:rgba(100,100,100,0.5);}"
        )
        
        circle_action = menu.addAction("Switch to Circle" if self.shape == "rectangle" else "Switch to Rectangle")
        
        menu.addSeparator()
        # Opacity slider
        opacity_action = QWidgetAction(menu)
        opacity_widget = QWidget()
        opacity_layout = QHBoxLayout(opacity_widget)
        opacity_layout.setContentsMargins(12, 8, 12, 8)
        opacity_label = QLabel("Opacity:")
        opacity_label.setStyleSheet("color:white;")
        opacity_slider = QSlider(Qt.Horizontal)
        opacity_slider.setRange(1, 100)
        opacity_slider.setValue(int(self.opacity * 100))
        opacity_slider.setFixedWidth(120)
        opacity_slider.setStyleSheet(
            "QSlider::groove:horizontal{height:6px;background:rgba(100,100,100,0.5);border-radius:3px;}"
            "QSlider::handle:horizontal{width:18px;margin:-6px 0;background:white;border-radius:9px;}"
        )
        opacity_slider.valueChanged.connect(self.set_opacity)
        opacity_layout.addWidget(opacity_label)
        opacity_layout.addWidget(opacity_slider)
        opacity_action.setDefaultWidget(opacity_widget)
        menu.addAction(opacity_action)

        action = menu.exec_(self.settings_btn.mapToGlobal(self.settings_btn.rect().bottomLeft()))

        if action == circle_action:
            self.shape = "rectangle" if self.shape == "circle" else "circle"
            self.update_widget_size()
            self.update_buttons_position()
            self.update()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        if self.flip:
            frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        self.frame = QImage(rgb.data, w, h, w * ch, QImage.Format_RGB888)
        self.update()

    def paintEvent(self, event):
        if self.frame is None:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        cx, cy = self.width() // 2, self.height() // 2
        
        if self.shape == "circle":
            r = self.size // 2
            path = QPainterPath()
            path.addEllipse(cx - r, cy - r, r * 2, r * 2)
            clip_w = clip_h = self.size
        else:
            rw = int(self.size * self.rect_width_ratio)
            rh = self.size
            rx = cx - rw // 2
            ry = cy - rh // 2
            path = QPainterPath()
            path.addRect(rx, ry, rw, rh)
            clip_w = rw
            clip_h = rh

        painter.setClipPath(path)

        frame_w = self.frame.width()
        frame_h = self.frame.height()
        
        scale = max(clip_w / frame_w, clip_h / frame_h)
        new_w = int(frame_w * scale)
        new_h = int(frame_h * scale)
        
        pix = QPixmap.fromImage(self.frame).scaled(
            new_w, new_h, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        
        dx = (self.width() - new_w) // 2
        dy = (self.height() - new_h) // 2
        painter.drawPixmap(dx, dy, pix)

        painter.setClipping(False)
        pen = QPen(QColor(0, 0, 0, 255), 3)
        painter.setPen(pen)

        if self.shape == "circle":
            r = self.size // 2
            painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)
        else:
            rw = int(self.size * self.rect_width_ratio)
            rh = self.size
            rx = cx - rw // 2
            ry = cy - rh // 2
            painter.drawRect(rx, ry, rw, rh)

    def mousePressEvent(self, e):
        if self.fixed:
            return
        if e.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start_pos = e.globalPos()
            self.drag_start_geom = self.pos()

    def mouseMoveEvent(self, e):
        if self.fixed or not self.dragging:
            return
        delta = e.globalPos() - self.drag_start_pos
        self.move(self.drag_start_geom + delta)

    def mouseReleaseEvent(self, e):
        self.dragging = False

    def mouseDoubleClickEvent(self, e):
        self.shape = "rectangle" if self.shape == "circle" else "circle"
        self.update_widget_size()
        self.update_buttons_position()
        self.update()

    def wheelEvent(self, e):
        delta = e.angleDelta().y()
        self.size = max(100, min(500, self.size + (20 if delta > 0 else -20)))
        self.update_widget_size()
        self.update_buttons_position()

    def contextMenuEvent(self, e):
        self.fixed = not self.fixed
        self.update_buttons_position()

    def close_app(self):
        self.cap.release()
        QApplication.quit()

    def closeEvent(self, event):
        self.cap.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WebcamOverlay()
    w.show()
    sys.exit(app.exec_())

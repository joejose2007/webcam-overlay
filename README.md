# 📹 Webcam Overlay

A lightweight desktop webcam overlay with a circular or rectangular shape that floats above all windows. Features drag-and-drop positioning, scroll-to-resize, opacity control, and shape switching.

## ✨ Features

- 🔵 **Circle or Rectangle shape** - Double-click to switch between shapes
- 🖱️ **Draggable** - Click and drag to move anywhere on screen
- 🔄 **Resize with scroll** - Use mouse wheel to adjust size (100px - 500px)
- 👁️ **Opacity control** - Adjust transparency via settings slider (1-100%)
- 🔒 **Lock position** - Right-click to lock/unlock position and hide controls
- ⬆️ **Always on top** - Stays above all other windows
- 🎨 **Black outline** - Clean black border around the webcam shape
- ↔️ **Correct orientation** - Video displays correctly (left is left, right is right)
- ⚙️ **Settings menu** - ⚙ button with shape switching and opacity controls
- ❌ **Close button** - ✕ button to close application (hidden when locked)
- 🎬 **Full video display** - Video fills the entire shape without cropping

## 📸 Screenshots

> 🎬 **Demo GIF or screenshot coming soon!** Add a visual demonstration of the overlay in action.

## 🎯 Use Cases

Perfect for:

- 🎮 **Gaming streams** - Twitch, YouTube Gaming, OBS streaming with live webcam feed
- 📹 **Content creation** - Video recordings, tutorials, screen captures with facecam overlay
- 🎥 **Online meetings** - Zoom, Microsoft Teams, Google Meet picture-in-picture
- 📺 **Broadcasting** - Live streaming your webcam feed independently
- 🎪 **Presentations** - Live presentations with your face visible over slides
- 📚 **Educational videos** - Instructional content with instructor visible in corner
- 🎬 **Video production** - Quick visual reference without fullscreen camera window

## 🚀 Quick Start

For experienced users, get up and running in seconds:

```bash
git clone https://github.com/joejose2007/webcam-overlay.git
cd webcam-overlay
python3 -m venv venv && source venv/bin/activate  # macOS/Linux (Windows: venv\Scripts\activate)
pip install PyQt5 opencv-python-headless && python webcam-overlay.py
```

## 📦 Installation

### 📋 Prerequisites

You need Python 3.7+ installed on your system.

---

### 🪟 Windows

1. **📥 Download Python** (if not installed):
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download and install Python (check "Add Python to PATH" during install)

2. **📂 Download this project**:
   - Click the green "Code" button above and select "Download ZIP"
   - Extract the ZIP file

3. **🖥️ Open Command Prompt** in the project folder:
   - Navigate to the extracted folder
   - Hold Shift + Right-click → "Open command window here" or "Open PowerShell here"

4. **⚙️ Install dependencies**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install PyQt5 opencv-python-headless
   ```

5. **▶️ Run the application**:
   ```cmd
   venv\Scripts\python.exe webcam-overlay.py
   ```

---

### 🐧 Linux (Ubuntu/Debian/Kali)

1. **📥 Install system dependencies**:
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-venv python3-pip
   ```

2. **📂 Navigate to the project folder**:
   ```bash
   cd /path/to/webcam-overlay
   ```

3. **📦 Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **⚙️ Install dependencies**:
   ```bash
   pip install PyQt5 opencv-python-headless
   ```

5. **▶️ Run the application**:
   ```bash
   python webcam-overlay.py
   ```

---

### 🍎 macOS

1. **📥 Install Python** (if not installed):
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - Or use Homebrew: `brew install python`

2. **🖥️ Open Terminal** and navigate to the project folder:
   ```bash
   cd /path/to/webcam-overlay
   ```

3. **📦 Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **⚙️ Install dependencies**:
   ```bash
   pip install PyQt5 opencv-python-headless
   ```

5. **▶️ Run the application**:
   ```bash
   python webcam-overlay.py
   ```

---

## 🎮 Usage

### 🕹️ Basic Controls

| Action | Control |
|--------|---------|
| 🖱️ Move overlay | Click and drag the webcam area |
| 📏 Resize | Scroll mouse wheel (100px - 500px) |
| 🔄 Switch shape | Double-click on the webcam |
| 🔒 Lock/unlock position | Right-click on the webcam |
| 👁️ Adjust opacity | Click ⚙ settings button |
| ❌ Close app | Click ✕ button (visible when unlocked) |

### 🎨 Interface Elements

- **⚙️ Settings Button**: Opens a menu with:
  - Switch between Circle and Rectangle shapes
  - Opacity slider (1% to 100%) to adjust transparency
  
- **❌ Close Button**: Closes the application (only visible when position is unlocked)

- **Right-Click**: Toggles between:
  - **🔓 Unlocked**: Draggable, both buttons visible
  - **🔒 Locked**: Fixed position, buttons hidden

### 🎬 Visual Features

- **🎨 Black outline**: Clean 3px black border around the shape
- **↔️ Video orientation**: Correctly oriented (moving left shows left on screen)
- **🎬 Full video display**: Video fills the entire shape without being cropped
- **⬆️ Always on top**: Window stays above all other applications

## 📋 Requirements

- 🐍 Python 3.7+
- 📦 PyQt5
- 📷 opencv-python-headless
- 📹 Working webcam

## ⚙️ Customization

You can easily customize the application by editing `webcam-overlay.py`:

### Common Modifications

**Change default shape** (Circle or Rectangle):
```python
# Find this line and change to False for rectangle
self.is_circle = True
```

**Adjust default overlay size**:
```python
# Change the initial size (default: 200 pixels)
initial_size = 200
```

**Modify minimum and maximum size limits**:
```python
# Line with scroll handler - change 100 and 500
min_size = 100
max_size = 500
```

**Change border thickness**:
```python
# Adjust border width (default: 3 pixels)
border_width = 3
```

**Use different camera**:
```python
# Change camera index if you have multiple cameras
# Try 0, 1, 2, etc.
self.cap = cv2.VideoCapture(0)
```

**Adjust border color**:
```python
# Change RGB values (currently black: 0, 0, 0)
border_color = (0, 0, 0)  # BGR format
```

## 🔧 Troubleshooting

**📹 Camera not detected:**
- Make sure no other application is using the webcam
- Try changing camera index in code: `cv2.VideoCapture(0)` → try `cv2.VideoCapture(1)` or `cv2.VideoCapture(2)`

**⬛ Black screen:**
- Check camera permissions in your OS settings
- Ensure webcam is connected and working

**⚠️ Qt/platform errors:**
- Use the virtual environment method shown above
- On Linux, you may need: `sudo apt install -y python3-pyqt5`

**🔒 Camera permissions denied:**
- **Windows**: Settings → Privacy & Security → Camera
- **macOS**: System Preferences → Security & Privacy → Camera
- **Linux**: Run `sudo usermod -aG video $USER` (restart after)

## 📄 License

MIT License - feel free to modify and distribute!

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

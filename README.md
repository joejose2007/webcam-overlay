# Webcam Overlay

A lightweight desktop webcam overlay with a circular or rectangular shape that floats above all windows. Features drag-and-drop positioning, scroll-to-resize, opacity control, and shape switching.

![Webcam Overlay Screenshot](screenshot.png)

## Features

- **Circle or Rectangle shape** - Double-click to switch between shapes
- **Draggable** - Click and drag to move anywhere on screen
- **Resize with scroll** - Use mouse wheel to adjust size (100px - 500px)
- **Opacity control** - Adjust transparency via settings slider (1-100%)
- **Lock position** - Right-click to lock/unlock position and hide controls
- **Always on top** - Stays above all other windows
- **Black outline** - Clean black border around the webcam shape
- **Correct orientation** - Video displays correctly (left is left, right is right)
- **Settings menu** - ⚙ button with shape switching and opacity controls
- **Close button** - ✕ button to close application (hidden when locked)
- **Full video display** - Video fills the entire shape without cropping

## Installation

### Prerequisites

You need Python 3.7+ installed on your system.

---

### Windows

1. **Download Python** (if not installed):
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download and install Python (check "Add Python to PATH" during install)

2. **Download this project**:
   - Click the green "Code" button above and select "Download ZIP"
   - Extract the ZIP file

3. **Open Command Prompt** in the project folder:
   - Navigate to the extracted folder
   - Hold Shift + Right-click → "Open command window here" or "Open PowerShell here"

4. **Install dependencies**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install PyQt5 opencv-python-headless
   ```

5. **Run the application**:
   ```cmd
   venv\Scripts\python.exe webcam-overlay.py
   ```

---

### Linux (Ubuntu/Debian/Kali)

1. **Install system dependencies**:
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-venv python3-pip
   ```

2. **Navigate to the project folder**:
   ```bash
   cd /path/to/webcam-overlay
   ```

3. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install PyQt5 opencv-python-headless
   ```

5. **Run the application**:
   ```bash
   python webcam-overlay.py
   ```

---

### macOS

1. **Install Python** (if not installed):
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - Or use Homebrew: `brew install python`

2. **Open Terminal** and navigate to the project folder:
   ```bash
   cd /path/to/webcam-overlay
   ```

3. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install PyQt5 opencv-python-headless
   ```

5. **Run the application**:
   ```bash
   python webcam-overlay.py
   ```

---

## Usage

### Basic Controls

| Action | Control |
|--------|---------|
| Move overlay | Click and drag the webcam area |
| Resize | Scroll mouse wheel (100px - 500px) |
| Switch shape | Double-click on the webcam |
| Lock/unlock position | Right-click on the webcam |
| Adjust opacity | Click ⚙ settings button |
| Close app | Click ✕ button (visible when unlocked) |

### Interface Elements

- **⚙ Settings Button**: Opens a menu with:
  - Switch between Circle and Rectangle shapes
  - Opacity slider (1% to 100%) to adjust transparency
  
- **✕ Close Button**: Closes the application (only visible when position is unlocked)

- **Right-Click**: Toggles between:
  - **Unlocked**: Draggable, both buttons visible
  - **Locked**: Fixed position, buttons hidden

### Visual Features

- **Black outline**: Clean 3px black border around the shape
- **Video orientation**: Correctly oriented (moving left shows left on screen)
- **Full video display**: Video fills the entire shape without being cropped
- **Always on top**: Window stays above all other applications

## Requirements

- Python 3.7+
- PyQt5
- opencv-python-headless
- Working webcam

## Troubleshooting

**Camera not detected:**
- Make sure no other application is using the webcam
- Try changing camera index in code: `cv2.VideoCapture(0)` → try `cv2.VideoCapture(1)` or `cv2.VideoCapture(2)`

**Black screen:**
- Check camera permissions in your OS settings
- Ensure webcam is connected and working

**Qt/platform errors:**
- Use the virtual environment method shown above
- On Linux, you may need: `sudo apt install -y python3-pyqt5`

## License

MIT License - feel free to modify and distribute!

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

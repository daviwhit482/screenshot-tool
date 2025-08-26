# Screenshot Tool

A powerful Windows screenshot application with automatic GitHub watermarking. Capture, watermark, and share your screenshots instantly.

![Screenshot Tool](https://img.shields.io/badge/Python-3.x-blue.svg)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🖼️ **Full screen capture** with automatic GitHub watermarking
- 📋 **Copy to clipboard** with watermark applied
- 💾 **Save as file** with custom location picker and watermark
- 🔗 **Upload & Share** - Instant ImgBB links with watermarked screenshots
- 🎨 **Automatic watermarking** - Your GitHub profile subtly added to every screenshot
- 🕒 **Automatic timestamps** in filenames (screenshot_2024-08-24_15-30.png)
- 🎨 **Clean, modern UI** with custom styling
- ✅ **Success notifications** to confirm actions
- 📁 **Multiple file formats** support (PNG, JPEG, BMP)
- ⚡ **Fast and lightweight**
- ⌨️ **Global hotkey support** (F12 to capture from anywhere)
- 🔔 **System tray integration** - runs quietly in background
- 🌐 **Instant sharing** - get shareable links automatically

## 🚀 Quick Start

### Download (Recommended)
1. Go to [Releases](https://github.com/daviwhit482/screenshot-tool/releases)
2. Download `main.exe`
3. Run the executable - no installation needed!

### Build from Source
```bash
git clone https://github.com/daviwhit482/screenshot-tool.git
cd screenshot-tool
pip install -r requirements.txt
python main.py
```

## 🎮 Usage

### Three Capture Options:
- **Copy to Clipboard** - Screenshots with watermark copied directly to clipboard
- **Save to File** - Choose location to save watermarked screenshot  
- **Upload & Share** - Instant upload to ImgBB with automatic link copying

### Quick Access:
- **F12 Hotkey** - Capture to clipboard from anywhere
- **System Tray** - Right-click for quick options
- **Always Available** - Runs quietly in background

## 🛠️ Technical Details

Built with:
- **tkinter** - GUI framework
- **pyautogui** - Screen capture functionality  
- **pywin32** - Windows clipboard integration
- **PIL (Pillow)** - Image processing and watermarking
- **pystray** - System tray integration
- **pynput** - Global hotkey support
- **requests** - ImgBB API integration
- **datetime** - Timestamp generation

## 📋 Requirements

### For Executable:
- Windows 10/11
- No additional software needed

### For Source Code:
- Python 3.x
- Required packages: `pyautogui`, `pywin32`, `pillow`, `pystray`, `pynput`, `requests`

## 🔧 Building Executable

To create your own standalone executable:

```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed main.py
```

The executable will be created in the `dist/` folder.

## 👨‍💻 Author

Made by **[David White](https://github.com/daviwhit482)**

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features  
- Submit pull requests
- Improve documentation

## 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/daviwhit482/screenshot-tool/issues) on GitHub.

## 🔮 Future Ideas

- ✂️ Region selection tool
- ⏱️ Capture delay timer
- 🎨 Screenshot annotation tools
- 🔧 Customizable watermark options
- 📊 Usage statistics

---

⭐ **If you find this tool helpful, please give it a star!**

🔗 **Share your watermarked screenshots and help spread the word!**

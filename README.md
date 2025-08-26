# Screenshot Tool

A lightweight Windows screenshot application built with Python and Tkinter. Capture your screen with one click and choose how to save it.

![Screenshot Tool](https://img.shields.io/badge/Python-3.x-blue.svg)
![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🖼️ **Full screen capture** with one click
- 📋 **Copy to clipboard** instantly 
- 💾 **Save as file** with custom location picker
- 🕒 **Automatic timestamps** in filenames (screenshot_2024-08-24_15-30.png)
- 🎨 **Clean, modern UI** with custom styling
- ✅ **Success notifications** to confirm actions
- 📁 **Multiple file formats** support (PNG, JPEG, BMP, GIF)
- ⚡ **Fast and lightweight**
- ⌨️ **Global hotkey support (F12 to capture from anywhere)**
- 🔔 **System tray integration**
- 🔗 **Share images online with option to upload image to a link**

## 🚀 Quick Start

### Requirements
- Python 3.x
- Windows OS

### Installation

1. Clone the repository:
```bash
git clone https://github.com/daviwhit482/screenshot-tool.git
cd screenshot-tool
```

2. Install required packages:
```bash
pip install pyautogui pywin32 pillow pystray pynput
```

3. Run the application:
```bash
python main.py
```

## 🎮 Usage

Launch the application and you'll see two buttons:

- **Copy to Clipboard** - Takes a screenshot and copies it directly to your clipboard. Perfect for pasting into Discord, emails, or documents.

- **Save to File** - Opens a file dialog where you can choose where to save your screenshot. Automatically suggests a filename with the current timestamp.

## 🛠️ Technical Details

Built with:
- **tkinter** - GUI framework
- **pyautogui** - Screen capture functionality  
- **pywin32** - Windows clipboard integration
- **datetime** - Timestamp generation

## 🔮 Upcoming Features

- ✂️ Region selection tool
- ⏱️ Capture delay timer
- 🎨 Screenshot annotation tools

## 👨‍💻 Author

Made by **David White**

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features  
- Submit pull requests

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

⭐ If you find this tool helpful, please give it a star!

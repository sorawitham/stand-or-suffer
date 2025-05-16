# stand-or-suffer 🧍💥

**A brutal reminder to stand up — or suffer the consequences of sitting too long.**  
This tiny Python app pops a notification every 15 minutes past the hour (00, 15, 30, 45) to remind you to stand, stretch, and escape the grip of your evil office chair.

## 💡 Why?
Because sitting is the new smoking, and your spine deserves better.

## 🔧 How it works
- Runs in the background
- Checks the clock every second
- At every 00, 15, 30, 45 minute mark → sends a desktop notification

## 🛠️ Requirements
- Python 3.6+
- `plyer` (for cross-platform notifications)

```bash
pip install plyer
```

## 🚀 Run it manually
```bash
python stand_or_suffer.py
```

## ⚙️ Run on startup (Windows 11)
To make the program run automatically when Windows boots:

1. Create a shortcut to the script
* Right-click on stand_or_suffer.py → Create shortcut

2. Find your Startup folder
* Press Win + R, then type:

```bash
shell:startup
```

This opens the Startup folder.

3. Move the shortcut
* Move your stand_or_suffer.py - Shortcut into the Startup folder.

💡 Tip: To avoid opening a terminal window every time, you can convert your .py to a .pyw file or use pyinstaller to generate an executable.

## 👀 Sample Notification
Stand Up!
Time to rise, stretch, and defy the chair gods.

## 📦 License
MIT — use it, hack it, meme it.

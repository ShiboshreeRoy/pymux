# 🐚 PyMUX - A Python Terminal Emulator Inspired by Termux

**PyMUX v2.0** is an advanced terminal emulator written in Python that mimics the core features of Termux. It provides a shell environment with support for common Linux commands, custom package management, and simulated Termux utilities like `termux-open`, `termux-info`, and more.

---

## 📦 Features

- 🔧 Real shell command execution (via Bash/sh)
- 📜 Command history with autocomplete (via `readline`)
- 📦 `pkg install <package>` wrapper (uses APT)
- 🌐 `termux-open <url>` support (opens browser)
- 📱 `termux-info` support (system info printout)
- 🗂️ Filesystem navigation (cd, ls, etc.)
- 🔌 Easily extensible with custom commands (plugin-friendly)

---

## 📁 Project Structure

```

pymux/
├── main.py                  # Entry point
├── shell.py                 # Command loop logic
├── utils.py                 # Helpers (colors, clear, etc.)
└── commands/                # Termux-like commands
├── **init**.py
├── pkg.py
├── termux\_info.py
└── termux\_open.py

````

---

## 🚀 Getting Started

### 1. Clone or Download

```bash
git clone https://github.com/shiboshreeroy/pymux.git
cd pymux
````

### 2. Install Python

Requires **Python 3.7+** on Windows, Linux, or Termux.

### 3. Run the App

```bash
python main.py
```

---

## 💡 Available Commands

| Command                   | Description                         |
| ------------------------- | ----------------------------------- |
| `ls`, `cd`, `mkdir`, etc. | Standard Linux commands (via shell) |
| `pkg install <package>`   | Installs a package via `apt`        |
| `termux-open <url>`       | Opens the given URL in your browser |
| `termux-info`             | Displays device and Python info     |
| `clear`                   | Clears the terminal screen          |
| `exit`                    | Exits the PyMUX shell               |

---

## 🧩 Extending PyMUX

You can add your own commands easily:

1. Create a file in `commands/` (e.g. `termux_battery.py`)
2. Define a `run(args)` function
3. Import it in `commands/__init__.py`
4. Register it in `shell.py`

Example:

```python
# commands/termux_battery.py
def run(args):
    print("🔋 Battery: 83% (simulated)")
```

---

## 🛠 TODO (Planned Features)

* ✅ Simulated SMS, battery, and camera access
* ⏳ Plugin loader (dynamic `.py` scripts)
* ⏳ File explorer in CLI
* ⏳ GUI version using Tkinter or Textual

---

## 👨‍💻 Author

**Developed by:** Shiboshree Roy
Python Terminal + Systems Engineer
Email: [shiboshreeroycse@gmail.com](mailto:shiboshreeroycse@gmail.com)

---

## ⚖️ License

This project is licensed under the MIT License. See `LICENSE` for details.

---

# 🎓 Day 3 – Python Installation & IDE Setup

---

# 🟦 Slide 1 — Title Slide

## Day 3:

### Python Installation & IDE Setup

Topics:

* What is an IDE?
* Why use an IDE?
* Installing IDE
* Installing Python Extension
* Running First Program

---

# 🟦 Slide 2 — Quick Recap

Recap from previous sessions:

* CPU understands binary
* Python → Bytecode → Virtual Machine → CPU
* Interpreter = runtime system

Today:

> We move from theory to real development setup.

---

# 🟦 Slide 3 — What is an IDE?

## IDE = Integrated Development Environment

Definition:

> A software application that provides tools to write, edit, run, and debug code.

Examples:

* Visual Studio Code
* PyCharm
* IDLE

---

# 🟦 Slide 4 — Why Do We Use an IDE?

Without IDE:

* Write code in Notepad
* Run in CMD manually
* Hard to debug
* No syntax help

With IDE:

* Syntax highlighting
* Auto-complete
* Error detection
* Debugger
* File explorer
* Integrated terminal

Conclusion:

> IDE increases productivity and reduces errors.

---

# 🟦 Slide 5 — Why We Will Use VS Code

We will use:

Visual Studio Code

Why?

* Free
* Lightweight
* Popular in industry
* Supports multiple languages
* Strong Python support
* Extension-based architecture

---

# 🟦 Slide 6 — Downloading VS Code

Steps:

1. Go to official website.
2. Download stable version.
3. Install with default settings.
4. Open VS Code.

(Show live demo during class)

---

# 🟦 Slide 7 — Understanding VS Code UI

When VS Code opens, show:

Main sections:

1️⃣ Activity Bar (left side icons)
2️⃣ Explorer (files)
3️⃣ Editor Window
4️⃣ Terminal Panel
5️⃣ Status Bar

Explain each briefly.

---

# 🟦 Slide 8 — Installing Python Extension

Important step.

Inside VS Code:

1. Click Extensions icon
2. Search: **Python**
3. Install extension by Microsoft

Explain:

> Extension connects VS Code with Python interpreter.

This extension enables:

* IntelliSense
* Debugging
* Linting
* Code formatting

---

# 🟦 Slide 9 — Selecting Python Interpreter in VS Code

After installing extension:

1. Press `Ctrl + Shift + P`
2. Type: **Python: Select Interpreter**
3. Choose installed Python version

Explain:

> VS Code must know which python.exe to use.

This links IDE to interpreter.

---

# 🟦 Slide 10 — Creating First Python File

Steps:

1. Click File → Open Folder
2. Create new folder (e.g., Day3)
3. Create file: `main.py`

Inside file:

```python
print("Hello World")
```

---

# 🟦 Slide 11 — Running First Program in IDE

Two ways:

### Method 1 — Run Button

Click ▶ Run icon.

### Method 2 — Terminal

Open Terminal in VS Code:

```bash
python main.py
```

Explain what happens:

* VS Code calls python.exe
* Interpreter compiles to bytecode
* VM executes
* Output printed in terminal

---

# 🟦 Slide 12 — Understanding Integrated Terminal

Explain:

Integrated terminal = built-in CMD/PowerShell inside IDE.

Benefits:

* No need to switch windows
* Run commands directly
* Install packages

Example:

```bash
python --version
```

---

# 🟦 Slide 13 — Installing Python Packages (Preview)

Brief intro to pip:

```bash
pip install requests
```

* pip installs external libraries
* Installed inside Python environment

---

# 🟦 Slide 14 — Common Errors & Fixes

### 1️⃣ Python not found

→ Select correct interpreter

### 2️⃣ Module not found

→ pip install package

### 3️⃣ Code not running

→ Check terminal path

---

# 🟦 Slide 15 — IDE vs Notepad Comparison

| Notepad        | IDE                |
| -------------- | ------------------ |
| Plain text     | Smart editor       |
| No error hints | Error highlighting |
| No debugger    | Debugger           |
| Manual run     | One-click run      |

Conclusion:

> IDE is industry standard tool.

---

# 🟦 Slide 16 — What Happens Behind the Scenes

When you press Run:

```text
VS Code
↓
Python Extension
↓
python.exe
↓
Bytecode
↓
VM
↓
CPU
↓
Output
```

Connect practical to theory.

---

# 🟦 Slide 17 — Homework

1. Install VS Code.
2. Install Python extension.
3. Create 1 programs:
   * Print name
4. Run using terminal.

---

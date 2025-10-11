### 📄 docs/installation_guide.md

# Installation Guide - Manim Animations Project

**🌐 Language / Idioma:** [English](installation_guide.md) | [Català](../ca/guia_execucio.md)

This guide will help you set up the environment and run the animations from this Research Project on your local computer.

## 📋 Prerequisites

Before you begin, make sure you have the following programs installed:

### 1. Python (3.9 or higher)

- **How to check?** Open a terminal and type:
  ```bash
  python --version
  # or
  python3 --version
  ```
- **If you don't have it**: Download and install it from [python.org](https://www.python.org/downloads/). **Important**: During installation, check the **"Add Python to PATH"** option.

### 2. FFmpeg (Mandatory)

Manim uses FFmpeg to render videos.

- **Windows**:
  1.  Download the latest `full` version from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
  2.  Extract the ZIP folder (e.g., to `C:\ffmpeg`).
  3.  **Add FFmpeg to PATH** ([Visual guide](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)).
- **macOS**:
  ```bash
  # Install Homebrew if you don't have it:
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Install FFmpeg:
  brew install ffmpeg
  ```
- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

### 3. LaTeX (MiKTeX) (Required for mathematical formulas)

Necessary for rendering text and mathematical formulas.

- **Windows**: Install [MiKTeX](https://miktex.org/download). **Recommended**: Choose the "Install missing packages on the fly" option during installation.
- **macOS/Linux**: Install [TeX Live](https://www.tug.org/texlive/).

## 🚀 Installation and Execution

### Step 1: Get the source code

Download or clone this repository to a folder on your computer.

### Step 2: Open a terminal in the project folder

Make sure your terminal is working in the project directory (where the `requirements.txt` and `README.md` files are located).

### Step 3: (Recommended) Create and activate a virtual environment

Isolate project dependencies to avoid conflicts.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**Note**: When the virtual environment is activated, the terminal prompt will show `(venv)` at the beginning.

### Step 4: Install Python dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This will install the correct version of ManimCE (0.19.0) and all necessary libraries.

### Step 5: Explore and run the animations

You're all set! To see which animations are available:

1.  **Explore the Python files** in the project to see the available scenes.
2.  **Look for classes that inherit from `Scene`** (or similar Manim classes).
3.  **Run a specific scene**:
    ```bash
    # Format: manim [options] file.py SceneClassName
    manim -pqh file.py SceneClassName
    ```

**Command examples**:

```bash
# Render in high quality and open the video
manim -pqh main.py IntroScene

# Render in low quality (faster) and play automatically
manim -pql animations.py CircleToSquare

# Render an animated GIF instead of a video
manim -pqh --format=gif scenes.py RotationExample

# List all available scenes in a file
manim --help scenes.py
```

The rendered videos will be saved in the `media/videos/` folder within your project.

## 🆘 Troubleshooting Common Issues

- **Error: "FFmpeg not found"**:

  - Make sure you have installed it and **added the `bin` folder to PATH**. Close and reopen the terminal after doing so.

- **Error: "LaTeX not found"**:

  - Make sure you have installed MiKTeX or TeX Live. On Windows, try restarting your computer after installation.

- **Error: "command not found: manim"**:

  - Make sure your virtual environment is **activated** (`(venv)` should appear at the prompt).
  - Make sure the dependencies were installed correctly with `pip install -r requirements.txt`.

- **Mathematical text not appearing**:

  - Make sure LaTeX is installed. MiKTeX may ask to install additional packages the first time; allow it.

- **Python version error**:
  - Make sure you have Python 3.9 or higher. If you have multiple versions, use `python3` instead of `python`.

## ℹ️ Additional Information

- **ManimCE Documentation**: [https://docs.manim.community/](https://docs.manim.community/)
- **Official Repository**: [https://github.com/ManimCommunity/manim](https://github.com/ManimCommunity/manim)
- **Community**: [Manim Community Discord](https://manim.community/discord)

If you continue to have problems, you can:

1.  Verify that all prerequisites are installed correctly
2.  Make sure the virtual environment is activated
3.  Consult the ManimCE documentation
4.  Open an "issue" in this repository

**Enjoy the animations! 🎬**

---

**🌐 Language / Idioma:** [English](installation_guide.md) | [Català](../ca/guia_execucio.md)

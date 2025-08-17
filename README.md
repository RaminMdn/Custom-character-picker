# Custom-character-picker
A character picker which gives you quick access to a short selected list of special characters of your choice.

# Character Picker 🔣

A **lightweight and handy tool** to quickly pick and copy **special characters** that are not available on a standard keyboard — perfect for creating folder trees, diagrams, or tables in places like **GitHub READMEs**.

![Character Picker Screenshot](path/to/screenshot.png)  
*📌 Placeholder image above – replace with your screenshot!*

---
<br><br>

## ✨ Features

- ⚡ **Lightweight and fast** – Launches instantly and closes without lag.
- 📋 **One-click copy** – Click a character and press "Copy" to send it to your clipboard.
- 📌 **Always on top option** – Keep the picker visible over other windows for quick access.
- 🧩 **Customizable** – Use your own character set (see [Customization](#-customization) below).
- ✅ Works out of the box – No complex setup required.
- 🖥️ Optimized window sizing and positioning for Windows systems.

---
<br><br>

## 🧭 Purpose

If you're someone who frequently uses line-drawing characters or other special symbols for:

- 📁 Creating **folder trees** in `README.md` files
- 📊 Making **ASCII-style diagrams or tables**
- 🎨 Enhancing documentation or plain-text layouts

...this tool saves you from searching symbols or using difficult `ALT + CODE` combinations every time.

---
<br><br>

## 📷 Example Use Case

Here’s a simple GitHub-style folder tree:

```
📦Project
 ├── 📁src
 │   └── main.py
 ├── 📁docs
 └── README.md
```

---
<br><br>

## 🖱️ How It Works

1. Launch the app (`character_picker.py`).
2. Click on the symbol you want to use.
3. Press **"Copy"**.
4. Paste it anywhere (in your code, README, etc.)!

---
<br><br>

## 📌 Always on Top Mode

Enable the **"Always on top"** checkbox to keep the picker window floating above all other windows — perfect for multitasking while writing documentation.

---
<br><br>

## ⚙️ Customization

You can replace the default characters with any symbols of your choice!

### 🔧 How?

Open the Python file and locate this line near the top:

```python
CHARACTERS = ['├', '│', '└', '─', '|', '\\']
```

Replace the list with any characters you frequently use. For example:

```python
CHARACTERS = ['✓', '✗', '★', '→', '§']
```

---
<br><br>

## 🖼️ Screenshot

_Add a screenshot of your app running below:_

![App Screenshot](path/to/screenshot.png)  
*Screenshot placeholder – replace with your actual image.*

---
<br><br>

## 🚀 Getting Started
<br>

### ✅ Requirements

- Python 3.x
- `pyperclip` library (for clipboard support)

### 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/character-picker.git
cd character-picker
```

2. Install dependencies:

```bash
pip install pyperclip
```

3. Run the app:

```bash
python character_picker.py
```

---
<br><br>

## 🧪 Developers & Contributors

If you find this tool helpful, please consider ⭐ **starring the repository**!  
It helps others discover it and motivates development.

---
<br><br>

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute it.

---

## 🙌 Support

If you have any suggestions or improvements, feel free to open an issue or submit a pull request!

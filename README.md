# 🎨 Qute — PySide6 Theme Framework

Qute is a lightweight, scalable theming framework for PySide6 applications.
It provides a centralized design system, dynamic theme switching, and a clean architecture for managing UI styles across projects.

---

## ✨ Features

* 🎯 Centralized design system (colors, spacing, typography, radius)
* 🔄 Runtime theme switching (light / dark / custom)
* 💾 Persistent theme (via QSettings)
* 🧩 Jinja2-powered QSS templating
* 📦 Multi-file QSS support
* 🧠 Strong theme validation (structure enforced via template)
* 🔌 Decoupled architecture with Qt signals
* 🧱 Ready-to-use UI components (optional)

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install PySide6 jinja2
```

---

### 2. Project structure

```
your_app/
├── assets/
│   └── fonts/
├── core/
│   └── signals.py
├── design_system/
│   ├── radius.py
│   ├── spacing.py
│   └── typography.py
├── example/
│   └── main.py
├── manager/
│   └── theme_manager.py
├── styles/
│   ├── base.qss.j2
│   └── buttons.qss.j2
├── themes/
│   ├── _template.json
│   ├── light.json
│   └── dark.json
└── widgets/
    ├── theme_radio_group.py
    └── theme_toggle_button.py
```

---

### 3. Initialize Qute

```bash
from PySide6.QtWidgets import QApplication
from manager.theme_manager import ThemeManager

app = QApplication([])

theme_manager = ThemeManager.instance(app)

app.exec()
```

---

### 4. Add a theme switcher (optional)

```bash
from widgets.theme_radio_group import ThemeRadioGroup

group = ThemeRadioGroup(theme_manager.available_themes())
```

---

## 🎨 Theme System

Themes are defined as JSON files and validated against a template.

### Example `_template.json`

```json
{
  "colors": {
    "base": {
      "background": "",
      "surface": "",
      "surface_secondary": ""
    }
  }
}
```

### Example `light.json`

```json
{
  "colors": {
    "base": {
      "background": "#F6F8FB",
      "surface": "#FFFFFF",
      "surface_secondary": "#F0F4F9"
    }
  }
}
```

---

## 🧠 Design Tokens

Qute exposes design tokens to both QSS and Python:

### In QSS (via Jinja2)

```css
QWidget {
    background-color: {{ colors.base.background }};
    color: {{ colors.text.primary }};
}
```

---

### In Python

```bash
theme_manager.get_color("primary.main")
```

---

## 🔄 Theme Switching

Qute uses Qt signals for decoupled communication.

### Change theme

```bash
from core.signals import theme_signals

theme_signals.theme_change_requested.emit("dark")
```

---

### Listen for changes

```bash
theme_signals.theme_applied.connect(callback)
```

---

## 🧩 Built-in Widgets

Qute provides optional UI helpers:

* `ThemeRadioGroup` → multiple themes selection
* `ThemeToggleButton` → light/dark toggle

You are free to build your own UI and connect signals manually.

---

## ⚙️ How It Works

1. Load theme JSON
2. Validate against `_template.json`
3. Render QSS using Jinja2
4. Apply stylesheet to the application
5. Persist selected theme
6. Notify UI via signals

---

## 🧱 Architecture

```
ThemeManager
 ├── Theme loading (JSON)
 ├── Validation (template-driven)
 ├── QSS rendering (Jinja2)
 ├── Application styling
 ├── Persistence (QSettings)
 └── Signal orchestration

Design System
 ├── Colors (JSON)
 ├── Spacing (Python)
 ├── Typography (Python)
 └── Radius (Python)

UI Layer (optional)
 ├── ThemeRadioGroup
 └── ThemeToggleButton
```

---

## 🎯 Philosophy

Qute aims to:

* centralize all styling logic
* enforce consistency across projects
* remain flexible and non-intrusive
* scale from small apps to complex software

It does **not** impose UI structure — only styling.

---

## 📦 Use Cases

* Desktop apps (PySide6)
* Internal tools
* Portfolio projects
* Scalable multi-view applications

---

## 🔮 Roadmap

* QSS caching
* Theme inheritance
* Hot reload (dev mode)
* Animation support
* Extended validation (colors, formats)

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome.

---

## 👨‍💻 Author

Built by Dorian CARDOSO as part of a professional development journey.

# example/main.py
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

from manager.theme_manager import ThemeManager
from widgets.theme_radio_group import ThemeRadioGroup
from widgets.theme_toggle_button import ThemeToggleButton


def run_app():
    app = QApplication([])

    theme_manager = ThemeManager.instance(app)
    theme_manager.set_theme("light")

    window = QWidget()
    layout = QVBoxLayout(window)

    # Example with radio buttons group to handle multiple themes
    group = ThemeRadioGroup(theme_manager.available_themes())
    layout.addWidget(group)

    # # Example with push buttons to handle themes pair (light/dark)
    # btn = ThemeToggleButton()
    # layout.addWidget(btn)

    window.show()

    app.exec()


if __name__ == "__main__":
    run_app()

from PySide6.QtWidgets import QApplication
from qute.utils.loader import load_stylesheet

class DesignManager:
    def __init__(self, app: QApplication, default_theme: str = "light"):
        self.app = app
        self._current_theme = default_theme
        self.apply_stylesheet()

    def set_theme(self, theme: str):
        self._current_theme = theme
        self.apply_stylesheet()

    def apply_stylesheet(self):
        stylesheet = load_stylesheet(self._current_theme)
        self.app.setStyleSheet(stylesheet)

    def get_current_theme(self):
        return self._current_theme

    def toggle_theme(self):
        current = self.get_current_theme()
        new_theme = "dark" if current == "light" else "light"
        self.set_theme(new_theme)

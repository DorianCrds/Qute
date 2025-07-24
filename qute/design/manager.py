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

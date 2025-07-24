import sys
from PySide6.QtWidgets import QApplication

from examples.demo_main_window import MainWindow
from qute.design.manager import DesignManager

class DemoApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.design = DesignManager(app=self.app)

        self.window = MainWindow(theme_switch_callback=self.toggle_theme)
        self.window.show()

    def toggle_theme(self):
        current = self.design.get_current_theme()
        new_theme = "dark" if current == "light" else "light"
        self.design.set_theme(new_theme)

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    DemoApp().run()

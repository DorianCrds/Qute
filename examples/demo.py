import sys
from PySide6.QtWidgets import QApplication

from examples.demo_main_window import DemoMainWindow
from qute.design.manager import DesignManager

class DemoApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.window = DemoMainWindow()

        self.design = DesignManager(app=self.app)

        self.window.theme_button.clicked.connect(self.design.toggle_theme)
        self.window.show()

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    DemoApp().run()

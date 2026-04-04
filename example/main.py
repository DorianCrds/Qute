from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

from manager.theme_manager import ThemeManager


def run_app():
    app = QApplication([])

    theme_manager = ThemeManager.instance(app)
    theme_manager.set_theme("light")

    window = QWidget()
    layout = QVBoxLayout(window)

    btn = QPushButton("Click me")
    btn.setObjectName("primaryButton")

    layout.addWidget(btn)
    window.show()

    app.exec()


if __name__ == "__main__":
    run_app()

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from qute.components.buttons import CustomPushButton

class MainWindow(QMainWindow):
    def __init__(self, theme_switch_callback):
        super().__init__()
        self.setWindowTitle("Qute Demo App")
        self.resize(400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Styled interface using Qute 🎨")
        self.button = CustomPushButton("Switch theme")
        self.button.clicked.connect(theme_switch_callback)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

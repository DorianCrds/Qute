from PySide6.QtWidgets import QMainWindow, QWidget


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_mainwindow")

        self.central_widget = QWidget()
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)

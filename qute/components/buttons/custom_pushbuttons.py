from PySide6.QtWidgets import QPushButton


class CustomPushButton(QPushButton):
    def __init__(self, text: str):
        super().__init__()

        self.setObjectName("custom_pushbutton")
        self.setText(text)

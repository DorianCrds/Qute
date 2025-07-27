from PySide6.QtWidgets import QLabel


class CustomLabel(QLabel):
    def __init__(self, text: str):
        super().__init__()

        self.setObjectName("custom_label")
        self.setText(text)

from PySide6.QtWidgets import QPlainTextEdit


class CustomPlainTextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_plaintextedit")
        self.setMinimumSize(150, 80)

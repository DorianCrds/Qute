from PySide6.QtWidgets import QLineEdit


class CustomLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_lineedit")
        self.setMinimumWidth(150)

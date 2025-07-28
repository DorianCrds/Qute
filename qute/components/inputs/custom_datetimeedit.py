from PySide6.QtWidgets import QDateEdit


class CustomDateEdit(QDateEdit):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_dateedit")

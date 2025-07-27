from PySide6.QtWidgets import QTextEdit


class CustomTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_textedit")
        self.setMinimumSize(150, 80)

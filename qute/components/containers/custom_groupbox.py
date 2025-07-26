from PySide6.QtWidgets import QGroupBox


class CustomGroupBox(QGroupBox):
    def __init__(self, title: str):
        super().__init__()

        self.setObjectName("custom_groupbox")
        self.setTitle(title)

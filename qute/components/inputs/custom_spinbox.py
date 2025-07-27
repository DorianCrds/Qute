from PySide6.QtWidgets import QSpinBox


class CustomSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_spinbox")
        self.setMinimumWidth(150)

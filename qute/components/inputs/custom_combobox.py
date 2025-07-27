from PySide6.QtWidgets import QComboBox


class CustomComboBox(QComboBox):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_combobox")
        self.setMinimumWidth(150)

from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox


class CustomSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_spinbox")
        self.setMinimumWidth(150)

class CustomDoubleSpinBox(QDoubleSpinBox):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_doublespinbox")
        self.setMinimumWidth(150)

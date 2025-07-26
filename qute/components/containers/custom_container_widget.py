from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

class CustomContainerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("custom_container_widget")

        self.setAttribute(Qt.WA_StyledBackground, True)

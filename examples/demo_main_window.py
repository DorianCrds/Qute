from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout

from qute.components.buttons.custom_pushbuttons import CustomPushButton
from qute.components.containers.custom_container_widget import CustomContainerWidget
from qute.components.containers.custom_mainwindow import CustomMainWindow


class DemoMainWindow(CustomMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qute Demo App")
        self.resize(400, 300)

        self.main_h_layout = QHBoxLayout(self.central_widget)

        self.standard_widget = QWidget(self.central_widget)
        self.standard_widget_v_layout = QVBoxLayout(self.standard_widget)

        self.theme_button = CustomPushButton("Switch app theme")
        self.standard_widget_v_layout.addStretch()
        self.standard_widget_v_layout.addWidget(self.theme_button)

        self.custom_widget = CustomContainerWidget()
        self.custom_widget_v_layout = QVBoxLayout(self.custom_widget)

        self.useless_button = CustomPushButton("Useless button")
        self.custom_widget_v_layout.addWidget(self.useless_button)

        self.main_h_layout.addWidget(self.standard_widget)
        self.main_h_layout.addWidget(self.custom_widget)

        self.main_h_layout.setStretch(0, 2)
        self.main_h_layout.setStretch(1, 1)

from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QSizePolicy

from qute.components.buttons.custom_pushbuttons import CustomPushButton
from qute.components.containers.custom_container_widget import CustomContainerWidget
from qute.components.containers.custom_groupbox import CustomGroupBox
from qute.components.containers.custom_label import CustomLabel
from qute.components.containers.custom_mainwindow import CustomMainWindow
from qute.components.inputs.custom_lineedit import CustomLineEdit


class DemoMainWindow(CustomMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qute Demo App")
        self.resize(900, 750)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setSizePolicy(size_policy)

        self.main_h_layout = QHBoxLayout(self.central_widget)

        self.standard_widget = QWidget(self.central_widget)
        self.standard_widget_v_layout = QVBoxLayout(self.standard_widget)

        self.standard_groupbox = CustomGroupBox("Example standard group box")
        self.standard_widget_v_layout.addWidget(self.standard_groupbox)

        self.standard_label = CustomLabel("Standard label example")
        self.standard_widget_v_layout.addWidget(self.standard_label)

        self.standard_widget_v_layout.addStretch()

        self.standard_lineedit = CustomLineEdit()
        self.standard_widget_v_layout.addWidget(self.standard_lineedit)

        self.theme_button = CustomPushButton("Switch app theme")
        self.standard_widget_v_layout.addWidget(self.theme_button)


        self.custom_widget = CustomContainerWidget()
        self.custom_widget_v_layout = QVBoxLayout(self.custom_widget)

        self.embedded_groupbox = CustomGroupBox("Embedded group box example")
        self.custom_widget_v_layout.addWidget(self.embedded_groupbox)

        self.embedded_lineedit = CustomLineEdit()
        self.custom_widget_v_layout.addWidget(self.embedded_lineedit)

        self.custom_widget_v_layout.addStretch()

        self.embedded_label = CustomLabel("Embedded label example")
        self.custom_widget_v_layout.addWidget(self.embedded_label)

        self.useless_button = CustomPushButton("Useless button")
        self.custom_widget_v_layout.addWidget(self.useless_button)

        self.main_h_layout.addWidget(self.standard_widget)
        self.main_h_layout.addWidget(self.custom_widget)

        self.main_h_layout.setStretch(0, 4)
        self.main_h_layout.setStretch(1, 1)

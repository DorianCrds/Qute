# widgets/theme_radio_group.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from core.signals import theme_signals


class ThemeRadioGroup(QWidget):
    def __init__(self, themes):
        super().__init__()

        layout = QVBoxLayout(self)
        group = QButtonGroup(self)

        for theme in themes:
            radio = QRadioButton(theme)
            group.addButton(radio)
            layout.addWidget(radio)

            radio.toggled.connect(
                lambda checked, t=theme: checked and theme_signals.theme_changed.emit(t)
            )
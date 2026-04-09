# core/signals.py
from PySide6.QtCore import QObject, Signal

class ThemeSignals(QObject):
    theme_changed = Signal(str)

theme_signals = ThemeSignals()

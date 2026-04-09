# manager/theme_manager.py
import json
from pathlib import Path

from PySide6.QtGui import QFontDatabase, QFont
from jinja2 import Environment, FileSystemLoader

from core.signals import theme_signals
from design_system.radius import Radius
from design_system.spacing import Spacing
from design_system.typography import Typography


class ThemeManager:
    _instance = None

    def __init__(self, app, themes_path=None, styles_path=None, fonts_path=None):
        self.app = app

        base_dir = Path(__file__).resolve().parent.parent

        self.themes_path = Path(themes_path) if themes_path else base_dir / "themes"
        self.styles_path = Path(styles_path) if styles_path else base_dir / "styles"
        self.fonts_path = Path(fonts_path) if fonts_path else base_dir / "assets" / "fonts"

        self.load_fonts()
        app.setFont(QFont("Inter", 14))

        self.env = Environment(loader=FileSystemLoader(str(self.styles_path)))

        self.current_theme = None
        self.current_theme_name = None

        theme_signals.theme_changed.connect(self.set_theme)

        theme_signals.theme_changed.emit(self.available_themes()[0])

    @classmethod
    def instance(cls, app=None, **kwargs):
        if cls._instance is None:
            if app is None:
                raise ValueError("App required for first init")
            cls._instance = cls(app, **kwargs)
        return cls._instance

    # ---------------------
    # PUBLIC API
    # ---------------------

    def set_theme(self, theme_name: str):
        if theme_name not in self.available_themes():
            raise ValueError(f"Unknown theme: {theme_name}")

        theme_data = self._load_theme(theme_name)
        self.current_theme = theme_data
        self.current_theme_name = theme_name

        qss = self._render_all_styles(theme_data)
        self.app.setStyleSheet(qss)

    def available_themes(self):
        return [f.stem for f in self.themes_path.glob("*.json")]

    def get_current_theme(self):
        return self.current_theme_name

    # ---------------------
    # INTERNALS
    # ---------------------

    def _load_theme(self, theme_name: str):
        path = self.themes_path / f"{theme_name}.json"

        if not path.exists():
            raise FileNotFoundError(f"Theme not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _render_all_styles(self, theme_data: dict):
        qss = ""

        for file in self.styles_path.glob("*.qss.j2"):
            template = self.env.get_template(file.name)
            qss += template.render(
                colors=theme_data['colors'],
                spacing=Spacing,
                typography=Typography,
                radius=Radius
            ) + "\n"

        return qss

    def load_fonts(self):
        for font_path in self.fonts_path.glob("*.ttf"):
            font_id = QFontDatabase.addApplicationFont(str(font_path))
            if font_id == -1:
                print(f"Failed to load font {font_path.name}")
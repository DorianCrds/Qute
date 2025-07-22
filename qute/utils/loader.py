from importlib.resources import files

def load_stylesheet(theme: str) -> str:
    path = files("qute.themes") / f"{theme}.qss"
    return path.read_text(encoding="utf-8")

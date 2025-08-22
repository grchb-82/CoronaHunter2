import json
from pathlib import Path
from copy import deepcopy
import pygame

CONFIG_PATH = Path("config.json")
DEFAULT_CONFIG = {
    "fullscreen": False,
    "resolution": [256, 224],
    "flags": ["HWSURFACE", "DOUBLEBUF", "RESIZABLE", "SCALED"]
}

FLAG_MAP = {
    "FULLSCREEN": pygame.FULLSCREEN,
    "HWSURFACE":  pygame.HWSURFACE,
    "DOUBLEBUF":  pygame.DOUBLEBUF,
    "RESIZABLE":  pygame.RESIZABLE,
    "NOFRAME":    pygame.NOFRAME,
    "OPENGL":     pygame.OPENGL,
    "SCALED":     pygame.SCALED
}

def load_config() -> dict:
    """
    Lädt Settings aus config.json, ergänzt fehlende Keys aus DEFAULT_CONFIG
    und gibt das vollständige Dict zurück.
    Ist die Datei nicht vorhanden oder ungültig, wird sie mit DEFAULT_CONFIG erstellt.
    """
    cfg = {}
    if CONFIG_PATH.is_file():
        try:
            with CONFIG_PATH.open("r", encoding="utf-8") as f:
                cfg = json.load(f)
        except json.JSONDecodeError:
            cfg = {}
    # Fehlende Keys aus DEFAULT_CONFIG nachtragen
    for key, val in DEFAULT_CONFIG.items():
        cfg.setdefault(key, deepcopy(val))
    return cfg


def save_config(config: dict) -> None:
    """
    Speichert das übergebene Dict als config.json.
    """
    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)


def compute_flags(config_dict: dict) -> int:
    """
    Erzeugt das OR-verknüpfte Flag-Bitfeld basierend auf config_dict.
    """
    flags = 0
    for name in config_dict.get("flags", []):
        flags |= FLAG_MAP.get(name, 0)
    if config_dict.get("fullscreen", False):
        flags |= pygame.FULLSCREEN
    return flags

# Einmaliges Laden mit Defaults
CONFIG = load_config()

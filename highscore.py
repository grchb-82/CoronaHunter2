import os
from asset_loader import AssetLoader

HS_FILE = "key"  # oder Pfad/Name deiner Wahl

def load_high_score():
    """
    Liest den Highscore als Hex-String und gibt ihn als int zurück.
    Falls die Datei fehlt oder ungültig ist, wird 0 zurückgegeben.
    """
    if not os.path.exists(HS_FILE):
        return 0

    try:
        with open(HS_FILE, "r", encoding="utf-8") as f:
            hex_str = f.read().strip()
        # int(hex_str, 16) wandelt Hex-String in int
        return int(hex_str, 16)
    except (ValueError, IOError):
        return 0

def save_high_score(points):
    """
    Speichert den Highscore als Hex-String
    """
    old = load_high_score()
    if points <= old:
        return

    # (optional) Verzeichnis anlegen, falls du HS_FILE in einem Unterordner ablegst
    directory = os.path.dirname(HS_FILE)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # format(points, 'x') gibt die Hex-Darstellung ohne "0x" zurück,
    # z. B. 255 → "ff"
    hex_str = format(points, 'x')
    with open(HS_FILE, "w", encoding="utf-8") as f:
        f.write(hex_str)

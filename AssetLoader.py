import os, sys, pygame

class AssetLoader:
    def __init__(self):
        pass

    @staticmethod
    def resource_path(relative_path: str) -> str:
        """Sorgt dafür, dass Assets auch im PyInstaller-Build gefunden werden."""
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    @classmethod
    def load_image(cls, relative_path: str, convert_alpha=True):
        """Bild laden und automatisch über resource_path auflösen"""
        path = cls.resource_path(relative_path)
        image = pygame.image.load(path)
        return image.convert_alpha() if convert_alpha else image.convert()

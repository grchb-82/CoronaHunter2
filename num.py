from asset_loader import AssetLoader
import pygame

class Number(pygame.sprite.Sprite):
    def __init__(self, digit, x, y):
        super().__init__()
        self.image = AssetLoader.load_image(f"assets/sprites/num{digit}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Breite jeder Ziffer im Spritesheet
digit_width = 5  # px

# Pfad zum Standard-Spritesheet (angepasst an dein Projektverzeichnis)
default_sheet_path = "assets/fonts/numbers_small.png"


def load_digits(sheet_path=default_sheet_path):
    """
    Lädt das Ziffern-Spritesheet und gibt ein Dict zurück,
    das jede Ziffer ("0" bis "9") auf ein pygame.Surface mappt.
    """
    sheet = AssetLoader.load_image(sheet_path).convert_alpha()
    height = sheet.get_height()
    digits = {}
    for i in range(10):
        # Rechteck für jede Ziffer im Sheet
        rect = pygame.Rect(i * digit_width, 0, digit_width, height)
        digits[str(i)] = sheet.subsurface(rect).copy()
    return digits

# Standard-Dict beim Import laden
DIGITS_SMALL = load_digits()


def draw_number(surface, number, x, y, digits= DIGITS_SMALL):
    """
    Zeichnet eine Zahl (int oder str) auf das Surface.

    :param surface: Ziel-Surface, z.B. dein game_surface
    :param number:  int oder str, z.B. 42 oder "007"
    :param x:       X-Koordinate des linken Rands
    :param y:       Y-Koordinate der Oberkante
    :param digits:  Dict mit Ziffern-Surfaces, standardmäßig DIGITS_SMALL
    """
    text = str(number)
    for ch in text:
        digit_surf = digits.get(ch)
        if digit_surf:
            surface.blit(digit_surf, (x, y))
            x += digit_width  # Breite der Ziffer weiterschalten

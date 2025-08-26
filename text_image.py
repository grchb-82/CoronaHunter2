import pygame
from asset_loader import AssetLoader

class ShieldTXT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/fonts/shield_txt.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class DamageTXT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/fonts/damage_txt.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class EnergyTXT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/fonts/energy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class ResumeGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/resume.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class FullscreenGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/fullscreen.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class QuitGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/quit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class SettingsGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/settings.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class ResolutionGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/resolution.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class SelectorGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/selector.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class RestartGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = AssetLoader.load_image("assets/GUI/restart.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
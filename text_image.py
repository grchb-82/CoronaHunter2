import pygame

class ShieldTXT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/fonts/shield_txt.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class DamageTXT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/fonts/damage_txt.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class EnergyTXT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/fonts/energy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class ResumeGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/GUI/resume.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class FullscreenGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/GUI/fullscreen.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class QuitGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/GUI/quit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class SettingsGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/GUI/settings.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class ResolutionGUI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/GUI/resolution.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class SelectorGui(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/GUI/selector.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
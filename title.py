import pygame
from settings import *

class Title(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/title.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT //2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Version(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/version.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (7, HEIGHT -3)


    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Back1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/back1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Game_Over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/game_over.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
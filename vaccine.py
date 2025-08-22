import pygame
from settings import *

class Vaccine(pygame.sprite.Sprite):
    def __init__(self, x, y,game_state):
        super().__init__()
        self.image = pygame.image.load(f"assets/sprites/vaccine{game_state.ammo_type}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = game_state.vacc_speed
        self.mask = pygame.mask.from_surface(self.image)


    def update(self,dt_game):
        self.rect.x += self.speed * (dt_game)
        if self.rect.left > WIDTH:
            self.kill()


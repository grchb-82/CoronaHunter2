import pygame
import random
from settings import *
from asset_loader import AssetLoader

class pup_ammo(pygame.sprite.Sprite):
    def __init__(self, x, y,speed, game_state):
        super().__init__()
        self.image = AssetLoader.load_image(f"assets/sprites/pup_ammo{game_state.pup_type}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.life = game_state.pup_life

        self.speed_x = -speed
        self.speed_y = random.uniform(-speed, speed)  # leicht nach oben, unten oder gerade
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        self.pup_type = game_state.pup_type
        self.mask = pygame.mask.from_surface(self.image)
        self.visible = True

    def update(self,dt,game_state,game_time):
        self.pos_x += self.speed_x * (dt)
        self.pos_y += self.speed_y * (dt)

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

        # Blinken bei Respawn
        if game_state.pup_blink:
           # now = pygame.time.get_ticks()
            self.visible = (game_time // .100) % 2 == 0
        else:
            self.visible = True

        if self.rect.right < 0:
            self.kill()

        if self.rect.top < 20 or self.rect.bottom > HEIGHT:
            self.speed_y = self.speed_y * -1




import pygame
#from settings import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        super().__init__()
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f"assets/sprites/explosion{num}.png").convert_alpha()
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.rect_center = [x,y]
        self.counter = 0

    def update(self):
        explosion_speed = 8
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            #print (self.index)

            self.image = self.images[self.index]
            #länge = len(self.images)
            #print(f"länge{länge}")
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                self.kill()






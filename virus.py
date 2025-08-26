import player
from asset_loader import AssetLoader
import pygame
import random
from pygame.math import Vector2

from settings import *

class Virus(pygame.sprite.Sprite):

    MODE_NORMAL = "normal"
    MODE_REPEL  = "repel"

    player.score = 0
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = AssetLoader.load_image("assets/sprites/virus.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = Vector2(self.rect.topleft)

        self.speed = speed

        #self.speed_x = -speed
        #self.speed_y = random.choice([-random.uniform(0,speed), 0, random.uniform(0,speed)])  # leicht nach oben, unten oder gerade

        #self.pos_x = float(self.rect.x)
        #self.pos_y = float(self.rect.y)

        vy = random.choice([-random.uniform(0, speed), random.uniform(0, speed)])
        self.vel = Vector2(-speed, vy)


        self.v_life=20
        self.basepoints=10

        # State-Machine
        self.mode         = self.MODE_NORMAL
        self.prev_vel     = self.vel.copy()
        self.repel_target = None
        self.repel_speed  = 0.0
        self.repel_timer  = 0.0
        self.repel_duration = 1.0  # Sekunden

    def collide_shield(self, shield):
        #print("collide_shield virus1", shield)
        #if self.mode == self.MODE_NORMAL:
        self.prev_vel     = self.vel.copy()
        self.mode         = self.MODE_REPEL
        self.repel_target = shield
        # Shield kann ggf. eine eigene speed haben; sonst nimm Viren-Speed
        self.repel_speed = shield.speed * 1.1
        self.repel_timer  = 0.0

        #if self.rect.top <= 20 or self.rect.bottom >= HEIGHT:
        #    self.vel.y *= -1

    #def update(self,game_state,dt):
    def update(self, game_state, dt_game,player):
        """Bewegt das Virus je nach Mode."""

        if self.mode == self.MODE_NORMAL:
            # Normale Bewegung
            self.pos += self.vel * dt_game

        elif self.mode == self.MODE_REPEL:
            # 1) Von Shield wegsteuern
            target_vec = Vector2(self.repel_target.rect.center)
            direction =  self.pos - target_vec
            dist = direction.length()

            if dist > 0:
                unit = direction.normalize()
                self.pos += unit * self.repel_speed * dt_game

            # 2) Timer hochzählen, danach zurücksetzen
            self.repel_timer += dt_game
            if self.repel_timer >= self.repel_duration:
                self.mode = self.MODE_NORMAL
                self.vel = self.prev_vel.copy()

        # Rect an neue Position anpassen
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

        # Alte Logik beibehalten:
        if self.rect.right < 0:
            self.kill()
            player.life_no -= 0.1

        if self.rect.top < 20 :
            self.vel.y *= -1
            self.rect.top = 20
        elif self.rect.bottom > HEIGHT:
            self.vel.y *= -1
            self.rect.bottom = HEIGHT

class Virus1_Animation(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        super().__init__()
        self.images = []
        for num in range(1,7):
            img = AssetLoader.load_image(f"assets/sprites/virus1_ani_{num}.png").convert_alpha()
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.rect_center = [x,y]
        self.counter = 0

    def update(self):
        virus1_speed = 5
        self.counter += 1

        if self.counter >= virus1_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            #print (self.index)

            self.image = self.images[self.index]
            #länge = len(self.images)
            #print(f"länge{länge}")
        if self.index >= len(self.images) - 1 and self.counter >= virus1_speed:
                self.kill()

class Virus2(pygame.sprite.Sprite):

    MODE_NORMAL = "normal"
    MODE_REPEL  = "repel"

    def __init__(self, x, y, speed):
        super().__init__()
        self.image = AssetLoader.load_image("assets/sprites/virus2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #self.speed = speed
        #self.speed_x = -speed / 2
        #self.speed_y = random.choice([-random.uniform(0,speed), 0, random.uniform(0,speed)])*2  # leicht nach oben, unten oder gerade
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = Vector2(self.rect.topleft)

        self.speed = speed

        #self.speed_x = -speed
        #self.speed_y = random.choice([-random.uniform(0,speed), 0, random.uniform(0,speed)])  # leicht nach oben, unten oder gerade

        #self.pos_x = float(self.rect.x)
        #self.pos_y = float(self.rect.y)

        vy = random.choice([-random.uniform(0, speed), random.uniform(0, speed)])
        self.vel = Vector2(-speed / 2 , vy * 2)

        #self.pos_x = float(self.rect.x)
        #self.pos_y = float(self.rect.y)
        self.v_life = 50
        self.basepoints = 50

        # State-Machine
        self.mode = self.MODE_NORMAL
        self.prev_vel = self.vel.copy()
        self.repel_target = None
        self.repel_speed = 0.0
        self.repel_timer = 0.0
        self.repel_duration = 1.0  # Sekunden

    def update(self,game_state,dt_game,player):
        """Bewegt das Virus je nach Mode."""
        if self.mode == self.MODE_NORMAL:
            # Normale Bewegung
            self.pos += self.vel * dt_game

        elif self.mode == self.MODE_REPEL:
            # 1) Von Shield wegsteuern
            target_vec = Vector2(self.repel_target.rect.center)
            direction = self.pos - target_vec
            dist = direction.length()

            if dist > 0:
                unit = direction.normalize()
                self.pos += unit * self.repel_speed * dt_game

            # 2) Timer hochzählen, danach zurücksetzen
            self.repel_timer += dt_game
            if self.repel_timer >= self.repel_duration:
                self.mode = self.MODE_NORMAL
                self.vel = self.prev_vel.copy()

        # Rect an neue Position anpassen
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

        if self.rect.right < 0:
            self.kill()
            player.life_no -= 0.2

        if self.rect.top < 20:
            self.vel.y *= -1
            self.rect.top = 20
        elif self.rect.bottom > HEIGHT:
            self.vel.y *= -1
            self.rect.bottom = HEIGHT

    def collide_shield(self, shield):
        #print("collide_shield virus2", shield)
        """Im Collision-Handler aufrufen, wenn Virus das Shield trifft."""
        #if self.mode == self.MODE_NORMAL:
        self.prev_vel     = self.vel.copy()
        self.mode         = self.MODE_REPEL
        self.repel_target = shield
        # Shield kann ggf. eine eigene speed haben; sonst nimm Viren-Speed
        self.repel_speed = shield.speed * 1.1
        self.repel_timer  = 0.0

        #if self.rect.top <= 20 or self.rect.bottom >= HEIGHT:
        #    self.vel.y *= -1

class  Boss_Virus_10(pygame.sprite.Sprite):

    MODE_NORMAL = "normal"
    MODE_REPEL  = "repel"

    def __init__(self, x, y, speed,gs):
        super().__init__()
        self.image = AssetLoader.load_image("assets/sprites/level_10_boss.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.boss_pos = pygame.math.Vector2(self.rect.center)
        self.speed = speed
        self.speed_x = -speed / 2
        self.speed_y = random.choice([-random.uniform(0, speed), 0, random.uniform(0, speed)]) * 2  # leicht nach oben, unten oder gerade
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.v_life = gs.boss_hp
        self.basepoints = 500

        self._retarget_timer = 0
        self._retarget_interval = 2
        self.vel = Vector2(-speed, speed)
        # State-Machine
        self.mode = self.MODE_NORMAL
        self.prev_vel = self.vel.copy()
        self.repel_target = None
        self.repel_speed = 0.0
        self.repel_timer = 0.0
        self.repel_duration = 1.0  # Sekunden

    def move_to(self, gs, max_dist,dt_game,player):
        self._retarget_timer += dt_game
        if self._retarget_timer >= self._retarget_interval:

            gs.target_pos = pygame.math.Vector2(player.player_pos)
            self._retarget_timer -= self._retarget_interval
            print(f"retarget to {gs.target_pos}")

        #target = pygame.math.Vector2(target)
        direction = gs.target_pos - self.pos
        dist = direction.length()
        if dist <= max_dist or dist == 0:
            self.pos = gs.target_pos
        else:
            self.pos += direction.normalize() * max_dist

        if self.rect.top < 20:
            self.vel.y *= -1
            self.rect.top = 20
        if self.rect.bottom > HEIGHT:
            self.vel.y *= -1
            self.rect.bottom = HEIGHT+1

    def collide_shield(self, shield):
        if self.mode == self.MODE_NORMAL:
            self.prev_vel     = self.vel.copy()
            self.mode         = self.MODE_REPEL
            self.repel_target = shield
            # Shield kann ggf. eine eigene speed haben; sonst nimm Viren-Speed
            self.repel_speed = shield.speed * 1.1
            self.repel_timer  = 0.0

        if self.rect.top < 20:
            self.vel.y *= -1
            self.rect.top = 20
        if self.rect.bottom > HEIGHT:
            self.vel.y *= -1
            self.rect.bottom = HEIGHT+1

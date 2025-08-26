import pygame
from asset_loader import AssetLoader
from settings import *        # Kinematik


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image       = AssetLoader.load_image("assets/sprites/new_player.png").convert_alpha()
        self.rect        = self.image.get_rect(center=(0, HEIGHT//2))
        #self.rect        = self.image.get_rect(center=(0, HEIGHT // 2))
        self.visible     = True
        self.mask        = pygame.mask.from_surface(self.image)
        self.player_pos = pygame.math.Vector2(self.rect.center)
        self.life_no     = 3
        self.friction    = 2

        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False
        self.SHOOT_KEY, self.ACTION1_KEY, self.ACTION2_KEY, self.ACTION3_KEY = False, False, False,False
        self.position    = pygame.math.Vector2(self.rect.topleft)
        self.velocity    = pygame.math.Vector2(0, 0)
        self.acceleration= pygame.math.Vector2(0, 0)

    def update(self, dt, game_state,game_time):
        self.horizontal_movement(dt,game_state)
        self.vertical_movement(dt,game_state)
        self.player_pos = pygame.math.Vector2(self.rect.center)
        self.rect.clamp_ip(pygame.Rect(0, 20, WIDTH, HEIGHT-20))
        # Position ans sichtbare Rect anpassen
        self.position.update(self.rect.topleft)

        # Blinken bei Respawn
        if game_state.respawn:
         #   now = pygame.time.get_ticks()
            self.visible = (game_time // .100) % 2 == 0
        else:
            self.visible = True

    def horizontal_movement(self, dt,game_state):
        if game_state.boost_active:
            game_state.player_acceleration = 3000
            self.friction = 10
        else:
            game_state.player_acceleration = 350
            self.friction = 2

        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= game_state.player_acceleration
        if self.RIGHT_KEY:
            self.acceleration.x +=game_state.player_acceleration

        # Reibung immer entgegen der aktuellen Bewegung
        self.acceleration.x += -self.velocity.x * self.friction

        # Update und Clamp
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(PLAYER_SPEED,game_state)

        # Kinematik
        self.position.x += self.velocity.x * dt + 0.5 * self.acceleration.x * dt * dt
        self.rect.x = round(self.position.x)

        #print(f"dt={dt:.4f} | acc={self.acceleration.x:.2f} | vel={self.velocity.x:.2f}")

    def vertical_movement(self, dt,game_state):
        if game_state.boost_active:
            game_state.player_acceleration = 3000
            self.friction = 10
        else:
            game_state.player_acceleration = 350
            self.friction = 2

        self.acceleration.y = 0
        if self.UP_KEY:
            self.acceleration.y -= game_state.player_acceleration
        if self.DOWN_KEY:
            self.acceleration.y += game_state.player_acceleration

        self.acceleration.y += -self.velocity.y * self.friction

        self.velocity.y += self.acceleration.y * dt
        self.limit_velocity(PLAYER_SPEED,game_state)

        self.position.y += self.velocity.y * dt + 0.5 * self.acceleration.y * dt * dt
        self.rect.y = round(self.position.y)

    def limit_velocity(self, max_vel, game_state):

        # X- und Y- Achse begrenzen
        if game_state.boost_active:
            max_vel = 800
        else:
            max_vel = 250

        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < 0.01:
            self.velocity.x = 0


        self.velocity.y = max(-max_vel, min(self.velocity.y, max_vel))
        if abs(self.velocity.y) < 0.01:
            self.velocity.y = 0





class Shield(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        # referenz auf den Spieler speichern
        self.player = player

        # Bild & Rect mittig auf den Spieler setzen
        self.image = AssetLoader.load_image("assets/sprites/shield.png").convert_alpha()
        self.rect = self.image.get_rect(center=self.player.rect.center)

    #    # Lebensdauer des Schildes
    #    self.life = game_state.energy_level

        # Maske für Kollisionen
        self.mask = pygame.mask.from_surface(self.image)

        # Position als Vector2 für glatte Bewegungen
        self.pos = pygame.math.Vector2(self.rect.center)
        self.visible = True

        self.speed = PLAYER_SPEED

    def update(self, dt, game_time,game_state=None):
        # 1) Lebensdauer runterzählen (optional)
    #self.life -= dt # dt ist in Sekunden, life vermutlich in ms
    #   if self.life <= 0:
    #        self.kill()
    #        game_state.energy_level = 3
    #        return

        # 2) Position ans Zentrum des Spielers anpassen
        self.pos.update(self.player.rect.center)
        self.speed = self.player.velocity.length()
        # 3) Rect mitsyncen
        self.rect.center = (int(self.pos.x), int(self.pos.y-0))


        if game_state.shield_blink:
           # now = pygame.time.get_ticks()
            self.visible = (game_time // .100) % 2 == 0

        else:
            self.visible = True

import random
import sys
import pygame
import logic
import os

if sys.platform == "win32":
    try:
        # ruft die Win32-API auf und deaktiviert DPI‐Virtualisierung
        from ctypes import windll
        windll.user32.SetProcessDPIAware()
    except Exception:
        pass
from logic import handle_collisions, spawn_virus, update_game,action
from player import Player
from settings import *
from vaccine import Vaccine
from virus import Virus
from title import Title, Back1, Game_Over,Version
from menu import Title_Screen, Start_Menu
from highscore import save_high_score
from game_over_ext import game_over_ext
from text_image import *
from config   import CONFIG, compute_flags
from asset_loader import AssetLoader

pygame.init()

flags  = compute_flags(CONFIG)
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
game_surface = pygame.Surface((WIDTH, HEIGHT))


icon_surf = AssetLoader.load_image("assets/icons/virus.ico")  # Pfad anpassen
pygame.display.set_icon(icon_surf)

pygame.display.set_caption("CoronaHunter2")

pygame.mixer.set_num_channels(16)

hit_sound = AssetLoader.load_sound("assets/sounds/mixkit-cartoon-blow-impact-2654.wav")
hit_sound.set_volume(0.7)
hit2_sound = AssetLoader.load_sound("assets/sounds/mixkit-explosion-in-battle-2809.wav")
shot_sound = AssetLoader.load_sound("assets/sounds/mixkit-fast-blow-2144.wav")
shot_sound.set_volume(0.3)
oneup_sound = AssetLoader.load_sound("assets/sounds/mixkit-player-boost-recharging-2040.wav")
pup1_sound = AssetLoader.load_sound("assets/sounds/pup1.ogg")
pup2_sound = AssetLoader.load_sound("assets/sounds/pup2.ogg")
start_sound = AssetLoader.load_sound("assets/sounds/df_start_snd.ogg")
start_sound.set_volume(0.4)
hs_sound = AssetLoader.load_sound("assets/sounds/hs.ogg")
fanfare_sound = AssetLoader.load_sound("assets/sounds/fanfare.ogg")
game_over_sound = AssetLoader.load_sound("assets/sounds/game_over.ogg")
level_complete_sound = AssetLoader.load_sound("assets/sounds/level_complete.ogg")
next_level_sound = AssetLoader.load_sound("assets/sounds/next_level.ogg")
boss_level_background_music = AssetLoader.load_sound("assets/sounds/boss_level_backmuc.ogg")
boss_explosion = AssetLoader.load_sound("assets/sounds/boss_explosion.ogg")
swoosh = AssetLoader.load_sound("assets/sounds/swoosh.ogg")
swoosh.set_volume(0.7)
sparks = AssetLoader.load_sound("assets/sounds/sparks.ogg")
shield_hit_sound = AssetLoader.load_sound("assets/sounds/shield_hit.ogg")
shield_hit_sound.set_volume(1)
pause_sound = AssetLoader.load_sound("assets/sounds/pause.ogg")
unpause_sound = AssetLoader.load_sound("assets/sounds/unpause.ogg")

from draw import draw_game
#_Game Initializing########################################################################
def init():
    from state import GameState

    clock = pygame.time.Clock()
    game_state = GameState()
    gs = game_state
    player1 = Player()
    back1 = Back1()
    bosses = pygame.sprite.Group()
    viruses1= pygame.sprite.Group()
    viruses2= pygame.sprite.Group()
    vaccines = pygame.sprite.Group()
    hearts_all = pygame.sprite.Group()
    pups = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player1)
    break_start = pygame.time.get_ticks()
    shields = pygame.sprite.Group()
    text_images = pygame.sprite.Group()
    virus1_animations = pygame.sprite.Group()
    gui_elements = pygame.sprite.Group()


    virus = Virus(WIDTH, random.randint(0, HEIGHT - 32),game_state.virus_speed)  # 32 = Höhe deines Sprites
    #virus2 = Virus(WIDTH, random.randint(0, HEIGHT - 34),game_state.virus_speed*0.5)  # 32 = Höhe deines Sprites
    #virus = Virus(WIDTH, random.randint(0, HEIGHT - 32), game_state.virus_speed)  # 32 = Höhe deines Sprites
    #all_sprites.add(virus)
    #viruses.add(virus)

    #####################################################################################

    # Joystick-Support initialisieren
    pygame.joystick.init()
    gs.joysticks = []
    for i in range(pygame.joystick.get_count()):
        joy = pygame.joystick.Joystick(i)
        #joy.init()
        gs.joysticks.append(joy)
        #print(f"Joystick {i} bereit: {joy.get_name()}")
        #try:
        #    print("Haptic-Geräte:", pygame.haptic.get_count())
        #except AttributeError:
        #    print("Keine Haptic-Geräte")

    #print("Pygame-CE Version:", pygame.version.ver)
    #try:
    #    sdl = pygame.get_sdl_version()
    #except AttributeError:
    #    sdl = ("<2.0.0",)
    #print("SDL2 Version:", sdl)
    #print("Haptic-Attribute in pygame:", [a for a in dir(pygame) if "haptic" in a.lower()])

    #game_state.joysticks = joysticks

    #try:
    #    # Stärke: 0.0–1.0, Dauer in ms
    #    joy.rumble(1.0, 1.0, 500)
    #    print("Rumble ausgelöst!")
    #except Exception as e:
    #    print("Rumble fehlgeschlagen:", e)

    return (
        clock, game_state, gs, player1, back1, viruses1, viruses2, vaccines, hearts_all, pups, all_sprites, virus, screen, hit_sound,
        hit2_sound, shot_sound, oneup_sound, pup1_sound, pup2_sound, start_sound, explosions, virus1_animations, break_start, bosses, shields,
        text_images, gui_elements
    )

def check_input(
        player,gs
):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Pygame‐Module sauber schließen
            sys.exit()  # Python‐Programm beenden

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                player.SHOOT_KEY = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.LEFT_KEY = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.RIGHT_KEY = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.UP_KEY = True
                #print("up")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.DOWN_KEY = True
                #print("down")
            elif event.key == pygame.K_ESCAPE:
                gs.PAUSE_KEY = True
            elif event.key == pygame.K_LCTRL and not gs.pause_active :
                player.ACTION1_KEY = True
            elif event.key == pygame.K_LALT:
                player.ACTION2_KEY = True
            elif event.key == pygame.K_RETURN:
                player.ACTION3_KEY = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.UP_KEY = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.DOWN_KEY = False
            elif event.key == pygame.K_ESCAPE:
                gs.PAUSE_KEY = False
            elif event.key == pygame.K_SPACE:
                player.SHOOT_KEY = False
            elif event.key == pygame.K_LCTRL and not gs.pause_active:
                player.ACTION1_KEY = False
            elif event.key == pygame.K_LALT:
                player.ACTION2_KEY = False
            elif event.key == pygame.K_RETURN:
                player.ACTION3_KEY = False
                # Analog-Sticks / Achsen bewegen
        elif event.type == pygame.JOYAXISMOTION:
            joy_id = event.joy  # Index des Joysticks
            axis = event.axis  # Achse 0,1,2…
            value = event.value  # Float in [-1.0, +1.0]
             #z.B. nur X-Achse auswerten:
            if axis == 0:
                if abs(value) > 0.1:  # Dead-Zone
                    print(f"Joystick {joy_id} X = {value:.2f}")
                else:
                    print(f"Joystick {joy_id} X in Dead-Zone")

        # Buttons drücken
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.joy == 0 and event.button == 0:
                player.SHOOT_KEY = True
            elif event.joy == 0 and event.button == 2:
                player.ACTION1_KEY = True
                #print ("Action Key 1 pressed")
            elif event.joy == 0 and event.button == 1:
                player.ACTION2_KEY = True
                #print ("Action Key 2 pressed")
            elif event.joy == 0 and event.button == 3:
                player.ACTION3_KEY = True
                #print ("Action Key 3 pressed")
            elif event.joy == 0 and event.button == 11:
                player.UP_KEY = True
            elif event.joy == 0 and event.button == 12:
                player.DOWN_KEY = True
            elif event.joy == 0 and event.button == 13:
                player.LEFT_KEY = True
            elif event.joy == 0 and event.button == 14:
                player.RIGHT_KEY = True
            elif event.joy == 0 and event.button == 6:
                gs.PAUSE_KEY = True


        elif event.type == pygame.JOYBUTTONUP:
            if event.joy == 0 and event.button == 0:
                player.SHOOT_KEY = False
            elif event.joy == 0 and event.button == 2 and not gs.pause_active:
                player.ACTION1_KEY = False
            elif event.joy == 0 and event.button == 1:
                player.ACTION2_KEY = False
            elif event.joy == 0 and event.button == 3:
                player.ACTION3_KEY = False
            elif event.joy == 0 and event.button == 11:
                player.UP_KEY = False
            elif event.joy == 0 and event.button == 12:
                player.DOWN_KEY = False
            elif event.joy == 0 and event.button == 13:
                player.LEFT_KEY = False
            elif event.joy == 0 and event.button == 14:
                player.RIGHT_KEY = False
            elif event.joy == 0 and event.button == 6:
                gs.PAUSE_KEY = False
            #joy_id = event.joy
            #btn = event.button
            #print(f"Joystick {joy_id} Button {btn} up")

        elif event.type == pygame.JOYDEVICEADDED:
            for i in range(pygame.joystick.get_count()):
                joy = pygame.joystick.Joystick(i)
                #joy.init()
                gs.joysticks.append(joy)
                #print(f"Joystick {i} bereit: {joy.get_name()}")

        elif event.type == pygame.JOYDEVICEREMOVED:
            for i in range(pygame.joystick.get_count()):
                joy = pygame.joystick.Joystick(i)
                #joy.init()
                gs.joysticks.append(joy)
                #print(f"Joystick {i} bereit: {joy.get_name()}")

        # D-Pad (Hat) bewegen
        elif event.type == pygame.JOYHATMOTION:
            joy_id = event.joy
            hat_index = event.hat  # meistens 0, wenn nur ein D-Pad vorhanden
            x, y = event.value  # x,y ∈ {-1,0,+1}
            #print(f"Joystick {joy_id} Hat {hat_index} = {event.value}")
            if x == -1:
                player.LEFT_KEY = True
                player.RIGHT_KEY = False

            elif x == 1:
                player.RIGHT_KEY = True
                player.LEFT_KEY = False
            elif x==0:
                player.LEFT_KEY = False
                player.RIGHT_KEY = False

            if y == 1:
                player.UP_KEY = True
                player.DOWN_KEY = False
            elif y == -1:
                player.DOWN_KEY = True
                player.UP_KEY = False
            elif y == 0:
                player.UP_KEY = False
                player.DOWN_KEY = False



def main():
    outer = True
    while outer:

        (clock,game_state,gs,player,back1,viruses1, viruses2,vaccines,hearts_all,pups,all_sprites,virus,
         screen,hit_sound,hit2_sound,shot_sound,oneup_sound,pup1_sound,pup2_sound,start_sound,explosions,virus1_animations, break_start,bosses,shields,
         text_images,gui_elements
         )  = init()

        #=Show Menu##########################################################################
        Title_Screen(Title,game_surface,screen,Version,gui_elements, player, gs, shot_sound, fanfare_sound)
        #start_time = pygame.time.get_ticks() / 1000
        game_state.last_shot_time = 0
        game_state.last_pup_spawn = 0
        level_start = 0
        break_start = 0
        #pup_timer = 0
        #pup_timer_interval = 10
        #pup_timer_blink = 3
        game_time = 0
        dt_game = 0

        ################################# GAME LOOP ##########################
        first= True
        gs.start_rumble = game_time
        gs.start_active = True

        Start_Menu(gui_elements, player, gs, shot_sound, fanfare_sound, screen)

        while gs.running:

            #  1=Timing================================
            dt = clock.tick(FPS) / 1000
            if first:
                dt = 0
                game_time += dt
                first = False
            if not gs.pause_active or not gs.start_active:
                game_time += dt
                dt_game = dt

            #print(f"Game time: {game_time}")

            ################################# CHECK PLAYER INPUT #################################

            check_input(
                player,gs
            )
            if not gs.pause_active or not gs.start_active:
                player.update(dt,game_state,game_time)

            #3=Logic==================================
# Wave beenden ###########################################################################################
            if not gs.pause_active or not gs.start_active:
#                now = pygame.time.get_ticks()
                if game_time - level_start > gs.wave_time and gs.level_active and not gs.boss_level:
                    gs.new_viruses = False
                    gs.level_break, gs.level_active = True, False
                    #print("wave ends")
# LEVELPAUSE Beginnt#####################################################################################
            if not gs.pause_active or not gs.start_active:
                if gs.level_break and len(viruses1) <= 0 and len(viruses2) <= 0:
                    if not   gs.all_death:
                        gs.all_death = True
                        break_start = game_time
                        level_complete_sound.play()
                        gs.points += 15 * gs.level
                        logic.points_highscore_life(gs, oneup_sound, hs_sound, player)
                        #if gs.shield_active:
                        #    gs.energy_level += gs.breaktime / 1000

# LEVELPAUSE Vorbei#####################################################################################
            if not gs.pause_active or not gs.start_active:
                if game_time - break_start > gs.breaktime and gs.level_break and gs.all_death and not gs.boss_level:
                    gs.virus_speed += gs.virus_speed_increase
                    gs.new_viruses = True
                    gs.level_break, gs.level_active = False, True
                    level_start = game_time
                    gs.all_death = False
                    next_level_sound.play()
                    gs.level += 1

                    if gs.level % 5 == 0:
                        gs.max_virus_spawn += 1
                        gs.virus2_freq *= .95
                        gs.boss_level = True
                        boss_level_background_music.play(loops=-1)

                update_game(
                    viruses1, viruses2, vaccines, game_state, hearts_all,
                    dt, pups, explosions, virus1_animations, bosses,
                    gs, player, shields,game_time,sparks
                )

            action(
                game_state, vaccines,Vaccine,player,all_sprites,shot_sound,gs,game_time,shields,sparks,
                pause_sound,unpause_sound,gui_elements,fanfare_sound,screen
            )
            if not gs.pause_active or not gs.start_active:
                handle_collisions(
                    player,vaccines,viruses1, viruses2,hit_sound,hit2_sound,game_state,oneup_sound,
                    pups,pup2_sound,gs,hs_sound,explosions, virus1_animations,bosses,shields, all_sprites,game_time,boss_level_background_music,
                    boss_explosion,swoosh,shield_hit_sound
                )
               # now=pygame.time.get_ticks()

                spawn_virus(
                    viruses1,viruses2, all_sprites, game_state, pups, game_time,pup1_sound,gs,player,bosses,dt_game
                )

                if game_state.respawn:
#                   #now = game_time
                    if game_time - game_state.respawn_start > 3:  #3 Sekunden
                        game_state.respawn = False
                        # Alle Viren „aufwecken“
                 #       game_state.virus_speed = game_state.speed_restore
                 #       for virus in viruses1:
                 #           virus.speed = game_state.virus_speed
                 #       for virus in viruses2 :
                 #           virus.speed = game_state.virus_speed

            #6=Drawing=================================
            #screen.fill((30, 144, 255))
            energy_text = EnergyTXT(5, 14)
            damage_text = DamageTXT(77, 14)
            text_images.add(energy_text, damage_text)
            draw_game(
                game_surface,all_sprites,screen,hearts_all,game_state,viruses1, viruses2,back1,explosions,
                virus1_animations,text_images,gui_elements
            )

            if gs.game_over:
                g_o = Game_Over()
                g_o.draw(game_surface)
                if boss_level_background_music:
                    boss_level_background_music.fadeout(3000)

                #scaled = pygame.transform.scale(game_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
                screen.blit(game_surface, (0, 0))
                pygame.display.flip()
                if gs.new_high_score:
                    save_high_score(gs.high_score)
                    fanfare_sound.play()
                else:
                    game_over_sound.play()
                game_over_ext()

                gs.running = False

if __name__ == "__main__":
    main()
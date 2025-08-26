import pygame

from asset_loader import AssetLoader
#import main
from highscore import save_high_score
#from settings import *
import sys
from text_image import QuitGUI,ResumeGUI,FullscreenGUI,SettingsGUI, ResolutionGUI, SelectorGUI,RestartGUI
from config   import CONFIG, compute_flags, save_config
from settings import WIDTH, HEIGHT

def Title_Screen(Title,game_surface,screen,Version,gui_elements, player, gs, shot_sound, fanfare_sound):
    start_sound = AssetLoader.load_sound("assets/sounds/df_start_snd.ogg")
    title = Title()
    version = Version()

    title.draw(game_surface)
    version.draw(game_surface)
    #scaled_surface = pygame.transform.scale(game_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    screen.blit(game_surface, (0, 0))

    pygame.display.flip()

    # Warten bis eine Taste gedrückt wird
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    start_sound.play()

            elif event.type == pygame.JOYBUTTONDOWN:
                    if event.joy == 0 and event.button == 6:
                        waiting = False
                        start_sound.play()

        pygame.display.flip()
    Start_Menu(gui_elements, player, gs, shot_sound, fanfare_sound, screen)

def Pause_Menu(gui_elements,player,gs,shot_sound, fanfare_sound,screen):
    #print("pause mode on")
    gui_x = 5
    gui_y = 31
    gui_y_increment = 19
    resume = ResumeGUI(gui_x, gui_y_increment * 1 + gui_y)
    restart = RestartGUI(gui_x, gui_y_increment * 2 + gui_y)
    quit = QuitGUI(gui_x, gui_y_increment * 3 + gui_y)
    settings = SettingsGUI(gui_x, gui_y_increment * 4 + gui_y)
    fullscreen = FullscreenGUI(gui_x, gui_y_increment * 5 + gui_y)
    resolution = ResolutionGUI(gui_x, gui_y_increment * 6 + gui_y)
    selector = SelectorGUI(gui_x, gui_y_increment * gs.selector_position + gui_y)
    gui_elements.add(resume,restart, quit, fullscreen,settings, resolution, selector)

    if player.UP_KEY and gs.selector_position > 1 and gs.selector_position <=5:
        gs.selector_position -= 1
        if gs.selector_position == 4:
            gs.selector_position -= 1
        #print("selector_position",gs.selector_position)
        player.UP_KEY = False
    elif player.DOWN_KEY and gs.selector_position >= 1 and gs.selector_position < 5:
        gs.selector_position += 1
        if gs.selector_position == 4:
            gs.selector_position += 1
        #print("selector_position",gs.selector_position)
        player.DOWN_KEY = False
    elif player.SHOOT_KEY or player.ACTION3_KEY:
        shot_sound.play()
        if gs.selector_position == 1:
            gs.pause_active = False
            for sprite in gui_elements:
                sprite.kill()
        elif gs.selector_position == 2:
            for sprite in gui_elements:
                sprite.kill()
            gs.running = False

            gs.pause_active = False
        elif gs.selector_position == 3:
            if gs.new_high_score:
                save_high_score(gs.high_score)
                fanfare_sound.play()
            pygame.quit()  # Pygame‐Module sauber schließen
            sys.exit()  # Python‐Programm beenden
        elif gs.selector_position == 4:
            pass
        elif gs.selector_position == 5:
            # Fullscreen toggeln
            CONFIG["fullscreen"] = not CONFIG["fullscreen"]
            save_config(CONFIG)

            # neuen Modus setzen
            flags = compute_flags(CONFIG)
            screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        elif gs.selector_position == 5:
            pass
        player.SHOOT_KEY = False
        player.ACTION3_KEY = False

        return screen

def Start_Menu(gui_elements, player, gs, shot_sound, fanfare_sound, screen):
    # print("pause mode on")

    gui_x = 5
    gui_y = 31
    gui_y_increment = 19
    resume = ResumeGUI(gui_x, gui_y_increment * 1 + gui_y)
    restart = RestartGUI(gui_x, gui_y_increment * 2 + gui_y)
    quit = QuitGUI(gui_x, gui_y_increment * 3 + gui_y)
    settings = SettingsGUI(gui_x, gui_y_increment * 4 + gui_y)
    fullscreen = FullscreenGUI(gui_x, gui_y_increment * 5 + gui_y)
    resolution = ResolutionGUI(gui_x, gui_y_increment * 6 + gui_y)
    selector = SelectorGUI(gui_x, gui_y_increment * gs.selector_position + gui_y)
    gui_elements.add(resume, restart, quit, fullscreen, settings, resolution, selector)

    if player.UP_KEY and gs.selector_position > 1 and gs.selector_position <= 5:
        gs.selector_position -= 1
        if gs.selector_position == 4:
            gs.selector_position -= 1
        # print("selector_position",gs.selector_position)
        player.UP_KEY = False
    elif player.DOWN_KEY and gs.selector_position >= 1 and gs.selector_position < 5:
        gs.selector_position += 1
        if gs.selector_position == 4:
            gs.selector_position += 1
        # print("selector_position",gs.selector_position)
        player.DOWN_KEY = False
    elif player.SHOOT_KEY or player.ACTION3_KEY:
        shot_sound.play()
        if gs.selector_position == 1:
            gs.pause_active = False
            for sprite in gui_elements:
                sprite.kill()
        elif gs.selector_position == 2:
            for sprite in gui_elements:
                sprite.kill()
            gs.running = False

            gs.pause_active = False
        elif gs.selector_position == 3:
            if gs.new_high_score:
                save_high_score(gs.high_score)
                fanfare_sound.play()
            pygame.quit()  # Pygame‐Module sauber schließen
            sys.exit()  # Python‐Programm beenden
        elif gs.selector_position == 4:
            pass
        elif gs.selector_position == 5:
            # Fullscreen toggeln
            CONFIG["fullscreen"] = not CONFIG["fullscreen"]
            save_config(CONFIG)

            # neuen Modus setzen
            flags = compute_flags(CONFIG)
            screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        elif gs.selector_position == 5:
            pass
        player.SHOOT_KEY = False
        player.ACTION3_KEY = False

        return screen
#return(title)
import pygame
import sys

def game_over_ext():
    # """Wartet auf beliebige Taste."""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit();
                    sys.exit()

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.joy == 0 and event.button == 6:
                    waiting = False
                elif event.joy == 0 and event.button == 4:
                    pygame.quit();
                    sys.exit()

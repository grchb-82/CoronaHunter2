import pygame
import math
from settings import *
from num import Number
from num import draw_number


def draw_game(
        game_surface, all_sprites, screen, hearts_all, game_state, viruses1,viruses2, back1, explosions,
        viruses1_animations, text_images,gui_elements
):
    # Hintergrund und Objekte auf dem internen Surface zeichnen

    if game_state.game_over:
        viruses1.empty()
        viruses2.empty()
        for virus in viruses1:
            virus.kill()
        for virus in viruses2:
            virus.kill()

    back1.draw(game_surface)

    for sprite in all_sprites:
        # Nur zeichnen, wenn sichtbar (für den Player)
        if hasattr(sprite, 'visible') and not sprite.visible:
            continue
        game_surface.blit(sprite.image, sprite.rect)

    hearts_all.draw(game_surface)
    explosions.draw(game_surface)
    viruses1_animations.draw(game_surface)
    text_images.draw(game_surface)

    def draw_score(points, surface):
        number_group = pygame.sprite.Group()
        spacing = 11
        x_start = WIDTH - ((spacing * 6) + 5)
        y_start = 1

        point_str = str(points).zfill(6)  # führende Nullen (optional)

        for i, digit in enumerate(point_str):
            x = x_start + i * spacing
            number = Number(digit, x, y_start)
            number_group.add(number)

        number_group.draw(surface)

    draw_score(game_state.points, game_surface)

    def draw_highscore(high_score, surface):
        number_group = pygame.sprite.Group()
        spacing = 11
        x_start = WIDTH - ((spacing * 6) + 5 + 110)
        y_start = 1

        hs_str = str(high_score).zfill(6)  # führende Nullen (optional)

        for i, digit in enumerate(hs_str):
            x = x_start + i * spacing
            number = Number(digit, x, y_start)
            number_group.add(number)
        number_group.draw(surface)

    def draw_level(game_state, surface):
        number_group = pygame.sprite.Group()
        spacing = 11
        x_start = WIDTH - ((spacing * 6) + 5 + 30)
        y_start = 1

        hs_str = str(game_state.level).zfill(2)  # führende Nullen (optional)

        for i, digit in enumerate(hs_str):
            x = x_start + i * spacing
            number = Number(digit, x, y_start)
            number_group.add(number)

        number_group.draw(surface)

    def draw_pause_menu(game_state, surface,gui_elements):
        if game_state.pause_active:
            gui_elements.draw(surface)



    draw_pause_menu(game_state, game_surface,gui_elements)


    draw_number(game_surface, math.ceil(game_state.energy_level), 46, 14)
    draw_number(game_surface, math.ceil(game_state.damage), 117, 14)

    draw_highscore(game_state.high_score, game_surface)
    draw_level(game_state, game_surface)
    # Surface vergrößern und auf das eigentliche Fenster zeichnen
    #scaled_surface = pygame.transform.scale(game_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    screen.blit(game_surface, (0, 0)),


    pygame.display.flip()

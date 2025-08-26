import random
import pygame

from menu import Pause_Menu
from pup import pup_ammo
from settings import *
from virus import Virus, Virus2, Boss_Virus_10, Virus1_Animation
from explosion import Explosion
from hearts import Hearts5, Hearts4, Hearts3, Hearts2, Hearts1, Hearts0
from hearts import Hearts43, Hearts33, Hearts23, Hearts13, Hearts03
from hearts import Hearts46, Hearts36, Hearts26, Hearts16, Hearts06
from player import Shield


def points_highscore_life(gs, oneup_sound, hs_sound, player):
    if player.life_no < gs.MAX_LIFE and gs.points >= gs.life_milestone:
        player.life_no += 1
        gs.life_milestone += gs.life_milestone_intervall
        gs.life_milestone_intervall *= 1.5
        oneup_sound.play()
    if player.life_no > gs.MAX_LIFE:
        player.life_no = gs.MAX_LIFE
    if gs.points >= gs.high_score and not gs.new_high_score:
        gs.high_score = gs.points
        gs.new_high_score = True
        hs_sound.play()
    if gs.points >= gs.high_score:
        gs.high_score = gs.points
def hearts_display(hearts_all,player,game_state):
    hearts_all.empty()
    if 4.5 < player.life_no <= 5:
        hearts_all.add(Hearts5(5, 1))
    elif 4.2 < player.life_no <= 4.5:
        hearts_all.add(Hearts46(5, 1))
    elif 4 < player.life_no <= 4.2:
        hearts_all.add(Hearts43(5, 1))

    elif 3.5 < player.life_no <= 4:
        hearts_all.add(Hearts4(5, 1))
    elif 3.2 < player.life_no <= 3.5:
        hearts_all.add(Hearts36(5, 1))
    elif 3 < player.life_no <= 3.2:
        hearts_all.add(Hearts33(5, 1))

    elif 2.5 < player.life_no <= 3:
        hearts_all.add(Hearts3(5, 1))
    elif 2.2 < player.life_no <= 2.5:
        hearts_all.add(Hearts26(5, 1))
    elif 2 < player.life_no <= 2.2:
        hearts_all.add(Hearts23(5, 1))

    elif 1.5 < player.life_no <= 2:
        hearts_all.add(Hearts2(5, 1))
    elif 1.2 < player.life_no <= 1.5:
        hearts_all.add(Hearts16(5, 1))
    elif 1 < player.life_no <= 1.2:
        hearts_all.add(Hearts13(5, 1))

    elif 0.5 < player.life_no <= 1:
        hearts_all.add(Hearts1(5, 1))
    elif 0.2 < player.life_no <= 0.5:
        hearts_all.add(Hearts06(5, 1))
    elif 0 < player.life_no <= 0.2:
        hearts_all.add(Hearts03(5, 1))

    elif player.life_no <= 0:
        hearts_all.add(Hearts0(5, 1))
        game_state.game_over = True
def update_game(viruses1, viruses2, vaccines, game_state, hearts_all,dt_game,pups,explosions,virus1_animations, bosses,gs,player,shields,game_time,sparks):
    viruses1.update(game_state,dt_game,player)
    viruses2.update(game_state,dt_game,player)
    vaccines.update(dt_game)
    pups.update(dt_game,game_state,game_time)
    explosions.update()
    virus1_animations.update()
    shields.update(dt_game,game_time,game_state)

    if gs.boss_level:
        for boss in bosses:
            max_dist = boss.speed * dt_game
            boss.move_to(gs, max_dist,dt_game,player)
            boss.rect.center = boss.pos

    hearts_display(hearts_all,player,game_state)

    #print(f"Now:{pygame.time.get_ticks() / 1000}")
    #print(f"Shields:{gs.energy_level}")
    if gs.shield_active and gs.level_active:
        gs.energy_level -= dt_game
    if gs.boost_active and gs.level_active:
        gs.energy_level -= dt_game/1.5
    if gs.energy_level <= 0 and gs.boost_active:
        gs.energy_level = 0
        gs.boost_active = False
    if gs.energy_level <= 0 and gs.shield_active:
        for shield in shields:
            shield.kill()
            sparks.fadeout(500)
        gs.shield_active = False
        gs.shield_blink = False
#        game_state.energy_level = 3
    if gs.energy_level  <= 1.5 and gs.shield_active:
        #print("Blinken")
        #print(f"gs.shield_blink {gs.shield_blink}")
        gs.shield_blink = True

    if gs.pup_timer_visible <= 0 and gs.pup_active:
        for pup in pups:
            pup.kill()
            gs.pup_active = False
            gs.pup_blink = False
    if gs.pup_timer_visible <= 1.5 and gs.pup_active:
        gs.pup_blink = True

    if gs.boost_active:
        pass

    elif not gs.boost_active:
        pass

def virus1_kill(
        virus, hit_sound, game_state, gs, oneup_sound, hs_sound, player, virus1_animations
    ):
    if virus.v_life <= 0:
        virus.kill()
        hit_sound.play()
        game_state.points += int(virus.basepoints * ((gs.virus_speed) * 0.1))
        points_highscore_life(gs, oneup_sound, hs_sound, player)
        virus1_animation_pos_x = virus.rect.x + 16
        virus1_animation_pos_y = virus.rect.y + 16
        virus1_animation = Virus1_Animation(virus1_animation_pos_x, virus1_animation_pos_y)
        virus1_animations.add(virus1_animation)
        for idx, joy in enumerate(gs.joysticks):
            # z. B. für Controller 0 einen kurzen Rumble:
            if idx == 0:
                joy.rumble(1, 0, 100)

def boss_kill(boss, boss_explosion, boss_level_backmuc, explosions, game_state, gs, oneup_sound, hs_sound, player):
    if boss.v_life <= 0:
        boss.kill()
        boss_explosion.play()
        boss_level_backmuc.fadeout(5000)
        explosion_pos_x = boss.rect.x + 32
        explosion_pos_y = boss.rect.y + 32
        explosion = Explosion(explosion_pos_x, explosion_pos_y)
        explosions.add(explosion)
        explosion_pos_x = boss.rect.x + 16
        explosion_pos_y = boss.rect.y + 16
        explosion = Explosion(explosion_pos_x, explosion_pos_y)
        explosions.add(explosion)
        explosion_pos_x = boss.rect.x + 48
        explosion_pos_y = boss.rect.y + 16
        explosion = Explosion(explosion_pos_x, explosion_pos_y)
        explosions.add(explosion)
        explosion_pos_x = boss.rect.x + 48
        explosion_pos_y = boss.rect.y + 48
        explosion = Explosion(explosion_pos_x, explosion_pos_y)
        explosions.add(explosion)
        explosion_pos_x = boss.rect.x + 16
        explosion_pos_y = boss.rect.y + 48
        explosion = Explosion(explosion_pos_x, explosion_pos_y)
        explosions.add(explosion)
        game_state.points += int(boss.basepoints * ((gs.virus_speed) * 0.1))
        gs.boss_hp *= 1.25
        gs.boss_level = False
        gs.new_viruses = False
        gs.level_break, gs.level_active = True, False
        points_highscore_life(gs, oneup_sound, hs_sound, player)
        gs.life_milestone_intervall = int(gs.life_milestone_intervall * 1.33)
        for idx, joy in enumerate(gs.joysticks):
            # z. B. für Controller 0 einen kurzen Rumble:
            if idx == 0:
                joy.rumble(1, 1, 1000)

def handle_collisions(
        player, vaccines, viruses1, viruses2, hit_sound,hit2_sound,game_state,oneup_sound, pups,pup2_sound,gs,hs_sound,
        explosions, virus1_animations, bosses,shields, all_sprites,game_time,boss_level_backmuc, boss_explosion,swoosh,shield_hit_sound
):
    for vaccine in list(vaccines):
        hits = pygame.sprite.spritecollide(vaccine, viruses1, False, pygame.sprite.collide_mask)
        if not hits:
            continue
        vaccine.kill()
        swoosh.play()
        for virus in hits:
            if hits:
                virus.v_life -= gs.damage

                virus1_kill(virus, hit_sound, game_state, gs, oneup_sound, hs_sound, player, virus1_animations)

    if not game_state.respawn:
        for shield in list(shields):
            hits3 = pygame.sprite.spritecollide(shield, viruses1, False ,pygame.sprite.collide_mask)
            if not hits3:
                continue
            gs.energy_level -= 1
            shield_hit_sound.play()
            for virus in hits3:
                if hits3:
                    virus.v_life -= 5

                    virus1_kill(virus, hit_sound, game_state, gs, oneup_sound, hs_sound, player, virus1_animations)

            for virus in hits3:
                virus.collide_shield(shield)

    for vaccine in list(vaccines):
        hits = pygame.sprite.spritecollide(vaccine, viruses2, False, pygame.sprite.collide_mask)
        if not hits:
            continue
        vaccine.kill()
        swoosh.play()
        for virus in hits:
            if hits:
                virus.v_life -= gs.damage

                if virus.v_life <= 0:
                    virus.kill()
                    hit_sound.play()

                    game_state.points += int(virus.basepoints * ((gs.virus_speed) * 0.1))
                    points_highscore_life(gs, oneup_sound, hs_sound, player)
                    explosion_pos_x = virus.rect.x + 16
                    explosion_pos_y = virus.rect.y + 16
                    explosion = Explosion(explosion_pos_x, explosion_pos_y)
                    explosions.add(explosion)

    if not game_state.respawn:
        for shield in list(shields):
            hits3 = pygame.sprite.spritecollide(shield, viruses2, False, pygame.sprite.collide_mask)
            if not hits3:
                continue
            gs.energy_level -= 1
            shield_hit_sound.play()

            for virus in hits3:
                if hits3:
                    virus.v_life -= 5

                    if virus.v_life <= 0:
                        virus.kill()
                        hit_sound.play()

                        game_state.points += int(virus.basepoints * ((gs.virus_speed) * 0.1))
                        points_highscore_life(gs, oneup_sound, hs_sound, player)
                        explosion_pos_x = virus.rect.x + 16
                        explosion_pos_y = virus.rect.y + 16
                        explosion = Explosion(explosion_pos_x, explosion_pos_y)
                        explosions.add(explosion)

            for virus in hits3:
                virus.collide_shield(shield)

    if not game_state.respawn:
        for shield in list(shields):
            hits4 = pygame.sprite.spritecollide(shield, bosses, False, pygame.sprite.collide_mask)
            if not hits4:
                continue
            gs.energy_level -= 1
            shield_hit_sound.play()
            for boss in hits4:
                if hits4:
                    boss.v_life -= 5
                    boss_kill(boss, boss_explosion, boss_level_backmuc, explosions, game_state, gs, oneup_sound,
                              hs_sound, player)

            for boss in hits4:
                boss.collide_shield(shield)

    for vaccine in list(vaccines):
        hits2 = pygame.sprite.spritecollide(vaccine, bosses, False, pygame.sprite.collide_mask)
        if not hits2:
            continue
        vaccine.kill()
        swoosh.play()
        for boss in hits2:
            if hits2:
                boss.v_life -= gs.damage
                boss_kill(boss, boss_explosion, boss_level_backmuc, explosions, game_state, gs, oneup_sound, hs_sound, player)

    if not game_state.respawn and not gs.shield_active:
        if pygame.sprite.spritecollide(player, viruses1, True, pygame.sprite.collide_mask):
            hit2_sound.play()
            explosion_pos_x = player.rect.x+15
            explosion_pos_y = player.rect.y+7

            for idx, joy in enumerate(gs.joysticks):
                # z. B. für Controller 0 einen kurzen Rumble:
                if idx == 0:
                    joy.rumble(0, 1, 500)

            explosion = Explosion(explosion_pos_x,explosion_pos_y)
            explosions.add(explosion)
            game_state.respawn = True
            game_state.respawn_start = game_time
            player.life_no -= 1
            game_state.ammo_type = 1
            game_state.shot_frequency = .300
            game_state.max_shots = 2
            gs.damage = gs.damage_default
            game_state.vacc_speed = gs.vacc_speed_default
            game_state.dual_shot = False
            game_state.speed_restore = game_state.virus_speed
        if pygame.sprite.spritecollide(player, viruses2, True, pygame.sprite.collide_mask):
            hit2_sound.play()
            for idx, joy in enumerate(gs.joysticks):
                # z. B. für Controller 0 einen kurzen Rumble:
                if idx == 0:
                    joy.rumble(0, 1, 500)
            explosion_pos_x = player.rect.x+15
            explosion_pos_y = player.rect.y+7
            explosion = Explosion(explosion_pos_x,explosion_pos_y)
            explosions.add(explosion)
            game_state.respawn = True
            game_state.respawn_start = game_time
            player.life_no -= 1
            game_state.ammo_type = 1
            game_state.shot_frequency = .300
            game_state.max_shots = 2
            gs.damage = gs.damage_default
            game_state.vacc_speed = gs.vacc_speed_default
            game_state.dual_shot = False
            game_state.speed_restore = game_state.virus_speed

        elif pygame.sprite.spritecollide(player, bosses, False, pygame.sprite.collide_mask):
            hit2_sound.play()
            for idx, joy in enumerate(gs.joysticks):
                # z. B. für Controller 0 einen kurzen Rumble:
                if idx == 0:
                    joy.rumble(0, 1, 500)
            explosion_pos_x = player.rect.x + 15
            explosion_pos_y = player.rect.y + 7
            explosion = Explosion(explosion_pos_x, explosion_pos_y)
            explosions.add(explosion)
            game_state.respawn = True
            game_state.respawn_start = game_time
            player.life_no -= 1
            for boss in bosses:
                boss.v_life -= 25
                #print (f"Boss life is {boss.v_life}")
            game_state.ammo_type = 1
            game_state.shot_frequency = .300
            game_state.max_shots = 2
            gs.damage = gs.damage_default
            game_state.vacc_speed = gs.vacc_speed_default
            game_state.dual_shot = False
            game_state.speed_restore = game_state.virus_speed

            for virus in viruses1:
                virus.speed = game_state.speed_safe
            for virus in viruses2:
                virus.speed = game_state.speed_safe

    hits = pygame.sprite.spritecollide(player, pups, True)  # True → entferne getroffenen Pup
    for pup in hits:
        if pup.pup_type == 1 :
            if not game_state.dual_shot:
                game_state.vacc_speed *= 1.1
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            game_state.dual_shot = False

        elif pup.pup_type == 2 :
            if game_state.dual_shot:
                game_state.vacc_speed *= 1.1
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            game_state.dual_shot = True

        elif pup.pup_type == 3:
            if gs.ammo_type == 3:
                gs.damage *= 1.05
                game_state.shot_frequency *= 0.9
                game_state.max_shots *= 1.1
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            elif gs.ammo_type != 3:
                gs.damage = 8
                game_state.shot_frequency = .050
                game_state.max_shots = 2
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            game_state.ammo_type = 3

        elif pup.pup_type == 4:
            if gs.ammo_type == 4:
                gs.damage *= 1.075
                game_state.shot_frequency *= 0.975
                game_state.max_shots *= 1.1
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            elif gs.ammo_type != 4:
                gs.damage = 10
                game_state.shot_frequency = .150
                game_state.max_shots = 4
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            game_state.ammo_type = 4

        elif pup.pup_type == 5:
            if gs.ammo_type == 5:
                gs.damage *= 1.1
                game_state.shot_frequency *= 0.95
                game_state.max_shots *= 1.1
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            elif gs.ammo_type != 5:
                gs.damage = 12
                game_state.shot_frequency = .250
                game_state.max_shots = 6
                #print(gs.damage)
                #print(gs.shot_frequency)
                #print(gs.max_shots)
            game_state.ammo_type = 5

        elif pup.pup_type == 6:
            #if len(shields) <=0 and not gs.shield_active:
            #    gs.energy_level = gs.additional_energy
            #    shield = Shield(player,game_state)
            #    gs.shield_active = True
            #    all_sprites.add(shield)
            #    shields.add(shield)
            #else:
            game_state.energy_level += gs.additional_energy

        pup2_sound.play()
        gs.pup_active = False
        gs.pup_blink = False

    for vaccine in vaccines:
        hits = pygame.sprite.spritecollide(vaccine, pups, False, pygame.sprite.collide_mask)

        if hits:
            vaccine.kill()
            swoosh.play()
            for pup in pups:
                pup.life -= 1
                if pup.life == 0:
                    pup.kill()
                    hit2_sound.play()
                    gs.pup_active = False
                    gs.points += gs.level*80
                    points_highscore_life(gs, oneup_sound, hs_sound, player)
                    for idx, joy in enumerate(gs.joysticks):
                        # z. B. für Controller 0 einen kurzen Rumble:
                        if idx == 0:
                            joy.rumble(0, 1, 100)

def action(
        game_state, vaccines,Vaccine,player,all_sprites,shot_sound,gs,game_time,shields,sparks,pause_sound,
        unpause_sound,gui_elements,fanfare_sound,screen
):

    if gs.pause_active:
        Pause_Menu(gui_elements, player,gs,shot_sound, fanfare_sound,screen)
    #print(f"game time: {game_time}")
    #print(f"game state.last_shot_time: {game_state.last_shot_time}")
    # print(f"game state.shot_frequency: {game_time - game_state.shot_frequency}")
    if (game_time - game_state.last_shot_time) >= game_state.shot_frequency and player.SHOOT_KEY and not gs.pause_active:
        #print(f"game time: {game_time}")
        #print(f"game state.last_shot_time: {game_state.last_shot_time}")
        #   print(f"game state.shot_frequency: {game_time-game_state.shot_frequency}")
        if len(vaccines) <= game_state.max_shots - 1:
            if game_state.dual_shot:
                vaccine = Vaccine(player.rect.right, player.rect.centery + 5, game_state)
                vaccines.add(vaccine)
                all_sprites.add(vaccine)
                vaccine = Vaccine(player.rect.right, player.rect.centery - 5, game_state)
                vaccines.add(vaccine)
                all_sprites.add(vaccine)

                shot_sound.play()
                game_state.last_shot_time = game_time
                player.SHOOT_KEY = False
            else:
                vaccine = Vaccine(player.rect.right, player.rect.centery, game_state)
                vaccines.add(vaccine)
                all_sprites.add(vaccine)

                shot_sound.play()
                game_state.last_shot_time = game_time
                player.SHOOT_KEY = False

    if gs.PAUSE_KEY:
        if not gs.pause_active:
            gs.pause_active = True
            pause_sound.play()
            gs.PAUSE_KEY = False

            gs.selector_position = 1


        else:
            gs.pause_active = False
            gs.PAUSE_KEY = False
            unpause_sound.play()
            #print("pause mode off")
            for sprite in gui_elements:
                sprite.kill()

    elif player.ACTION1_KEY:
        if not gs.shield_active and gs.energy_level > 0:
            shield = Shield(player)
            sparks.play(loops=-1)
            gs.shield_active = True
            all_sprites.add(shield)
            shields.add(shield)
            player.ACTION1_KEY = False
        else:
            for shield in shields:
                shield.kill()
                sparks.fadeout(1000)
            gs.shield_active = False
            #gs.shield_blink = False
            player.ACTION1_KEY = False
    elif player.ACTION2_KEY:
        if gs.energy_level > 0:
            gs.boost_active = True

    elif not player.ACTION2_KEY:
        gs.boost_active = False

    elif player.ACTION3_KEY:
        if gs.energy_level > 0 and not gs.boost_active:
            gs.boost_active = True
            player.velocity.y += 500

    elif not player.ACTION3_KEY and gs.boost_active:
        if gs.energy_level > 0 and not gs.boost_active:
            gs.boost_active = False
            player.velocity.y -= 500

def spawn_virus(
        viruses1,viruses2, all_sprites , game_state, pups, game_time,pup1_sound,gs,player,bosses,dt
):
    #print(f"gs.energy_level: {gs.energy_level}")
    if not gs.boss_level and not gs.level_break:
        # Pup spawnt alle 60 Sekunden
        if gs.pup_active:
            gs.pup_timer_visible -= dt
            #print(f"gs.pup_timer_visible: {gs.pup_timer_visible}")
        if game_time - game_state.last_pup_spawn > gs.pup_frequency:
            #print("game time: " + str(game_time))
            if len(pups) <= 0:
                game_state.pup_type = random.randint(gs.pup_from, gs.pup_to )
                new_pup = pup_ammo(WIDTH, random.randint(20, HEIGHT - 32), game_state.pup_speed, game_state)
                gs.pup_active = True
                gs.pup_timer_visible =  gs.pup_timer_visible_default
                #gs.pup_timer_visible = gs.pup_timer_visible_default
                #print(f"pup_timer_visible: {gs.pup_timer_visible}")
                pup1_sound.play()
                all_sprites.add(new_pup)
                pups.add(new_pup)
                game_state.last_pup_spawn = game_time  # Zeitstempel aktualisieren
            else:
                pass
        if len(viruses1) <= game_state.max_virus_spawn-1:
           # now=pygame.time.get_ticks()
            if game_time - gs.last_virus_spawn >= gs.virus_freq and gs.new_viruses:
                new_virus = Virus(WIDTH, random.randint(20, HEIGHT - 32), game_state.virus_speed)
                all_sprites.add(new_virus)
                viruses1.add(new_virus)
                gs.last_virus_spawn = game_time

#        now=pygame.time.get_ticks()
        if game_time - gs.last_virus2_spawn >= gs.virus2_freq and gs.new_viruses:
            new_virus = Virus2(WIDTH, random.randint(20, HEIGHT - 34), game_state.virus_speed*0.8)
            all_sprites.add(new_virus)
            viruses2.add(new_virus)
            gs.last_virus2_spawn = game_time

    elif gs.boss_level:

#        now=pygame.time.get_ticks()

        if len(bosses) <= 0 and gs.new_viruses:
            #if now - gs.last_virus2_spawn >= gs.virus2_freq and gs.new_viruses:
            boss = Boss_Virus_10(WIDTH, random.randint(20+32, HEIGHT - 32), game_state.virus_speed*0.5,gs)
            #gs.new_viruses = True
            all_sprites.add(boss)
            bosses.add(boss)
            gs.target_pos = player.player_pos
        if game_time - gs.last_virus2_spawn >= 3 and len(viruses2) <= gs.level/5 and gs.new_viruses:
            new_virus = Virus2(WIDTH, random.randint(20, HEIGHT - 34), game_state.virus_speed*0.8)
            all_sprites.add(new_virus)
            viruses2.add(new_virus)
            gs.last_virus2_spawn = game_time
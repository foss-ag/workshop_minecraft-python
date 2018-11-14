import pygame
import math
import time
from ColorGenerator import ColorGenerator
from Bullet import Bullet
from GameState import GameState
from Astroid import Astroid
from Player import Player

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
s_shoot_timer = time.time()

state = GameState()
player = Player(500, 400)
color_generator = ColorGenerator()


def write_time_life():
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str(int((state.game_minutes * 90000 - pygame.time.get_ticks()) / 60000)) + ":" +
                               str(int((2 * 90000 - pygame.time.get_ticks()) / 1000 % 60)).zfill(2),
                               True, (255, 255, 255))
    textRect = survivedtext.get_rect()
    textRect.topright = [size[0] - 5, 5]
    screen.blit(survivedtext, textRect)
    life_text = font.render(str(state.lifes), True, (255, 255, 255))
    life_text_rect = life_text.get_rect()
    life_text_rect.topright = [15, 6]
    screen.blit(life_text, life_text_rect)
    score_text = font.render("score: " + str(-1 * state.score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect()
    score_text_rect.topright = [size[0]/2, 6]
    screen.blit(score_text, score_text_rect)

def player_astroid_collision_check(astroid_inst, astroid_rect, player_rect):
    check = astroid_rect.colliderect(player_rect)
    if check:
        state.remove_astroid(astroid_inst)
    return check


def check_bullet_astroid_hit(bullet, bullet_rect, astroid_rect):
    # checks if the astroid was hit by the bullet
    check = astroid_rect.colliderect(bullet_rect)
    if check:
        state.remove_shot(bullet)
    return check


# Hauptschleife
while not state.done:
    screen.fill((0, 0, 0))

    player.rotate()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            state.set_done()
        if event.type == pygame.MOUSEBUTTONDOWN:
            e_shoot_time = time.time()
            if e_shoot_time - s_shoot_timer > 0.09:
                state.increment_num_shots()
                color = color_generator.next()
                state.add_shot(Bullet(math.atan2(player.direction_y - (player.y+32), player.direction_x - (player.x+26)),
                                      player.x+32, player.y+32, color))
                s_shoot_timer = e_shoot_time

    # shooting
    for bullet in state.shots:
        velx = math.cos(bullet.something) * 10
        vely = math.sin(bullet.something) * 10
        bullet.move(velx, vely)
        if bullet.x < -64 or bullet.y > size[0] + 40 or bullet.y < -64 or bullet.y > size[1] + 80:
            state.remove_shot(bullet)

        for projectile in state.shots:
            projectile.image.fill((0, 0, 0, 255), None, pygame.BLEND_RGB_MULT)
            projectile.image.fill(projectile.color, None, pygame.BLEND_RGB_ADD)
            # rotate image
            shoot1 = pygame.transform.rotate(projectile.image, 270 - projectile.something * 180 / math.pi)
            screen.blit(shoot1, (projectile.x, projectile.y))

    # schreibe die Spielzeit und die Anzahl der Leben
    write_time_life()

    # astroids
    ##### Schritt 1
    ######################### Dein Code kommt hier rein ###############################
    if state.astroid_timer == 0:
        Astroid.create_astroid(state, size)
        state.set_astroid_timer(100 - (state.astroids_faster * 2))
        if state.astroids_faster >= 35:
            state.set_astroids_faster(35)
        else:
            state.set_astroids_faster(state.astroids_faster + 5)
    ####################################################################################

    for astroid in state.astroids:
        if astroid.x < -64:
            state.remove_astroid(astroid)
        astroid.move(-state.astroid_speed)
        player_rect = player.get_rect()

        ##### Schritt 2
        ######################### Dein Code kommt hier rein ###############################
        if player_astroid_collision_check(astroid, astroid.get_rect(), player_rect):
            if state.lifes > 0:
                state.reduce_lifes()
            else:
                state.set_done()
        ####################################################################################ds

        ##### Schritt 3
        ######################### Dein Code kommt hier rein ###################d#############
        for bullet in state.shots:
            bullet_rect = bullet.get_rect()
            if check_bullet_astroid_hit(bullet, bullet_rect, astroid.get_rect()):
                state.increment_num_hits()
                if not astroid.hit_count == 1:
                    astroid.increment_hit_count()
                else:
                    state.remove_astroid(astroid)
                    state.increment_score(astroid.scale)
    ####################################################################################

    for astroid in state.astroids:
        screen.blit(astroid.image, astroid.pos)

    ##### Schritt 4
    ######################### Dein Code kommt hier rein ###############################
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player.move(0, -state.player_speed)
    if pressed[pygame.K_s]:
        player.move(0, state.player_speed)
    if pressed[pygame.K_a]:
        player.move(-state.player_speed, 0)
    if pressed[pygame.K_d]:
        player.move(state.player_speed, 0)
    ####################################################################################

    screen.blit(player.image, player.pos)
    state.set_astroid_timer(state.astroid_timer - 1)

    pygame.display.flip()
    clock.tick(60)

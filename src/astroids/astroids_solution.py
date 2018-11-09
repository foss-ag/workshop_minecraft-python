import pygame
import math
import random
import time
from ColorGenerator import ColorGenerator
from Bullet import Bullet
from GameState import GameState

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

state = GameState()

x = 500
y = 400

clock = pygame.time.Clock()
image = pygame.image.load('src/player.png')
astroid = pygame.image.load('src/astroid.png')
astroid1 = astroid
s_shoot_timer = time.time()

color_generator = ColorGenerator()

# Funktionen des Spieles
def rotate_player():
    # hole Mausposition und berechne anhand des Winkels die entsprechende Rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (y + 27), position[0] - (x + 25))
    rotimage = pygame.transform.rotate(image, 270 - angle * 180 / math.pi)
    return position, rotimage, (x - rotimage.get_rect().centerx, y - rotimage.get_rect().centery)

def write_time_life():
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(
        str(int((state.game_minutes * 90000 - pygame.time.get_ticks()) / 60000)) + ":" + str(
            int((2 * 90000 - pygame.time.get_ticks()) / 1000 % 60)).zfill(2), True, (255, 255, 255))
    textRect = survivedtext.get_rect()
    textRect.topright = [size[0] - 5, 5]
    screen.blit(survivedtext, textRect)
    life_text = font.render(str(state.lifes), True, (255, 255, 255))
    life_text_rect = life_text.get_rect()
    life_text_rect.topright = [15, 6]
    screen.blit(life_text, life_text_rect)


def get_rect_astroid_player(astroid_inst, new_pos, rotimage):
    sizen = astroid.get_size()
    astroid_n = pygame.transform.scale(astroid, (sizen[0] * astroid_inst[2], sizen[1] * astroid_inst[2]))
    astroid_rect = pygame.Rect(astroid_n.get_rect())
    astroid_rect.top = astroid_inst[1]
    astroid_rect.left = astroid_inst[0]
    play_rect = pygame.Rect(rotimage.get_rect())
    play_rect.top = new_pos[1] - pygame.Rect(image.get_rect()).x
    play_rect.left = new_pos[0] - pygame.Rect(image.get_rect()).y
    return astroid_rect, play_rect


def create_astroid():
    # x pos, y pos, size scale, shooted
    state.add_astroid([size[0] - 5, random.randint(50, size[1] - 30), random.randint(1, 6), 0])


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

    # berechne neue Pfeil ausrichtung anhand der Maus
    position, rotimage, new_pos = rotate_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            state.set_done()
        if event.type == pygame.MOUSEBUTTONDOWN:
            e_shoot_time = time.time()
            if e_shoot_time - s_shoot_timer > 0.09:
                state.increment_num_shots()
                color = color_generator.next()
                state.add_shot(Bullet(math.atan2(position[1] - (y+32), position[0] - (x+26)), x+32, y+32, color))
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
        create_astroid()
        state.set_astroid_timer(100 - (state.astroids_faster * 2))
        if state.astroids_faster >= 35:
            state.set_astroids_faster(35)
        else:
            state.set_astroids_faster(state.astroids_faster + 5)
    ####################################################################################

    for astroid_inst in state.astroids:
        if astroid_inst[0] < -64:
            state.remove_astroid(astroid_inst)
        astroid_inst[0] -= state.astroid_speed
        astroid_rect, player_rect = get_rect_astroid_player(astroid_inst, new_pos, rotimage)

        ##### Schritt 2
        ######################### Dein Code kommt hier rein ###############################
        if player_astroid_collision_check(astroid_inst, astroid_rect, player_rect):
            if state.lifes > 0:
                state.reduce_lifes()
            else:
                state.set_done()
        ####################################################################################

        ##### Schritt 3
        ######################### Dein Code kommt hier rein ################################
        for bullet in state.shots:
            bullet_rect = bullet.get_rect()
            if check_bullet_astroid_hit((bullet), bullet_rect, astroid_rect):
                state.increment_num_hits()
                if not astroid_inst[-1] == 1:
                    astroid_inst[-1] += 1
                else:
                    state.remove_astroid(astroid_inst)
    ####################################################################################

    for astroid_inst in state.astroids:
        sizen = astroid.get_size()
        astroid_n = pygame.transform.scale(astroid, (sizen[0] * astroid_inst[2], sizen[1] * astroid_inst[2]))
        screen.blit(astroid_n, astroid_inst[:-2])

    ##### Schritt 4
    ######################### Dein Code kommt hier rein ###############################
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= state.player_speed
    if pressed[pygame.K_s]:
        y += state.player_speed
    if pressed[pygame.K_a]:
        x -= state.player_speed
    if pressed[pygame.K_d]:
        x += state.player_speed
    ####################################################################################

    screen.blit(rotimage, new_pos)
    state.set_astroid_timer(state.astroid_timer - 1)

    pygame.display.flip()
    clock.tick(60)

from Obstacle import Obstacle
from Player import Player
from OneUP import OneUP
from Multiplier import Multiplier
import pygame
import random

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
player = Player(500, 400)
end_game = False

# number of ticks a message will be shown (250)
message_ticks = 0
message = ''

# score variables
multiplier = 1
bonus = 20
score = 0

# extra life symbol
symbol = pygame.image.load("src/extra_lifes.png")
symbol_rect = symbol.get_rect()
symbol_rect.topleft = [980, 10]

# define border height, width and thickness
border_height = 35
border_width = 1000

# used colors
white = (255, 255, 255)
grey = (150, 150, 150)

# obstacle parameters
obstacle_speed = 5
obstacle_p = 1
power_up_obstacles = 0

obstacles = []
powerups = []


def reset_variables():
    global message_ticks
    global multiplier
    global score
    global obstacle_p
    global obstacle_speed
    global power_up_obstacles
    global obstacles
    global powerups

    message_ticks = 0
    multiplier = 1
    score = 0
    obstacle_speed = 5
    obstacle_p = 1
    power_up_obstacles = 0
    obstacles = []
    powerups = []


def set_message(msg):
    global message, message_ticks
    message = msg
    message_ticks = 250


def show_info():
    font = pygame.font.Font(None, 24)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = [500, 17]
    screen.blit(text, text_rect)


def write_score_and_multiplier():
    font = pygame.font.Font(None, 24)
    text = font.render('x' + str(multiplier) + ' | ' + str(score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(text, text_rect)


def write_extra_lifes():
    font = pygame.font.Font(None, 24)
    text = font.render(str(player.extra_lifes) + 'x ', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = [980, 10]
    screen.blit(text, text_rect)
    screen.blit(symbol, symbol_rect)


def generate_obstacle():
    p = random.randint(0, 100)
    if p < obstacle_p:
        obstacles.append(Obstacle(obstacle_speed))


def generate_oneup():
    p = random.randint(0, 5000)
    if p < 1:
        powerups.append(OneUP())


def generate_multiplier():
    p = random.randint(0, 1000)
    if p < 1:
        powerups.append(Multiplier(3))
    elif p < 2:
        powerups.append(Multiplier(2))


def check_collision(other):
    other_rect = other.image.get_rect()
    (x, y) = other.pos
    other_rect.top = y
    other_rect.left = x

    player_rect = player.image.get_rect()
    (x, y) = player.pos
    player_rect.top = y
    player_rect.left = x

    return other_rect.colliderect(player_rect)


while not end_game:
    screen.fill((0, 0, 0))

    # if player is dead press enter to restart or escape to end the game
    if player.dead:
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)
        font = pygame.font.Font(None, 24)
        text = font.render('TRY AGAIN? (ENTER) / QUIT (ESC)', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 400]
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_game = True
                if event.key == pygame.K_RETURN:
                    player = Player(500, 400)
                    reset_variables()

        pygame.display.flip()
        clock.tick(60)
        continue


    write_score_and_multiplier()
    write_extra_lifes()
    generate_obstacle()
    generate_oneup()
    generate_multiplier()
    if message_ticks > 0:
        message_ticks -= 1
        show_info()

    # check collision with bounds
    (_, y) = player.pos
    if y <= 35:
        pygame.draw.rect(screen, grey, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        score += bonus * multiplier
        power_up_obstacles += bonus * multiplier
    elif y >= 710:
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, grey, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        score += bonus * multiplier
        power_up_obstacles += bonus * multiplier
    else:
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)

    # check if obstacles should be made faster or spawn more likely
    if power_up_obstacles >= 10000:
        power_up_obstacles = 0
        p = random.randint(0, 100)
        if p <= 33:
            set_message('GEOMETRY SPEED UP!')
            obstacle_speed += 1
        else:
            set_message('GEOMETRY INTENSIFIES!')
            obstacle_p += 1

    # check collision with obstacles
    for obstacle in obstacles:
        if check_collision(obstacle):
            obstacles.remove(obstacle)
            player.onedown()
            multiplier = 1
            set_message("OUCH!")
            if player.extra_lifes < 0:
                player.kill()
                break

    # check collision with powerups
    for powerup in powerups:
        if check_collision(powerup):
            if isinstance(powerup, OneUP):
                set_message("1-UP!")
                player.oneup()
            else:
                if multiplier == 1:
                    multiplier = powerup.multiplier
                else:
                    multiplier += powerup.multiplier
                set_message("MULTIPLIER INCREASED!")
            powerups.remove(powerup)

    # check if any powerups must be removed
    for powerup in powerups:
        remove = powerup.decrease_ticks()
        if remove:
            powerups.remove(powerup)

    # check pressed buttons
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player.kill()
                end_game = True
                continue
            if event.key == pygame.K_LEFT:
                player.set_move_left(True)
                player.set_move_right(False)
            if event.key == pygame.K_RIGHT:
                player.set_move_left(False)
                player.set_move_right(True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.set_move_left(False)
            if event.key == pygame.K_RIGHT:
                player.set_move_right(False)

    player.move()
    screen.blit(player.image, player.pos)

    for obstacle in obstacles:
        obstacle.move()
        if obstacle.out_of_bounds():
            obstacles.remove(obstacle)
        else:
            screen.blit(obstacle.image, obstacle.pos)

    for powerup in powerups:
        screen.blit(powerup.image, powerup.pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

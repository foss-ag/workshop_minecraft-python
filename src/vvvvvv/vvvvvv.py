from Obstacle import Obstacle
from Player import Player
from OneUP import OneUP
import pygame
import random

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
player = Player(500, 400)

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

obstacles = []
powerups = []


def write_score():
    font = pygame.font.Font(None, 24)
    score_text = font.render(str(score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = [10, 10]
    screen.blit(score_text, score_text_rect)
    screen.blit(symbol, symbol_rect)


def write_extra_lifes():
    font = pygame.font.Font(None, 24)
    text = font.render(str(player.extra_lifes) + 'x ', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = [980, 10]
    screen.blit(text, text_rect)


def generate_obstacle():
    p = random.randint(0, 100)
    if p < 1:
        obstacles.append(Obstacle())


def generate_oneup():
    p = random.randint(0, 5000)
    if p < 1:
        powerups.append(OneUP())


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


while not player.dead:
    screen.fill((0, 0, 0))
    write_score()
    write_extra_lifes()
    generate_obstacle()
    generate_oneup()

    # check collision with bounds
    (_, y) = player.pos
    if y <= 35:
        pygame.draw.rect(screen, grey, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        score += bonus * multiplier
    elif y >= 710:
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, grey, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        score += bonus * multiplier
    else:
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)

    # check collision with obstacles
    for obstacle in obstacles:
        if check_collision(obstacle):
            obstacles.remove(obstacle)
            player.onedown()
            if player.extra_lifes < 0:
                player.kill()
                break

    # check collision with powerups
    for powerup in powerups:
        if check_collision(powerup):
            player.oneup()
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

from Obstacle import Obstacle
from Player import Player
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

# define border height, width and thickness
border_height = 35
border_width = 1000

# used colors
white = (255, 255, 255)
grey = (150, 150, 150)

obstacles = []

def write_score():
    font = pygame.font.Font(None, 24)
    score_text = font.render(str(score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = [10, 10]
    screen.blit(score_text, score_text_rect)


def generate_obstacle():
    p = random.randint(0, 100)
    if p < 3:
        obstacles.append(Obstacle())


while not player.dead:
    screen.fill((0, 0, 0))
    write_score()
    generate_obstacle()

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
            print(obstacle.pos)
            screen.blit(obstacle.image, obstacle.pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

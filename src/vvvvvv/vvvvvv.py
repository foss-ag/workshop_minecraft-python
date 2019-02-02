import pygame
from Player import Player

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

player = Player(500, 400)
speed = 5

dead = False
move_up = True
move_right = False
move_left = False

while not dead:
    screen.fill((0, 0, 0))

    # check pressed buttons
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dead = True
                continue
            if event.key == pygame.K_SPACE:
                move_up = not move_up
            if event.key == pygame.K_LEFT:
                move_left = True
                move_right = False
            if event.key == pygame.K_RIGHT:
                move_right = True
                move_left = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    if move_up:
        player.move(0, speed)
    else:
        player.move(0, -speed)

    if move_right:
        player.move(speed, 0)
    if move_left:
        player.move(-speed, 0)

    screen.blit(player.image, player.pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

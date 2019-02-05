import pygame
from Player import Player

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

player = Player(500, 400)

while not player.dead:
    screen.fill((0, 0, 0))

    # define border height, width and thickness
    border_height = border_thickness = 35
    border_width = 1000
    # draw upper and lower bounds
    pygame.draw.rect(screen, (200, 0, 0), (0, 0, border_width, border_height), border_thickness)
    pygame.draw.rect(screen, (200, 0, 0), (0, size[1] - border_height, border_width, border_height), border_thickness)

    # define tolerance factor for more precise border collision
    tolerance = 15
    # check collision with bounds
    (_, y) = player.pos
    if y <= 35 + tolerance or y >= 710 - tolerance:
        player.kill()
        continue

    # check pressed buttons
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player.kill()
                continue
            if event.key == pygame.K_SPACE:
                player.change_move_up()
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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

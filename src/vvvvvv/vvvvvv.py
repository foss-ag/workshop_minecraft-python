import pygame
from Player import Player

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

player = Player(500, 400)

dead = False

while not dead:

    # check pressed buttons
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dead = True
                continue
            if event.key == pygame.K_SPACE:
                print("SPACE")
            if event.key == pygame.K_UP:
                print("UP")
            if event.key == pygame.K_DOWN:
                print("DOWN")
            if event.key == pygame.K_LEFT:
                print("LEFT")
            if event.key == pygame.K_RIGHT:
                print("RIGHT")

    screen.blit(player.image, player.pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

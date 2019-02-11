from Obstacle import Obstacle
from Player import Player
from OneUP import OneUP
from Multiplier import Multiplier
import pygame
import random

# initialize pygame and global variables
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
quit_game = False

# create player and set position
player = Player(500, 400)

# number of ticks the message will be shown
message_ticks = 0
message = ''

# score variables
multiplier = 1
bonus = 20
score = 0

# extra life symbol
symbol = pygame.image.load("src/extra_lives.png")
symbol_rect = symbol.get_rect()
symbol_rect.topleft = [980, 10]

# define border height and width
border_height = 35
border_width = 1000

# used colors
white = (255, 255, 255)
grey = (150, 150, 150)

# obstacle parameters
obstacle_speed = 5
obstacle_prob = 1
# if power_up_obstacles exceeds 10000 reset and power up obstacle parameters
power_up_obstacles = 0

# list of current obstacles and powerups in the game
obstacles = []
powerups = []


def reset_variables():
    """
    Reset global variables for every new try.
    """
    global message_ticks
    global multiplier
    global score
    global obstacle_prob
    global obstacle_speed
    global power_up_obstacles
    global obstacles
    global powerups

    message_ticks = 0
    multiplier = 1
    score = 0
    obstacle_speed = 5
    obstacle_prob = 1
    power_up_obstacles = 0
    obstacles = []
    powerups = []


def set_message(msg):
    """
    Set message and number of ticks the message will be shown.
    Number of ticks = 250.

    :param msg:
        Message that will be shown in the info bar.
    """
    global message, message_ticks
    message = msg
    message_ticks = 250


def show_info():
    """
    Show message in info bar.
    """
    font = pygame.font.Font(None, 24)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = [500, 17]
    screen.blit(text, text_rect)


def write_score_and_multiplier():
    """
    Show player score and score multiplier in info bar.
    """
    font = pygame.font.Font(None, 24)
    text = font.render('x' + str(multiplier) + ' | ' + str(score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(text, text_rect)


def write_extra_lives():
    """
    Show extra lives in info bar.
    """
    font = pygame.font.Font(None, 24)
    text = font.render(str(player.extra_lives) + 'x ', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = [980, 10]
    screen.blit(text, text_rect)
    screen.blit(symbol, symbol_rect)


def generate_obstacle():
    """
    Generate a new obstacle with a probability of obstacle_prob percent.
    """
    p = random.randint(0, 100)
    if p < obstacle_prob:
        obstacles.append(Obstacle(obstacle_speed))


def generate_oneup():
    """
    Generate a new 1-UP powerup with a probability of 1/50 percent.
    """
    p = random.randint(0, 5000)
    if p < 1:
        powerups.append(OneUP())


def generate_multiplier():
    """
    Generate a new x2 multiplier with a probability of 0.1 percent
    or a new x3 multiplier with a probability of 0.2 percent.
    """
    p = random.randint(0, 1000)
    if p < 1:
        powerups.append(Multiplier(3))
    elif p < 2:
        powerups.append(Multiplier(2))


def check_collision(other):
    """
    Check collision with other object.

    :param other:
        Obstacle or Powerup.
    :return:
        True if player collides with another object, False otherwise.
    """
    other_rect = other.image.get_rect()
    (x, y) = other.pos
    other_rect.top = y
    other_rect.left = x

    player_rect = player.image.get_rect()
    (x, y) = player.pos
    player_rect.top = y
    player_rect.left = x

    return other_rect.colliderect(player_rect)


while not quit_game:
    screen.fill((0, 0, 0))

    # if player is dead press enter to restart or escape to end the game
    if player.dead:
        # show try again text
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)
        font = pygame.font.Font(None, 24)
        text = font.render('TRY AGAIN? (ENTER) / QUIT (ESC)', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [500, 400]
        screen.blit(text, text_rect)

        # check buttons pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # ESC -> quit game
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
                # RETURN -> restart game
                if event.key == pygame.K_RETURN:
                    player = Player(500, 400)
                    reset_variables()

        pygame.display.flip()
        clock.tick(60)
        continue

    # update info bar
    write_score_and_multiplier()
    write_extra_lives()
    if message_ticks > 0:
        message_ticks -= 1
        show_info()

    # generate random objects
    generate_obstacle()
    generate_oneup()
    generate_multiplier()

    (_, y) = player.pos
    # check collision with upper bound
    if y <= 35:
        # collision animation
        pygame.draw.rect(screen, grey, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        # increase score when colliding with bounds
        score += bonus * multiplier
        power_up_obstacles += bonus * multiplier
    # check collision with lower bound
    elif y >= 710:
        # collision animation
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, grey, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        # increase score when colliding with bounds
        score += bonus * multiplier
        power_up_obstacles += bonus * multiplier
    else:
        # draw bounds
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)

    # powerup obstacles if player reaches another 10000 points
    if power_up_obstacles >= 10000:
        # reset counter
        power_up_obstacles -= 10000
        p = random.randint(0, 100)
        # with probability of 1/3 increase obstacle speed by 1
        if p <= 33:
            set_message('GEOMETRY SPEED UP!')
            obstacle_speed += 1
        # with probability of 2/3 increase obstacle spawn probability by 1 percent
        else:
            set_message('GEOMETRY INTENSIFIES!')
            obstacle_prob += 1

    # check collision with obstacles, reset multiplier, decrease extra lives
    for obstacle in obstacles:
        if check_collision(obstacle):
            obstacles.remove(obstacle)
            player.onedown()
            multiplier = 1
            set_message("OUCH!")
            # kill player if no extra lives were left
            if player.extra_lives < 0:
                player.kill()
                break

    # check collision with powerups and increase extra lives or multiplier respectively
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
                quit_game = True
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

    # update player position
    player.move()
    screen.blit(player.image, player.pos)

    # update obstacle positions
    for obstacle in obstacles:
        obstacle.move()
        if obstacle.out_of_bounds():
            obstacles.remove(obstacle)
        else:
            screen.blit(obstacle.image, obstacle.pos)

    # show powerups
    for powerup in powerups:
        screen.blit(powerup.image, powerup.pos)

    # render screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

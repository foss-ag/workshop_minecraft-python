from GameState import GameState
from Obstacle import Obstacle
from Player import Player
from OneUP import OneUP
from Multiplier import Multiplier
import pygame
import random
import csv

# initialize pygame and game state
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
state = GameState()
update_highscore = True
input_nick = True
nick_pos = 0

# create player and set position
player = Player(500, 400)

# number of ticks the message will be shown
message_ticks = 0
message = ''

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
    text = font.render('x' + str(state.multiplier) + ' | ' + str(state.score), True, (255, 255, 255))
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
    if p < state.obstacle_prob:
        state.add_obstacle(Obstacle(state.obstacle_speed))


def generate_oneup():
    """
    Generate a new 1-UP powerup with a probability of 1/50 percent.
    """
    p = random.randint(0, 5000)
    if p < 1:
        state.add_powerup(OneUP())


def generate_multiplier():
    """
    Generate a new x2 multiplier with a probability of 0.1 percent
    or a new x3 multiplier with a probability of 0.2 percent.
    """
    p = random.randint(0, 1000)
    if p < 1:
        state.add_powerup(Multiplier(3))
    elif p < 2:
        state.add_powerup(Multiplier(2))


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


while not state.quit:
    screen.fill((0, 0, 0))

    # if player is dead press enter to restart or escape to end the game
    if player.dead:
        # update highscore if necessary
        if state.update_highscore:
            # add new highscore entry if current player score is higher than any in the top ten
            if state.new_highscore:
                state.add_highscore_entry()
            # set to False such that the highscore is only updated once
            state.highscore_updated()

        if state.new_highscore and state.input_nick:
            # check buttons pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        state.next_char()
                    if event.key == pygame.K_DOWN:
                        state.prev_char()
                    if event.key == pygame.K_LEFT:
                        state.prev_nick_pos()
                    if event.key == pygame.K_RIGHT:
                        state.next_nick_pos()
                    if event.key == pygame.K_RETURN:
                        state.set_nick()

        # show highscore nicks
        for i, nick in enumerate(state.nicks):
            font = pygame.font.Font(None, 24)
            text = font.render('{:15}'.format(nick), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topleft = [400, 200 + i*30]
            screen.blit(text, text_rect)

        # show highscore scores
        for i, score in enumerate(state.scores):
            font = pygame.font.Font(None, 24)
            text = font.render('{:>10}'.format(score), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topright = [600, 200 + i*30]
            screen.blit(text, text_rect)

        # show try again text
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)

        font = pygame.font.Font(None, 42)
        highscore_text = font.render('HIGHSCORE', True, (255, 255, 255))
        highscore_rect = highscore_text.get_rect()
        highscore_rect.center = [500, 100]
        screen.blit(highscore_text, highscore_rect)

        # do not check further pressed buttons while input player nick
        if state.new_highscore and state.input_nick:
            pygame.display.flip()
            clock.tick(60)
            continue

        font = pygame.font.Font(None, 24)
        again = font.render('TRY AGAIN? (ENTER)', True, (255, 255, 255))
        again_rect = again.get_rect()
        again_rect.center = [500, 700]
        screen.blit(again, again_rect)

        quit_text = font.render('QUIT (ESC)', True, (255, 255, 255))
        quit_rect = quit_text.get_rect()
        quit_rect.center = [500, 720]
        screen.blit(quit_text, quit_rect)

        # check buttons pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # ESC -> quit game
                if event.key == pygame.K_ESCAPE:
                    state.quit_game()
                # RETURN -> restart game
                if event.key == pygame.K_RETURN:
                    player = Player(500, 400)
                    message_ticks = 0
                    state = GameState()

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
        state.increase_score()
    # check collision with lower bound
    elif y >= 710:
        # collision animation
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, grey, (0, size[1] - border_height, border_width, 3), 3)
        player.flip()
        # increase score when colliding with bounds
        state.increase_score()
    else:
        # draw bounds
        pygame.draw.rect(screen, white, (0, border_height, border_width, 3), 3)
        pygame.draw.rect(screen, white, (0, size[1] - border_height, border_width, 3), 3)

    # powerup obstacles if player reaches another 10000 points
    if state.power_up_obstacles >= 10000:
        # reset counter
        state.reset_power_up_obstacles()
        p = random.randint(0, 100)
        # with probability of 1/3 increase obstacle speed by 1
        if p <= 33:
            set_message('GEOMETRY SPEED UP!')
            state.increase_obstacle_speed()
        # with probability of 2/3 increase obstacle spawn probability by 1 percent
        else:
            set_message('GEOMETRY INTENSIFIES!')
            state.increase_obstacle_prob()

    # check collision with obstacles, reset multiplier, decrease extra lives
    for obstacle in state.obstacles:
        if check_collision(obstacle):
            state.remove_obstacle(obstacle)
            player.onedown()
            state.reset_multiplier()
            set_message("OUCH!")
            # kill player if no extra lives were left
            if player.extra_lives < 0:
                player.kill()
                break

    # check collision with powerups and increase extra lives or multiplier respectively
    for powerup in state.powerups:
        if check_collision(powerup):
            if isinstance(powerup, OneUP):
                set_message("1-UP!")
                player.oneup()
            else:
                if state.multiplier == 1:
                    state.set_multiplier(powerup.multiplier)
                else:
                    state.increase_multiplier(powerup.multiplier)
                set_message("MULTIPLIER INCREASED!")
            state.remove_powerup(powerup)

    # check if any powerups must be removed
    for powerup in state.powerups:
        remove = powerup.decrease_ticks()
        if remove:
            state.remove_powerup(powerup)

    # check pressed buttons
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player.kill()
                state.quit_game()
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
    for obstacle in state.obstacles:
        obstacle.move()
        if obstacle.out_of_bounds():
            state.remove_obstacle(obstacle)
        else:
            screen.blit(obstacle.image, obstacle.pos)

    # show powerups
    for powerup in state.powerups:
        screen.blit(powerup.image, powerup.pos)

    # render screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

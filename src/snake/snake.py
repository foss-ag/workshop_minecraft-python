import pygame
import random

# Initialize pygame and clock
pygame.init()
clock = pygame.time.Clock()

# Define colors with rgb values
white = (200, 200, 200)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 140, 0)

# Screen dimensions
display_width = 800
display_height = 600

# Initialize game window and title
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

# Block size used to represent all objects
block_size = 10
# Frame rate (frames per second)
FPS = 30


# Draws the entire snake
def snake(block_size, snake_list):
    # Iterate through each segment in the list
    for segment in snake_list:
        # Segments consist of x and y coordinates
        snake_x, snake_y = segment
        # Draw each segment at its respective location
        pygame.draw.rect(gameDisplay, green, [snake_x, snake_y, block_size, block_size])

    pygame.display.update()


# Initialize font, must be done to use text, None uses default
font = pygame.font.Font(None, 25)


# Convert the text string into a rectangle, used for centering text
def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# Print text onto the screen
def message_to_screen(msg, color, y_displace=0):
    text_surface, text_rect = text_objects(msg, color)
    # Center the text object by its center
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(text_surface, text_rect)


def show_end_screen(snake_length):
    # End game screen asking user what to do next
    gameDisplay.fill(white)
    text_play_again = "Press C to play again or Q to quit"
    text_score = "You ate " + str(snake_length - 1) + " apples"
    message_to_screen("GAME OVER", red, y_displace=-50)
    message_to_screen(text_play_again, black)
    message_to_screen(text_score, green, y_displace=50)
    pygame.display.update()
    # Ask for user input
    for event in pygame.event.get():
        # Pressing x on window
        if event.type == pygame.QUIT:
            done = True
            gameOver = False
        # Running user commands from prompts
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
                gameOver = False
            if event.key == pygame.K_c:
                gameLoop()


def get_new_apple_x():
    return round(random.randrange(0, display_width - block_size) / 10.0) * 10.0


def get_new_apple_y():
    return round(random.randrange(0, display_height - block_size) / 10.0) * 10.0


def snake_bit(snake_list, snake_segment):
    for each in snake_list[:-1]:
        if each == snake_segment:
            return True
    return False


def draw_apple(apple_x, apple_y):
    # Paint the background
    gameDisplay.fill(white)
    # Draw apple at the calculated random location
    pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, block_size, block_size])


def snake_left_screen(snake_x, snake_y):
    return not (0 < snake_x and snake_x <= display_width) or not (0 < snake_y and snake_y <= display_height)


def get_pressed_button():
    events = pygame.event.get()
    if len(events) > 0:
        event = events[0]
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            return event.type, event.key
        else:
            return None, None
    else:
        return None, None


# Run the game! Has inner loops to allow game reset
def gameLoop():
    done = False
    gameOver = False

    # Current position of a snake block, when called this is the head
    snake_x = display_width / 2
    snake_y = display_height / 2
    # Rate of change of movement, x and y indicate direction
    snake_x_change = 0
    snake_y_change = 0
    # Store each segment in a list, note that length is defined seperately
    snake_list = [[snake_x, snake_y]]
    snake_length = 1
    # Randomly generate position of an apple
    apple_x = get_new_apple_x()
    apple_y = get_new_apple_y()


    ##### Schritt 1
    ####################### Deinen Code hier einfügen ############################







    ##### Schriit 2
    ####################### Deinen Code hier einfügen ########################










    ##########################################################################

    ##### Schritt 3
    ##################### Deinen Code hier einfügen ##########################









    ###########################################################################

    ##### Schritt 4:
    ##################### Deinen Code hier einfügen ###########################





    ##########################################################################################

    # Increment the while loop according to the frame rate previously defined
    clock.tick(FPS)


# When loops exit, quit the game and close the window
pygame.quit()
quit()

# Code outside of def gameLoop() that starts the loop
gameLoop()

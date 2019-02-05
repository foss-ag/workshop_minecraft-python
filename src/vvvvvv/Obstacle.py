import random
import pygame


class Obstacle:

    def __init__(self):
        # load player image
        self.__img = pygame.image.load('src/obstacle.png')
        # obstacle position
        self.__x = random.sample([0, 1000], 1)[0]
        self.__y = random.randint(35, 800-35-26)
        # movement direction, moves right if obstacles starts at x=0 otherwise it moves left
        self.__move_left = self.__x != 0
        # movement speed
        self.__speed = 5

    @property
    def image(self):
        return self.__img

    @property
    def pos(self):
        return self.__x, self.__y

    def move(self):
        self.__x += self.__speed * (not self.__move_left) - self.__speed * self.__move_left

    def out_of_bounds(self):
        return self.__x < -26 or self.__x > 1000



import random
import pygame


class OneUP:

    def __init__(self):
        # load player image
        self.__img = pygame.image.load('src/powerup2.png')
        self.__color = (10, 255, 50, 255)
        self.__img.fill((0, 0, 0, 255), None, pygame.BLEND_RGB_MULT)
        self.__img.fill(self.__color, None, pygame.BLEND_RGB_ADD)
        # position
        self.__x = random.randint(0, 1000-26)
        self.__y = random.randint(35, 800-35-26)
        # life time
        self.__ticks = 250

    @property
    def image(self):
        return self.__img

    @property
    def color(self):
        return self.__color

    @property
    def pos(self):
        return self.__x, self.__y

    def decrease_ticks(self):
        """
        Decrease life time (ticks).

        :return:
            If remaining ticks are 0 return True else return False
        """
        self.__ticks -= 1
        if self.__ticks == 0:
            return True
        else:
            return False

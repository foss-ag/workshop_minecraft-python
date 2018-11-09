import pygame
import random


class Astroid():

    def __init__(self, x, y, scale):
        self.__x = x
        self.__y = y
        self.__scale = scale
        self.__hit_count = 0
        self.__img = pygame.image.load('src/astroid.png')

        size = self.__img.get_size()
        self.__img = pygame.transform.scale(self.__img, (size[0] * self.__scale, size[1] * self.__scale))
        self.__astroid_rect = pygame.Rect(self.__img.get_rect())

    @staticmethod
    def create_astroid(state, size):
        # x pos, y pos, size scale, shooted
        state.add_astroid(Astroid(size[0] - 5, random.randint(50, size[1] - 30), random.randint(1, 6)))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def pos(self):
        return (self.__x, self.__y)

    @property
    def scale(self):
        return self.__scale

    @property
    def hit_count(self):
        return self.__hit_count

    @property
    def image(self):
        return self.__img

    def get_rect(self):
        self.__astroid_rect.top = self.__y
        self.__astroid_rect.left = self.__x
        return self.__astroid_rect

    def increment_hit_count(self):
        self.__hit_count += 1

    def move(self, x):
        """
        TODO

        :param x:
            x-offset
        :return:
        """
        self.__x += x


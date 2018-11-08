import pygame

class Bullet:

    def __init__(self, something, x, y, color):
        """
        :param something: probably direction
        :param x:
            x coordinate
        :param y:
            y coordinate
        :param color:
            RGBA color
        """
        # what is this?
        self.__something = something
        self.__x = x
        self.__y = y
        self.__color = color
        self.__img = pygame.image.load('src/shoot.png')

    @property
    def color(self):
        return self.__color

    @property
    def something(self):
        return self.__something

    @property
    def image(self):
        return self.__img

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def get_rect(self):
        bullrect = pygame.Rect(self.__img.get_rect())
        bullrect.left = self.__x
        bullrect.top = self.__y
        return bullrect

    def move(self, x, y):
        """
        :param x:
            x-offset
        :param y:
            y-offset
        :return:
        """
        self.__x += x
        self.__y += y
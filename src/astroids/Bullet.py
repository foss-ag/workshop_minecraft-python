import pygame


class Bullet:

    def __init__(self, orientation, x, y, color):
        """
        :param something:
            # TODO
            probably direction
        :param x:
            Start position X
        :param y:
            Start position Y
        :param color:
            RGBA color
        """
        # TODO what is this?
        # bullet position
        self.__orientation = orientation
        self.__x = x
        self.__y = y
        # bullet color
        self.__color = color
        # bullet image
        self.__img = pygame.image.load('src/shoot.png')

    @property
    def color(self):
        return self.__color

    @property
    def orientation(self):
        return self.__orientation

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
        """
        Returns rectangle of bullet.

        :return:
            Bullet rectangle
        """
        bullrect = pygame.Rect(self.__img.get_rect())
        bullrect.left = self.__x
        bullrect.top = self.__y
        return bullrect

    def move(self, x, y):
        """
        Update position by x and y offset.

        :param x:
            x offset
        :param y:
            y offset
        """
        self.__x += x
        self.__y += y

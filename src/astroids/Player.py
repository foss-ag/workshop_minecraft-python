import math
import pygame


class Player():

    def __init__(self, x, y):
        """
        Create player object.

        :param x:
            Start position X
        :param y:
            Start position Y
        """
        # load player image
        self.__img = pygame.image.load('src/player.png')
        self.__rot_img = self.__img
        self.__x = x
        self.__y = y
        self.__rot_x = x
        self.__rot_y = y
        self.__direction_x = x
        self.__direction_y = y

    def rotate(self):
        """
        Get mouse position and rotate player.
ss
        :return:
        """
        (self.__direction_x, self.__direction_y) = pygame.mouse.get_pos()
        angle = math.atan2(self.__direction_y - (self.__y + 27), self.__direction_x - (self.__x + 25))
        self.__rot_img = pygame.transform.rotate(self.__img, 270 - angle * 180 / math.pi)
        rect = self.__rot_img.get_rect()
        self.__rot_x = self.__x - rect.centerx
        self.__rot_y = self.__y - rect.centery

    def get_rect(self):
        player_rect = pygame.Rect(self.__rot_img.get_rect())
        player_rect.top = self.__rot_y - pygame.Rect(self.__img.get_rect()).x
        player_rect.left = self.__rot_x - pygame.Rect(self.__img.get_rect()).y
        return player_rect

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
    def direction_x(self):
        return self.__direction_x

    @property
    def direction_y(self):
        return self.__direction_y

    @property
    def direction(self):
        return (self.__direction_x, self.__direction_y)

    @property
    def image(self):
        return self.__rot_img

    def move(self, x, y):
        """
        TODO

        :param x:
            x-offset
        :param y:
            y-offset
        :return:
        """
        self.__x += x
        self.__y += y

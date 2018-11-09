import pygame
import math

class Player():

    def __init__(self, x, y):
        self.__img = pygame.image.load('src/player.png')
        self.__x = x
        self.__y = y

    def rotate(self):
        # hole Mausposition und berechne anhand des Winkels die entsprechende Rotation
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1] - (self.__y + 27), position[0] - (self.__x + 25))
        rotimage = pygame.transform.rotate(self.__img, 270 - angle * 180 / math.pi)
        return (position, rotimage, (self.__x - rotimage.get_rect().centerx, self.__y - rotimage.get_rect().centery))

    def get_rect(self):
        player_rect = pygame.Rect(self.__img.get_rect())
        player_rect.top = self.__y - pygame.Rect(self.__img.get_rect()).x
        player_rect.left = self.__x - pygame.Rect(self.__img.get_rect()).y
        return player_rect

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

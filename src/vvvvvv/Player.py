import pygame


class Player:

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
        # player position
        self.__x = x
        self.__y = y

    @property
    def pos(self):
        return self.__x, self.__y

    @property
    def image(self):
        return self.__img

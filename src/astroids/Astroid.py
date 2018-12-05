import pygame
import random


class Astroid:

    def __init__(self, x, y, scale):
        """
        Create Astroid object.

        :param x:
            Start position X.
        :param y:
            Start position Y.
        :param scale:
            Astroid size scale.
        """
        # astroid position
        self.__x = x
        self.__y = y
        # astroid size scale
        self.__scale = scale
        # hit count
        self.__hit_count = 0
        # astroid image
        self.__img = pygame.image.load('src/astroid.png')

        # scale astroid image and get astroid rectangle
        size = self.__img.get_size()
        self.__img = pygame.transform.scale(self.__img, (size[0] * self.__scale, size[1] * self.__scale))
        self.__astroid_rect = pygame.Rect(self.__img.get_rect())

    @staticmethod
    def create_astroid(state, size):
        """
        Create new random astroid and add it to the astroids list in the game state.

        :param state:
            Game state with astroids list.
        :param size:
            Screen size.
        """
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
        """
        Get new astroid rectangle for new position.

        :return:
            Astroid rectangle
        """
        self.__astroid_rect.top = self.__y
        self.__astroid_rect.left = self.__x
        return self.__astroid_rect

    def increment_hit_count(self):
        """
        Increment astroid hit count by 1.
        """
        self.__hit_count += 1

    def move(self, x):
        """
        Update astroid position by x offset.

        :param x:
            x-offset
        """
        self.__x += x


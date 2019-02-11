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
        # player still alive?
        self.__dead = False
        # movement variables
        self.__move_up = True
        self.__move_right = False
        self.__move_left = False
        # movement speed
        self.__speed = 10
        # extra lives
        self.__extra_lives = 0

    @property
    def dead(self):
        return self.__dead

    @property
    def move_up(self):
        return self.__move_up

    @property
    def move_left(self):
        return self.__move_left

    @property
    def move_right(self):
        return self.__move_right

    @property
    def pos(self):
        return self.__x, self.__y

    @property
    def image(self):
        return self.__img

    @property
    def extra_lives(self):
        return self.__extra_lives

    def oneup(self):
        self.__extra_lives += 1

    def onedown(self):
        self.__extra_lives -= 1

    def flip(self):
        """
        Changes move_up to False if True and vice versa.
        """
        self.__move_up = not self.__move_up
        self.__img = pygame.transform.rotate(self.__img, 180)

    def set_move_left(self, b):
        """
        Changes move_left given Boolean b.

        :param b: Boolean.
        """
        self.__move_left = b

    def set_move_right(self, b):
        """
        Changes move_right to given Boolean b.

        :param b: Boolean
        """
        self.__move_right = b

    def move(self):
        """
        Update player position depending on move variables.
        """
        self.__x += self.__speed * self.__move_right - self.__speed * self.__move_left

        if self.__x < 0 and self.__move_left:
            self.__x += 1000 - 26
        if self.__x > 1000 - 26 and self.__move_right:
            self.__x -= 1000 - 26

        self.__y += self.__speed * self.__move_up - self.__speed * (not self.__move_up)

    def kill(self):
        """
        Change dead status variable to True.
        """
        self.__dead = True

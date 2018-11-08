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

    @property
    def color(self):
        return self.__color

    @property
    def something(self):
        return self.__something

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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
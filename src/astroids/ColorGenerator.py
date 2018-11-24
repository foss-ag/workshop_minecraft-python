class ColorGenerator:

    def __init__(self):
        self.__index = 0
        self.__rainbow = [(r, g, 0, 0) for r in range(255, -1, -10) for g in range(0, 256, 10) if r + g == 255] + \
                  [(0, g, b, 0) for g in range(255, -1, -10) for b in range(0, 256, 10) if g + b == 255] + \
                  [(r, 0, b, 0) for b in range(255, -1, -10) for r in range(0, 256, 10) if b + r == 255]

    def next(self):
        color = self.__rainbow[self.__index]
        if self.__index + 1 >= len(self.__rainbow):
            self.__index = 0
        else:
            self.__index += 1

        return color

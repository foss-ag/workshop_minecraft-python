class GameState():

    def __init__(self, game_minutes=4, player_speed=3, astroid_speed=7, astroid_timer=100, astroids_faster=0):
        self.__done = False
        self.__game_minutes = game_minutes
        self.__player_speed = player_speed

        self.__astroid_speed = astroid_speed
        self.__astroid_timer = astroid_timer
        self.__astroids_faster = astroids_faster

        self.__astroids = []
        self.__shoots = []

    @property
    def astroid_timer(self):
        return self.__astroid_timer

    @property
    def astroid_speed(self):
        return self.__astroid_speed

    @property
    def astroids_faster(self):
        return self.__astroids_faster

    @property
    def player_speed(self):
        return self.__player_speed

    @property
    def game_minutes(self):
        return self.__game_minutes

    @property
    def done(self):
        return self.__done

    @property
    def shoots(self):
        return self.__shoots

    @property
    def astroids(self):
        return self.__astroids

    def set_done(self):
        self.__done = True

    def add_astroid(self, astroid):
        self.__astroids.append(astroid)

    def remove_astroid(self, astroid):
        self.__astroids.remove(astroid)

    def remove_shot(self, bullet):
        self.__shoots.remove(bullet)

    def add_shot(self, bullet):
        self.__shoots.append(bullet)

    def set_astroid_timer(self, t):
        self.__astroid_timer = t

    def set_astroids_faster(self, s):
        self.__astroids_faster = s


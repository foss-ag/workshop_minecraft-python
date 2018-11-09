class GameState():

    def __init__(self, game_minutes=4, lifes=5, player_speed=3, astroid_speed=7, astroid_timer=100, astroids_faster=0):
        self.__done = False
        self.__game_minutes = game_minutes
        self.__lifes = lifes
        self.__player_speed = player_speed

        self.__astroid_speed = astroid_speed
        self.__astroid_timer = astroid_timer
        self.__astroids_faster = astroids_faster

        self.__astroids = []
        self.__shots = []

        self.__num_hits = 0
        self.__num_shots = 0

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
    def lifes(self):
        return self.__lifes

    @property
    def done(self):
        return self.__done

    @property
    def shots(self):
        return self.__shots

    @property
    def astroids(self):
        return self.__astroids

    @property
    def num_hits(self):
        return self.__num_hits

    @property
    def num_shots(self):
        return self.__num_shots

    def set_done(self):
        self.__done = True

    def add_astroid(self, astroid):
        self.__astroids.append(astroid)

    def remove_astroid(self, astroid):
        self.__astroids.remove(astroid)

    def remove_shot(self, bullet):
        self.__shots.remove(bullet)

    def add_shot(self, bullet):
        self.__shots.append(bullet)

    def set_astroid_timer(self, t):
        self.__astroid_timer = t

    def set_astroids_faster(self, s):
        self.__astroids_faster = s

    def reduce_lifes(self):
        self.__lifes -= 1

    def increment_num_shots(self):
        self.__num_shots += 1

    def increment_num_hits(self):
        self.__num_hits += 1

class GameState:

    def __init__(self, game_minutes=4, lifes=5, player_speed=3, astroid_speed=7, astroid_timer=100, astroids_faster=0):
        """
        Create game state object.

        :param game_minutes:
            Game duration in minutes (default: 4)
        :param lifes:
            Player lifes (default: 5)
        :param player_speed:
            Player speed (default: 3)
        :param astroid_speed:
            Astroid speed (default: 7)
        :param astroid_timer:
            Initial astroid timer. Frequency of spawning astroids in milliseconds (default: 100)
        :param astroids_faster:
            Milliseconds reducing the astroid timer (default: 0)
        """
        self.__done = False
        self.__game_minutes = game_minutes
        self.__lifes = lifes
        self.__player_speed = player_speed

        self.__astroid_speed = astroid_speed
        self.__astroid_timer = astroid_timer
        self.__astroids_faster = astroids_faster

        # list of current astroids and shots
        self.__astroids = []
        self.__shots = []

        # number of hits, shots and score
        self.__num_hits = 0
        self.__num_shots = 0
        self.__score = 0

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
    def score(self):
        return self.__score

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
        """
        Game is done!
        """
        self.__done = True

    def add_astroid(self, astroid):
        """
        Add astroid to astroid list

        :param astroid:
            Astroid object
        """
        self.__astroids.append(astroid)

    def remove_astroid(self, astroid):
        """
        Remove astroid from astroid list

        :param astroid:
            Astroid object
        """
        self.__astroids.remove(astroid)

    def remove_shot(self, bullet):
        """
        Remove shot from shot list

        :param bullet:
            Bullet object
        """
        self.__shots.remove(bullet)

    def add_shot(self, bullet):
        """
        Add shot to shot list

        :param bullet:
            Bullet object
        """
        self.__shots.append(bullet)

    def set_astroid_timer(self, t):
        """
        Set astroid timer.

        :param t:
            New astroid timer
        """
        self.__astroid_timer = t

    def set_astroids_faster(self, s):
        """
        Set astroids faster.

        :param s:
            New astroid timer reduction.
        """
        self.__astroids_faster = s

    def reduce_lifes(self):
        """
        Reduce player life by 1.
        """
        self.__lifes -= 1

    def increment_num_shots(self):
        """
        Increment number of shots by 1.
        """
        self.__num_shots += 1

    def increment_num_hits(self):
        """
        Increment number of hits by 1.
        """
        self.__num_hits += 1

    def increment_score(self, astroid_scale):
        """
        Increment score depending on astroid scale.
        Smaller astroids result in a higher score.

        :param astroid_scale:
            Astroid scale.
        """
        self.__score -= (10 - astroid_scale) * 10

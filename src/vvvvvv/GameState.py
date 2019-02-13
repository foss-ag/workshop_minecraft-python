class GameState():

    def __init__(self):
        self.__quit_game = False
        # score parameters
        self.__bonus = 20
        self.__multiplier = 1
        self.__score = 0
        # obstacle parameters
        self.__obstacle_speed = 5
        self.__obstacle_prob = 1
        # if power_up_obstacles exceeds 10000 reset and power up obstacle parameters
        self.__power_up_obstacles = 0
        # list of current obstacles and powerups in the game
        self.__obstacles = []
        self.__powerups = []

    @property
    def bonus(self):
        """
        Bonus that is added to the score every time the player hits the boundaries.
        """
        return self.__bonus

    @property
    def multiplier(self):
        """
        Score multiplier.
        """
        return self.__multiplier

    @property
    def obstacles(self):
        """
        List of current obstacles
        """
        return self.__obstacles

    @property
    def powerups(self):
        """
        List of current powerups.
        """
        return self.__powerups

    @property
    def obstacle_prob(self):
        """
        "Probability" for spawning new obstacles
        """
        return self.__obstacle_prob

    @property
    def obstacle_speed(self):
        """
        Obstacle movement speed
        """
        return self.__obstacle_speed

    @property
    def power_up_obstacles(self):
        """
        Score counter until next obstacle power up.
        """
        return self.__power_up_obstacles

    @property
    def score(self):
        """
        Player score.
        """
        return self.__score

    @property
    def quit(self):
        """
        Check if game is ended.
        """
        return self.__quit_game

    def add_powerup(self, powerup):
        """
        Add powerup to list of current powerups.

        :param powerup:
            New powerup object.
        """
        self.__powerups.append(powerup)

    def add_obstacle(self, obstacle):
        """
        Add obstacle to list of current obstacles.

        :param obstacle:
            New obstacle object
        """
        self.__obstacles.append(obstacle)

    def remove_powerups(self, powerup):
        """
        Remove powerup from list of current powerups.
        """
        self.__powerups.remove(powerup)

    def remove_obstacle(self, obstacle):
        """
        Remove obstacle from list of current obstacles.
        """
        self.__obstacles.remove(obstacle)

    def reset_multiplier(self):
        """
        Reset multiplier to 1.
        """
        self.__multiplier = 1

    def reset_power_up_obstacles(self):
        """
        Decrease power_up_obstacles counter by 10000
        """
        self.__power_up_obstacles -= 10000

    def set_multiplier(self, multiplier):
        """
        Set score multiplier.

        :param multiplier:
            New score multiplier.
        """
        self.__multiplier = multiplier

    def increase_multiplier(self, x):
        """
        Increase score multiplier by x.

        :param x:
            Integer
        """
        self.__multiplier += x

    def increase_obstacle_speed(self):
        """
        Increase obstacle speed by 1
        """
        self.__obstacle_speed += 1

    def increase_score(self):
        """
        Increase player score by multiplier * bonus
        """
        self.__score += self.__multiplier * self.__bonus
        self.__power_up_obstacles += self.__multiplier * self.__bonus

    def increase_obstacle_prob(self):
        """
        Increase obstacle_prob by 1
        """
        self.__obstacle_prob += 1

    def quit_game(self):
        """
        Set quit_game to True.
        """
        self.__quit_game = True

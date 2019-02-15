import csv

class GameState():

    def __init__(self):
        self.__quit_game = False
        # score parameters
        self.__bonus = 20
        self.__multiplier = 1
        self.__score = 0
        self.__nick = 'AAA'
        # obstacle parameters
        self.__obstacle_speed = 5
        self.__obstacle_prob = 1
        # if power_up_obstacles exceeds 10000 reset and power up obstacle parameters
        self.__power_up_obstacles = 0
        # list of current obstacles and powerups in the game
        self.__obstacles = []
        self.__powerups = []
        # load nick names and scores from highscore file
        self.__nicks, self.__scores = self.__load_highscore("highscore.csv")
        # update highscore
        self.__update_highscore = True
        # rank of new highscore
        self.__highscore_pos = None
        # check if player reached new highscore
        self.__new_highscore = False
        # check if player needs to input nick
        self.__input_nick = True
        # character position while nick input
        self.__nick_pos = 0
        # possible nick characters
        self.__chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%*+=-_'

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

    @property
    def new_highscore(self):
        """
        Player reached new highscore.
        """
        # if new_highscore is already set to True do not check again
        if self.__new_highscore:
            return self.__new_highscore
        self.__new_highscore = self.score > self.scores[-1]
        return self.__new_highscore

    @property
    def scores(self):
        """
        Highscore scores
        """
        return self.__scores

    @property
    def nicks(self):
        """
        Highscore nicks
        """
        return self.__nicks

    @property
    def input_nick(self):
        """
        Check if player needs to input nick
        """
        return self.__input_nick

    @property
    def nick_pos(self):
        """
        Current character position for nick input
        """
        return self.__nick_pos

    @property
    def update_highscore(self):
        """
        True if update wasn't updated yet, False otherwise
        """
        return self.__update_highscore

    def next_char(self):
        """
        Go to next character in nick at nick_pos
        """
        char_pos = self.__chars.index(self.__nick[self.__nick_pos]) + 1
        if char_pos >= len(self.__chars):
            char_pos = 0
        prefix = self.__nick[:self.__nick_pos]
        postfix = self.__nick[self.__nick_pos+1:]
        self.__nick = prefix + self.__chars[char_pos] + postfix
        # update highscore
        self.add_highscore_entry()

    def prev_char(self):
        """
        Go to previous character in nick at nick_pos
        """
        char_pos = self.__chars.index(self.__nick[self.__nick_pos]) - 1
        if char_pos < 0:
            char_pos = len(self.__chars) - 1
        prefix = self.__nick[:self.__nick_pos]
        postfix = self.__nick[self.__nick_pos+1:]
        self.__nick = prefix + self.__chars[char_pos] + postfix
        # update highscore
        self.add_highscore_entry()

    def next_nick_pos(self):
        """
        Increase character position for nick input
        """
        if self.__nick_pos < 2:
            self.__nick_pos += 1

    def prev_nick_pos(self):
        """
        Decrease character position for nick input
        """
        if self.__nick_pos > 0:
            self.__nick_pos -= 1

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

    def remove_powerup(self, powerup):
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

    def add_highscore_entry(self):
        """
        Add new highscore entry (nick, score).
        """
        if self.__highscore_pos is None:
            self.__highscore_pos = [self.__score > s for s in self.__scores].index(True)
        self.__nicks.insert(self.__highscore_pos, self.__nick)
        self.__nicks = self.__nicks[:-1]
        self.__scores.insert(self.__highscore_pos, self.__score)
        self.__scores = self.__scores[:-1]

    def quit_game(self):
        """
        Set quit_game to True.
        """
        self.__quit_game = True

    def highscore_updated(self):
        """
        Set update_highscore to False
        """
        self.__update_highscore = False

    def set_nick(self):
        """
        Set input_nick to False
        """
        self.__input_nick = False
        self.__write_highscore('highscore.csv')

    def __write_highscore(self, file):
        """
        Write highscore to csv file

        :param file:
            csv file containing nicknames and highscore
        """
        with open(file, 'w') as f:
            writer = csv.writer(f)
            # write entries to file
            for entry in zip(self.__nicks, self.__scores):
                writer.writerow (entry)
        f.close()

    def __load_highscore(self, file):
        """
        Load highscore from csv file,

        :param file:
            csv file containing nicknames and highscores
        :return:
            Loaded highscore.
        """
        nicks = []
        scores = []
        with open(file) as f:
            top_ten = csv.reader(f)
            # read first ten entries and ignore the remaining
            for nick, score in top_ten:
                nicks.append(nick)
                scores.append(int(score))
                if len(nicks) == 10:
                    break
            f.close()
        return nicks, scores

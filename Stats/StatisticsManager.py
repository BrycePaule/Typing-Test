import pygame

from Settings import BG_COLOR

from Stats.Timer import Timer
from Stats.WordCounter import WordCounter


class StatisticsManager():

    """ Middle man class for all statistics.  Timer / WPM / Accuracy. """

    def __init__(self):
        self.timer = Timer()
        self.counter = WordCounter()

        self.surface = pygame.Surface((150, 300))


    def update(self, typed_word_count):
        self.counter.update(self.timer.curr_time, typed_word_count)


    def draw(self):
        self.surface.fill(BG_COLOR)

        self.surface.blit(self.timer.draw(), (0, 0))
        self.surface.blit(self.counter.draw(), (0, 30))

        return self.surface


    def check_timer(self):
        """ Checks the current timer, returns True if finished, False if not. """

        return self.timer.is_time_up()


    def reset(self):
        """ Resets all stats classes. """

        self.__init__()
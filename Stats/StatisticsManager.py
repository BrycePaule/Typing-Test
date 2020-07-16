import pygame

from Settings import BG_COLOR

from Stats.Timer import Timer
from Stats.WPMCalculator import WPMCalculator
from Stats.Accuracy import Accuracy


class StatisticsManager():

    """ Middle man class for all statistics.  Timer / WPM / Accuracy. """

    def __init__(self):
        self.timer = Timer()
        self.WPM = WPMCalculator()
        self.accuracy = Accuracy()

        self.cache_timer = None
        self.cache_WPM = None
        self.cache_accuracy = None

        self.surface = pygame.Surface((150, 300))


    def update(self, typed_word_count, results):
        self.WPM.update(self.timer.curr_time, typed_word_count)
        self.accuracy.update(results)


    def draw(self):
        self.surface.fill(BG_COLOR)

        self.surface.blit(self.timer.draw(), (0, 0))
        self.surface.blit(self.WPM.draw(), (0, 30))
        self.surface.blit(self.accuracy.draw(), (0, 60))

        return self.surface


    def check_timer(self):
        """ Checks the current timer, returns True if finished, False if not. """

        return self.timer.is_time_up()


    def reset(self):
        """ Resets all stats classes, caches previous results"""

        self.cache_timer = self.timer.curr_time_in_seconds
        self.cache_WPM = self.WPM.wpm
        self.cache_accuracy = self.accuracy.accuracy

        self.timer.__init__()
        self.WPM.__init__()
        self.accuracy.__init__()
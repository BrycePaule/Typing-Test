import pygame

from Settings import BG_COLOR

from Stats.Timer import Timer
from Stats.WordCounter import WordCounter
from Stats.Accuracy import Accuracy


class StatisticsManager():

    """ Middle man class for all statistics.  Timer / WPM / Accuracy. """

    def __init__(self):
        self.timer = Timer()
        self.counter = WordCounter()
        self.accuracy = Accuracy()

        self.surface = pygame.Surface((150, 300))


    def update(self, typed_word_count, keystrokes):
        self.counter.update(self.timer.curr_time, typed_word_count)
        self.accuracy.update(keystrokes)


    def draw(self):
        self.surface.fill(BG_COLOR)

        self.surface.blit(self.timer.draw(), (0, 0))
        self.surface.blit(self.counter.draw(), (0, 30))
        self.surface.blit(self.accuracy.draw(), (0, 60))

        return self.surface


    def check_timer(self):
        """ Checks the current timer, returns True if finished, False if not. """

        return self.timer.is_time_up()


    def set_accuracy_text(self, text):
        self.accuracy.text = text


    def reset(self):
        """ Resets all stats classes. """

        self.__init__()
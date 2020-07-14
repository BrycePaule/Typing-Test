import pygame

from Settings import FONT
from Settings import BG_COLOR, TEXT_MAIN


class Timer():

    """
    Times runs of the typing tester, counts backwards from given interval time.
    """

    def __init__(self):
        self.start_time = 0
        self.interval = 60000

        self.active = False
        self.curr_time = 0
        self.curr_time_in_seconds = '0 s'

        self.surface = pygame.Surface((100, 100))


    def draw(self):
        self.surface.fill(BG_COLOR)

        time_text = FONT.render(self.curr_time_in_seconds, 1, TEXT_MAIN)
        self.surface.blit(time_text, (0, 0))

        return self.surface


    def start(self):
        """ Starts the timer. """

        self.active = True
        self.start_time = pygame.time.get_ticks()


    def stop(self):
        """ Sets timer to inactive. """

        self.active = False


    def is_time_up(self):
        """
        If timer is active, checks the current time.

        :returns
        True if completed.
        False if still going.
        """

        if self.active:
            now = pygame.time.get_ticks()
            dt = now - self.start_time

            self.curr_time = dt
            self.curr_time_in_seconds = self.convert_ticks_to_time(dt)

            if dt > self.interval:
                self.active = False
                return True

            else:
                return False


    def convert_ticks_to_time(self, milliseconds):
        """ Converts timer in ticks to printable strings for display. """

        dec_places = 1

        milli = milliseconds
        seconds = milli // 1000
        milli -= seconds

        if milli < 1000:
            return f'{seconds}.{str(milli)[-3:-3 + dec_places]} s'
        else:
            return f'{seconds}.{str(milli)[-3:-3 + dec_places]} s'
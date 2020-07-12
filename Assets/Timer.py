import pygame

from Assets.Settings import FONT
from Assets.Settings import BG_COLOR, TEXT_MAIN


class Timer():

    def __init__(self):
        self.start_time = 0
        self.interval = 30000

        self.active = False
        self.curr_time_in_seconds = '0'

        self.surface = pygame.Surface((100, 100))


    def draw(self):
        self.surface.fill(BG_COLOR)

        time_text = FONT.render(self.curr_time_in_seconds, 1, TEXT_MAIN)
        self.surface.blit(time_text, (0, 0))

        return self.surface


    def start(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()


    def is_time_up(self):
        if self.active:
            now = pygame.time.get_ticks()
            dt = now - self.start_time

            self.curr_time_in_seconds = self.convert_ticks_to_time(dt)

            if dt > self.interval:
                self.active = False
                return True

            else:
                return False


    def convert_ticks_to_time(self, milliseconds):
        """ DOESN'T WORK CURRENTLY """

        dec_places = 1

        milli = milliseconds
        seconds = milli // 1000
        milli -= seconds

        if milli < 1000:
            return f'{seconds}.{str(milli)[0:dec_places]}'
        else:
            return f'{seconds}.{str(milli)[1:dec_places + 1]}'
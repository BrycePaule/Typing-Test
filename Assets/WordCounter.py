import pygame

from Assets.Settings import BG_COLOR, TEXT_MAIN
from Assets.Settings import FONT


class WordCounter():


    def __init__(self):
        self.word_count = 0
        self.time = 0
        self.wpm = 0

        self.surface = pygame.Surface((100, 100))


    def update(self):
        self.calculate_wpm()


    def draw(self):
        self.surface.fill(BG_COLOR)

        time_text = FONT.render(str(self.wpm), 1, TEXT_MAIN)
        self.surface.blit(time_text, (0, 0))

        return self.surface

    def calculate_wpm(self):

        minutes = round(self.time / 60000, ndigits=2)

        print(self.word_count)
        print(minutes)
        if self.word_count != 0:
            print(self.word_count / minutes)


        if self.word_count == 0:
            return 0
        self.wpm = int(round(self.word_count / minutes))
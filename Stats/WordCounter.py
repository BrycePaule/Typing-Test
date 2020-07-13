import pygame

from Settings import BG_COLOR, TEXT_MAIN
from Settings import FONT


class WordCounter():


    def __init__(self):
        self.word_count = 0
        self.time = 0
        self.wpm = 0

        self.surface = pygame.Surface((100, 100))


    def update(self, time, typed_word_count):
        self.time = time
        self.word_count = typed_word_count

        self.calculate_wpm()


    def draw(self):
        self.surface.fill(BG_COLOR)

        time_text = FONT.render(f'{self.wpm} wpm', 1, TEXT_MAIN)
        self.surface.blit(time_text, (0, 0))

        return self.surface


    def calculate_wpm(self):
        if self.word_count == 0: return 0
        if self.time == 0: return 0

        self.wpm = int(round(self.word_count * (60000 / self.time), ndigits=0))
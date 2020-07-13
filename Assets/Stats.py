import pygame

from Assets.Settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.Settings import BG_COLOR

from Assets.Timer import Timer
from Assets.WordCounter import WordCounter


class Stats():


    def __init__(self):
        self.timer = Timer()
        self.counter = WordCounter()

        self.surface = pygame.Surface((150, 300))


    def update(self):
        self.counter.update()


    def draw(self):
        self.surface.fill(BG_COLOR)

        self.surface.blit(self.timer.draw(), (0, 0))
        self.surface.blit(self.counter.draw(), (0, 30))

        return self.surface
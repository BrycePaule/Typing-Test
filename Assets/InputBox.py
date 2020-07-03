import pygame

from Assets.Settings import INPUT_BOX_COLOR

class InputBox():

    def __init__(self):
        self.width = 200
        self.height = 50

        self.surface = pygame.Surface((self.width, self.height))


    def update(self):
        pass


    def draw(self):
        self.surface.fill(INPUT_BOX_COLOR)

        return self.surface
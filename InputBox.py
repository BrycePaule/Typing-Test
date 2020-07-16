import pygame

from Settings import BG_COLOR, INPUT_BOX_COLOR
from Settings import FONT
from Settings import TEXT_MAIN



class InputBox():

    def __init__(self):
        self.width = 600
        self.height = 40

        self.surface = pygame.Surface((self.width, self.height))

        self.current_typed_word = ''


    def update(self, current_typed_word):
        self.current_typed_word = current_typed_word


    def draw(self):
        self.surface.fill(BG_COLOR)
        pygame.draw.rect(self.surface, INPUT_BOX_COLOR, (0, 0, self.width, self.height), border_radius=10)

        word_text = FONT.render(self.current_typed_word, True, TEXT_MAIN)
        self.surface.blit(word_text, (self.width / 2 - word_text.get_width() / 2, self.height / 2 - word_text.get_height() / 2))

        return self.surface
import os
import pygame

from Settings import BG_COLOR


class Keyboard():
    """ Handles everything to do with the visual keyboard. """


    def __init__(self):

        self.key_filepath = 'D:/Scripts/Python/TypingTest/Assets/Sprites/Keycaps/'

        self.key_size = 40
        self.gap_size = 5
        self.width = self.key_size * 10 + (self.gap_size * 9)
        self.height = self.key_size * 3 + (self.gap_size * 3)

        self.surface = pygame.Surface((self.width, self.height))

        self.keys_main = self.import_keys_main()
        self.keys_highlight = self.import_keys_highlight()


    def draw(self):
        self.surface.fill(BG_COLOR)
        self.surface.blit(self.keys_main[97], (0, 0))

        return self.surface


    def import_keys_main(self):
        keys = os.listdir(f'{self.key_filepath}Main/')

        key_dict = {}
        for index, key in enumerate(keys):
            key_dict[index + 97] = pygame.image.load(f'{self.key_filepath}Main/{key}')

        return key_dict


    def import_keys_highlight(self):
        keys = os.listdir(f'{self.key_filepath}Highlight/')

        key_dict = {}
        for index, key in enumerate(keys):
            key_dict[index + 97] = pygame.image.load(
                f'{self.key_filepath}Highlight/{key}')

        return key_dict
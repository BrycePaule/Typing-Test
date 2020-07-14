import os
import pygame

from Settings import BG_COLOR


class Keyboard():
    """ Handles everything to do with the visual keyboard. """


    def __init__(self):

        self.key_filepath = 'D:/Scripts/Python/TypingTest/Assets/Sprites/Keycaps/'

        self.key_size = 40
        self.gap_size = 1
        self.width = self.key_size * 10 + (self.gap_size * 9)
        self.height = self.key_size * 3 + (self.gap_size * 2)

        self.surface = pygame.Surface((self.width, self.height))

        self.keys_main = self.import_keys_main()
        self.keys_highlight = self.import_keys_highlight()
        self.keys_order = [
            113, 119, 101, 114, 116, 121, 117, 105, 111, 112,
            97, 115, 100, 102, 103, 104, 106, 107, 108,
            122, 120, 99, 118, 98, 110, 109,
        ]

        self.key_highlight_frames = 20
        self.keys_pressed = []


    def update(self):
        if len(self.keys_pressed) > 1:
            self.keys_pressed = [[key_num, timer - 1] for key_num, timer in self.keys_pressed if (timer - 1) > 0]
        else:
            self.keys_pressed = [[key_num, timer - 1] for key_num, timer in self.keys_pressed if (timer - 1) > -self.key_highlight_frames * 5]


    def draw(self):
        self.surface.fill(BG_COLOR)

        for index, key in enumerate(self.keys_order[:10]):
            if key in [key_num for key_num, timer in self.keys_pressed]:
                self.surface.blit(self.keys_highlight[key], (self.key_size * index + (self.gap_size * index), 0))
            else:
                self.surface.blit(self.keys_main[key], (self.key_size * index + (self.gap_size * index), 0))

        for index, key in enumerate(self.keys_order[10:19]):
            if key in [key_num for key_num, timer in self.keys_pressed]:
                self.surface.blit(self.keys_highlight[key], (self.key_size * index + (self.gap_size * index) + (self.key_size / 2), self.key_size + self.gap_size))
            else:
                self.surface.blit(self.keys_main[key], (self.key_size * index + (self.gap_size * index) + (self.key_size / 2), self.key_size + self.gap_size))

        for index, key in enumerate(self.keys_order[19:]):
            if key in [key_num for key_num, timer in self.keys_pressed]:
                self.surface.blit(self.keys_highlight[key], (self.key_size * index + (self.gap_size * index) + (self.key_size * 3 / 2), self.key_size * 2 + self.gap_size * 2))
            else:
                self.surface.blit(self.keys_main[key], (self.key_size * index + (self.gap_size * index) + (self.key_size * 3 / 2), self.key_size * 2 + self.gap_size * 2))

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


    def add_key_press(self, key_num):
        self.keys_pressed.append([key_num, self.key_highlight_frames])
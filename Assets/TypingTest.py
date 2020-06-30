import os
import pygame

from Assets.Settings import *


class TypingTest():

    """ main game class, contains game loop """

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Typing Test')

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (window_x, window_y)


    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    """ GAME LOGIC """
    def start_game(self):
        self.loop()


    def loop(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

            self.screen.fill((215, 175, 255))

            pygame.display.update()


    """ TESTERS """
    def read_in_words(self, lower=False):
        index = 1
        word_dict = {}

        with open(WORD_LIST_FILEPATH, 'r') as f:
            for line in f:
                if lower:
                    line = line.lower()
                word_dict[index] = line
                index += 1

        return word_dict


    def print_word_list(self):
        words = self.read_in_words(lower=True)

        for word in words:
            print(f'{word} {words[word]}')
import os
import pygame

from Assets.Settings import *
from Assets.TextManager import TextManager
from Assets.BlurbBox import BlurbBox


class TypingTest():

    """ Main game class, contains game loop """

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Typing Test')

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (WINDOW_X, WINDOW_Y)


    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.text_manager = TextManager()
        self.blurb_box = BlurbBox()


    """ GAME LOGIC """

    def start_game(self):
        """ Initialises game variables. """

        self.blurb_box.blurb = self.text_manager.create_random_blurb()
        self.blurb_box.convert_blurb_to_lines()
        self.main_loop()


    def main_loop(self):
        """ Main game loop. """

        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

            self.screen.fill(BG_COLOR)
            self.draw_blurb_box()

            pygame.display.update()


    def draw_blurb_box(self):
        self.screen.blit(self.blurb_box.draw(),
                         ((SCREEN_WIDTH / 2) - (self.blurb_box.width / 2),
                          (SCREEN_HEIGHT / 2) - self.blurb_box.height))


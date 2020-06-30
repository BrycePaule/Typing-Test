import os
import pygame

from Assets.Settings import *
from Assets.TextManager import TextManager


class TypingTest():

    """ main game class, contains game loop """

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Typing Test')

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (window_x, window_y)


    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.text_manager = TextManager()
        self.burb = None


    """ GAME LOGIC """
    def start_game(self):
        """ Initialises game variables. """

        self.blurb = self.text_manager.create_random_blurb()
        self.loop()


    def loop(self):
        """ Main game loop. """

        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

            self.screen.fill((215, 175, 255))
            self.blurb_box()

            pygame.display.update()


    def blurb_box(self):
        box_width = 500
        box_height = 200

        blurb_box = pygame.Surface((500, 200))
        blurb_box.fill((255, 255, 255))


        font = pygame.font.SysFont('Arial', 12)
        text = font.render(self.blurb, 1, (255, 0, 0))
        blurb_box.blit(text, (50, 50))

        self.screen.blit(blurb_box,
                         ((SCREEN_WIDTH / 2) - (box_width / 2),
                          (SCREEN_HEIGHT / 2) - box_height))


import os
import pygame

from Assets.Settings import *

from Assets.TextManager import TextManager
from Assets.Blurb import Blurb
from Assets.InputBox import InputBox
from Assets.InputManager import InputManager
from Assets.Timer import Timer
from Assets.Stats import Stats


class Type():

    """ Main game class, contains game loop """

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Typing Test')

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (WINDOW_X, WINDOW_Y)


    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.blurb = Blurb()
        self.input_box = InputBox()

        self.text_manager = TextManager()
        self.input_manager = InputManager(self.blurb)

        self.stat_tracker = Stats()


    """ GAME LOGIC """

    def start_game(self):
        """ Initialises game variables. """

        self.blurb.text = self.text_manager.create_random_blurb()
        self.blurb.convert_text_to_state_pairs()

        self.stat_tracker.timer.start()
        self.main_loop()


    def main_loop(self):
        """ Main game loop. """

        while True:
            self.clock.tick(FPS)

            self.input_manager.handle_events()
            self.blurb.update()
            self.stat_tracker.update()
            self.stat_tracker.counter.word_count = self.blurb.word_count
            self.stat_tracker.counter.time = self.stat_tracker.timer.curr_time
            if self.stat_tracker.timer.is_time_up():
                break

            self.screen.fill(BG_COLOR)
            self.draw_blurb_box()
            self.draw_stats()

            pygame.display.update()


    def draw_blurb_box(self):
        self.screen.blit(
            self.blurb.draw(),
            ((SCREEN_WIDTH / 2) - (self.blurb.width / 2),
            (SCREEN_HEIGHT / 2) - self.blurb.height))


    def draw_stats(self):
        self.screen.blit(
            self.stat_tracker.draw(),
            (SCREEN_WIDTH - (SCREEN_WIDTH / 8),
             SCREEN_HEIGHT - 7 * (SCREEN_HEIGHT / 8)))


    def draw_input_box(self):
        self.screen.blit(
            self.input_box.draw(),
            ((SCREEN_WIDTH / 2) - (self.input_box.width / 2),
            (SCREEN_HEIGHT / 2) - self.input_box.height / 2))
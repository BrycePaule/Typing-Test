import os

from Settings import *

from TextManager import TextManager
from Blurb import Blurb
from InputBox import InputBox
from InputManager import InputManager
from Stats.StatisticsManager import StatisticsManager
from Keyboard.Keyboard import Keyboard


class Type():

    """ Main game class, contains game loop """

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Typing Test')

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (WINDOW_X, WINDOW_Y)


    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.text_manager = TextManager()
        self.blurb = Blurb(self.text_manager.create_random_blurb())
        self.stat_tracker = StatisticsManager()
        self.keyboard = Keyboard()
        self.input_manager = InputManager(self)
        self.running = False


    """ GAME LOGIC """

    def setup_game(self):
        """ Initialises game variables. """

        self.running = False
        self.blurb.words = self.text_manager.create_random_blurb()
        self.blurb.convert_words_to_state_pairs()
        self.main_loop()


    def start_game(self):
        """ Resets stats and starts a new game. """

        # self.reset()
        # self.stat_tracker.timer.start()
        # self.stat_tracker.set_accuracy_text(self.blurb.words)
        self.running = True
        self.main_loop()


    def stop_game(self):
        """ Stops the current game, halts timer, DOESN'T reset. """

        # self.stat_tracker.timer.stop()
        self.running = False
        self.main_loop()


    def main_loop(self):
        """ Main game loop. """

        while True:
            self.clock.tick(FPS)

            # check finish blurb
            if self.blurb.index >= self.blurb.max_words - 1:
                self.blurb.words = self.text_manager.create_random_blurb()
                # self.stat_tracker.set_accuracy_text(self.blurb.words)
                self.blurb.results = ''

            # check finished
            # if self.stat_tracker.check_timer():
            #     print(f'WPM: {self.stat_tracker.counter.wpm}')
            #     self.stop_game()

            # updates
            self.input_manager.handle_events()
            self.keyboard.update()
            self.blurb.update()
            # self.stat_tracker.update(self.blurb.completed_word_count, self.blurb.keystrokes)

            # draw
            self.screen.fill(BG_COLOR)
            self.draw_blurb_box()
            # self.draw_stats()
            self.draw_keyboard()

            pygame.display.update()


    """ DRAWING """

    def draw_blurb_box(self):
        """ Draw the blurb. """

        self.screen.blit(
            self.blurb.draw(),
            (SCREEN_WIDTH / 2 - self.blurb.width / 2, SCREEN_HEIGHT / 2 - self.blurb.height)
        )


    def draw_stats(self):
        """ Draws all stats.  Stats manages wpm / timer / accuracy. """

        self.screen.blit(
            self.stat_tracker.draw(),
            (SCREEN_WIDTH - SCREEN_WIDTH / 8, SCREEN_HEIGHT - 7 * SCREEN_HEIGHT / 8)
        )


    def draw_keyboard(self):
        """ Draws the on screen keyboard. """

        self.screen.blit(
            self.keyboard.draw(),
            (SCREEN_WIDTH / 2 - self.keyboard.width / 2, SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 8)
        )


    """ UTILITIES """

    def reset(self):
        """
        Resets the stat tracker, intended for multiple runs in the same session.

        TODO: rework so it carries over accuracy / wpm etc
        """
        self.stat_tracker.__init__()
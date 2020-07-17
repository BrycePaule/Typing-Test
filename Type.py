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
        self.stat_manager = StatisticsManager()
        self.keyboard = Keyboard()
        self.input_manager = InputManager(self)
        self.input_box = InputBox()

        self.running = False
        self.first_run = True


    """ GAME LOGIC """

    def setup_game(self):
        """ Initialises game variables. """

        self.running = False
        self.main_loop()


    def start_game(self):
        """ Resets stats and starts a new game. """

        self.running = True

        if self.first_run:
            self.first_run = False
        elif not self.first_run:
            self.reset_game()

        self.stat_manager.timer.start()


    def stop_game(self):
        """ Stops the current game, halts timer, DOESN'T reset. """

        self.stat_manager.timer.stop()
        self.running = False


    def reset_game(self):
        """ Resets game variables to run again, for multiple games. """

        self.blurb.__init__(self.text_manager.create_random_blurb())
        self.stat_manager.reset()


    def main_loop(self):
        """ Main game loop. """

        while True:
            self.clock.tick(FPS)

            # check finished
            if self.running:

                if self.stat_manager.check_timer():
                    self.stop_game()

                if self.blurb.finished:
                    self.stop_game()

            # updates
            self.input_manager.handle_events()
            self.keyboard.update()
            self.blurb.update()
            self.input_box.update(self.blurb.current_word_typed)
            self.stat_manager.update(self.blurb.completed_word_count, self.blurb.results)

            # draw
            self.screen.fill(BG_COLOR)
            lower_bound = self.draw_blurb_box()
            self.draw_input_box(lower_bound)
            self.draw_stats()
            self.draw_keyboard()

            # print(str(int(self.clock.get_fps())))

            pygame.display.update()


    """ DRAWING """

    def draw_blurb_box(self):
        """ Draw the blurb. """

        self.screen.blit(
            self.blurb.draw(),
            (SCREEN_WIDTH / 2 - self.blurb.width / 2, 30)
        )

        return self.blurb.height + 30


    def draw_input_box(self, blurb_lower_bound):
        """ Draw the input box just under blurb. """

        blurb_lower_bound_y = blurb_lower_bound

        self.screen.blit(
            self.input_box.draw(),
            (SCREEN_WIDTH / 2 - self.input_box.width / 2, blurb_lower_bound_y + 5)
        )


    def draw_stats(self):
        """ Draws all stats.  Stats manages wpm / timer / accuracy. """

        self.screen.blit(
            self.stat_manager.draw(),
            (SCREEN_WIDTH - SCREEN_WIDTH / 8, SCREEN_HEIGHT - 7 * SCREEN_HEIGHT / 8)
        )


    def draw_keyboard(self):
        """ Draws the on screen keyboard. """

        self.screen.blit(
            self.keyboard.draw(),
            (SCREEN_WIDTH / 2 - self.keyboard.width / 2, SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 8)
        )


    """ UTILITIES """


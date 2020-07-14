import os

from Settings import *

from TextManager import TextManager
from Blurb import Blurb
from InputBox import InputBox
from InputManager import InputManager
from Stats.Stats import Stats
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

        self.blurb = Blurb()
        self.input_box = InputBox()

        self.text_manager = TextManager()
        self.stat_tracker = Stats()
        self.keyboard = Keyboard()
        self.input_manager = InputManager(self)
        self.running = False


    """ GAME LOGIC """

    def setup_game(self):
        """ Initialises game variables. """

        self.running = False
        self.blurb.text = self.text_manager.create_random_blurb()
        self.blurb.convert_text_to_state_pairs()
        self.main_loop()


    def start_game(self):
        self.reset()
        self.stat_tracker.timer.start()
        self.running = True
        self.main_loop()


    def stop_game(self):
        self.stat_tracker.timer.stop()
        self.running = False
        self.main_loop()


    def main_loop(self):
        """ Main game loop. """

        while True:
            self.clock.tick(FPS)

            # check finish blurb
            if self.blurb.current_index >= len(self.blurb.text) - 1:
                self.blurb.text = self.text_manager.create_random_blurb()
                self.blurb.keystrokes = ''
                self.blurb.convert_text_to_state_pairs()

            # check finished
            if self.stat_tracker.check_timer():
                print(f'WPM: {self.stat_tracker.counter.wpm}')
                self.stop_game()

            # updates
            self.input_manager.handle_events()
            self.keyboard.update()
            self.blurb.update()
            self.stat_tracker.update(self.blurb.word_count)

            # draw
            self.screen.fill(BG_COLOR)
            self.draw_blurb_box()
            self.draw_stats()
            self.draw_keyboard()

            pygame.display.update()


    def draw_blurb_box(self):
        self.screen.blit(
            self.blurb.draw(),
            (SCREEN_WIDTH / 2 - self.blurb.width / 2,
             SCREEN_HEIGHT / 2 - self.blurb.height))


    def draw_stats(self):
        self.screen.blit(
            self.stat_tracker.draw(),
            (SCREEN_WIDTH - SCREEN_WIDTH / 8,
             SCREEN_HEIGHT - 7 * SCREEN_HEIGHT / 8))


    def draw_keyboard(self):
        self.screen.blit(
            self.keyboard.draw(),
            (SCREEN_WIDTH / 2 - self.keyboard.width / 2,
             SCREEN_HEIGHT - 3 * SCREEN_HEIGHT / 8))


    def reset(self):
        self.stat_tracker.__init__()


    # def draw_input_box(self):
    #     self.screen.blit(
    #         self.input_box.draw(),
    #         ((SCREEN_WIDTH / 2) - (self.input_box.width / 2),
    #         (SCREEN_HEIGHT / 2) - self.input_box.height / 2))
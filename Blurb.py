import pygame

from Settings import FONT, BG_COLOR
from Settings import TEXT_MAIN, TEXT_HIGHLIGHT, TEXT_CORRECT, TEXT_INCORRECT


class Blurb():

    """
    Blurb handler, responsible for updating and rendering the text the user
    has to type.
    """

    def __init__(self, words):
        self.width = 650
        self.height = 200
        self.surface = pygame.Surface((self.width, self.height))

        self.line_char_limit = 65
        self.max_words = 50

        self.words = words[:self.max_words]
        self.word_states = self.convert_words_to_state_pairs()

        self.state_colours = {
            0: pygame.Color('BLUE'),
            1: TEXT_MAIN,
            2: TEXT_CORRECT,
            3: TEXT_INCORRECT,
            4: TEXT_HIGHLIGHT,
        }

        self.index = 0
        self.current_word = self.words[0]
        self.current_word_typed = ''

        self.completed_word_count = 0
        self.results = []


    def update(self):
        # print(self.words)
        # print(f'{self.current_word}   {self.current_word_typed}')
        pass


    def draw(self):
        self.surface.fill(BG_COLOR)

        x_offset = 0
        y_offset = 0
        space_width = 10
        line_height = 20

        for i, (word, state) in enumerate(self.word_states):

            if i > self.max_words: break

            if i == self.index:
                word_text = FONT.render(word, True, TEXT_HIGHLIGHT)
            else:
                word_text = FONT.render(word, True, self.state_colours[state])


            if x_offset + word_text.get_width() > self.width:
                x_offset = 0
                y_offset += line_height

            self.surface.blit(word_text, (x_offset, y_offset))
            x_offset += word_text.get_width() + space_width

        return self.surface


    def convert_words_to_state_pairs(self):
        """ Converts text into a list of [word, state] pairs. """

        return [[word, 1] for word in self.words]


    def mark_and_shift(self):
        """ Called by InputManager, marks current word and moves on.  """

        self.results.append([self.current_word, self.current_word_typed])
        self.completed_word_count = len(self.results)

        if self.current_word_typed == self.current_word:
            self.word_states[self.index][1] = 2
        else:
            self.word_states[self.index][1] = 3

        self.index += 1
        self.current_word = self.words[self.index]
        self.current_word_typed = ''
import pygame

from Settings import FONT, BG_COLOR
from Settings import TEXT_MAIN, TEXT_HIGHLIGHT, TEXT_CORRECT, TEXT_INCORRECT


class Blurb():

    """
    Blurb handler, responsible for updating and rendering the text the user
    has to type.
    """

    def __init__(self):
        self.width = 650
        self.height = 200
        self.surface = pygame.Surface((self.width, self.height))

        self.line_char_limit = 60
        self.text = None
        self.text_states = None
        self.lines = None

        self.state_colour = {
            0: TEXT_HIGHLIGHT,
            1: TEXT_MAIN,
            2: TEXT_CORRECT,
            3: TEXT_INCORRECT,
            4: TEXT_HIGHLIGHT,
        }

        self.current_index = 0
        self.prev_index = 0
        self.current_word = None

        self.word_count = 0
        self.keystrokes = ''


    def update(self):
        self.current_index = len(self.keystrokes)
        self.prev_index = self.current_index - 1

        print(self.current_index)
        print(len(self.text))

        if len(self.keystrokes):
            self.update_char_state()

        self.update_word_count()


    def draw(self):
        self.surface.fill(BG_COLOR)

        xpos = 10
        ypos = 10
        line_height = 20

        x_offset = 0
        y_offset = 0

        for index, (character, state) in enumerate(self.text_states):

            current_word = self.get_current_word(index)

            # update x_offset / y_offset
            line = index // self.line_char_limit
            cum_line_limit = (line + 1) * self.line_char_limit

            y_offset = (index // self.line_char_limit) * line_height
            if index + len(current_word) > cum_line_limit:
                y_offset += line_height
                if x_offset > 300:
                    x_offset = 0


            # # TESTING -----------------------------------------------
            # if index == self.current_index:
            #     print(f'{index} "{current_word}" {cum_line_limit} - {line} {y_offset} {x_offset}  |||  {index + len(current_word) > cum_line_limit}  |||  {current_word == ""}  |||')
            # # -------------------------------------------------------

            char = FONT.render(character, True, self.state_colour[state])
            self.surface.blit(char, (xpos + x_offset, ypos + y_offset))

            # catches end of line spaces
            if character == ' ':
                if index == cum_line_limit - self.line_char_limit:
                    y_offset += line_height
                    x_offset = 0
                elif index == cum_line_limit - 1:
                    y_offset += line_height
                    x_offset = 0

            # offset each letter by the previous letter's width
            *_, char_width = FONT.metrics(character)[0]
            x_offset += char_width

        return self.surface


    def get_current_word(self, index):
        """ Returns the current word """

        return self.text[index:].split(' ')[0]


    def convert_text_to_state_pairs(self):
        """ Converts text into a list of (char, state) pairs. """

        self.text_states = [[char, 1] for char in self.text]


    def update_char_state(self):
        """ Colours the typed character based on correctness """

        self.text_states[self.current_index][1] = 4

        if self.keystrokes[self.prev_index] == self.text[self.prev_index]:
            self.text_states[self.prev_index] = [self.text_states[self.prev_index][0], 2]
        else:
            self.text_states[self.prev_index] = [self.text_states[self.prev_index][0], 3]


    def backspace_recolour(self):
        """ Resets backspaced character's state back to default. """

        self.text_states[self.current_index][1] = 1


    def update_word_count(self):
        """ WORKS - currently counts the word you're typing as COMPLETE """

        words = [word for word in self.text[:self.current_index].split(' ') if word != '']

        if len(words) == 0:
            return 0
        else:
            self.word_count = len(words)
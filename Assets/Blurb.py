import pygame

from Assets.Settings import FONT, BG_COLOR

class Blurb():

    """
    Blurb handler, responsible for updating and rendering the text the user
    has to type.
    """

    def __init__(self):
        self.width = 600
        self.height = 200
        self.surface = pygame.Surface((self.width, self.height))

        self.line_char_limit = 80
        self.text = None
        self.text_states = None
        self.lines = None

        self.state_colour = {
            0: pygame.Color('white'),
            1: pygame.Color('black'),
            2: pygame.Color('green'),
            3: pygame.Color('red'),
            4: pygame.Color('white'),
        }

        self.current_index = 0
        self.prev_index = 0
        self.current_word = None

        self.keystrokes = ''



    def update(self):
        self.current_index = len(self.keystrokes)
        self.prev_index = self.current_index - 1

        self.text_states[self.current_index][1] = 4

        print(f'{self.current_index} {self.text[self.current_index]}')

        if len(self.keystrokes):
            if self.keystrokes[self.prev_index] == self.text[self.prev_index]:
                self.text_states[self.prev_index] = [self.text_states[self.prev_index][0], 2]
            else:
                self.text_states[self.prev_index] = [self.text_states[self.prev_index][0], 3]


    def draw(self):
        self.surface.fill(BG_COLOR)

        xpos = 10
        ypos = 10
        line_height = 20

        x_offset = 0
        y_offset = 0

        for index, (character, state) in enumerate(self.text_states):
            char = FONT.render(character, 1, self.state_colour[state])

            # calc y_offset, reset x_offset if end of line
            y_offset = (index // self.line_char_limit) * line_height
            if index % self.line_char_limit == 0:
                x_offset = 0

            self.surface.blit(char, (xpos + x_offset, ypos + y_offset))

            # offset each letter by the previous letter's width
            *_, char_width = FONT.metrics(character)[0]
            x_offset += char_width

        return self.surface


    def draw2(self):
        self.surface.fill(BG_COLOR)

        xpos = 10
        ypos = 10
        line_height = 20

        for index, line in enumerate(self.lines):
            chars_typed = line[:self.current_index]
            chars_remaining = line[self.current_index:]

            offset = sum(char_width for (_, _, _, _, char_width) in FONT.metrics(chars_typed))

            text = FONT.render(chars_remaining, 1, pygame.Color('black'))
            self.surface.blit(text, (xpos + offset, ypos + (line_height * index)))

            text = FONT.render(chars_typed, 1, pygame.Color('red'))
            self.surface.blit(text, (xpos, ypos + (line_height * index)))

            # text = FONT.render(chars_typed, 1, pygame.Color('green'))
            # self.surface.blit(text, (xpos, ypos + (line_height * index)))


        return self.surface


    def draw3(self):
        self.surface.fill(BG_COLOR)

        line_lengths = [(len(line) - 1) for line in self.lines]

        xpos = 10
        ypos = 10
        line_height = 20

        x_offset = 0
        y_offset = 0
        current_line = 0

        for index, char in enumerate(self.text):
            chars_typed = self.text[:self.current_index]
            chars_remaining = self.text[self.current_index:]
            x_offset += FONT.metrics(char)[0][4]

            if index > line_lengths[current_line]:
                current_line += 1
                x_offset = 0

            text = FONT.render(char, 1, pygame.Color('black'))
            self.surface.blit(text, (xpos + x_offset, ypos + (line_height * current_line)))

        return self.surface


    # def convert_blurb_to_lines(self):
    #     """ Converts a blurb into lines long enough to print to screen.  """
    #
    #     self.lines = []
    #
    #     current_line = ''
    #     chars = 0
    #
    #     for word in self.text.split():
    #         if chars + len(word) > self.line_char_limit:
    #             self.lines.append(current_line)
    #             current_line = ''
    #             chars = 0
    #
    #         current_line += f'{word} '
    #         chars += len(word) + 1


    def convert_text_to_state_pairs(self):
        """ Converts text into a list of (char, state) pairs. """

        self.text_states = [[char, 1] for char in self.text]


    def backspace_recolour(self):
        """
        Called when user backspaces, resets any chars typed back to black.
        """

        self.text_states[self.current_index][1] = 1
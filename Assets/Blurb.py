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
        self.lines = None

        self.current_index = 0
        self.current_word = None

        self.keystrokes = ''


    def update(self):
        self.current_index = len(self.keystrokes)


    def draw(self):
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


    def convert_blurb_to_lines(self):
        """ Converts a blurb into lines long enough to print to screen.  """
        self.lines = []

        current_line = ''
        chars = 0

        for word in self.text.split():
            if chars + len(word) > self.line_char_limit:
                self.lines.append(current_line)
                current_line = ''
                chars = 0

            current_line += f'{word} '
            chars += len(word) + 1
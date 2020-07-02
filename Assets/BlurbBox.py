import pygame

from Assets.Settings import FONT, BG_COLOR

class BlurbBox():

    """
    Blurb handler, responsible for updating and rendering the text the user
    has to type.
    """

    def __init__(self):
        self.width = 600
        self.height = 200
        self.surface = pygame.Surface((self.width, self.height))

        self.line_char_limit = 80
        self.blurb = None
        self.lines = None


    def update(self):
        pass


    def draw(self):
        self.surface.fill(BG_COLOR)

        for index, line in enumerate(self.lines):
            text = FONT.render(line, 1, (0, 0, 0))
            self.surface.blit(text, (10, 10 + (20 * index)))

        return self.surface


    def convert_blurb_to_lines(self):
        """ Converts a blurb into lines long enough to print to screen.  """
        self.lines = []

        current_line = ''
        chars = 0

        for word in self.blurb.split():
            if chars + len(word) > self.line_char_limit:
                self.lines.append(current_line)
                current_line = ''
                chars = 0

            current_line += f'{word} '
            chars += len(word) + 1
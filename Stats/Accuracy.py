import pygame

from Settings import BG_COLOR, TEXT_MAIN
from Settings import FONT


class Accuracy():

    """ Handles calculating and displaying the user's typing accuracy. """


    def __init__(self):
        self.text = None
        self.keystrokes = None

        self.accuracy = 0

        self.surface = pygame.Surface((100, 100))


    def update(self, keystrokes):
        self.keystrokes = keystrokes

        if self.text is not None and self.keystrokes is not None:
            self.calculate_accuracy()


    def draw(self):
        self.surface.fill(BG_COLOR)

        accuracy = FONT.render(f'{self.accuracy} %', 1, TEXT_MAIN)
        self.surface.blit(accuracy, (0, 0))

        return self.surface


    def calculate_accuracy(self):
        """ Calculates letter accuracy percentage. """

        text_words = [word for word in self.text.split(' ')]
        typed_words = [word for word in self.keystrokes.split(' ')][:-1]

        typed_char_count = sum([len(char) for char in typed_words if char != ' '])
        correct_char_count = 0

        for i, word in enumerate(typed_words):

            # if word is correct
            if word == text_words[i]:
                correct_char_count += len(word)

            else:
                t_word = text_words[i]
                for j, char in enumerate(word):
                    if j <= len(t_word) - 1:
                        if char == text_words[i][j]:
                            correct_char_count += 1

                correct_char_count -= abs(len(word) - len(t_word))

        if correct_char_count != 0 and typed_char_count != 0:
            self.accuracy = int(round(correct_char_count / typed_char_count * 100))
        else:
            self.accuracy = 0
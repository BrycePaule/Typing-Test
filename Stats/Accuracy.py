import pygame

from Settings import BG_COLOR, TEXT_MAIN
from Settings import FONT


class Accuracy():

    """ Handles calculating and displaying the user's typing accuracy. """


    def __init__(self):
        self.results = None
        self.accuracy = 0

        self.surface = pygame.Surface((100, 100))


    def update(self, results):
        self.results = results
        self.calculate_accuracy()


    def draw(self):
        self.surface.fill(BG_COLOR)

        accuracy = FONT.render(f'{self.accuracy} %', 1, TEXT_MAIN)
        self.surface.blit(accuracy, (0, 0))

        return self.surface


    def calculate_accuracy(self):
        """
        Calculates letter accuracy percentage as:
            correct_chars / total_chars * 100

        Checks if word == typed_word, if not iterates through characters to
        find how many were correct.
        """

        if not self.results: return

        total_chars = sum(len(word) for word, _ in self.results)
        correct_chars = 0

        for word, t_word in self.results:
            if word == t_word:
                correct_chars += len(t_word)

            else:
                for i, char in enumerate(word):
                    if i < len(t_word):
                        if char == t_word[i]:
                            correct_chars += 1

                if diff := (len(t_word) - len(word)) > 0:
                    total_chars += diff


        self.accuracy = int(round(correct_chars / total_chars * 100))
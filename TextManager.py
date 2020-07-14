import random

from Settings import WORD_LIST_FILEPATH


class TextManager():

    """
    Responsible for everything to do with the word list, reads from file,
    creates random blurbs, etc.
    """

    def __init__(self):
        self.words = self.read_in_words(lower=True)
        self.word_count = len(self.words)
        self.blurb_char_limit = 110


    def read_in_words(self, lower=False):
        """ Reads in word list from .txt file """

        index = 0
        word_dict = {}

        with open(WORD_LIST_FILEPATH, 'r') as f:
            for line in f:
                if lower:
                    line = line.lower()
                word_dict[index] = line.strip()
                index += 1

        return word_dict


    def create_random_blurb(self):
        """
        Creates a random string of words.  Adds a space at the end to allow
        for transition to next blurb if player finishes the current blurb.
        """

        chars = 0
        text = ''

        while chars < self.blurb_char_limit:
            new_word = self.get_random_word()

            while new_word in text:
                new_word = self.get_random_word()

            text += f'{self.words[random.randint(0, self.word_count - 1)]} '
            chars = len(text)

        text += ' '
        return text


    def create_w_blurb(self):
        """
        Creates a long string of W's to test for line width / spacing.

        W is the widest character
        """

        chars = 0
        text = ''

        while chars < self.blurb_char_limit:
            word = self.words[random.randint(0, self.word_count - 1)]
            word = 'w' * len(word)
            text += f'{word} '
            chars = len(text)

        text += ' '
        return text


    def get_random_word(self):
        return self.words[random.randint(0, self.word_count - 1)]


    def print_word_list(self):
        """ Prints entire list of words on separate lines.  """

        for word in self.words:
            print(f'{word} {self.words[word]}')
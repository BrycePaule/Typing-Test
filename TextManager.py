import random
from random import shuffle


from Settings import WORD_LIST_FILEPATH


class TextManager():

    """
    Responsible for everything to do with the word list, reads from file,
    creates random blurbs, etc.
    """

    def __init__(self):
        self.words = self.read_in_words(lower=True)
        self.word_count = len(self.words)
        self.blurb_word_limit = 200


    def read_in_words(self, lower=False):
        """ Reads in word list from .txt file to enumerated dictionary. """

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
        """ Returns random list of words, self.blurb_word_limit in length. """

        return [self.words[random.randint(0, self.word_count - 1)] for _ in range(self.blurb_word_limit)]


    def create_w_blurb(self):
        """ Returns list of 'W', self.blurb_word_limit in length. """

        return [('W' * random.randint(0, 6)) for _ in range(self.blurb_word_limit)]
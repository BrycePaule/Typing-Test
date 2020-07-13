

class WordListManager():
    """
    Handles everything to do with curating and editing the word list used for
    the typing tester.
    """


    def __init__(self):
        self.word_list_filename = 'WORD_LIST.txt'
        self.word_list_filepath = '../WordList/'


    def curate(self):
        """
        Current fix criteria:
            - all words lowercase
            - only words 7 characters or less
        """

        self.convert_lowercase()
        self.remove_X_length_words(7)


    def convert_uppercase(self):
        """ Converts the entire word list to uppercase. """

        with open(f'{self.word_list_filepath}{self.word_list_filename}','r') as f:
            word_list = [word.upper().strip() for word in f]

        with open(f'{self.word_list_filepath}{self.word_list_filename}','w') as f:
            for word in word_list:
                f.write(f'{word}\n')


    def convert_lowercase(self):
        """ Converts the entire word list to lowercase. """

        with open(f'{self.word_list_filepath}{self.word_list_filename}', 'r') as f:
            word_list = [word.lower().strip() for word in f]

        with open(f'{self.word_list_filepath}{self.word_list_filename}', 'w') as f:
            for word in word_list:
                f.write(f'{word}\n')


    def remove_X_length_words(self, word_length_cap):
        """ Removes words over word_length_cap from the word list. """

        with open(f'{self.word_list_filepath}{self.word_list_filename}', 'r') as f:
            word_list = [word.strip() for word in f if len(word.strip()) <= word_length_cap]

        with open(f'{self.word_list_filepath}{self.word_list_filename}', 'w') as f:
            for word in word_list:
                f.write(f'{word}\n')


WLM = WordListManager()
WLM.curate()
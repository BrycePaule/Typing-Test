

WORD_LIST_FILEPATH = 'WORD_LIST'


def read_words(lower=False):
    index = 1
    word_dict = {}

    with open(WORD_LIST_FILEPATH, 'r') as f:
        for line in f:
            if lower:
                line = line.lower()
            word_dict[index] = line
            index += 1

    return word_dict


words = read_words(lower=True)
for word in words:
    print(f'{word} {words[word]}')
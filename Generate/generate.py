# This file contains a function, that
# extracts all valid words from file
from Decorators import time


@time.benchmark
def generate_dataset(words_list):
    """This function reads all the words
    from file and puts them into a set.
    Abbreviations are excluded from this set.

    :param words_list: path (absolute or relative) to 
                       the file with list of words.

    :return: set with all words from file
    """

    result = set()

    with open(words_list, 'r', encoding='utf-8') as file:
        for line in file:
            # Filter most of abbreviations
            if '-' not in line and '.' not in line:
                result.add(line.replace('\n', '').lower())
    
    return result

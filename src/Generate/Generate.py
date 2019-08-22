# This file contains a function, that
# extracts all valid words from file


def generate_dataset(words_list):
    """This function reads all the words
    from file and puts them into a set.
    Abbreviations are excluded from this set.

    :param words_list: path (absolute or relative) to 
                       the file with list of words.

    :return: set with all words from file
    """

    with open(words_list, 'r') as file:
        result = set()

        for line in file:
            # Filter most of abbreviations
            if not '-' in line and not '.' in line:
                result.add(line.translate(None, '\n\t\r')

    return result

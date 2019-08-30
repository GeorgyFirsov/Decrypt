#
# Generate/generate.py
# Decrypt
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
#

from Decorators import time


@time.benchmark
def generate_dataset(file_path: str) -> set:
    """This function reads all the words
    from file and puts them into a set.
    Abbreviations are excluded from this set.

    :param file_path: path (absolute or relative) to 
                       the file with list of words.

    :return: set with all words from file
    """

    result = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Filter most of abbreviations
            if '-' not in line and '.' not in line:
                result.add(line.replace('\n', '').lower())
    
    return result

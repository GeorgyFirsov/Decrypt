# This file contains some helper functions
from frozendict import frozendict

import pandas as pd

from Decorators import time


def custom_hash(word):
    """Calculates a number based on word.
    This number is unique with high probability
    """

    result = 0
    for index, letter in enumerate(word):
        result += letter * (index + 1) ** 2

    return result


@time.benchmark
def map_codes_and_words(words_dict, *args):
    """Helper function. It constructs dict with encrypted
    words as keys and their codes as values.
    """

    return frozendict(
        {words_dict[key]: tuple([f(words_dict[key].encode('utf-8')) for f in args]) for key in words_dict}
    )


def map_to_numbers(start, *args):
    """Helper function. Receives variadic amount
    of arguments and puts them to dictionary as
    keys. Values of resulting dictionary are
    increasing numbers: start, start + 1 ...

    :raises: ValueError if no items to map passed
    """
    if len(args) < 1:
        raise ValueError

    return {args[i]: start + i for i in range(len(args))}


def calculate_intersection(first, second):
    """Helper function. It returns an intersection of
    values sets of two dicts.
    """

    first_set = {key for key in first}
    second_set = {key for key in second}
    return first_set.intersection(second_set)


@time.benchmark
def create_data_frame(mapping):
    """Combines all dictionaries in mapping to single data frame

    :param mapping: variadic amount of dictionaries
                    with encrypted words and their hashes.
                    Each dictionary is a value in mapping,
                    each key is corresponding number from classes_map

    :return: Pandas DataFrame
    """

    data = {
          'Word': []
        , 'Crc32': []
        , 'Hash': []
        , 'Class': []
    }

    for dictionary, number in mapping.items():
        data['Word'] += [key for key in dictionary]
        data['Crc32'] += [value[0] for value in dictionary.values()]
        data['Hash'] += [value[1] for value in dictionary.values()]
        data['Class'] += [number for _ in range(len(dictionary))]

    return pd.DataFrame(data)

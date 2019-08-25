# This file contains some helper functions
from frozendict import frozendict
import random

import pandas as pd

from Decorators import time
from Utility.data import alphabet


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
def create_data_frame_hash(mapping):
    """Combines all dictionaries in mapping to single data frame

    :param mapping: variadic amount of dictionaries
                    with encrypted words and their hashes.
                    Each dictionary is a value in mapping,
                    each key is corresponding number from classes_map

    :return: Pandas DataFrame
    """

    data = {
          'Word': list()
        , 'Crc32': list()
        , 'Hash': list()
        , 'Class': list()
    }

    for dictionary, number in mapping.items():
        data['Word'] += [key for key in dictionary]
        data['Crc32'] += [value[0] for value in dictionary.values()]
        data['Hash'] += [value[1] for value in dictionary.values()]
        data['Class'] += [number for _ in range(len(dictionary))]

    return pd.DataFrame(data)


@time.benchmark
def create_data_frame_vectorized(mapping):
    """Combines all dictionaries in mapping to single data frame

    :param mapping: variadic amount of dictionaries
                    with encrypted words and their vectors.
                    Each dictionary is a value in mapping,
                    each key is corresponding number from classes_map

    :return: Pandas DataFrame
    """

    columns = ['Word', *tuple(list(alphabet)), 'Class']
    data = list()

    for dictionary, number in mapping.items():
        for word, vector in dictionary.items():
            data.append([word, *vector, number])

    return pd.DataFrame(data, columns=columns)


@time.benchmark
def get_n_random(n, dictionary):
    """Extracts n random elements from dictionary
    """

    pre_result = random.sample(dictionary.items(), n)
    return {item[0]: item[1] for item in pre_result}


def vectorize_word(word, mapped_alphabet):
    """Vectorizes a word and turns it into a
    list-vector with n dimensions (n is a length
    of alphabet).
    """

    result = [0 for _ in range(len(mapped_alphabet))]
    for letter in word:
        try:
            result[mapped_alphabet[letter]] += 1
        except KeyError:
            pass  # Just skip

    return tuple(result)


@time.benchmark
def vectorize(dictionary, mapped_alphabet):
    """Vectorizes each word in dictionary and
    makes another dictionary with encrypted word
    as a key and its vector representation as a value
    """

    return frozendict(
        {value: vectorize_word(value, mapped_alphabet) for value in dictionary.values()}
    )

#
# Utility/functions.py
# Decrypt
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
#

from frozendict import frozendict
import random

import pandas as pd

from Decorators import time
from Utility.data import alphabet
from Encrypt import *


def custom_hash(word: str) -> int:
    """Calculates a number based on word.
    This number is unique with high probability
    """

    result = 0
    for index, letter in enumerate(word):
        result += letter * (index + 1) ** 2

    return result


@time.benchmark
def map_codes_and_words(words_dict: dict, *args):
    """Helper function. It constructs dict with encrypted
    words as keys and their codes as values.
    """

    return frozendict(
        {words_dict[key]: tuple([f(words_dict[key].encode('utf-8')) for f in args]) for key in words_dict}
    )


def map_to_numbers(start: int, *args) -> dict:
    """Helper function. Receives variadic amount
    of arguments and puts them to dictionary as
    keys. Values of resulting dictionary are
    increasing numbers: start, start + 1 ...

    :raises: ValueError if no items to map passed
    """

    if len(args) < 1:
        raise ValueError

    return {args[i]: start + i for i in range(len(args))}


def calculate_intersection(first: dict, second: dict):
    """Helper function. It returns an intersection of
    values sets of two dicts.
    """

    first_set = {key for key in first}
    second_set = {key for key in second}
    return first_set.intersection(second_set)


@time.benchmark
def create_data_frame_hash(mapping: dict):
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
def create_data_frame_vectorized(mapping: dict):
    """Combines all dictionaries in mapping to single data frame

    :param mapping: variadic amount of dictionaries
                    with encrypted words and their vectors.
                    Each dictionary is a value in mapping,
                    each key is corresponding number from classes_map

    :return: Pandas DataFrame
    """

    columns = ['Word', *tuple(alphabet), 'Class']
    data = list()

    for dictionary, number in mapping.items():
        for word, vector in dictionary.items():
            data.append([word, *vector, number])

    return pd.DataFrame(data, columns=columns)


@time.benchmark
def get_n_random(n: int, dictionary: dict) -> dict:
    """Extracts n random elements from dictionary
    and returns them as dictionary
    """

    pre_result = random.sample(dictionary.items(), n)
    return {item[0]: item[1] for item in pre_result}


def vectorize_word(word: str, mapped_alphabet: dict) -> tuple:
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
def vectorize(dictionary: dict, mapped_alphabet: dict) -> frozendict:
    """Vectorizes each word in dictionary and
    makes another dictionary with encrypted word
    as a key and its vector representation as a value
    """

    return frozendict(
        {value: vectorize_word(value, mapped_alphabet) for value in dictionary.values()}
    )


def swap_keys_and_values(dictionary: dict) -> dict:
    """Swaps keys and values in dictionary and
    returns constructed one.
    """

    return {value: key for key, value in dictionary.items()}


def put_card_of_intersection_to(destination: list, first_dict: dict, second_dict: dict):
    """Appends a cardinality of intersection of sets of keys from
    two dictionaries: first_dict and second_dict
    """

    destination.append(
        len(calculate_intersection(swap_keys_and_values(first_dict)
                                   , swap_keys_and_values(second_dict)))
    )


def show_demo(mapping: dict, classifier):
    """Receives a dictionary with pairs of encrypted
    and original words, decrypts each encrypted one
    and prints comparison.

    :param mapping: dictionary with structure: {encrypted: original}
    :param classifier: predictor
    """

    classes = classifier.predict(mapping.keys())
    decrypted = list()

    for cls, encrypted in zip(classes, mapping.keys()):
        if cls == 1: decrypted.append(caesar.decrypt_word(encrypted, 3))
        elif cls == 2: decrypted.append(caesar.decrypt_word(encrypted, 4))
        elif cls == 3: decrypted.append(caesar.decrypt_word(encrypted, 5))
        elif cls == 4: decrypted.append(affine.decrypt_word(encrypted, 3, 4))
        elif cls == 5: decrypted.append(affine.decrypt_word(encrypted, 5, 2))
        elif cls == 6: decrypted.append(affine.decrypt_word(encrypted, 9, 11))
        else: raise RuntimeError('Broken predictor')

    for decrypted_word, (encrypted, original) in zip(decrypted, mapping.items()):
        print(
            "'{}' decrypted to '{}'.\nOriginal: '{}'\n".format(encrypted, decrypted_word, original)
        )




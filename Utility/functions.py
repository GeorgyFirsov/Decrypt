# This file contains some helper functions
from Decorators import time


@time.benchmark
def map_codes_and_words(words_dict, hash_func):
    """Helper function. It constructs dict with encrypted
    words as keys and their codes as values.
    """
    return {words_dict[key]: hash_func(words_dict[key].encode('utf-8')) for key in words_dict}


def calculate_intersection(first, second):
    """Helper function. It returns an intersection of
    values sets of two dicts.
    """
    first_set = {value for value in first.values()}
    second_set = {value for value in second.values()}
    return first_set.intersection(second_set)
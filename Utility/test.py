#
# Utility/test.py
# Decrypt
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
#

from Utility.functions import custom_hash, calculate_intersection
from Decorators import time


@time.benchmark
def run_all_tests():
    test_number = 1
    try:
        assert (custom_hash(b'name') == custom_hash(b'name'))

        test_number += 1
        assert (custom_hash(b'mean') != custom_hash(b'name'))

        test_number += 1
        assert (custom_hash(b'letter') == 10041)

        test_number += 1
        assert (custom_hash(b'caesar') == 9765)

        test_number += 1
        assert (calculate_intersection({'a': 97, 'b': 98}, {'c': 99, 'd': 100}) == set())

        test_number += 1
        assert (calculate_intersection({'a': 97, 'b': 99}, {'b': 99, 'd': 100}) == {'b'})

        print("All {} tests passed".format(test_number))
        return True

    except AssertionError:
        print("Test {} failed".format(test_number))
        return False

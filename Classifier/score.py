#
# Classifier/score.py
# Decrypt
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
#


def stats(correct_value, list_to_check: list):
    """Returns count of wrong values in list
    and percentage of right values as a string.
    """

    count_of_errors = len(list_to_check) - list_to_check.count(correct_value)
    percentage = (len(list_to_check) - count_of_errors) / len(list_to_check) * 100
    return "Errors: {}. Percentage: {}".format(count_of_errors, percentage)

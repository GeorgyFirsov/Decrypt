# This module provides Caesar encryption
# with different letter shift
from Decorators import time


alphabet = 'abcdefghijklmnopqrstuvwxyz'
max_len = len(alphabet) - 1


@time.benchmark
def encrypt(words, shift):

    if not 1 <= shift <= max_len:
        raise RuntimeError

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    result = dict()
    for word in words:
        result[word] = encrypt_word(word, shifted_alphabet)

    return result


def encrypt_word(word, shifted_alphabet):
    table = str.maketrans(alphabet, shifted_alphabet)
    return word.translate(table)

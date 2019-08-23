# This module provides Caesar encryption
# with different letter shift
from Decorators import time


alphabet = 'abcdefghijklmnopqrstuvwxyz'
max_len = len(alphabet) - 1


@time.benchmark
def encrypt(words, shift):
    """Function encrypts all words in container 'words'
    with Caesar cipher.

    :raises: RuntimeError if shift is less than one
             or more than length of alphabet - 1

    :param words: container with words
    :param shift: alphabet shift

    :return: dictionary with original words as keys
             and encrypted words as values
    """

    if not 1 <= shift <= max_len:
        raise RuntimeError

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    result = dict()
    for word in words:
        result[word] = encrypt_word(word, shifted_alphabet)

    return result


def encrypt_word(word, shifted_alphabet):
    """Encrypts single word with Caesar cipher.

    :param word: word to encrypt
    :param shifted_alphabet: encrypted alphabet

    :return: encrypted word
    """
    table = str.maketrans(alphabet, shifted_alphabet)
    return word.translate(table)

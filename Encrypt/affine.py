# This module provides Affine encryption
# with different letter shift and index multiplier
from Decorators import time
from math import gcd
from Utility.data import alphabet


@time.benchmark
def encrypt(words, multiplier, shift):
    """Affine cipher is provided by following formula:
                   y = (ax + b) mod m
    Where x is index of original letter and y is index,
    that original letter maps into.
    m is alphabet length

    :raises: RuntimeError if multiplier and alphabet
             length are not coprime numbers

    :param words: iterable container with word to encrypt
    :param multiplier: is multiplier a
    :param shift: alphabet shift

    :return: dictionary with original words as keys
             and encrypted words as values
    """

    if gcd(len(alphabet), multiplier) != 1:
        raise RuntimeError

    encrypted_alphabet = encrypt_alphabet(multiplier, shift)
    return {word: encrypt_word(word, encrypted_alphabet) for word in words}


def encrypt_word(word, encrypted_alphabet):
    """Encrypts single word with Affine cipher.

    :param word: word to encrypt
    :param encrypted_alphabet: encrypted alphabet

    :return: encrypted word
    """

    table = str.maketrans(alphabet, encrypted_alphabet)
    return word.translate(table)


def decrypt_word(word, multiplier, shift):
    """Decrypts an encrypted word from affine
    cipher with specified multiplier and shift.

    :raises: RuntimeError if multiplier and alphabet
             length are not coprime numbers
    """

    if gcd(len(alphabet), multiplier) != 1:
        raise RuntimeError

    encrypted_alphabet = encrypt_alphabet(multiplier, shift)
    table = str.maketrans(encrypted_alphabet, alphabet)

    return word.translate(table)


def encrypt_alphabet(multiplier, shift):
    result = str()
    length = len(alphabet)

    for i in range(length):
        result += alphabet[(multiplier * i + shift) % length]

    return result

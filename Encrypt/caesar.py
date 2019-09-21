#
# Encrypt/caesar.py
# Decrypt
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
#

from Decorators import time
from Utility.data import alphabet


@time.benchmark
def encrypt(words: set, shift: int) -> dict:
    """Function encrypts all words in container 'words'
    with Caesar cipher.

    :raises: RuntimeError if shift is less than one
             or more than length of alphabet - 1

    :param words: container with words
    :param shift: alphabet shift

    :return: dictionary with original words as keys
             and encrypted words as values
    """

    if not 1 <= shift <= len(alphabet) - 1:
        raise RuntimeError

    encrypted_alphabet = alphabet[shift:] + alphabet[:shift]
    return {word: encrypt_word(word, encrypted_alphabet) for word in words}


def encrypt_word(word: str, encrypted_alphabet: str) -> str:
    """Encrypts a single word with Caesar cipher.

    :param word: word to encrypt
    :param encrypted_alphabet: encrypted alphabet

    :return: encrypted word
    """

    table = str.maketrans(alphabet, encrypted_alphabet)
    return word.translate(table)


def decrypt_word(word: str, shift: int) -> str:
    """Decrypts a single word, encrypted with Caesar
    cipher with specific shift.

    :raises: RuntimeError if shift is less than one
             or more than length of alphabet - 1
    """

    if not 1 <= shift <= len(alphabet) - 1:
        raise RuntimeError

    encrypted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(encrypted_alphabet, alphabet)

    return word.translate(table)

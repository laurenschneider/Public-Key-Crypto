# public key encryption

import random

def blockEncrypt(block, pubkey):
    """
    :param block: int, 31 bits
    :param pubkey: dictionary [p: 0, g: 0, eTwo: 0] of the public key
    :return: tuple of ciphertext integers
    """

    # get random k
    k = random.randint(0, pubkey['p'] - 1)
    cOne = (pubkey['g'] ** k) % pubkey['p']
    cTwo = ((pubkey['eTwo'] ** k) * block) % pubkey['p']

    # cOne, Ctwo two ints
    ciphertext = (cOne, cTwo)

    return ciphertext


def encrypt():
    """
    :param: input string in ASCII
    :return: ciphertext, list of int tuples
    """

    pass

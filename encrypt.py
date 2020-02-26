# public key encryption

import random
import keygen
import utils

def blockEncrypt(block, pubkey):
    """
    :param block: int, 31 bits
    :param pubkey: dictionary [p: 0, g: 0, eTwo: 0] of the public key
    :return: tuple of ciphertext integers
    """
    p = pubkey['p']
    g = pubkey['g']
    e = pubkey['eTwo']

    # get random k
    k = random.randint(0, pubkey['p'] - 1)

    cOne = pow(g, k, p)

    # ab mod m = (a mod m * b mod m ) mod m
    a = pow(e, k, p)
    b = block % p
    cTwo = (a * b) % p

    # cOne, Ctwo two ints
    ciphertext = (cOne, cTwo)

    return ciphertext


def encrypt(plaintext, pubkeys):
    """
    :param plaintext: input string in ASCII
    :return: ciphertext, list of int tuples
    :return: dictionary of pubkeys
    """

    #pubkeys, d = keygen.keygen()

    # get 4 bytes, 4 char blocks. high bit of ascii always 0

    # check if padding is needed
    if (len(plaintext) % 4) != 0:
        print("adding padding to input")
        print(plaintext)
        r = len(plaintext) % 4
        for i in range(0,4-r):
            plaintext = plaintext + '.'

    # split into list of 32 bit strings
    blocks = [plaintext[i:i+4] for i in range(0, len(plaintext), 4)]
    print(blocks)

    ciphertext = []         # will be list of int tuples

    # block encrypt for each block
    for i in range(0, len(blocks)):

        # format first block to int
        hexBlock = ''.join([ "{:02x}".format(ord(k)) for k in blocks[i] ])
        intBlock = int(hexBlock, 16)

        if utils.getNumBits(intBlock) < 31:
            print("less than 31 bits")

        print(intBlock)

        c = blockEncrypt(intBlock, pubkeys)
        ciphertext.append(c)

    return ciphertext

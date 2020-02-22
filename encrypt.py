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

    pubkeys = {'p': 1, 'g': 1, 'eTwo': 1}

    # need 31 bit blocks. high bit of ASCII is always 0
    ‭# get 4 bytes, 4 char blocks

    # check if padding is needed
    if (len(input) % 4) != 0:
        print("adding padding to input")
        print(input)
        r = len(input) % 4
        for i in range(0,4-r):
            input = input + ' '

    # split into list of 32 bit strings
    blocks = [input[i:i+4] for i in range(0, len(input), 4)]

    ciphertext = []         # will be list of int tuples

    # block encrypt for each block
    for i in range(0, len(blocks)):

        # format first block to int
        hexBlock = ''.join([ "{:02x}".format(ord(k)) for k in blocks[i] ])
        intBlock = int(hexBlock, 16)

        c = blockEncrypt(intBlock, pubkeys)
        ciphertext.append(c)

    return ciphertext

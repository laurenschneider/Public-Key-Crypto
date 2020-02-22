# ( (C1 ^ (p-1-d) mod p) * (C2 mod p) ) mod p = m

def blockDecrypt(cpair, keys):
    """
    :param cpair: tuple of ciphertext ints
    :param keys: dictionary with p and d
    :return: one block of plaintext integer form
    """

    cOne = cpair[0]
    cTwo = cpair[1]
    p = keys['p']
    d = keys['d']

    cOneModP = (cOne ** (p - 1 - d)) % p
    cTwoModP = cTwo % p
    m = (cOneModP * cTwoModP) % p

    return m


def decrypt():
    """
    :param:
    :return:
    """

    # decrypt one block
    m = blockDecrypt()

    # convert integer block m to ascii 

    pass

# ( (C1 ^ (p-1-d) mod p) * (C2 mod p) ) mod p = m

def blockDecrypt(cpair, keys):
    """
    :param cpair: tuple of ciphertext ints
    :param keys: dictionary with p and d
    :return: one block of plaintext integer form
    """

    print("\n\n", cpair, "\n\n")
    cOne = cpair[0]
    cTwo = cpair[1]
    p = keys['p']
    d = keys['d']

    cOneModP = pow(cOne, (p-1-d), p)
    cTwoModP = cTwo % p
    m = (cOneModP * cTwoModP) % p

    return m


def decrypt(ciphertext, keys):
    """
    :param ciphertext: list of int tuples
    :param keys: dictionary {'p':0, 'd':0}
    :return: ascii string of plaintext
    """

    plaintext = ''
    for block in ciphertext:
        # decrypt one block
        m = blockDecrypt(block, keys)

        # convert integer block m to ascii
        hexBlock = hex(m)[2:]
        print("\n",hexBlock)
        text = bytes.fromhex(hexBlock).decode("ASCII")
        plaintext = plaintext + text

    return plaintext

import random
import millerrabin


def genSafePrime(kBits):
    """
    :param kBits: size of prime to generate
    :return: prime int
    """

    primeFound = False
    while not primeFound:
        print("still no prime found")
        q = 2
        while not q % 12 == 5:
            print("finding prime q")
            # lowest 31 bit int: 1073741824
            # highest 31 bit int: 2147483647
            q = random.randint(1073741824,2147483647)

        p = 2*q + 1
        if millerrabin.primeTest(p, 128) == True:
            primeFound = True

    return p

def keygen():
    """
    :return: public key dictionary {p, g, eTwo}
    :return: private key d
    """

    sd = input("Please enter a seed: ")
    random.seed(int(sd))

    # get large prime
    p = genSafePrime(32)

    # 1 <= d <= p-2
    d = random.randint(1, p-2)
    eOne = 2
    eTwo = pow(eOne, d, p)

    pubkey = {'p': p, 'g': eOne, 'eTwo': eTwo}

    return pubkey, d

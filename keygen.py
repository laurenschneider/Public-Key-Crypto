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
            q = random.getrandbits(kBits-1)

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
    random.seed(55)

    # get large prime
    p = genSafePrime(32)

    # 1 <= d <= p-2
    d = random.randint(1, p)
    eOne = random.randint(1, p-1)
    eTwo = pow(eOne, d, p)

    pubkey = {'p': p, 'g': eOne, 'eTwo': eTwo}

    return pubkey, d

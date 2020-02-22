import random

def primeTest(p, k):
    """
    p some input, greater than 1, to check for primeness
    k rounds to run
    return true if p is prime with high probability
    """

    # check for trivial case and even num
    if p == 2:
        return True

    if p % 2 == 0:
        return False


    # write p as 2r·d + 1 with d odd (by factoring out powers of 2 from p − 1)
    r = 0
    d = p - 1
    while d % 2 == 0:
        r = r + 1
        d = d // 2

    for i in range(0, k):
        a = random.randint(2, p-2)
        x = (a**d) % p

        if x == 1 or x == (p - 1):
            continue

        for j in range(0, (r - 1)):
            x = (x ** 2) % p

            if x == 1:
                return False
            if x == p - 1:
                return True

        if x != p - 1:
            return False

    return True                     # finish loop, then probably prime

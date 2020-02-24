# util methods 

def getNumBits(num):
    # return number of bits in an integer
    b = bin(num)[2:]
    return len(b)

def getIntFromBits(bitLen):
    # return the int of a given bit length
    b = "".join("1" for _ in range(bitLen))
    return int(b,2)

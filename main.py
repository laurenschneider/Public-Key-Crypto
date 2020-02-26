import keygen
import encrypt
import decrypt


# prompt user to choose
done = False
encrypted = False
ciphertext = []
pubkey = {}

while not done:
    res = input("\n\nPlease choose one of the following options:\n1. key generation\n2. encrypt\n3. decrypt\n4. exit\n\n")

    if res == "1":
        print("Generating keys ... \n\n")
        pubkey, d = keygen.keygen()

    elif res == "2":
        if not bool(pubkey):
            print("Please generate keys first.\n\n")
        else:
            print("Encryption started ... \n\n")

            pFile = open("plaintext.txt", "r")
            plaintext = pFile.read()
            pFile.close()

            res = plaintext.split('\n')
            newplain = res[0]

            ciphertext = encrypt.encrypt(newplain, pubkey)

            cFile = open("ciphertext.txt", "w")
            cFile.write(str(ciphertext))
            cFile.close()

            encrypted = True

    elif res == "3":
        if not encrypted or not bool(pubkey):
            print("Please generate keys and run encryption first.\n\n")
        else:
            print("Decryption started ... \n\n")

            keys = {"p": pubkey["p"], "d": d}
            plain = decrypt.decrypt(ciphertext, keys)

            pFile = open("plaintextResult.txt", "w")
            pFile.write(plain)
            pFile.close()

            print(plain)

    elif res == "4":
        done = True

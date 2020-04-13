Lauren Schneider
braun@pdx.edu

Public-Key-Crypto is an implementation of a public key encryption scheme very similar to ElGamal.

To run this program:
Enter your message on one continuous line in a file called
plaintext.txt.

Execute the command:
  python main.py

First choose the key generation. You will be prompted to enter a seed.
Then choose encrypt. The ciphertext will be output to a file called ciphertextResult.txt.
Next, choose decrypt to see the original message.

Files inlcluded in this submission:

encrypt.py
  The encryption of the plaintext.

decrypt.py
  The decryption of the generated ciphertext.

keygen.py
  Generates the public and private keys for the encryption scheme.

millerrabin.py
  Performs the Miller-Rabin primes test on an integer.

main.py
  Main driver program.

plaintext.txt
  Message to be encrypted. Must have this file before running program.

ciphertextResult.txt
  Ciphertext produced by encryption.

plaintextResult.txt
  Plaintext produced by decryption. 

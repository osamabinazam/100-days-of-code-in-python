# A Caesar cipher is a simple method of encoding messages. Caesar ciphers use a substitution
# method where letters in the alphabet are shifted by some fixed number of spaces to yield an e
# ncoding alphabet. A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N,
# and a Z as an A, and so on.

import Alphabets

def encrypt(message , shiftKey):
    ciphertext = ""
    for letter in message:
        if letter in Alphabets.small:
            position = int(Alphabets.small.index(letter))
            newPosition = position + shiftKey
            newLetter = Alphabets.small[newPosition]
            ciphertext += newLetter
        elif letter in Alphabets.large:
            position = int(Alphabets.large.index(letter))
            newPosition = position + shiftKey
            newLetter = Alphabets.large[newPosition]
            ciphertext += newLetter
    print(f"Encrypted message: {ciphertext}")

def decrypt(message, shiftKey):
    plaintext = ""
    for letter in message:
        if letter in Alphabets.small:
            position = int(Alphabets.small.index(letter))
            newPosition = position - shiftKey
            plaintext += Alphabets.small[newPosition]
        elif letter in Alphabets.large:
            position = int(Alphabets.large.index(letter))
            newPosition = position - shiftKey
            plaintext += Alphabets.large[newPosition]
    print(f"Decrypted message: {plaintext}")


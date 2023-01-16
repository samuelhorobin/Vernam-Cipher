""" Vernam Cipher is a Polyalphabetic cipher that uses XOR logic to combine keys and plaintext for ciphered code
    The same key can be applied to the ciphertext to get the original plaintext """

from random import randint

def generate_key(plainText) -> str:
    """ Generates a random ASCII key """
    key = []
    for _ in range(0,len(plainText)):
        key.append(chr(randint(0, 128)))
    return "".join(key)

def get_binary(string) -> list:
    """ Returns a list of binary values for each string character in input """
    binary = []
    for character in string:
        asciiChar = ord(character)
        binChar = f'{asciiChar:07b}' # Converts asciiChar to binary with 7 bits
        binary.append(binChar)
    return binary

def convert(text, key) -> str:
    """ Encodes the input plaintext with a key using Vernam cipher """
    cipherText = []
    binKey = get_binary(key)
    for strIndex, binary in enumerate(get_binary(text)): # Fix bug here
        cipherCharacter = []
        for binIndex, binVal in enumerate(binary):
            cipherCharacter.append(str((int(binVal) + int(binKey[strIndex][binIndex])) % 2))
        cipherText.append("".join(cipherCharacter))
    return bin_to_str(cipherText)

def bin_to_str(binaryList) -> None:
    """ Prints a list of ASCII binary values as a string """
    for index, binary in enumerate(binaryList):
        binaryList[index] = chr(int(binary, 2))
    return "".join(binaryList)


__plainText__ = "Example"
__key__ = generate_key(__plainText__) # Generates a __plainText__ size-d key
__cipherText__ = convert(__plainText__, __key__) # Converts __plainText__ to cipher text and assigns it to __cipherText__
__plainText__ = convert(__cipherText__, __key__) # Converts __cipherText__ back using the same key to prove it is reversable and assigns it to __plainText__

print(f"Text: {__plainText__}\nKey: {__key__}\nConverted: {__cipherText__}\nConverted back: {__plainText__}")




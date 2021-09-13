# day 8 project
import string

alphabet = string.ascii_lowercase

prompt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

'''STEP 1: ENCRYPT FUNCTION'''
def encrypt(message, shift):
    cipher_text = ""
    for letter in message:
        index = alphabet.find(letter)   # find the index of the current letter - returns INDEX
        position = index + shift    # [z] = 25, len(alphabet) = 26, 
        if position >= len(alphabet):    # if IndexError error, subtract it by length size
            position -= len(alphabet)
        cipher_text += alphabet[position]  # add the new letter to the string
    print(f"The encoded message is: {cipher_text}")
encrypt(message=message, shift=shift)   # keyword arguments

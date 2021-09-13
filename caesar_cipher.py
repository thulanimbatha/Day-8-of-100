# day 8 project
import string

alphabet = string.ascii_lowercase

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

'''STEP 2: DECRYPT FUNCTION'''
def decrypt(message, shift):
    cipher_text = ""
    for letter in message:
        index = alphabet.find(letter)   # find the index of the current letter - returns INDEX
        position = index - shift    # [a] = 0, len(alphabet) = 26, [a - 1] = -1 => -1 + 26 = 25 = [z]
        if position <= alphabet.index("a"):    # if IndexError error, add length size
            position += len(alphabet)
        cipher_text += alphabet[position]  # add the new letter to the string
    print(f"The decoded message is: {cipher_text}")

'''PROGRAM START'''
prompt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if prompt.lower() == "encode":
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(message=message, shift=shift)
elif prompt.lower() == "decode":
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(message=message, shift=shift)
else:
    print("Invalid input!")

# day 8 project
import string

alphabet = string.ascii_lowercase

prompt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

'''STEP 1: ENCRYPT FUNCTION'''
def encrypt(message, shift):
    shift_letter = ""
    for letter in message:
        index = alphabet.find(letter)
        shift_letter += alphabet[index + shift]
    print(f"The message is: {shift_letter}")
encrypt(message, shift)

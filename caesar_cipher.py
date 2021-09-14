# day 8 project
import string

alphabet = string.ascii_lowercase
exit = False

'''COMBINE INTO ONE FUNCTION'''
def caesar_cipher(message, shift, type):
    cipher_text = ""
    position = -1
    if type.lower() == "decode":
        shift *= -1 # turn 'shift' into '-shift'
    for letter in message:
        index = alphabet.find(letter)   # find the index of the current letter - returns INDEX
        position = index + shift    # [z] = 25, [a] = 0, len(alphabet) = 26, [a - 1] = -1 => -1 + 26 = 25 = [z]
        if position >= len(alphabet):    # if IndexError error, subtract it by length size
            position -= len(alphabet)
        elif position < alphabet.index("a"):   # if IndexError error, add length size
            position += len(alphabet)
        cipher_text += alphabet[position]  # add the new letter to the string
    print(f"The {type}d message is: {cipher_text}")

'''PROGRAM START'''
while not exit:
    prompt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # what if user enters a big number? -> modulus
    shift %= len(alphabet)  # shift = shift mod 26 -> eg.45 mod 26 = 18 => which is within the range 
    caesar_cipher(message=message, shift=shift, type=prompt)
    end = input("Do you want to try again?\nType 'yes' or 'no': ")
    if end == "yes":
        exit = False
        print("\nLet's go\n")
    elif end == "no":
        exit = True
        print("Goodbye!")


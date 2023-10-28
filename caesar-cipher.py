import string
letters = list(string.ascii_lowercase)
letters_length = len(letters)

def encrypt(message, shift):
    encrypted_message = ''
    for letter in message:
        if letter in letters:
            idx = letters.index(letter) + shift
            if (idx > letters_length):
                idx -= letters_length
            encrypted_message += letters[idx]
        else:
            encrypted_message += letter
    print('Your encrypted message: ', encrypted_message)

def decrypt(message, shift):
    decryptd_message = ''
    for letter in message:
        if letter in letters:
            idx = letters.index(letter) - shift
            if idx < 0:
                idx += letters_length
            decryptd_message += letters[idx]
        else:
            decryptd_message += letter
    print('Your decrypted message: ', decryptd_message)

use_app = True

while use_app:
    print('Welcome to the Caesar Cipher')
    print("Type 'encode' to encrypt")
    print("Type 'decode' to decrypt")
    print("Type 'quit' to exit the program")
    user_choice = input(': ')
    if user_choice == 'quit':
        use_app = False
        break
    message = input('Write your message: ')
    shift = int(input('Write your shift: '))
    if user_choice == 'encode':
        encrypt(message, shift)
    elif user_choice == 'decode': 
        decrypt(message, shift)

    
import string
import random

password = []

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = []

for number in range(0,10):
    numbers.append(number)

simbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nLetters = int(input('How many letters would you like: '))
nNumbers = int(input('How many numbers would you like: '))
nSymbols = int(input('How many symbols would you like: '))
totalChars = nLetters + nNumbers + nSymbols
i = 0

for index in range(0, totalChars):
    if nLetters > 0:
        idx = random.randint(0, len(letters) - 1)
        password.append(letters[idx])
        nLetters -= 1
    elif nNumbers > 0:
        idx = random.randint(0, len(numbers) - 1)
        password.insert(random.randint(0, len(password) - 1), str(numbers[idx]))
        nNumbers -= 1
    elif nSymbols > 0:
        idx = random.randint(0, len(simbols) - 1)
        password.insert(random.randint(0, len(password) - 1), simbols[idx])
        nSymbols -= 1

strPassword = ''.join(password)
print('Your password is: ', strPassword)
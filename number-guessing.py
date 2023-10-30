import random

def compare(guess, machine_number):
    if guess == machine_number:
        print('You win')
        global attemps
        attemps = 0
    elif guess < machine_number:
        print('Go higher')
    else:
        print('Go lower')

machine_number = random.randint(1, 10)

print('Welcome to Number Guessing Game')
print('I am thinking on a number between 1 and 100')
mode = input('Choose a dificult. Yupe easy or hard: ')
attemps = 5

if mode == 'easy':
    attemps = 10

print('You have ' + str(attemps) + ' attemps')

while attemps > 0:
    guess = int(input('Make a guess'))
    compare(guess, machine_number)
    attemps -= 1
    if attemps == 0:
        print('You lost')


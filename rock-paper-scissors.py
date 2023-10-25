################### Rock Paper Scissors Game ###################

import random

movesList = ['Rock', 'Paper', 'Scissors']

print('Welcome to the game pick the following numbers.')
print('1 -> Rock')
print('2 -> Paper')
print('3 -> Scissors')

machine = movesList[random.randint(0,2)]
userGuess = movesList[int(input('Which one do you choose: ')) - 1]

print('You choose: ', userGuess)
print('Machine is: ', machine)

if machine == 'Rock':
    match userGuess:
        case 'Rock':
            print('even')
        case 'Scissors':
            print('You lost')
        case 'Paper':
            print('You won')
elif machine == 'Paper':
    match userGuess:
        case 'Paper':
            print('even')
        case 'Rock':
            print('You lost')
        case 'Scissors':
            print('You won')
elif machine == 'Scissors':
    match userGuess:
        case 'Scissors':
            print('even')
        case 'Paper':
            print('You lost')
        case 'Rock':
            print('You won')



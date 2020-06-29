print("Welcome Code breaker! Let's see if you can guess my three digit number")

import random

while True:
    num = random.randint(100, 999)
    numstr = str(num)
    if numstr[0] != numstr[1] or numstr[0] != numstr[2] or numstr[1] != numstr[2]:
        break

print("Code has been generated, please guess a three digit numer")

while True:
    guess = input('What is your guess?\n')
    guess_res = 'Nope'

    if guess == numstr:
        print("Congratulations, You have correctly guessed the number.")
        break

    if guess == 'quit':
        break

    for i in range(3):
        if guess[i] == numstr[i]:
            guess_res = 'Match'
            break

    for i in range(3):
        if guess[i] in numstr and guess_res!='Match':
            guess_res = 'Close'
            break

    print('Here is the result of your guess:\n{}'.format(guess_res))

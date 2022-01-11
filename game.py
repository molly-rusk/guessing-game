"""A number-guessing game."""

import random 

randomNum = random.randint(0,100)

playerName = input('Hello, what is your name?')
print(f"{playerName} I'm thinking of a number between 1 and 100.")
print('Try to guess my number')
playerGuess = input('Your guess?')

guessCount = 1

solved = False

intPlayerGuess = int(playerGuess)
while solved == False:
    
    if intPlayerGuess > randomNum:
        print('Your guess is too high, try again.')
        intPlayerGuess = int(input('Your guess?'))
        guessCount += 1
        continue
    elif intPlayerGuess < randomNum:
        print('Your guess is too low, try again.')
        intPlayerGuess = int(input('Your guess?'))
        guessCount += 1
        continue
    else:
        print(f"Well done, {playerName}! You found my number in {guessCount} tries ")
        solved = True
       

        
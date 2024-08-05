print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    #Ask the user for a guess
    guess = input("Guess a number between 1 and 10: ")
    #If guess is correct?
    if int(guess) == number:
        #If correct, let them know
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    #If incorrect, keep guessing since in the while loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
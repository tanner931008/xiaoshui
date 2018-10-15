#!/bin/python
#this is a guess for game
import random
secretnumber = random.randint(1,20)
print('I am thinking of number between 1 and 20')

#Ask player to guess 6 times
for guessestaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretnumber:
        print('the number you have guessed is too low.')
    elif guess > secretnumber:
        print('the number you have guessed is too high.')
    else:
        break #this condition is the correct number!
if guess == secretnumber:
    print('Good job! you get correct number in '+ str(guessestaken) + ' guesses!')
else:
    print('Nope,the number I am thinking of was ' + str(secretnumber) + '!')

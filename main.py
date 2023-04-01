# Faints Number Guessing Game!

from time import sleep as wait
from colorama import Fore,init
import os
import random

def clear():
    os.system('cls')

def numberGuessingGame(randomNum1,randomNum2):
    while True:
        print(Fore.LIGHTMAGENTA_EX)
        clear()
        init()
        wait(1)
        randomNumber = random.randint(randomNum1,randomNum2)
        guess = int(input(f'Choose a number {randomNum1}-{randomNum2}! '))
        if guess == randomNumber:
            print(f'Correct! Restarting Game...')
        else:
            print(f'Incorrect, the number was {str(randomNumber)}! Restarting Game...')

# Replace params with range of the random number.
numberGuessingGame(10,100)
"""
This module implements a number guessing game.
"""

import random

ANSWER = random.randint(0, 40)
PROMPT = 'Guess a number between 0 - 40: '
ATTEMPTS = 0  # Initialize the attempts counter

while True:
    quest = input(PROMPT)
    try:
        guess = int(quest)
        ATTEMPTS += 1  # Increment the attempts counter
        if guess == ANSWER:
            print('That is Correct! It only took you', ATTEMPTS, 'attempts this time.')
            break
        if guess < ANSWER:
            print('Guess higher number')
        else:
            print('Guess lower number')
    except ValueError:
        print("Invalid input, please enter a number\n")

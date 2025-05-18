# Guess the Number Game Python Project (computer)

import random

def guess_the_number(x):
    # Generate a random number between 1 and x
    random_number = random.randint(1, x)
    guess = 0

    # Continue until the user guesses the correct number
    while guess != random_number:
        # Get user's guess
        guess = int(input(f"Guess a number between 1 and {x}: "))

        # Provide feedback on the guess
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")

    print(f"Congratulations! You've guessed the number {random_number} correctly!")

guess_the_number(10)
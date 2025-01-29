"""
Guess the Number Game

The player has 6 chances to guess a randomly selected number between 1 and 20.
After each guess, they receive feedback on whether their guess is too low, too high, or correct.
"""

import random


def guess_the_number() -> None:
    """Runs a guess the number game where player has 6 attempts to guess correctly"""
    secret_number = random.randint(1, 20)
    max_attempts = 6

    print("Welcome to the Guess the Number game!\n")
    print(
        f"I am thinking of a number between 1 and 20. You have {max_attempts} guesses.\n"
    )
    for attempt in range(max_attempts):
        while True:
            try:
                guess = int(
                    input(f"Attempt {attempt + 1}/{max_attempts} - Take a guess:")
                )
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempt + 1} guesses!")
            return  # This condition is the correct guess!

    print(f"Out of attempts! The number I was thinking of was {secret_number}")


# Run the game
if __name__ == "__main__":
    guess_the_number()

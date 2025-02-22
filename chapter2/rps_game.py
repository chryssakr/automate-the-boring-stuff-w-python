"""
Rock Paper Scissors Game

The player can enter their move by writing the corresponding letter:
(r)ock (p)aper (s)cissors or (q)uit
The player plays against a random move from the program, the game goes on until the player types (q)uit
"""

import random, sys


def rps_game() -> None:
    """Runs a guess of rock paper scissors"""

    print("ROCK, PAPER, SCISSORS")

    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0
    while True:  # The main game loop.
        print(f"{wins=}, {losses=}, {ties=}")
        while True:  # The player input loop.
            player_move = input(
                "Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n"
            )
            if player_move == "q":
                sys.exit()  # Quit the program.
            if player_move == "r" or player_move == "p" or player_move == "s":
                break  # Break out of the player input loop.
            print("Invalid move. Type one of r, p, s, or q.")

        # Display what the player chose:
        if player_move == "r":
            print("ROCK versus...")
        elif player_move == "p":
            print("PAPER versus...")
        elif player_move == "s":
            print("SCISSORS versus...")

        # Display what the computer chose:
        random_number = random.randint(1, 3)
        if random_number == 1:
            computer_move = "r"
            print("ROCK")
        elif random_number == 2:
            computer_move = "p"
            print("PAPER")
        elif random_number == 3:
            computer_move = "s"
            print("SCISSORS")

        # Display and record the win/loss/tie:
        if player_move == computer_move:
            print("It is a tie!")
            ties = ties + 1
        elif player_move == "r" and computer_move == "s":
            print("You win!")
            wins = wins + 1
        elif player_move == "p" and computer_move == "r":
            print("You win!")
            wins = wins + 1
        elif player_move == "s" and computer_move == "p":
            print("You win!")
            wins = wins + 1
        elif player_move == "r" and computer_move == "p":
            print("You lose!")
            losses = losses + 1
        elif player_move == "p" and computer_move == "s":
            print("You lose!")
            losses = losses + 1
        elif player_move == "s" and computer_move == "r":
            print("You lose!")
            losses = losses + 1


# Run the game
if __name__ == "__main__":
    rps_game()

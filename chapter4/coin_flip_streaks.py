import random


def flip(times: int) -> list[str]:
    """
    Flips a coin a number of times.

    Args:
        times (int): The number of times I want to flip the coin.

    Returns:
        list[str]: A list containing all the coin flips.
    """
    flips = []
    for _ in range(times):
        if random.randint(0, 1):
            flips.append("Τ")
        else:
            flips.append("Η")
    return flips


def find_streaks(flips: list[str]) -> bool:
    """
    Finds whether or not there is a streak of 6 in the list.

    Args:
        flips (list[str]): The list that contains all the coin flips.

    Returns:
        bool: Returns True/False if there is a streak or not.
    """
    streaks = 0
    in_row = 0
    streak_num = 6

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            in_row += 1
        else:
            if in_row == streak_num:
                streaks += 1
            in_row = 0
    # checking if the last ones add to the streak
    if in_row == streak_num:
        return True
    return False


def main() -> None:
    number_of_experiments = 10000
    containing_streak = 0
    for _ in range(number_of_experiments):
        flip_times = 100
        flips = flip(flip_times)
        streaks = find_streaks(flips)
        if streaks:
            containing_streak += 1
    chance_of_streak = containing_streak / number_of_experiments * 100
    chance_of_streak = round(chance_of_streak, 4)
    print(f"Chance of streak: {chance_of_streak}%")


if __name__ == "__main__":
    main()

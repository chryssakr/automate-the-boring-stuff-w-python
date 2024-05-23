import random

def flip(times: int) -> list[str]:
    flips = []
    for _ in range(times):
        if random.randint(0, 1) == 0:
            flips.append("H")
        else:
            flips.append("T")
    return flips

def find_streaks(flips: list[str]) -> int:
    streaks = 0
    in_row = 0
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            in_row += 1
        else:
            if in_row == 6:
                streaks += 1
            in_row = 0
    # checking if the last ones add to the streak
    if in_row == 6:
        streaks += 1
    return streaks
# TODO: change number of experiments to 10000 and number or repetitions per exp to 100

def main() -> None:
    number_of_experiments = 10000
    # TODO: make 6 a variable
    flips = flip(number_of_experiments)
    streaks = find_streaks(flips)
    print(f"Chance of streak: {streaks/100}")
    
if __name__ == "__main__":
    main()
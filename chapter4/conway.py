# Conway's Game of Life
import random, time, copy
from typing import List

WIDTH = 60
HEIGHT = 20


def create_grid(width: int, height: int) -> List[List[str]]:
    """
    Create a grid of given width and height, initialized with random living or dead cells.
    """
    next_cells = []
    for _ in range(width):
        column = []  # create a new column
        for _ in range(height):
            if random.randint(0, 1) == 0:
                column.append("#")  # add a living cell
            else:
                column.append(" ")  # add a dead cell
        next_cells.append(column)  # next_cells is a list of column lists
    return next_cells


def print_grid(grid: List[List[str]]) -> None:
    """
    Print the grid to the console.
    """
    print("\n" * 5)  # separate each step with newlines
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(grid[x][y], end="")
        print()  # to change line


def count_neighbors(grid: List[List[str]], x: int, y: int) -> int:
    """
    Count the number of living neighbors for a cell at position (x, y).
    """
    # % WIDTH/HEIGHT to ensure coordinates are always between 0 and WIDTH/HEIGHT - 1
    left = (x - 1) % WIDTH
    right = (x + 1) % WIDTH
    above = (y - 1) % HEIGHT
    below = (y + 1) % HEIGHT
    living_neigh_sum = sum(
        grid[nx][ny] == "#"  # 1 if this is true, 0 is it's false
        for nx, ny in [
            (left, above),
            (x, above),
            (right, above),
            (left, y),
            (right, y),
            (left, below),
            (x, below),
            (right, below),
        ]
    )
    return living_neigh_sum


def update_grid(current_grid: List[List[str]]) -> List[List[str]]:
    """
    Compute the next state of the grid based on Conway's Game of Life rules.
    """
    next_grid = copy.deepcopy(current_grid)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(current_grid, x, y)
            if current_grid[x][y] == "#" and neighbors in (2, 3):
                next_grid[x][y] = "#"  # stay alive
            elif current_grid[x][y] == " " and neighbors == 3:
                next_grid[x][y] = "#"  # become alive
            else:
                next_grid[x][y] = " "  # die or stay dead
    return next_grid


def main() -> None:
    """
    Main function to run Conway's Game of Life simulation.
    """
    grid = create_grid(WIDTH, HEIGHT)
    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(1)  # add a 1-second pause to reduce flickering


if __name__ == "__main__":
    main()

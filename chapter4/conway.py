# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20
# Create a list of lists for the cells:
next_cells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
    next_cells.append(column) # next_cells is a list of column lists
while True: # main program loop
    print('\n\n\n\n\n') # separate each step with newlines
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='') # print the # or space
        print() # print a newline at the end of the row

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures left_coord is always between 0 and WIDTH - 1
            left_coord  = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1 # top-left neighbor is alive
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1 # top neighbor is alive
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1 # top-right neighbor is alive
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1 # left neighbor is alive
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1 # right neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1 # bottom-left neighbor is alive
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1 # bottom neighbor is alive
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1 # bottom-right neighbor is alive

            # Set cell based on Conway's Game of Life rules:
            if current_cells[x][y] == '#' and (num_neighbors == 2 or
num_neighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                next_cells[x][y] = ' '
    time.sleep(1) # add a 1-second pause to reduce flickering
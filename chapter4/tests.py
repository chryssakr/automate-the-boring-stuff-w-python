"""
WIDTH = 5
HEIGHT = 5
# Create a list of lists for the cells:
next_cells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        column.append('(' + str(x) + ',' + str(y) + ') ')
    next_cells.append(column) # next_cells is a list of column lists

# Print current_cells on the screen:
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(next_cells[x][y], end='') # print the # or space
    print() # print a newline at the end of the row

"""

"""
spam = ['a', 'b', 'c', 'd']
spam[int(int('3'*2) // 11)]
spam[int(int('33') // 11)]
spam[int(33 // 11)]
spam[int(3)]
spam[3] # evaluates to d
print(spam[int(int('3'*2) // 11)])
print('spam[-1]: ' + spam[-1]) # evaluates to d
print('spam[:2]: ')
print(spam[:2]) # evaluates to ['a', 'b']
"""

bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat')) # 1
bacon.append(99) # [3.14, 'cat', 11, 'cat', True, 99]
print(bacon) # [3.14, 'cat', 11, 'cat', True, 99]
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat') 
print(bacon) # [3.14, 11, 'cat', True]
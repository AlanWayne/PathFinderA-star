import classes 
import random

# field size
width = 10
height = 10

# initiate field
grid = [[0] * width for i in range(height)]

# fill the field with objects
for i in range(width):
    for k in range(height):
        grid[i][k] = classes.Cell(i,k)
        if random.randint(1,100) < 10:
            grid[i][k].state = 'wall'
        else:
            grid[i][k].state = 'field'

# set start and end
grid[0][0].state = 'start'
grid[width-1][height-1].state = 'end'

# fill the Neighbors array
for i in range(width):
    for k in range(height):
        if i > 0:
            grid[i][k].neighbors.append(grid[i-1][k])
        if i < width - 1:
            grid[i][k].neighbors.append(grid[i+1][k])
        if k > 0:
            grid[i][k].neighbors.append(grid[i][k-1])
        if k < height - 1:
            grid[i][k].neighbors.append(grid[i][k+1])            
        if i > 0 and k > 0:
            grid[i][k].neighbors.append(grid[i-1][k-1])
        if i > 0 and k < height - 1:
            grid[i][k].neighbors.append(grid[i-1][k+1])
        if i < width - 1 and k > 0:
            grid[i][k].neighbors.append(grid[i+1][k-1])
        if i < width - 1 and k < height  - 1:
            grid[i][k].neighbors.append(grid[i+1][k+1])





# console output
for i in range(width):
    for k in range(height):
        if grid[i][k].state == 'field':
            print('_', end = ' ')
        elif grid[i][k].state == 'wall':
            print('W', end = ' ')
        elif grid[i][k].state == 'start':
            print('S', end = ' ')
        elif grid[i][k].state == 'end':
            print('E', end = ' ')
    print('')

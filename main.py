from cmath import inf
import classes 
import random
import math

# field size
width = 10
height = 10

# initiate field
grid = [[0] * width for i in range(height)]

# fill the field with objects
for i in range(width):
    for k in range(height):
        grid[i][k] = classes.Cell(i,k)
        if random.randint(1,100) < 30:
            grid[i][k].state = 'wall'
        else:
            grid[i][k].state = 'field'

# set start and end
start = grid[0][0]
start.state = 'start'
end = grid[width-1][height-1]
end.state = 'end'

# fill the Neighbors array
for i in range(width):
    for k in range(height):
        if i > 0                             and grid[i-1][k].state != 'wall':
            grid[i][k].neighbors.append(grid[i-1][k])
        if i < width - 1                     and grid[i+1][k].state != 'wall':
            grid[i][k].neighbors.append(grid[i+1][k])
        if k > 0                             and grid[i][k-1].state != 'wall':
            grid[i][k].neighbors.append(grid[i][k-1])
        if k < height - 1                    and grid[i][k+1].state != 'wall':
            grid[i][k].neighbors.append(grid[i][k+1])            
        if i > 0 and k > 0                   and grid[i-1][k-1].state != 'wall':
            grid[i][k].neighbors.append(grid[i-1][k-1])
        if i > 0 and k < height - 1          and grid[i-1][k+1].state != 'wall':
            grid[i][k].neighbors.append(grid[i-1][k+1])
        if i < width - 1 and k > 0           and grid[i+1][k-1].state != 'wall':
            grid[i][k].neighbors.append(grid[i+1][k-1])
        if i < width - 1 and k < height  - 1 and grid[i+1][k+1].state != 'wall':
            grid[i][k].neighbors.append(grid[i+1][k+1])

openSet = []
closeSet = []

openSet.append(start)
current = start

#while openSet != 0:
for i in range(1000):
    tempSet = []
    tempSet.clear()
    if current == end:
        break
    
    for k in range(len(current.neighbors)):
        if not(current.neighbors[k] in openSet) and not(current.neighbors[k] in closeSet):
            tempSet.append(current.neighbors[k])
    
    for k in range(len(tempSet)):        
        if tempSet[k] != current:
            if tempSet[k].price == 0:
                tempSet[k].price = current.price + 1
        
    for k in range(len(tempSet)):
        openSet.append(tempSet[k])
    
    best = openSet[0]
    if len(openSet) > 1:
        for i in range(1,len(openSet)):
            if openSet[i].price < best.price:
                best = openSet[i]
                
    for k in range(len(openSet)-1):
        if openSet[k] == current:
            openSet.remove(current)
            closeSet.append(current)
    
    current = best


# console output
for i in range(width):
    for k in range(height):
        '''if grid[i][k].state == 'field':
            print('_', end = ' ')
        elif grid[i][k].state == 'wall':
            print('W', end = ' ')
        elif grid[i][k].state == 'start':
            print('S', end = ' ')
        elif grid[i][k].state == 'end':
            print('E', end = ' ')'''
        print(grid[i][k].price, end = ' ')
    print('')
    
#print(grid[0][0].neighbors)
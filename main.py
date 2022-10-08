import classes 
import random
import pygame as pg
import math

scr_width = 640
scr_height = 640
screen = pg.display.set_mode((scr_width,scr_height))

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
            grid[i][k].value = 99
        else:
            grid[i][k].state = 'field'

# set start and end
start = grid[0][0]
start.state = 'start'
start.value = 0
end = grid[width-1][height-1]
end.state = 'end'
end.value = 0

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

# field of available paths
openSet = []
# field of passed paths
closeSet = []

openSet.append(start)
current = start

pg.display.flip()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #while openSet != 0:
    tryes = 0
    while len(openSet) > 0 and tryes < 1000000:
        tryes += 1
        # temporary list of new available paths
        tempSet = []
        tempSet.clear()
        
        # if we are looking at the End cell
        if current == end:
            break
        
        # add new available paths to the temp list
        for k in range(len(current.neighbors)):
            if not(current.neighbors[k] in openSet) and not(current.neighbors[k] in closeSet):
                tempSet.append(current.neighbors[k])
        
        # setting the Cell's price (price to approach to the cell)
        for k in range(len(tempSet)):        
            if tempSet[k] != current:
                if tempSet[k].price == 0:
                    tempSet[k].price = current.price + 1
                if tempSet[k].dist == 0:
                    tempSet[k].dist = math.sqrt((end.x - tempSet[k].x)*(end.x - tempSet[k].x) + (end.y - tempSet[k].y)*(end.y - tempSet[k].y))
                tempSet[k].value = tempSet[k].price + tempSet[k].dist
        # add temp paths to the open paths
        for k in range(len(tempSet)):
            openSet.append(tempSet[k])
        
        # choose the best path
        best = openSet[0]
        if len(openSet) > 1:
            for i in range(1,len(openSet)):
                if openSet[i].value < best.value:
                    best = openSet[i]
            
        # set the current Cell as not available        
        for k in range(len(openSet)-1):
            if openSet[k] == current:
                openSet.remove(current)
                closeSet.append(current)
        
        best.previous = current
        current = best
        
        path = current
        while path.previous != None:
            pg.draw.line(screen,(250,0,250),(path.x,path.y),(path.previous.x,path.previous.y),2)
            path = path.previous
            
        pg.display.flip()

    # console output
    for i in range(width):
        for k in range(height):
            if grid[i][k].state == 'wall':
                pg.draw.circle(screen,(255,255,255),(k * scr_height / height + scr_height / height / 2, i * scr_width / width + scr_width / width / 2), 10)
            elif grid[i][k].state == 'start':
                pg.draw.circle(screen,(50,50,200),(k * scr_height / height + scr_height / height / 2, i * scr_width / width + scr_width / width / 2), 10)
            elif grid[i][k].state == 'end':
                pg.draw.circle(screen,(50,200,50),(k * scr_height / height + scr_height / height / 2, i * scr_width / width + scr_width / width / 2), 10)
            print(round(grid[i][k].value), end = ' ')
        print('')



        

    #print(grid[0][0].neighbors)
fileContents = open("AdventOfCode2023/Day 10/input.txt")
arr = fileContents.read().split("\n")

from queue import PriorityQueue

grid = []
grid.append(['.' for i in range(len(arr[0])+2)])
for row in arr:
    newRow = []
    newRow.append('.')
    for item in row:
        newRow.append(item)
    newRow.append('.')
    grid.append(newRow)
grid.append(['.' for i in range(len(arr[0])+2)])

SLoc = (-1, -1)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            SLoc = (i,j)
            grid[i][j] = '|'

def getNeighborsFromLocAndShape(Loc, shape):
    match shape:
        case '|':
            return (Loc[0]-1, Loc[1]), (Loc[0]+1, Loc[1])
        case 'S':
            #print(Loc)
            return (Loc[0], Loc[1]+1), (Loc[0]+1, Loc[1])
        case '-':
            return (Loc[0], Loc[1]-1), (Loc[0], Loc[1]+1)
        case 'L':
            return (Loc[0]-1, Loc[1]), (Loc[0], Loc[1]+1)
        case 'J':
            return (Loc[0]-1, Loc[1]), (Loc[0], Loc[1]-1)
        case '7':
            return (Loc[0]+1, Loc[1]), (Loc[0], Loc[1]-1)
        case 'F':
            return (Loc[0]+1, Loc[1]), (Loc[0], Loc[1]+1)
    raise(TypeError)

queue = PriorityQueue()
visited = dict() # location to distance, only things on loop should be here
visited[SLoc] = 0

for neighbor in getNeighborsFromLocAndShape(SLoc, grid[SLoc[0]][SLoc[1]]):
    queue.put((1, neighbor))
    visited[neighbor] = 1

while queue.qsize() > 0:
    investigate = queue.get()
    for neighbor in getNeighborsFromLocAndShape(investigate[1], grid[investigate[1][0]][investigate[1][1]]):
        if neighbor not in visited:
            visited[neighbor] = investigate[0]+1
            queue.put((investigate[0]+1, neighbor))

def updateFence(shape, interior):
    match shape:
        case '|':
            return not interior
        case '-':
            return interior
        case 'L':
            return not interior
        case '7':
            return interior
        case 'F':
            return interior
        case 'J':
            return not interior

interior_count = 0
for i, row in enumerate(grid):
    interior = False
    for j, item in enumerate(grid[0]):
        if (i,j) not in visited and interior:
            grid[i][j] = 'I'
            interior_count += 1
        elif (i,j) not in visited:
            grid[i][j] = 'O'
            continue
        else:
            interior = updateFence(grid[i][j], interior)
print(interior_count)


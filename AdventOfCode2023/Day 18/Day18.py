
fileContents = open("AdventOfCode2023/Day 18/input.txt")
arr = fileContents.read().split("\n")

dirs = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def addPos(a, b):
    return (a[0] + b[0], a[1] + b[1])

grid = set()
current_pos = (0,0)
for ins in arr:
    d = ins.split(' ')[0]
    l = int(ins.split(' ')[1])
    for i in range(l):
        grid.add((*current_pos, d))
        current_pos = addPos(current_pos, dirs[d])

def findBoundingCoords(g):
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for p in g:
        if min_x == None or p[0] < min_x:
            min_x = p[0]
        if min_y == None or p[1] < min_y:
            min_y = p[1]
        if max_x == None or p[0] > max_x:
            max_x = p[0]
        if max_y == None or p[1] > max_y:
            max_y = p[1]
    if min_x == None or min_y == None or max_x == None or max_y == None:
        raise(ValueError)
    return min_x, min_y, max_x+1, max_y+1

x1, y1, x2, y2 = findBoundingCoords(grid)
print(x1, y1, x2, y2)


def isSurroundedByGridStuff(row, col, g):
    sameRow = [x for x in set(g) if x[0] == row and x[1] < col]
    ups, downs = 0, 0
    for x in sameRow:
        if x[2] == 'U':
            ups += 1
        if x[2] == 'D':
            downs += 1
    return (ups + downs)%2 == 1

edges = set()   
for item in grid:
    edges.add((item[0], item[1]))
    
s = ''
interiors = 0
for row in range(x1, x2):
    s += '\n'
    for col in range(y1, y2):
        if (row, col) in edges:
            s += 'e'
            continue
        
        elif isSurroundedByGridStuff(row,col, grid):
            s += '.'
            interiors += 1
        else:
            s += '.'
print(interiors + len(edges))
print(s)
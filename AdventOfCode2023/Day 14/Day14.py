fileContents = open("AdventOfCode2023/Day 14/sampleInput.txt")
grid = fileContents.read().split("\n")

rows = len(grid)
cols = len(grid[0])

contents = dict()
for r in range(rows):
    for c in range(cols):
        contents[(r,c)] = grid[r][c]

def printContents(c):
    for row in range(rows):
        for col in range(cols):
            print(c[row,col], end='')
        print('')


def findRockBelow(g, r, c):
    for search_row in range(r, rows):
        if g[(search_row, c)] == 'O':
            return search_row
        if g[(search_row, c)] == '#':
            return None
    return None

def tiltNorth(rocksnstuff):
    for r in range(rows):
        for c in range(cols):
            if rocksnstuff[(r, c)] == '.':
                rowOfRock = findRockBelow(rocksnstuff, r, c)
                if rowOfRock:
                    rocksnstuff[(r, c)] = 'O'
                    rocksnstuff[(rowOfRock, c)] = '.'
    return rocksnstuff

def rotateBoard(rocksnstuff):
    newBoard = dict()
    for r in range(rows):
        for c in range(cols):
            newBoard[(r,c)] = rocksnstuff[(rows-c-1, r)]
    return newBoard
                
def CalculateLoad(g):
    total = 0
    for r in range(rows):
        for c in range(cols):
            if g[(r,c)] == 'O':
                total += rows - r
    return total



for i in range(1030):
    contents = tiltNorth(contents)
    contents = rotateBoard(contents)
    contents = tiltNorth(contents)
    contents = rotateBoard(contents)
    contents = tiltNorth(contents)
    contents = rotateBoard(contents)
    contents = tiltNorth(contents)
    contents = rotateBoard(contents)
    if i >= 1000:
        print(i, CalculateLoad(contents))


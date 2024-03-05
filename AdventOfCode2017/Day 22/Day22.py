fileContents = open("AdventOfCode2017/Day 22/input.txt")
grid = fileContents.read().split('\n')

infected = set()
weakened = set()
flagged = set()

for row, line in enumerate(grid):
    for col, c in enumerate(line):
        if c == '#':
            infected.add((row,col))

rows = len(grid)
cols = len(grid[0])
currentLocation = (rows//2, cols//2)

NWSE = [(-1,0), (0,-1), (1,0), (0,1)]
currentDir = 0
spores = 0

def turnLeft(currentDir):
    return (currentDir+1)%4

def turnRight(currentDir):
    return ((currentDir-1)+4)%4

def turnAround(currentDir):
    return (currentDir+2)%4

def addPts(a,b):
    return (a[0] + b[0], a[1] + b[1])

def takeStep(currentLocation, currentDir):
    global infected
    global weakened
    global flagged
    global spores
    if currentLocation in infected:
        currentDir = turnRight(currentDir)
        infected.remove(currentLocation)
        flagged.add(currentLocation)
    elif currentLocation in weakened:
        weakened.remove(currentLocation)
        infected.add(currentLocation)
        spores += 1
    elif currentLocation in flagged:
        currentDir = turnAround(currentDir)
        flagged.remove(currentLocation)
    else: # clean
        currentDir = turnLeft(currentDir)
        weakened.add(currentLocation)
    return addPts(currentLocation, NWSE[currentDir]), currentDir

for i in range(10000000):
    currentLocation, currentDir = takeStep(currentLocation, currentDir)

print(spores)
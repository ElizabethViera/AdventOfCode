fileContents = open("AdventOfCode2021/Day 20/sampleInput.txt")

arr = fileContents.read().split("\n\n")

decodeString = arr[0]
imageEnhance = arr[1].split('\n')

pixelCoords = set()

for r,line in enumerate(imageEnhance):
    for c,ch in enumerate(line):
        if ch == '#':
            pixelCoords.add((r,c))

dirs = [
    (-1,-1), (-1,0), (-1,1), 
    (0,-1), (0,0), (0,1), 
    (1,-1), (1,0), (1,1)
    ]

def addPx(a,b):
    return (a[0] + b[0], a[1] + b[1])

def getSurroundingPx(coord, pc, isEven):
    min_i, max_i = min(p[0] for p in pc), max(p[0] for p in pc)
    min_j, max_j = min(p[1] for p in pc), max(p[1] for p in pc)
    result = ''
    for direction in dirs:
        friendCoord = addPx(coord,direction)
        if friendCoord in pc:
            result += '1'
        else:
            if isEven and min_i > friendCoord[0] or max_i < friendCoord[0] or min_j > friendCoord[1] or max_j < friendCoord[1]:
                    result += '1'
            else:
                result += '0'

    return int(result,2)

def takeStep(pc, isEven):

    newPC = set()
    
    for pixel in pc:
            for direction in dirs:
                closeCoord = addPx(pixel, direction)
                if decodeString[getSurroundingPx(closeCoord, pc, isEven)] == '#':
                    newPC.add(closeCoord)
    return newPC

mpc = pixelCoords

for i in range(2):
    mpc = takeStep(mpc, i%2 == 1)

def printPC(pc):
    for i in range(-5, 105):
        for j in range(-5, 105):
            if (i,j) in pc:
                print('#', end='')
            else:
                print(',', end='')
        print('\n')
printPC(mpc)
fileContents = open("AdventOfCode2022/Day 23/input.txt")
arr = fileContents.read().split("\n")

elves = set()

def rotatePrecedence(arr):
    return arr[1:] + [arr[0]]

# print(rotatePrecedence(['M', 'O', 'V', 'E']))

for row, line in enumerate(arr):
    for col, c in enumerate(line):
        if c == '#':
            elves.add((row,col))

neighborDirs = [(-1,0), (-1, -1), (-1, 1),
                (1,0), (1,1), (1,-1),
                (0,1), (0,-1)]

def getNeighborPos(row,col):
    result = set()
    for neighbor in neighborDirs:
        result.add((row+neighbor[0], col+neighbor[1]))
    return result

def checkElves(current_pos, elves, listOfCoords):
    for coord in listOfCoords:
        if(current_pos[0] + coord[0], current_pos[1] + coord[1]) in elves:
            return False
    return True

def canMoveInDirection(current_pos, elves, direction):
    match direction:
        case 'N':
            return checkElves(current_pos, elves, [(-1,0), (-1, 1), (-1, -1)])
        case 'S':
            return checkElves(current_pos, elves, [(1,1), (1, 0), (1, -1)])
        case 'E':
            return checkElves(current_pos, elves, [(0,1), (1,1), (-1,1)])
        case 'W':
            return checkElves(current_pos, elves, [(0,-1), (1,-1), (-1,-1)])
                
def directionToPos(coords, direction):
    match direction:
        case 'N':
            return (coords[0]-1 , coords[1])

        case 'S':
            return (coords[0]+1, coords[1])

        case 'E':
            return (coords[0], coords[1]+1)

        case 'W':
            return (coords[0], coords[1] - 1)

def consider(current_pos, elves, precedence_dirs):
    wantsToMove = False
    neighbors = getNeighborPos(current_pos[0], current_pos[1])
    for neighbor in neighbors:
        if neighbor in elves:
            wantsToMove = True
    if wantsToMove:
        for direction in precedence_dirs:
            if canMoveInDirection(current_pos, elves, direction):
                return directionToPos(current_pos, direction)
    # Either doesn't want to move or nowhere to move
    return current_pos
    
def checkIfCanMove(elvesWantingToMove):
    observedMovePlaces = set()
    results = set()
    for elf in elvesWantingToMove:
        if elf in observedMovePlaces:
            results.remove(elf)
        else:
            observedMovePlaces.add(elf)
            results.add(elf)
    return results

def moveElf(elf, new_elf, elves):
    elves.remove(elf)
    elves.add(new_elf)
    return elves
            
def processRound(elves, precedenceDirs):
    elves = set(elves)
    wantsToMove = {}
    for elf in elves:
        placeToMove = consider(elf, elves, precedenceDirs)
        if placeToMove != elf:
            wantsToMove[elf] = placeToMove
    noDuplicateMoves = checkIfCanMove(wantsToMove.values())
    for elf_key in wantsToMove:
        if wantsToMove[elf_key] in noDuplicateMoves:
            elves = moveElf(elf_key, wantsToMove[elf_key], elves)
    return elves

def doTheRounds(elves):
    precedenceDirs = ['N', 'S', 'W', 'E']
    i = 0
    while(True):
        i += 1
        newElves = processRound(elves, precedenceDirs)
        precedenceDirs = rotatePrecedence(precedenceDirs)
        if elves == newElves:
            print(i)
            return i
        elves = newElves
'''
def countWhiteSpace(elves):
    minElfLeft = 3
    maxElfRight = 3
    minElfTop = 3
    maxElfBottom = 3
    for elf in elves:
        if elf[1] < minElfLeft:
            minElfLeft = elf[1]
        if elf[1] > maxElfRight:
            maxElfRight = elf[1]
        if elf[0] < minElfTop:
            minElfTop = elf[0]
        if elf[0] > maxElfBottom:
            maxElfBottom = elf[0]
    result = 0
    print(minElfLeft, maxElfRight, minElfTop, maxElfBottom)
    for row in range(minElfTop, maxElfBottom+1):
        for col in range(minElfLeft, maxElfRight+1):
            if (row,col) not in elves:
                # print('.', end="")
                result += 1
            else:
                pass
                # print('#', end="")
        # print()
    return result
'''

elves = doTheRounds(elves)
fileContents = open("AdventOfCode2022/Day 9/input.txt")
arr = fileContents.read().split("\n")

positionHead = (0,0)
positionTail = (0,0)
positionsTailHasBeen = set((0,0))

adjacentSpaces = [(1,0), (1,1), (1,-1), 
                  (0,0), (0,1), (0, -1),
                  (-1,0), (-1,1), (-1,-1)]

diagnoalDirections = [(-1,-1), (1,1), (-1,1), (1,-1)]
otherDirections = [(1,0), (0,1), (0,-1), (-1,0)]

directions = {
                'L': (-1, 0),
                'R': (1, 0),
                'D': (0, -1),
                'U': (0, 1),
                }

def isDiagonal(positionHead, positionTail):
    coords = (abs(positionHead[0] - positionTail[0]), abs(positionHead[1] - positionTail[1])) 
    if coords in diagnoalDirections:
        return True

def adjacent(positionTail, positionHead):
    #print(positionTail, positionHead)
    coords = (abs(positionHead[0] - positionTail[0]), abs(positionHead[1] - positionTail[1])) 
    if coords in adjacentSpaces:
        return True

def followHeadDiagonal(positionTail, positionHead):
    for dir in diagnoalDirections:
        possibleNewPlace = (positionTail[0] + dir[0], positionTail[1] + dir[1])
        # print("Possible New Place", possibleNewPlace)
        if adjacent(possibleNewPlace, positionHead):
            return possibleNewPlace
    # print(positionHead, positionTail, "What happened?")

def followHeadNormal(positionTail, positionHead):
    for dir in otherDirections:
        possibleNewPlace = (positionTail[0] + dir[0], positionTail[1] + dir[1])
        # print("Possible New Place", possibleNewPlace)
        if adjacent(possibleNewPlace, positionHead):
            return possibleNewPlace

def moveHead(direction, positionHead):
    newPositionHead = (positionHead[0] + directions[direction][0], positionHead[1] + directions[direction][1])
    # print(newPositionHead)
    return newPositionHead

def moveTail(positionHead, newPositionHead, positionTail, addToDict = False):
    # print("a", positionHead, positionTail, newPositionHead)
    if adjacent(positionTail, newPositionHead):
        newPositionTail = positionTail
    else:
        if isDiagonal(positionHead,positionTail):
            newPositionTail = followHeadDiagonal(positionTail, newPositionHead)
        else: 
            newPositionTail = followHeadNormal(positionTail, newPositionHead)
        if addToDict:
            positionsTailHasBeen.add(newPositionTail)
    return newPositionTail

all_tail_head_positions = [(0,0)]

for line in arr:
    leftright = line.split(' ')
    direction = leftright[0]
    count = int(leftright[1])
    for i in range(count):
        newPositionHead = moveHead(direction, positionHead)
        if i == 4:
            addToDict = True
        else:
            addToDict = False
        newPositionTail = moveTail(positionHead, newPositionHead, positionTail, addToDict)
        positionHead, positionTail = newPositionHead, newPositionTail
        all_tail_head_positions.append(positionTail)

print(all_tail_head_positions)

for i in range(9):
    positionHead = (0,0)
    positionTail = (0,0)
    new_all_tail_head_positions = []
    for newHeadPosition in all_tail_head_positions:
        newPositionTail = moveTail(positionHead, newHeadPosition, positionTail)
        headPosition, tailPosition = newHeadPosition, newPositionTail
        new_all_tail_head_positions.append(positionTail)
    all_tail_head_positions = new_all_tail_head_positions
    # print(len(all_tail_head_positions))


print(len(positionsTailHasBeen))
print(len(set(all_tail_head_positions)))
print(positionsTailHasBeen)


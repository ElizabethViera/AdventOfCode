fileContents = open("AdventOfCode2022/Day 9/input.txt")
arr = fileContents.read().split("\n")

coords = {
    'Head': (0,0),
    '1': (0,0),
    '2': (0,0),
    '3': (0,0),
    '4': (0,0),
    '5': (0,0),
    '6': (0,0),
    '7': (0,0),
    '8': (0,0),
    '9': (0,0),
    }

placesNineHasBeen = set()

diagonalDirs = ['LU', 'LD', 'RD', 'RU']

orthoDirs = ['L', 'R', 'D', 'U']

def movePointInDirection(point, direction):
    if direction == 'L':
        return (point[0]-1, point[1])
    if direction == 'R':
        return (point[0]+1, point[1])
    if direction == 'U':
        return (point[0], point[1] + 1)
    if direction == 'D':
        return (point[0], point[1] - 1)
    if direction == 'LU':
        return (point[0]-1, point[1] + 1)
    if direction == 'LD':
        return (point[0]-1, point[1] - 1)
    if direction == 'RD':
        return (point[0]+1, point[1] - 1)
    if direction == 'RU':
        return (point[0]+1, point[1] + 1)
    if direction == 'O':
        return (point[0], point[1])
    print("HEY, THIS DIRECTION ISN'T VALID", direction)

def getDirectionOfMovement(oldCoords, newCoords):
    if oldCoords == newCoords:
        return 'O'
    for direction in diagonalDirs + orthoDirs:
        if movePointInDirection(oldCoords, direction) == newCoords:
            return direction

def isAdjacent(point1, point2):
    return abs(point1[0] - point2[0]) in [0,1] and abs(point1[1] - point2[1]) in [0,1]

def isDiagonal(point1, point2):
    return abs(point1[0] - point2[0]) !=  abs(point1[1] - point2[1])

def headAndTailInLine(point1, point2):
    return point1[0] == point2[0] or point1[1] == point2[1]

def shouldMoveTail(head, tail):
    return not isAdjacent(head, tail)

def moveTail(headCoords, tailCoords):
    dirs = orthoDirs if headAndTailInLine(headCoords, tailCoords) else diagonalDirs

    for dir in dirs:
        possibleNewPlace = movePointInDirection(tailCoords, dir)
        if isAdjacent(headCoords, possibleNewPlace):
            return possibleNewPlace
    print("HELP, I DIDN'T FIND A PLACE TO PUT MY TAIL")

def moveSnakeSegment(direction, headCoords, tailCoords):
    if direction == 'O':
        return (headCoords, tailCoords)
    movedHeadCoords = movePointInDirection(headCoords, direction)
    if shouldMoveTail(movedHeadCoords, tailCoords):    
        movedTailCoords = moveTail(movedHeadCoords, tailCoords)
        return (movedHeadCoords, movedTailCoords)
    return (movedHeadCoords, tailCoords)

def moveWholeSnake(direction):
    # print(direction)
    newHead, newTail = moveSnakeSegment(direction, coords['Head'], coords['1'])
    coords['Head'] = newHead
    tail_direction = getDirectionOfMovement(coords['1'], newTail)
    
    OneNewPlace, TwoNewPlace = moveSnakeSegment(tail_direction, coords['1'], coords['2'])
    coords['1'] = OneNewPlace
    tail_direction = getDirectionOfMovement(coords['2'], TwoNewPlace)

    TwoNewPlace, ThreeNewPlace = moveSnakeSegment(tail_direction, coords['2'], coords['3'])
    coords['2'] = TwoNewPlace
    tail_direction = getDirectionOfMovement(coords['3'], ThreeNewPlace)

    ThreeNewPlace, FourNewPlace = moveSnakeSegment(tail_direction, coords['3'], coords['4'])
    coords['3'] = ThreeNewPlace
    tail_direction = getDirectionOfMovement(coords['4'], FourNewPlace)

    FourNewPlace, FiveNewPlace = moveSnakeSegment(tail_direction, coords['4'], coords['5'])
    coords['4'] = FourNewPlace
    tail_direction = getDirectionOfMovement(coords['5'], FiveNewPlace)

    FiveNewPlace, SixNewPlace = moveSnakeSegment(tail_direction, coords['5'], coords['6'])
    coords['5'] = FiveNewPlace
    tail_direction = getDirectionOfMovement(coords['6'], SixNewPlace)

    SixNewPlace, SevenNewPlace = moveSnakeSegment(tail_direction, coords['6'], coords['7'])
    coords['6'] = SixNewPlace
    tail_direction = getDirectionOfMovement(coords['7'], SevenNewPlace)

    SevenNewPlace, EightNewPlace = moveSnakeSegment(tail_direction, coords['7'], coords['8'])
    coords['7'] = SevenNewPlace
    tail_direction = getDirectionOfMovement(coords['8'], EightNewPlace)

    EightNewPlace, NineNewPlace = moveSnakeSegment(tail_direction, coords['8'], coords['9'])
    coords['8'] = EightNewPlace

    coords['9'] = NineNewPlace
    placesNineHasBeen.add(NineNewPlace)

for line in arr:
    leftright = line.split(' ')
    direction = leftright[0]
    count = int(leftright[1])
    for i in range(count):
        moveWholeSnake(direction)
    #print(coords)

print(len(placesNineHasBeen))

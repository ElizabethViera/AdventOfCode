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

def shouldMoveTail(head, tail):
    return not isAdjacent(head, tail)

def moveTail(headCoords, tailCoords, dirs):
    for dir in dirs:
        possibleNewPlace = movePointInDirection(tailCoords, dir)
        if isAdjacent(headCoords, possibleNewPlace):
            return possibleNewPlace

def moveSnakeSegment(direction, headName, tailName):
    if direction == 'O':
        return (coords[headName], coords[tailName])
    movedHeadCoords = movePointInDirection(coords[headName], direction)
    if shouldMoveTail(movedHeadCoords, coords[tailName]):
        
        dirs = orthoDirs if isDiagonal(coords[headName], coords[tailName]) else diagonalDirs
            
        movedTailCoords = moveTail(movedHeadCoords, coords[tailName], dirs)
        return (movedHeadCoords, movedTailCoords)
    return (movedHeadCoords, coords[tailName])

def moveWholeSnake(direction):
    print(direction)
    newHead, newTail = moveSnakeSegment(direction, 'Head', '1')
    coords['Head'] = newHead
    tail_direction = getDirectionOfMovement(coords['1'], newTail)
    
    OneNewPlace, TwoNewPlace = moveSnakeSegment(tail_direction, '1', '2')
    coords['1'] = OneNewPlace
    tail_direction = getDirectionOfMovement(coords['2'], TwoNewPlace)

    print('Moved 1')

    TwoNewPlace, ThreeNewPlace = moveSnakeSegment(tail_direction, '2', '3')
    coords['2'] = TwoNewPlace
    tail_direction = getDirectionOfMovement(coords['3'], ThreeNewPlace)

    ThreeNewPlace, FourNewPlace = moveSnakeSegment(tail_direction, '3', '4')
    coords['3'] = ThreeNewPlace
    tail_direction = getDirectionOfMovement(coords['4'], FourNewPlace)

    FourNewPlace, FiveNewPlace = moveSnakeSegment(tail_direction, '4', '5')
    coords['4'] = FourNewPlace
    tail_direction = getDirectionOfMovement(coords['5'], FiveNewPlace)

    FiveNewPlace, SixNewPlace = moveSnakeSegment(tail_direction, '5', '6')
    coords['5'] = FiveNewPlace
    tail_direction = getDirectionOfMovement(coords['6'], SixNewPlace)

    SixNewPlace, SevenNewPlace = moveSnakeSegment(tail_direction, '6', '7')
    coords['6'] = SixNewPlace
    tail_direction = getDirectionOfMovement(coords['7'], SevenNewPlace)

    SevenNewPlace, EightNewPlace = moveSnakeSegment(tail_direction, '7', '8')
    coords['7'] = SevenNewPlace
    tail_direction = getDirectionOfMovement(coords['8'], EightNewPlace)

    EightNewPlace, NineNewPlace = moveSnakeSegment(tail_direction, '8', '9')
    coords['8'] = EightNewPlace

    coords['9'] = NineNewPlace
    placesNineHasBeen.add(NineNewPlace)

for line in arr:
    leftright = line.split(' ')
    direction = leftright[0]
    count = int(leftright[1])
    for i in range(count):
        moveWholeSnake(direction)
    print(coords)

print(len(placesNineHasBeen))

fileContents = open("AdventOfCode2022/Day 15/input.txt")
arr = fileContents.read().split("\n")
Sensors = []
Beacons = []
blockedOut = set()

for line in arr:
    contents = line.split(' ')
    Sx,Sy,Bx,By = int(contents[2][2:-1]), int(contents[3][2:-1]), int(contents[-2][2:-1]), int(contents[-1][2:]) 
    Sensors.append((Sx, Sy))
    Beacons.append((Bx, By))

def getDistance(pointA, pointB):
    # Manhattan Distance
    xDist = abs(pointA[0] - pointB[0])
    yDist = abs(pointA[1] - pointB[1])
    return xDist + yDist


def isBlocked(point):
    for i in range(len(Beacons)):
        distance = getDistance(Beacons[i], Sensors[i])
        if getDistance(Sensors[i], point) <= distance and point not in Beacons:
            return True
    return False

def addPoints(pointA, pointB):
    x = pointA[0] + pointB[0]
    y = pointA[1] + pointB[1]
    return (x,y)

def check(row, col):
    if row < 0 or col < 0 or row > 4000000 or col > 4000000:
        return
    if not isBlocked((row,col)):
        print( "FOUND: ", row,col)

def blockOut2(coord, distance):
    total = distance+1
    for i in range(total+1):
        row = coord[0] + total - i
        col = coord[1] + i
        check(row,col)
        row = coord[0] - total + i
        col = coord[1] - i
        check(row,col)
        row = coord[0] - total + i
        col = coord[1] + i
        check(row,col)
        row = coord[0] + total - i
        col = coord[1] - i
        check(row,col)

def blockOut(coord, distance):
    for row in range(distance):
        for col in range(distance):
            if row+col <= distance:
                blockedOut.add(addPoints(coord, (row,col)))
                blockedOut.add(addPoints(coord, (-row,-col)))
                blockedOut.add(addPoints(coord, (row,-col)))
                blockedOut.add(addPoints(coord, (-row,col)))

for i in range(len(Sensors)):
    print(i)
    # i indexes into sensors and beacons for associated things
    distance = getDistance(Sensors[i], Beacons[i])
    blockOut2(Sensors[i], distance)


'''
count = 0
for i in range(0, 4000000):
    for j in range(0, 4000000):
        if not isBlocked((i, j)):
            print(i, j)
    if i%100000 == 0:
        print(i)

maxDistance = 0
for i in range(len(Beacons)):
    distance = getDistance(Beacons[i], Sensors[i])
    if Beacons[i][0] + distance > maxDistance:
        maxDistance = Beacons[i][0] + distance
print(maxDistance)


def filterOnRow(item):
    if item[0] == 2000000:
        return True
    return False
'''
'''
count = 0
filteredListByRow = filter(filterOnRow, blockedOut)
for s in filteredListByRow:
    count += 1

print(count)
'''
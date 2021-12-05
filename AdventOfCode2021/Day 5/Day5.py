import math
fileContents = open("Day 5/input.txt")
arr = fileContents.read().split('\n')


starts = [x.split(' ')[0] for x in arr]

ends = [x.split(' ')[2] for x in arr]

coveredPoints = set()
duplicatedPoints = set()

for index in range(len(starts)):
    start = starts[index].split(',')
    x1 = int(start[0])
    y1 = int(start[1])
    end = ends[index].split(',')
    x2 = int(end[0])
    y2 = int(end[1])

    x_change = abs(x2-x1) + 1
    y_change = abs(y2-y1) + 1
    dir = [math.copysign(1, x2-x1), math.copysign(1, y2-y1)]
    if (x1 == x2):
        dir[0] = 0
    if (y1 == y2):
        dir[1] = 0
    for r in range(max(x_change, y_change)):
        x = x1 + r*(dir[0])
        y = y1 + r*(dir[1])
        if (x, y) in coveredPoints:
            duplicatedPoints.add((x, y))
        coveredPoints.add((x, y))
print('\n', len(duplicatedPoints))

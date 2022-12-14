fileContents = open("AdventOfCode2022/Day 14/input.txt")
arr = fileContents.read().split("\n")

rocks = set()
for line in arr:
    points = line.split(' -> ')
    coords = []
    for point in points:
        x, y = int(point.split(',')[0]), int(point.split(',')[1])
        coords.append((x,y))
    previous = coords[0]
    for current in coords[1:]:
        if previous[0] == current[0]:
            for y in range(previous[1], current[1]+1):
                rocks.add((previous[0], y))
            for y in range(current[1], previous[1]+1):
                rocks.add((previous[0], y))
        if previous[1] == current[1]:
            # range is x coord
            for x in range(previous[0], current[0]+1):
                rocks.add((x, previous[1]))
            for x in range(current[0], previous[0]+1):
                rocks.add((x, previous[1]))
        previous = current
def sortkey(rock):
    return rock[1]

print(sorted(rocks, key=sortkey)[::-1])
# print(len(rocks))
sand = set()


def canMoveSand(point):
    x,y = point[0], point[1]
    if (point[0], point[1]+1) not in rocks:
        return (point[0], point[1]+1)
    if  (point[0]-1, point[1]+1) not in rocks:
        return (point[0]-1, point[1]+1)
    if (point[0]+1, point[1]+1) not in rocks:
        return (point[0]+1, point[1]+1)
    return False

def rainSand():
    currentSand = (500, 0)
    while(True):
        rocks.add(currentSand)
        can_move = canMoveSand(currentSand)
        if not can_move:
            sand.add(currentSand)
            return True
        else:
            rocks.remove(currentSand)
            currentSand = can_move

count = 0
while(True):
    count += 1
    rainSand()
    if (500,0) in sand:
        break
        
    

print(count)
# print(rocks)
'''
for col in range(0, 11):
    for row in range(490, 505):
        if (row, col) in sand:
             print('o', end='')
        elif (row,col) in rocks:
            print('x', end='')
        else:
            print(',', end='')
    print('')
'''
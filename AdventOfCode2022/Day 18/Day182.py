fileContents = open("AdventOfCode2022/Day 18/input.txt")
arr = fileContents.read().split("\n")
import sys
sys.setrecursionlimit(20000)

MIN_NUMBER = 0
MAX_NUMBER = 21

cubes = set()
for cube in arr:
    x,y,z = int(cube.split(',')[0]), int(cube.split(',')[1]), int(cube.split(',')[2])
    cubes.add((x,y,z))


dirs = [(0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,0,-1), (0,0,1)]

def addDir(cube, direction):
    # print(cube, direction)
    return cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2]

def outOfBounds(point):
    if point[0] < 0 or point[0] > MAX_NUMBER or point[1] < 0 or point[1] > MAX_NUMBER or point[2] < 0 or point[2] > MAX_NUMBER:
        return True
    return False

faces = 0

visited = set()

def floodFill(point):
    # print(point)
    visited.add(point)
    neighbors = [addDir(point, dir) for dir in dirs]
    for neighbor in neighbors:
        if outOfBounds(neighbor):
            continue
        elif neighbor in visited or neighbor in cubes:
            continue
        else:
            floodFill(neighbor)

floodFill((0,0,0))

airPocket = set()
for i in range(MIN_NUMBER,MAX_NUMBER):
    for j in range(MIN_NUMBER, MAX_NUMBER):
        for k in range(MIN_NUMBER,MAX_NUMBER):
            if (i,j,k) not in visited and (i,j,k) not in cubes:
                airPocket.add((i,j,k))

for air in airPocket:
    cubes.add(air)

print(sorted(airPocket))

faces = 0
for cube in sorted(cubes):
    for direction in dirs:
        neighbor = addDir(cube, direction)
        if neighbor not in cubes:
            faces += 1
print(faces)
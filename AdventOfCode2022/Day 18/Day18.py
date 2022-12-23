fileContents = open("AdventOfCode2022/Day 18/input.txt")
arr = fileContents.read().split("\n")

cubes = set()
for cube in arr:
    x,y,z = int(cube.split(',')[0]), int(cube.split(',')[1]), int(cube.split(',')[2])
    cubes.add((x,y,z))

print(cubes)

dirs = [(0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,0,-1), (0,0,1)]

def addDir(cube, direction):
    print(cube, direction)
    return cube[0] + direction[0], cube[1] + direction[1], cube[2] + direction[2]

faces = 0
for cube in sorted(cubes):
    for direction in dirs:
        neighbor = addDir(cube, direction)
        if neighbor not in cubes:
            faces += 1
print(faces)

fileContents = open("AdventOfCode2023/Day 21/input.txt")
arr = fileContents.read().split("\n")

rock_coords = set()
walkable_coords = set()

start_pos = (-1, -1)

for r,line in enumerate(arr):
    for c, i in enumerate(line):
        if i == 'S':
            start_pos = (r,c)
        if i != '#':
            walkable_coords.add((r,c))

neighbors = dict()

dirs = [(1,0), (-1,0), (0,-1), (0,1)]

def addPts(a,b):
    return (a[0] + b[0], a[1]+b[1])

def getNeighbors(c):
    result = []
    for direction in dirs:
        if addPts(c, direction) in walkable_coords:
            result.append(addPts(c, direction))
    return result
    

for walkable_coord in walkable_coords:
    neighbors[walkable_coord] = getNeighbors(walkable_coord)


reachable = dict()
reachable[0] = [start_pos]


for i in range(64):
    reachable[i+1] = []
    for coord in reachable[i]:
        for neighbor in neighbors[coord]:
            reachable[i+1].append(neighbor)
    reachable[i+1] = list(set(reachable[i+1]))

print(len(set(reachable[64])))

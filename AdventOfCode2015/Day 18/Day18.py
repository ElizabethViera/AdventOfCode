def changeLights(on_set_at_time):
    new_on_set = set()
    for light in alwaysOn:
        new_on_set.add(light)
    for i in range(rows+1):
        for j in range(cols+1):
            count = 0
            all_neighbors = getNeighbors(i, j)
            for neighbor in all_neighbors:
                if neighbor in on_set_at_time:
                    count += 1
            if (i,j) in on_set_at_time:
                if count == 2 or count == 3:
                    new_on_set.add((i,j))
            else:
                if count == 3:
                    new_on_set.add((i,j))
    return new_on_set

def isValidNeighbor(row,col):
    if row < 0 or row > rows:
        return False
    if col < 0 or col > cols:
        return False
    return True

def getNeighbors(row,col):
    neighbors = []
    neighbor_dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for neighbor in neighbor_dirs:
        if isValidNeighbor(row + neighbor[0], col + neighbor[1]):
            neighbors.append((row + neighbor[0], col + neighbor[1]))
    return neighbors

def printGrid(lightSet):
    for i in range(rows+1):
        for j in range(col+1):
            if (i,j) in lightSet:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("\n")

def callLightSwitchNTimes(n, original_on_set):
    for i in range(n):
        original_on_set = changeLights(original_on_set)
    return(original_on_set)

alwaysOn = [(0,0), (0,99), (99,0), (99,99)]

fileContents = open("AdventOfCode2015/Day 18/input.txt")
arr = fileContents.read().split("\n")

rows = 99
cols = 99

on_set = set()

for light in alwaysOn:
    on_set.add(light)
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col] == "#":
            on_set.add((row,col))

print(len(on_set))
print(len(callLightSwitchNTimes(100, on_set)))






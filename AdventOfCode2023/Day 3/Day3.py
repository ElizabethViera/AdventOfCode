fileContents = open("AdventOfCode2023/Day 3/input.txt")
arr = fileContents.read().split("\n")



def inbounds(row, col):
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return False
    return True

def getNeighbors(row, col):
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1),
                ]
    results = []
    for neighbor in neighbors:
        if inbounds(row+neighbor[0], col+neighbor[1]):
            results.append((row+neighbor[0], col+neighbor[1]))
    return results

numbersWithInterestingNeighbors = dict()
numbersWithSymbolNeighbors = set()

def gridAt(g):
    return arr[g[0]][g[1]]

for row in range(len(arr)):
    for col in range(len(arr[0])):
        loc = (row, col)
        if gridAt(loc) in '1234567890':
            neighbors = getNeighbors(row, col)
            for neighbor in neighbors:
                if gridAt(neighbor) != '.':
                    if loc not in numbersWithInterestingNeighbors:
                        numbersWithInterestingNeighbors[loc] = []
                    numbersWithInterestingNeighbors[loc].append(neighbor)
                    if gridAt(neighbor) not in '1234567890':
                        numbersWithSymbolNeighbors.add(loc)
print(len(numbersWithInterestingNeighbors), len(numbersWithSymbolNeighbors))


def doesNumberHaveSymbolNearIt(loc):
    visited = set()
    q = [loc]
    foundSymbol = False
    while q != []:
        current = q.pop()
        visited.add(current)
        if current in numbersWithSymbolNeighbors:
            foundSymbol = True
        
        for neighbor in numbersWithInterestingNeighbors[current]:
            if neighbor not in visited:
                q.append(neighbor)
    if foundSymbol:
        return visited
    return []

greenRegions = set()
for num in numbersWithInterestingNeighbors:
    for green in doesNumberHaveSymbolNearIt(num):
        greenRegions.add(green)

def printGrid(s):
    for i in range(10):
        for j in range(10):
            if (i,j) in s:
                print('G', end='')
            else:
                print('.', end='')
        print('\n')

printGrid(sorted(greenRegions))
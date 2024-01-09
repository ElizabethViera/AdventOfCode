from pydoc import describe
from re import search


fileContents = open("AdventOfCode2016/Day 24/input.txt")
lines = fileContents.read().split("\n")

walls = set()
destinations = dict()
for row, r in enumerate(lines):
    for col, c in enumerate(r):
        if c == '.':
            continue
        if c == '#':
            walls.add((row,col))
        else:
            destinations[int(c)] = (row,col)


def getNeighbors(x,y) -> list[tuple[int,int]]:
    neighbors = []
    neighborDirs = [(-1,0), (1,0), (0,-1), (0,1)]
    for n in neighborDirs:
        if (x+n[0], y+n[1]) not in walls:
            neighbors.append((x+n[0], y+n[1]))
    return neighbors

def shortestPathLength(a,b):
    searching: list[tuple[tuple[int, int], int]] = [(a,0)]
    visited = set()
    while searching != []:
        current = searching.pop(0)
        if current[0] == b:
            return current[1]
        neighbors = getNeighbors(current[0][0], current[0][1])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                searching.append((neighbor, current[1]+1))

shortestPaths = dict()
for d1 in destinations:
    for d2 in destinations:
        if d1 == d2:
            continue
        else:
            shortestPaths[(d1, d2)] = shortestPathLength(destinations[d1], destinations[d2])

from itertools import permutations
shortestSum = 100000
for p in permutations([1,2,3,4,5,6,7]):
    total = 0

    total += shortestPaths[(0, p[0])]
    total += shortestPaths[(0, p[6])]
    for i in range(1,7):
        total += shortestPaths[(p[i-1], p[i])]
   
    if total < shortestSum:
        shortestSum = total
print(shortestSum)
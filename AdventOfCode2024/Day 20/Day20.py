from queue import PriorityQueue
from datetime import datetime

begin = datetime.now()

listsContents = open("AdventOfCode2024/Day 20/input.txt")
lines = listsContents.read().split("\n")

walls = set()
walkable = set()


for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char == "#":
            walls.add((r, c))
        if char == ".":
            walkable.add((r, c))
        if char == "S":
            start = (r, c)
            walkable.add(start)
        if char == "E":
            end = (r, c)
            walkable.add(end)


def getNeighbors(p, walkable):
    results = []
    for d in dirs:
        neighbor = (p[0] + d[0], p[1] + d[1])
        if neighbor in walkable:
            results.append(neighbor)
    return results


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def getDistance(walkable):
    distances = dict()
    to_search = PriorityQueue()
    to_search.put((0, (start[0], start[1])))
    while to_search.qsize() > 0:
        current = to_search.get()  # (distance, (coord, coord))
        if current[1] in distances:
            continue
        if (current[1][0], current[1][1]) == end:
            return current[0]
        else:
            distances[current[1]] = current[0]
            distance = current[0]
            pos = current[1]
            neighbors = getNeighbors(pos, walkable)
            for neighbor in neighbors:
                to_search.put((distance + 1, (neighbor[0], neighbor[1])))
    raise (ValueError)


base_distance = getDistance(walkable)
print(base_distance)

result = 0

print(len(walls))
i = 0
for wall in walls:
    i += 1
    if i % 1000 == 0:
        print(i)
    walkable.add(wall)
    new_distance = getDistance(walkable)
    if base_distance - new_distance > 99:
        result += 1
    walkable.remove(wall)
print(result)
finish = datetime.now()

print(finish - begin)

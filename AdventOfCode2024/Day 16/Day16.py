from queue import PriorityQueue

listsContents = open("AdventOfCode2024/Day 16/input.txt")
tiles = listsContents.read().split("\n")

pos = tuple[str, int, int]

walls = set()
walkable = set()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

for r, row in enumerate(tiles):
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


def getNeighbors(pos):
    result = dict()
    d = pos[0]
    if d > 3:
        d %= 4
    if d < -3:
        d += 4
    result["left"] = (d - 1, pos[1], pos[2])
    result["right"] = (d + 1, pos[1], pos[2])
    direction = dirs[d]
    forward = pos[1] + direction[0], pos[2] + direction[1]
    result["forward"] = (d, forward[0], forward[1])
    return result


def getDistance():
    distances = dict()
    to_search = PriorityQueue()
    to_search.put((0, (0, start[0], start[1])))
    while to_search.qsize() > 0:
        current = to_search.get()  # (distance, (direction, coord, coord))
        if current[1] in distances:
            continue
        if (current[1][1], current[1][2]) == end:
            return current[0]
        else:
            distances[current[1]] = current[0]
            distance = current[0]
            pos = current[1]
            neighbors = getNeighbors(pos)
            to_search.put((distance + 1000, neighbors["left"]))
            to_search.put((distance + 1000, neighbors["right"]))
            if (neighbors["forward"][1], neighbors["forward"][2]) in walkable:
                to_search.put((distance + 1, neighbors["forward"]))

    return distances


all_distances = getDistance()
print(all_distances)

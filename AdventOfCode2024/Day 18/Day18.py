listsContents = open("AdventOfCode2024/Day 18/input.txt")
ins = listsContents.read().split("\n")


def getNeighbors(p, walkable):
    results = []
    for d in dirs:
        neighbor = (p[0] + d[0], p[1] + d[1])
        if neighbor in walkable:
            results.append(neighbor)
    return results


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def canGetToDestination(walls):
    walkable = set()
    destination = (70, 70)

    for r in range(71):
        for c in range(71):
            if (r, c) not in walls:
                walkable.add((r, c))

    visited = dict()
    visited[(0, 0)] = 0
    visit = [(0, 0)]
    while visit != []:
        current = visit.pop(0)
        neighbors = getNeighbors(current, walkable)
        for n in neighbors:
            if n in visited:
                continue
            else:
                visited[n] = visited[current] + 1
                visit.append(n)
    return destination in visited


walls = set()

for i in ins:
    left, right = i.split(",")
    left, right = int(left), int(right)
    walls.add((left, right))
    if not canGetToDestination(walls):
        print(left, right)
        break

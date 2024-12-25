listsContents = open("AdventOfCode2024/Day 10/input.txt")
rows = listsContents.read().split("\n")

trails = dict()

pos = tuple[int, int]

for r, row in enumerate(rows):
    for c, char in enumerate(row):
        if char != ".":
            trails[(r, c)] = int(char)


def add_pts(a, b):
    return a[0] + b[0], a[1] + b[1]


def getNeighbors(p: pos) -> list[pos]:
    result = []
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for dir in dirs:
        neighbor = add_pts(dir, p)
        if neighbor in trails:
            result.append(neighbor)
    return result


def get_trail_ends(s: pos):
    result: set[tuple[pos, ...]] = set()
    explore_paths: list[tuple[pos, ...]] = [(s,)]
    while explore_paths != []:
        path: tuple[pos, ...] = explore_paths.pop(0)  # (a, b, c, d)
        if trails[path[-1]] == 9:
            result.add(path)
            continue
        for neighbor in getNeighbors(path[-1]):
            if trails[neighbor] == trails[path[-1]] + 1:
                new_trail = list(path) + [neighbor]  # [a, b, c] + [d]
                explore_paths.append(tuple(new_trail))
    return len(result)


result = 0
for trail in trails:
    if trails[trail] == 0:
        result += get_trail_ends(trail)

print(result)

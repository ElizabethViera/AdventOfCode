listsContents = open("AdventOfCode2024/Day 10/input.txt")
rows = listsContents.read().split("\n")

trails = dict()


for r, row in enumerate(rows):
    for c, char in enumerate(row):
        if char != ".":
            trails[(r, c)] = int(char)


def add_pts(a, b):
    return a[0] + b[0], a[1] + b[1]


def getNeighbors(p):
    result = []
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for dir in dirs:
        neighbor = add_pts(dir, p)
        if neighbor in trails:
            result.append(neighbor)
    return result


def get_trail_ends(s):
    result = set()
    explore_paths = [s]
    while explore_paths != []:
        # print(explore_paths)
        path = explore_paths.pop(0)
        for neighbor in getNeighbors(path):
            if trails[neighbor] == trails[path] + 1:
                if trails[neighbor] == 9:
                    result.add(neighbor)
                explore_paths.append(neighbor)
    # print(result)
    return len(result)


result = 0
for trail in trails:
    if trails[trail] == 0:
        # print(get_trail_ends(trail))
        result += get_trail_ends(trail)

print(result)

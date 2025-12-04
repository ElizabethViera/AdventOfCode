fileContents = open("AdventOfCode2025/Day 4/input.txt")
arr = fileContents.read().split("\n")
# print(arr)


def parse(s):
    rolls = set()
    for row, line in enumerate(s):
        for col, c in enumerate(line):
            if c == ".":
                pass
            if c == "@":
                rolls.add((row, col))

    return rolls


def addPts(a, b):
    return a[0] + b[0], a[1] + b[1]


def getNeighbors(p, rolls):
    total = 0
    neighborLocs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
    ]
    for loc in neighborLocs:
        neighbor = addPts(p, loc)
        if neighbor in rolls:
            total += 1
    return total


all_rolls = parse(arr)


def remove_stuff(rolls):
    to_remove = set()
    count = 0
    while True:
        for roll in rolls:
            neighbors = getNeighbors(roll, rolls)
            if neighbors < 4:
                to_remove.add(roll)
        if len(to_remove) == 0:
            break
        for r in to_remove:
            if r in rolls:
                rolls.remove(r)
                count += 1
        to_remove = set()
    return count


print(remove_stuff(all_rolls))

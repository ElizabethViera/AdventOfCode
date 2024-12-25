listsContents = open("AdventOfCode2024/Day 25/input.txt")
lines = listsContents.read().split("\n\n")

keys = dict()
locks = dict()

for b, block in enumerate(lines):
    heights = [0, 0, 0, 0, 0]
    for r, row in enumerate(block.split("\n")):
        for c, char in enumerate(row):
            if char == "#":
                heights[c] += 1
    isLock = block[0][0] == "#"
    if isLock:
        locks[b] = heights
    else:
        keys[b] = heights

result = 0
for key in keys:
    for lock in locks:
        fits = True
        for i in range(5):
            if keys[key][i] + locks[lock][i] > 7:
                fits = False
        if fits:
            result += 1
print(result)

fileContents = open("AdventOfCode2025/Day 7/input.txt")
arr = fileContents.read().split("\n")
# print(arr)

tachyons = set()

for r, row in enumerate(arr):
    for c, char in enumerate(row):
        if char == "^":
            tachyons.add((r, c))
        if char == "S":
            start = (r, c)

rows = len(arr)

total = 0
beam = [start]
visited = set()
while beam != []:
    current_place = beam.pop()
    if current_place in visited:
        continue
    visited.add(current_place)
    if current_place[0] > rows:
        continue
    elif current_place in tachyons:
        total += 1
        beam.append((current_place[0], current_place[1] - 1))
        beam.append((current_place[0], current_place[1] + 1))
    else:
        beam.append((current_place[0] + 1, current_place[1]))

print(total)

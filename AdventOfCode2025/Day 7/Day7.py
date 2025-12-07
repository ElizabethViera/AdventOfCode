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

# total = 0
# beam = [start]
# visited = set()
# while beam != []:
#     current_place = beam.pop()
#     if current_place in visited:
#         continue
#     visited.add(current_place)
#     if current_place[0] > rows:
#         continue
#     elif current_place in tachyons:
#         total += 1
#         beam.append((current_place[0], current_place[1] - 1))
#         beam.append((current_place[0], current_place[1] + 1))
#     else:
#         beam.append((current_place[0] + 1, current_place[1]))

# print(total)


def computeNextLayer(sources):
    next_sources = dict()
    if sources[0][0][0] > rows:
        return sum([i[1] for i in sources])
    for source in sources:
        # a source is a location, and a number of ways to get to that location
        if source[0] in tachyons:
            left = (source[0][0] + 1, source[0][1] + 1)
            right = (source[0][0] + 1, source[0][1] - 1)
            if left not in next_sources:
                next_sources[left] = source[1]
            else:
                next_sources[left] += source[1]
            if right not in next_sources:
                next_sources[right] = source[1]
            else:
                next_sources[right] += source[1]
        else:
            next = (source[0][0] + 1, source[0][1])
            if next not in next_sources:
                next_sources[next] = source[1]
            else:
                next_sources[next] += source[1]
    result = []
    for s in next_sources:
        result.append((s, next_sources[s]))
    return computeNextLayer(result)


print(computeNextLayer([(start, 1)]))

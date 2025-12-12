fileContents = open("AdventOfCode2025/Day 11/input.txt")
arr = fileContents.read().split("\n")
# print(arr)

connections = dict()

for line in arr:
    key = line.split(": ")[0]
    values = line.split(": ")[1].split()
    connections[key] = values


def getPaths(connects, source):
    if source == "out":
        return 1
    else:
        total = 0
        for child in connects[source]:
            total += getPaths(connects, child)
        return total


print(getPaths(connections, "svr"))

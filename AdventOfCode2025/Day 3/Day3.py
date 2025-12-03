fileContents = open("AdventOfCode2025/Day 3/input.txt")
arr = fileContents.read().split("\n")
print(arr)

total = 0
for line in arr:
    highest = 0
    for ind, c1 in enumerate(line):
        for c2 in line[ind + 1 :]:
            # print(c1, c2)
            if 10 * int(c1) + int(c2) > highest:
                highest = (10 * int(c1)) + int(c2)
    # print(total)
    total += highest
print(total)

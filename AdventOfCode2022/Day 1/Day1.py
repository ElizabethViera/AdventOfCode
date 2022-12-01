fileContents = open("AdventOfCode2022/Day 1/input.txt")
arr = fileContents.read().split('\n')


elfTotal = 0
elvesTotals = []
for line in arr:
    if line == "":
        elvesTotals.append(elfTotal)
        elfTotal = 0
    else:
        elfTotal += int(line)

print(sum(sorted(elvesTotals)[-3:]))
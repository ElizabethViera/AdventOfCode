fileContents = open("AdventOfCode2017/Day 5/input.txt")
arr = fileContents.read().split("\n")

dirs = dict()
for i,line in enumerate(arr):
    dirs[i] = int(line)

steps = 0
current = 0
while current in dirs:
    steps += 1
    next_ins = dirs[current] + current
    if dirs[current] >= 3:
        dirs[current] -= 1
    else:
        dirs[current] += 1
    current = next_ins

print(steps)
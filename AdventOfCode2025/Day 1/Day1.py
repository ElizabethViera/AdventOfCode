fileContents = open("AdventOfCode2025/Day 1/input.txt")
arr = fileContents.read().split("\n")
print(arr)

total = 0
index = 50
for rotation in arr:
    num = int(rotation[1:])
    for i in range(num):
        if rotation[0] == "R":
            index += 1
        else:
            index -= 1
        index %= 100
        if index == 0:
            total += 1
print(total)

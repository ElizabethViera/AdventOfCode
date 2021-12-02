fileContents = open("AdventOfCode2021/Day 2/input.txt")
arr = fileContents.read().split('\n')
arr = [i.split(' ') for i in arr]
print(arr)

depth = 0
fwd = 0
aim = 0
for i in arr:
    if i[0] == 'forward':
        fwd += int(i[1])
        depth += aim * int(i[1])
    else:
        if i[0] == 'up':
            aim -= int(i[1])
        if i[0] == 'down':
            aim += int(i[1])
print(fwd*depth)

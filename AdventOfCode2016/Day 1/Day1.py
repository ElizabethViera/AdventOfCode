fileContents = open("AdventOfCode2016/Day 1/input.txt")
arr = fileContents.read().split(", ")

dirs = ['N', 'W', 'S', 'E']
direction = 0
updown = 0
leftright = 0

def step(dir, n, updown, leftright):
    for i in range(n):
        if dir == "up":
            updown += 1
        if dir == "down":
            updown -= 1
        if dir == "left":
            leftright += 1
        if dir == "right":
            leftright -= 1
        if (updown, leftright) in seen:
            print(updown, leftright)
            print("found", updown, leftright)
            break
        seen.add((updown, leftright))
    return updown, leftright

seen = set()

for ins in arr:
    if ins[0] == "L":
        direction += 1
        direction %= 4
    else:
        direction -= 1
        direction += 4
        direction %= 4
    if dirs[direction] == 'N':
        updown, leftright = step("up", int(ins[1:]), updown, leftright)
    if dirs[direction] == 'S':
        updown, leftright = step("down", int(ins[1:]), updown, leftright)
    if dirs[direction] == 'W':
        updown, leftright = step("left", int(ins[1:]), updown, leftright)
    if dirs[direction] == 'E':
        updown, leftright = step("right", int(ins[1:]), updown, leftright)
    
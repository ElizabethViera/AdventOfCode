fileContents = open("AdventOfCode2023/Day 22/input.txt")
lines = fileContents.read().split("\n")

bricks = []

for line in lines:
    left, right = line.split('~')[0],line.split('~')[1]
    x_l,y_l,z_l = [int(x) for x in left.split(',')]
    x_r,y_r,z_r = [int(x) for x in right.split(',')]
    brick = []
    for x in range(x_l, x_r+1):
        for y in range( y_l, y_r+1):
            for z in range(z_l, z_r+1):
                brick.append((x,y,z))
    bricks.append(brick)

def drop_brick(b):
    new_brick = []
    for wall in b:
        new_wall = (wall[0], wall[1], wall[2]-1)
        new_brick.append(new_wall)
    return new_brick

def is_valid(n, s, ns):
    for wall in n:
        if wall[2] < 1:
            return False
        for b in s:
            if wall in b:
                return False
        for b in ns:
            if wall in b:
                return False
    return True

def drop_all_bricks(brick_list):
    old_state = sorted(brick_list)
    while True:
        new_state = []
        for i, brick in enumerate(old_state):
            new_brick = drop_brick(brick)
            if is_valid(new_brick, old_state[i+1:], new_state):
                new_state.append(new_brick)
            else:
                new_state.append(brick)
        new_state = sorted(new_state)
        if new_state == old_state:
            break
        old_state = new_state
    return new_state


bricks = drop_all_bricks(bricks)

total = 0
for i, brick in enumerate(bricks):
    if i%10 == 0:
        print(i)
    old_bricks = bricks[:i] + bricks[i+1:]
    new_bricks = drop_all_bricks(old_bricks)
    fallen_bricks = len([i for i in new_bricks if i not in old_bricks])
    total += fallen_bricks
print(total)
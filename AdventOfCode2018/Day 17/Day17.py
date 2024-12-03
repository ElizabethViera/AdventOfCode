fileContents = open("AdventOfCode2018/Day 17/input.txt")
contents = fileContents.read().split("\n")

#######
# Misc Helpers
########


def add_pts(x, y):
    return x[0] + y[0], x[1] + y[1]


def sort_by_y(p):
    return p[1]


def sort_by_x(p):
    return p[0]


########
# Parse Initial State
########

walls = set()
falling_water = set()
pooling_water = set()
water_source = (500, 7)
falling_water.add(water_source)

for line in contents:
    left, right = line.split(", ")[0], line.split(", ")[1]
    x = None
    y = None
    if left.startswith("x="):
        x = int(left[2:])
        right = right[2:]
        l = int(right.split("..")[0])
        r = int(right.split("..")[1])
        for k in range(l, r + 1):
            walls.add((x, k))
    else:
        y = int(left[2:])
        right = right[2:]
        l = int(right.split("..")[0])
        r = int(right.split("..")[1])
        for k in range(l, r + 1):
            walls.add((k, y))

########
# Get bounds for when we want to print the grid
########

walls = sorted(walls, key=sort_by_y)
highest_y = walls[-1][1]
lowest_y = walls[0][1]
print(lowest_y)

walls = sorted(walls, key=sort_by_x)
lowest_x = walls[0][0] - 1
highest_x = walls[-1][0] + 1

print(highest_y)

walls = set(walls)


#########
# Render Grid
#########
def render_grid():
    for y in range(0, highest_y + 1):
        line = ""
        for x in range(lowest_x, highest_x + 1):
            if (x, y) == water_source:
                line = line + "+"
            elif (x, y) in walls:
                line = line + "#"
            elif (x, y) in falling_water:
                line = line + "|"
            elif (x, y) in pooling_water:
                line = line + "~"
            else:
                line = line + " "
        print(line)


# render_grid()


def water_falling():
    new_water = []
    for water in falling_water:
        below = add_pts(water, (0, 1))
        if (
            below not in falling_water
            and below not in walls
            and below not in pooling_water
            and below[1] <= highest_y
        ):
            new_water.append(below)
        if below in walls or below in pooling_water:
            # spread left and right
            right = add_pts(water, (-1, 0))
            left = add_pts(water, (1, 0))
            if (
                right not in falling_water
                and right not in walls
                and right not in pooling_water
            ):
                new_water.append(right)
            if (
                left not in falling_water
                and left not in walls
                and left not in pooling_water
            ):
                new_water.append(left)
    return new_water


def identify_pooled_water():
    new_pool = []
    for water in falling_water:
        is_pool_candidate = True

        # left is all water until a wall
        left = add_pts(water, (1, 0))
        while left in falling_water:
            left = add_pts(left, (1, 0))
        if left not in walls:
            is_pool_candidate = False

        # right is all water until a wall
        right = add_pts(water, (-1, 0))
        while right in falling_water:
            right = add_pts(right, (-1, 0))
        if right not in walls:
            is_pool_candidate = False

        # there is a floor below all of these
        if is_pool_candidate:
            for floor_x in range(right[0] + 1, left[0]):
                floor = (floor_x, water[1] + 1)
                if floor not in walls and floor not in pooling_water:
                    is_pool_candidate = False

        if is_pool_candidate:
            new_pool.append(water)
    return new_pool


i = 0
while True:
    i += 1
    # if i % 1000 == 0:
    # print(i)
    new_water = water_falling()
    if new_water != []:
        for w in new_water:
            falling_water.add(w)
        continue

    new_pool = identify_pooled_water()
    if new_pool != []:
        for w in new_pool:
            falling_water.remove(w)
            pooling_water.add(w)
    if new_pool == [] and new_water == []:
        break
# render_grid()
print(len(pooling_water))

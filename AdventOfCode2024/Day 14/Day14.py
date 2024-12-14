listsContents = open("AdventOfCode2024/Day 14/input.txt")
lines = listsContents.read().split("\n")

robots = dict()

wide = 101
tall = 103

for i, line in enumerate(lines):
    left, right = (
        line.split(" v=")[0][2:],
        line.split(" v=")[1],
    )
    p = int(left.split(",")[0]), int(left.split(",")[1])
    v = int(right.split(",")[0]), int(right.split(",")[1])
    robots[(i, v)] = p


def move(v, p):
    return (v[0] + p[0]) % wide, (v[1] + p[1]) % tall


def print_robots(robots):
    locations = dict()
    for robot in robots:
        if robots[robot] not in locations:
            locations[robots[robot]] = 0
        locations[robots[robot]] += 1

    for y in range(tall):
        line = ""
        for x in range(wide):
            if (x, y) in locations:
                line += str(locations[(x, y)])
            else:
                line += "."
        print(line)


# print_robots(robots)

for i in range(10000):
    for robot in robots:
        robots[robot] = move(robot[1], robots[robot])
    print("\n \n ")
    print(" #### seconds: ", i)
    print("\n\n")
    print_robots(robots)


def getQuadrant(x, y):
    if x == wide // 2:
        return None
    elif x < wide // 2:
        isLeft = True
    else:
        isLeft = False

    if y == tall // 2:
        return None
    elif y < tall // 2:
        isTop = True
    else:
        isTop = False
    if isLeft and isTop:
        return 0
    if isLeft and not isTop:
        return 2
    if not isLeft and isTop:
        return 1
    if not isLeft and not isTop:
        return 3


result = [0, 0, 0, 0]
for robot in robots:
    quad = getQuadrant(robots[robot][0], robots[robot][1])
    if quad is not None:
        result[quad] += 1

answer = 1
for r in result:
    answer *= r
print(answer)

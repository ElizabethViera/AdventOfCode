listsContents = open("AdventOfCode2024/Day 15/input.txt")
lines = listsContents.read().split("\n")

movesContents = open("AdventOfCode2024/Day 15/moves.txt")
moves = movesContents.read()

walls = set()
boxes = set()

bot_pos = (0, 0)

for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char == "#":
            walls.add((r, c))
        if char == "O":
            boxes.add((r, c))
        if char == "@":
            bot_pos = (r, c)

dirs = dict()

dirs["^"] = (-1, 0)
dirs["v"] = (1, 0)
dirs[">"] = (0, 1)
dirs["<"] = (0, -1)


def add_pts(a, b):
    return a[0] + b[0], a[1] + b[1]


def move(d: str):
    global bot_pos
    m = dirs[d]
    destination = add_pts(bot_pos, m)
    if destination in walls:
        return
    if destination in boxes:
        while destination in boxes:
            destination = add_pts(destination, m)
        if destination in walls:
            return
        else:
            new_bot_pos = add_pts(bot_pos, m)
            boxes.remove(new_bot_pos)
            boxes.add(destination)
            bot_pos = new_bot_pos
            return
    else:
        bot_pos = destination
        return


def print_grid():
    for r in range(10):
        line = ""
        for c in range(10):
            if (r, c) in walls:
                line += "#"
            elif (r, c) in boxes:
                line += "O"
            elif (r, c) == bot_pos:
                line += "@"
            else:
                line += "."
        print(line)


print_grid()

for m in moves:
    move(m)
    # print("m = ", m)
    # print_grid()

result = 0
for b in boxes:
    result += 100 * b[0] + b[1]
print(result)

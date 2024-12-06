listsContents = open("AdventOfCode2024/Day 6/input.txt")
map_data = listsContents.read().split("\n")

walkable_all = set()
walls_all = set()
walked_all = set()

dir = 0

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for r, row in enumerate(map_data):
    for c, char in enumerate(row):
        if char == "#":
            walls_all.add((c, r))
        elif char == "^":
            guard = (c, r, 0)
            walkable_all.add((c, r))
            walked_all.add((c, r))
        else:
            walkable_all.add((c, r))


def add_pts(a, b):
    return a[0] + b[0], a[1] + b[1]


def guard_path(
    guard: tuple[int, int, int], dir: int, walls: set[tuple[int, int]], walkable
) -> bool:
    walked = set()
    walked.add(guard)
    while True:
        new_pos = add_pts(guard, dirs[dir])
        if (new_pos[0], new_pos[1], dir) in walked:
            return True
        if new_pos in walls:
            dir += 1
            dir %= 4
            walked.add((guard[0], guard[1], dir))
            continue
        if (new_pos[0], new_pos[1]) not in walkable:
            return False
        else:
            guard = (new_pos[0], new_pos[1], dir)
            walked.add((new_pos[0], new_pos[1], dir))


total = 0
for i, pos in enumerate(walkable_all):
    test_walls = set(walls_all)
    test_walls.add(pos)
    if pos != (guard[0], guard[1]) and guard_path(guard, dir, test_walls, walkable_all):
        total += 1
print(total)

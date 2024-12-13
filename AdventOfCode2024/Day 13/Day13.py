listsContents = open("AdventOfCode2024/Day 13/input.txt")
machines = listsContents.read().split("\n\n")

all_machines = dict()

for i, machine in enumerate(machines):
    A, B, prize = machine.split("\n")
    a_coords_x, a_coords_y = (
        int(A.split(": ")[1].split(",")[0][2:]),
        int(A.split(": ")[1].split(", Y+")[1]),
    )
    b_coords_x, b_coords_y = (
        int(B.split(": ")[1].split(",")[0][2:]),
        int(B.split(": ")[1].split(", Y+")[1]),
    )
    prize_coords_x, prize_coords_y = (
        int(prize.split(": ")[1].split(",")[0][2:]),
        int(prize.split(": ")[1].split(", Y=")[1]),
    )
    all_machines[i] = (
        a_coords_x,
        a_coords_y,
        b_coords_x,
        b_coords_y,
        prize_coords_x + 10000000000000,
        prize_coords_y + 10000000000000,
    )


def calculate_cost(a, b):
    return 3 * a + b


total = 0
for mach in all_machines:
    m = all_machines[mach]
    best = None
    ax = m[0]
    ay = m[1]
    bx = m[2]
    by = m[3]
    px = m[4]
    py = m[5]
    j = (ay * px - ax * py) / (ay * bx - ax * by)
    if j < 0:
        continue
    if j != (ay * px - ax * py) // (ay * bx - ax * by):
        continue
    i = (px - j * bx) / ax
    if i < 0:
        continue
    if i != (px - j * bx) // ax:
        continue
    total += calculate_cost(int(i), int(j))
print(total)

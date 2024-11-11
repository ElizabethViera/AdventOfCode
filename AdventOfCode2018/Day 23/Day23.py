programContents = open("AdventOfCode2018/Day 23/input.txt")
contents = programContents.read().split("\n")

best_line = (0, 0, 0, 0)


def in_range(row1, row2):
    beacon_range = row1[3]
    x_dist = abs(row1[0] - row2[0])
    y_dist = abs(row1[1] - row2[1])
    z_dist = abs(row1[2] - row2[2])
    return x_dist + y_dist + z_dist <= beacon_range


all_beacons = []

for row in contents:
    # pos=<0,0,0>, r=4
    x, y, z, r = (
        int(row[5:].split(",")[0]),
        int(row[5:].split(",")[1]),
        int(row[5:].split(",")[2][:-1]),
        int(row.split("=")[2]),
    )
    all_beacons.append((x, y, z, r))
    if r > best_line[3]:
        best_line = (x, y, z, r)

total = 0
for beacon in all_beacons:
    if in_range(best_line, beacon):
        total += 1

print(total)

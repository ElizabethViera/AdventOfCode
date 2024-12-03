fileContents = open("AdventOfCode2021/Day 22/input.txt")
arr = fileContents.read().split("\n")

on_coords = set()

for i, line in enumerate(arr):
    print(i)
    isOn = line.split(" ")[0] == "on"
    dimensions = line.split(" ")[1].split(",")
    x, y, z = dimensions[0], dimensions[1], dimensions[2]
    xl, xr = x.split("=")[1].split("..")
    yl, yr = y.split("=")[1].split("..")
    zl, zr = z.split("=")[1].split("..")

    for xc in range(int(xl), int(xr) + 1):
        for yc in range(int(yl), int(yr) + 1):
            for zc in range(int(zl), int(zr) + 1):
                if isOn:
                    on_coords.add((xc, yc, zc))
                else:
                    if (xc, yc, zc) in on_coords:
                        on_coords.remove((xc, yc, zc))

print(len(on_coords))

total = 0

for fx in range(-50, 51):
    for fy in range(-50, 51):
        for fz in range(-50, 51):
            if (fx, fy, fz) in on_coords:
                total += 1
print(total)

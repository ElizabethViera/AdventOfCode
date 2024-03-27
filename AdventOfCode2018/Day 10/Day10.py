#position=< 9,  1> velocity=< 0,  2>

fileContents = open("AdventOfCode2018/Day 10/input.txt")
lines = fileContents.read().split("\n")

points = dict()
for i, line in enumerate(lines):
    left, right = line.split('velocity=<')[0], line.split(' velocity=<')[1]
    position = left.split('<')[1]
    posx = int(position.split(',')[0].strip())
    posy = int(position.split(',')[1][:-2].strip())
    velx = int(right.split(',')[0].strip())
    vely = int(right.split(',')[1][:-1].strip())
    points[i] = (posx, posy, velx, vely)

def updatePoint(p):
    px, py, vx, vy = p[0], p[1], p[2], p[3]
    return px + vx, py + vy, vx, vy

def printPoints(pts, steps):
    pts = sorted(pts)
    x_min = pts[0][0]
    x_max = x_min + 400
    y_min = pts[0][1]
    for point in pts:
        if point[1] < y_min:
            y_min = point[1]
    y_max = y_min+400
    triple = False
    for p in pts:
        if (p[0]+1, p[1]+1) in pts and (p[0]+2, p[1]+2) in pts:
            triple = True
    if not triple:
        return
    print('\n\n\n', steps)
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            if (x,y) in pts:
                print('#', end='')
            else:
                print('.', end='')
        print('')

def step(points):
    all_points = set()
    for point in points:
        points[point] = updatePoint(points[point])
        all_points.add((points[point][0], points[point][0]))
    return list(points)

for i in range(100000):
    step(points)
    printPoints([(points[x][0], points[x][1]) for x in points], i)
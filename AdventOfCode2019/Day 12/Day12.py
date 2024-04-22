fileContents = open("AdventOfCode2019/Day 12/input.txt")
moons = fileContents.read().split("\n")

initial_moons = dict()

for i,moon in enumerate(moons):
    x,y,z = int(moon.split(', ')[0]), int(moon.split(', ')[1]), int(moon.split(', ')[2])
    initial_moons[i] = (x,y,z, 0, 0, 0)

def get_new_velocities(a,b):
    if a[0] == b[0]:
        new_ax, new_bx = 0, 0
    else:
        if a[0] > b[0]:
            new_ax, new_bx = -1, +1
        else:
            new_ax, new_bx = +1, -1
    if a[1] == b[1]:
        new_ay, new_by = 0, 0
    else:
        if a[1] > b[1]:
            new_ay, new_by = -1, +1
        else:
            new_ay, new_by = +1, -1
    if a[2] == b[2]:
        new_az, new_bz = 0, 0
    else:
        if a[2] > b[2]:
            new_az, new_bz = -1, +1
        else:
            new_az, new_bz = +1, -1

    new_a =  (new_ax, new_ay, new_az)
    new_b = (new_bx, new_by, new_bz)
    return new_a, new_b

def add_deltas(a,b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def update_moons(ms):
    deltas = dict()
    deltas[0] = (0,0,0)
    deltas[1] = (0,0,0)
    deltas[2] = (0,0,0)
    deltas[3] = (0,0,0)
    for m in ms:
        for n in ms:
            if m != n:
                delta_m, delta_n = get_new_velocities(ms[m], ms[n])
                deltas[m] = add_deltas(delta_m, deltas[m])
                deltas[n] = add_deltas(delta_n, deltas[n])
    # update velocity
    for m in ms:
        ms[m] = (ms[m][0], ms[m][1], ms[m][2], deltas[m][0]//2 + ms[m][3], deltas[m][1]//2+ ms[m][4], deltas[m][2]//2+ ms[m][5])
    # update position
    for m in ms:
        ms[m] = (ms[m][0] +  ms[m][3], ms[m][1] +  ms[m][4], ms[m][2] + ms[m][5], ms[m][3], ms[m][4], ms[m][5])
    return ms

cycles = dict()
cycles[x] = dict()
cycles[y] = dict()
cycles[z] = dict()

all_moons = initial_moons
for i in range(287000):
    all_moons = update_moons(all_moons)
    if tuple([(all_moons[moon][0], all_moons[moon][3]) for moon in all_moons]) in cycles[x]:
        print('x cycle found at:', cycles[x][tuple([(all_moons[moon][0], all_moons[moon][3]) for moon in all_moons])], i) #286332
    cycles[x][tuple([(all_moons[moon][0], all_moons[moon][3]) for moon in all_moons])] = i
    #if tuple([(all_moons[moon][1], all_moons[moon][4]) for moon in all_moons]) in cycles[y]:
        #print('y cycle found at:', i) # 161428
    #cycles[y].add(tuple([(all_moons[moon][1], all_moons[moon][4])  for moon in all_moons]))
    #if tuple([(all_moons[moon][2], all_moons[moon][5])  for moon in all_moons]) in cycles[z]:
        #print('z cycle found at:', i) # 102356
    #cycles[z].add(tuple([(all_moons[moon][2], all_moons[moon][5]) for moon in all_moons]))

# 286332
# 161428
# 102356
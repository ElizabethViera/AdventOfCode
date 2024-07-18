fileContents = open("AdventOfCode2018/Day 17/input.txt")
contents = fileContents.read().split("\n")

#######
# Misc Helpers
########

def sort_by_y(p):
    return p[1]

def sort_by_x(p):
    return p[0]

def xy_in_water(x,y):
    for w in water:
        if x == w[0] and y == w[1]:
            return True
    return False

########
# Parse Initial State 
########

walls = set()
water_source = (500,1)
water: set[tuple[int, int]] = set([water_source])

for line in contents:
    left, right = line.split(', ')[0], line.split(', ')[1]
    x = None
    y = None
    if left.startswith('x='):
        x = int(left[2:])
        right = right[2:]
        l = int(right.split('..')[0])
        r = int(right.split('..')[1])
        for k in range(l,r+1):
            walls.add((x,k))
    else:
        y = int(left[2:])
        right = right[2:]
        l = int(right.split('..')[0])
        r = int(right.split('..')[1])
        for k in range(l,r+1):
            walls.add((k,y))

########
# Get bounds for when we want to print the grid
########

walls = sorted(walls, key=sort_by_y)    
lowest_y = walls[-1][1]

walls = sorted(walls, key=sort_by_x)
lowest_x = walls[0][0]
highest_x = walls[-1][0]
print(lowest_y, lowest_x, highest_x)


#########
# Render Grid
#########
def render_grid():
    for y in range(0, lowest_y+1):
        line = ''
        for x in range(lowest_x, highest_x+1):
            if xy_in_water(x,y):
                line = line + '~'
            elif (x,y) in walls:
                line = line + '#'
            else:
                line = line + '.'
        print(line)            

def add_water():
    sorted_water = sorted(water, key = sort_by_y)
    while(len(sorted_water)>0):
        current_water = sorted_water.pop()
        down_1 = (current_water[0], current_water[1]+1)
        if down_1[1] > lowest_y:
            return None
        if down_1 not in water and down_1 not in walls:
            return down_1
        left_1 = (current_water[0]-1, current_water[1])
        if left_1 not in water and left_1 not in walls:
            return left_1
        right_1 = (current_water[0]+1, current_water[1])
        if right_1 not in water and right_1 not in walls:
            return right_1
    return None

i = 0
while True:
    if len(water)%1000 == 0:
        print(len(water))
    new_water = add_water()
    if new_water == None:
        break
    water.add(new_water)

print(len(water))
print("first pass done")
render_grid()
'''
total = len(water)
water = set()
 
for coord in new_coords:
    water.add(coord)

while True:
    new_water = add_water()
    if new_water == None:
        break
    water.add(new_water)
print(len(water) + total)
render_grid()
'''
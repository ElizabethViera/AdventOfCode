fileContents = open("AdventOfCode2018/Day 17/input.txt")
contents = fileContents.read().split("\n")

points = set()
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
            points.add((x,k))
    else:
        y = int(left[2:])
        right = right[2:]
        l = int(right.split('..')[0])
        r = int(right.split('..')[1])
        for k in range(l,r+1):
            points.add((k,y))


def sort_by_y(p):
    return p[1]

points = sorted(points, key=sort_by_y)    
lowest_y = points[-1][1]
print(lowest_y)

def sort_by_x(p):
    return p[0]

points = sorted(points, key=sort_by_x)
lowest_x = points[0][0]
highest_x = points[-1][0]
print(lowest_x, highest_x)

def xy_in_water(x,y):
    for w in water:
        if x == w[0] and y == w[1]:
            return True
    return False

#########
# Render Grid
#########
def render_grid():
    for y in range(0, lowest_y+1):
        line = ''
        for x in range(lowest_x, highest_x+1):
            if xy_in_water(x,y):
                line = line + '~'
            elif (x,y) in points:
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
            print("Done! ", len(water))
            render_grid()
            raise(ValueError)
        if down_1 not in water and down_1 not in points:
            return down_1
        left_1 = (current_water[0]-1, current_water[1])
        if left_1 not in water and left_1 not in points:
            return left_1
        right_1 = (current_water[0]+1, current_water[1])
        if right_1 not in water and right_1 not in points:
            return right_1
    print("Done! ", len(water))
    raise(ValueError)
        
while len(water) < 60:
    new_water = add_water()
    water.add(new_water)
print(len(water))
render_grid()
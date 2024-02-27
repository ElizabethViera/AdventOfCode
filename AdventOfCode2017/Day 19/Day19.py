north = (-1,0)
south = (1,0)
east = (0,1)
west = (0,-1)

fileContents = open("AdventOfCode2017/Day 19/input.txt")
arr = fileContents.read().split('\n')

coords = dict()

for r,row in enumerate(arr):
    for c,char in enumerate(row):
        coords[(r,c)] = char

def add_pts(a,b):
    return a[0] + b[0], a[1] + b[1]

def go_in_straight_line(current_direction, current_coord):
    print(current_direction)
    total = 0
    # returns new direction and new coords
    next_coord = add_pts(current_direction, current_coord)
    while coords[next_coord] != '+':
        total += 1
        if coords[next_coord] == 'F':
            return total, None, None
        next_coord = add_pts(current_direction, next_coord)
    if current_direction == north or current_direction == south:
        if coords[add_pts(next_coord, east)] == '-' or coords[add_pts(next_coord, east)] == 'B':
            next_direction = east
        elif coords[add_pts(next_coord, west)] == '-':
            next_direction = west
        else:
            print('error')
            next_direction = None
    else:
        if coords[add_pts(next_coord, north)] == '|' or coords[add_pts(next_coord, north)] == 'D':
            next_direction = north
        elif coords[add_pts(next_coord, south)] == '|' or coords[add_pts(next_coord, south)] == 'C':
            next_direction = south
        else:
            print('error')
            next_direction = None
    return total+1, next_coord, next_direction

current_direction = south
current_coord = (0, 5)
total = 0
while(True):
    if current_coord == None:
        print(total)
        break
    next_total, current_coord, current_direction = go_in_straight_line(current_direction, current_coord)
    total += next_total
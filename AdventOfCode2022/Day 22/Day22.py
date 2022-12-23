fileContents = open("AdventOfCode2022/Day 22/input.txt")
fileContents2 = open("AdventOfCode2022/Day 22/input2.txt")
arr = fileContents.read().split("\n")

cube_width = 50

fileContents3 = open("AdventOfCode2022/Day 22/input3.txt")
arr3 = fileContents3.read().split("\n")
faces = {}
region_coords = {}
for row, line in enumerate(arr3):
    for col, c in enumerate(line):
        if c == ' ':
            continue
        faces[(row, col)] = int(c)
        if int(c) not in region_coords:
            region_coords[int(c)] = (row,col)


        

coordinates = {}
walls = set()


traversals = {(4,2): 'D', (4,5): 'U', (4,6): 'U', (4,3): 'D',
            (2,3):'R', (2,4): 'R', (2,1): 'D', (2,5): 'R',
            (1, 2): 'U', (1,5): 'D', (1,6): 'D', (1,3): 'U',
            (3, 6): 'L', (3,2): 'L', (3,1): 'L', (3, 4): 'U',
            (5, 6): 'R', (5,1): 'R', (5,2): 'R', (5, 4): 'D',
            (6,5): 'L', (6,3): 'L', (6,4):'L', (6,1): 'U' }

region_neighbors = {
    1: {'U': 2, 'R': 3, 'D': 6, 'L': 5},
    2: {'U': 4, 'R': 3, 'D': 1, 'L': 5},
    3: {'U': 4, 'R': 6, 'D': 1, 'L': 2},
    4: {'U': 5, 'R': 6, 'D': 3, 'L': 2},
    5: {'U': 1, 'R': 6, 'D': 4, 'L': 2},
    6: {'U': 1, 'R': 3, 'D': 4, 'L': 5},
}

traversalsToIndex = {'D': '1', 'R': 0, 'U': 3, 'L':2}

for row, line in enumerate(arr):
    for col, char in enumerate(line):
        if char == '.' or char == '#':
            coordinates[(row, col)] = {}
        if char  == '#':
            walls.add((row,col))


def move_dir(location, direction):
    match direction:
        case 'Up':
            return (location[0] - 1, location[1])
        case 'Down':
            return (location[0] + 1, location[1])
        case 'Left':
            return (location[0], location[1] - 1)
        case 'Right':
            return (location[0], location[1] + 1)

def get_index_from_clockwise_edge(row, col, dir):
    match dir:
        case 'Up':
            assert(row == 0)
            return col
        case 'Down':
            assert(row == cube_width -1)
            return cube_width - col - 1
        case 'Right':
            assert(col == cube_width - 1)
            return row
        case 'Left':
            assert(col == 0)
            return cube_width - row - 1

def given_index_tell_me_new_local_coords(dir, index):
    match dir:
        case 'U':
            return (cube_width - 1, index)
        case 'D':
            return (0, cube_width - index - 1)
        case 'R':
            return ( index , 0)
        case 'L':
            return (cube_width - index - 1, cube_width - 1)
    print(dir)
            


def compute_neighbor(row, col, dir):
    new_place = move_dir((row,col), dir)
    if new_place in faces and faces[new_place] == faces[(row,col)]:
        #normal case
        return new_place, dir
    else:
        # jumping to a new region
        old_region = faces[(row,col)]
        new_region = region_neighbors[old_region][dir[:1]]
        old_face_coords = (row%cube_width, col%cube_width)
        index = get_index_from_clockwise_edge(old_face_coords[0], old_face_coords[1], dir)
        new_face_coords = given_index_tell_me_new_local_coords(traversals[(old_region, new_region)], index)
        new_region_row, new_region_col = region_coords[new_region]

        return (new_region_row+new_face_coords[0], new_region_col+new_face_coords[1]), traversals[(old_region, new_region)]

assert(compute_neighbor(108, 49, 'Right') == ((108, 50), 'R'))
assert(compute_neighbor(100, 60, 'Up') == ((99, 60), 'U'))
assert(compute_neighbor(108, 50, 'Left') == ((108, 49), 'L'))
assert(compute_neighbor(99, 60, 'Down') == ((100, 60), 'D'))
assert(compute_neighbor(100, 49, 'Up') == ((99, 50), 'R'))
assert(compute_neighbor(99, 50, 'Left') == ((100, 49), 'D'))
assert(compute_neighbor(100, 0, 'Left') == ((49,50), 'R'))

for coord in coordinates:
    (row, col) = coord
    for dir in ["Left", "Right", "Up", "Down"]:
        coordinates[row, col][dir] = compute_neighbor(row, col, dir)
    # build neighbors

    # coordinates[(row, col)]["region"] = faces[(row, col)] 

def current_direction_to_int(dir):
    match dir:
        case 'R':
            return 0
        case 'D':
            return 1
        case 'L':
            return 2
        case 'U':
            return 3


direction_map = fileContents2.read()

def turnDirection(turn, current_direction):
    current_direction = current_direction_to_int(current_direction)
    if turn == "R":
        current_direction += 1
        return current_direction%4
    if turn == "L":
        current_direction -= 1
        return (current_direction + 4)%4

def newDirection(oldRegion, newRegion):
    newDirection = traversals((oldRegion, newRegion))
    return traversalsToIndex(newDirection)

def move_single(current_position, current_direction):
    # print("Move", move_forward, current_direction, current_position)
    current_direction = current_direction[0]
    if current_direction == "R":
        keyToDict = "Right"
    if current_direction == "L":
        keyToDict = "Left"
    if current_direction == "U":
        keyToDict = "Up"
    if current_direction == "D":
        keyToDict = "Down"
    # print(current_position, coordinates[current_position], current_direction)
    new_place = coordinates[current_position][keyToDict]
    if new_place[0] in walls:
        #print("found a wall")
        return current_position, current_direction
    else:
       # print("print", coordinates[current_position])
        current_position, current_direction = coordinates[current_position][keyToDict]
    
    return current_position, current_direction[:1]

def move(move_forward, current_position, current_direction):
    for i in range(move_forward):
        current_position, current_direction = move_single(current_position, current_direction)
    return current_position, current_direction

print(move(49, (149, 58), 'D'))

import re

current_position = (0,50)
current_direction = 0

dirs = ["R", "D", "L", "U"]

my_directions = re.split(r'R|L', direction_map)
my_directions = [int(direction) for direction in my_directions]
my_turns = re.split(r'\d', direction_map)
my_turns = [turn for turn in my_turns if turn != '']
# print(my_directions, my_turns)

while my_directions != [] and my_turns != []:
    move_forward = my_directions.pop(0)
    current_position, current_direction = move(move_forward, current_position, dirs[current_direction])

    turn = my_turns.pop(0)
    current_direction = turnDirection(turn, current_direction)
    # print(current_position, current_direction)

if my_directions != []:
    move_forward = my_directions.pop(0)
    current_position, current_direction = move(move_forward, current_position, dirs[current_direction])

if my_turns != []:
    turn = my_turns.pop(0)
    current_direction = turnDirection(turn, current_direction)

# Row 149 Col 59 Move R Add R49 gets wrong answer
print((current_position[0]+1), (current_position[1]+1), current_direction_to_int(current_direction))
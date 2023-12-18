
fileContents = open("AdventOfCode2023/Day 16/sampleInput.txt")
grid = fileContents.read().split("\n")

dirs = {'N': (-1,0), 'S': (1,0), 'W': (0,-1), 'E':(0,1)}

grid_arr = []

for row in grid:
    new_row = []
    for col in row:
        new_row.append(col)
    grid_arr.append(new_row)

total_rows = len(grid_arr)
total_cols = len(grid_arr[0])

def add_coords(a,b) -> tuple[int, int]:
    return a[0]+b[0], a[1]+b[1]

def inbounds(next_coord):
    return next_coord[0] < len(grid_arr) and next_coord[0] >= 0 and next_coord[1] < len(grid_arr[0]) and next_coord[1] >= 0

def gridAt(coords):
    return grid_arr[coords[0]][coords[1]]

def move(coord, dir):
    next_coord = add_coords(coord, dirs[dir])
    while inbounds(next_coord) and gridAt(next_coord) == '.':
        next_coord = add_coords(next_coord, dirs[dir])
    if not inbounds(next_coord):
        return []
    match gridAt(next_coord):
        case '/':
            if dir == 'N':
                next_dir = 'E'
            elif dir == 'S':
                next_dir = 'W'
            elif dir == 'E':
                next_dir = 'N'
            elif dir == 'W':
                next_dir = 'S'
            else:
                raise(ValueError)
            return [(next_coord, next_dir)]
        case '\\': 
            if dir == 'N':
                next_dir = 'W'
            elif dir == 'S':
                next_dir = 'E'
            elif dir == 'E':
                next_dir = 'S'
            elif dir == 'W':
                next_dir = 'N'
            else:
                raise(ValueError)
            return [(next_coord, next_dir)]
        case '|':
            if dir == 'N' or dir == 'S':
                return [(next_coord, dir)]
            else:
                return [(next_coord, 'N'), (next_coord, 'S')]
        case '-':
            if dir == 'N' or dir == 'S':
                return [(next_coord, 'E'), (next_coord, 'W')]
            else:
                return [(next_coord, dir)]
    raise(ValueError)

def getStarts(first_item, first_direction):
    starts_seen = set()
    starts_to_process = []
    starts_to_process.append((first_item, first_direction))
    starts_seen.add((first_item, first_direction))

    while starts_to_process != []:
        current = starts_to_process.pop()
        new_starts = move(current[0], current[1])
        for new_start in new_starts:
            if new_start not in starts_seen:
                starts_to_process.append(new_start)
                starts_seen.add(new_start)

    starts_coords = set()
    for start in starts_seen:
        starts_coords.add(start[0])

    all_coords = set()
    all_coords.add((0,0))
    for start in starts_seen:
        all_coords.add(start[0])
        current = add_coords(start[0], dirs[start[1]])
        while current not in starts_coords and inbounds(current):
            all_coords.add(current)
            current = add_coords(current, dirs[start[1]])
        
    return len(all_coords)
        

max_config = 0
for i in range(total_cols):
    candidate = getStarts((-1, i), 'S')
    if candidate > max_config:
        max_config = candidate

for i in range(total_cols):
    candidate = getStarts((total_rows, i), 'N')
    if candidate > max_config:
        max_config = candidate

for i in range(total_rows):
    candidate = getStarts((i, -1), 'E')
    if candidate > max_config:
        max_config = candidate

for i in range(total_rows):
    candidate = getStarts((i, total_cols), 'W')
    if candidate > max_config:
        max_config = candidate

print(max_config-1)
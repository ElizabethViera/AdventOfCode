fileContents = open("Day 17/input")
arr = fileContents.read().split('\n')

coords_to_state = {}


def get_coord_neighbors(coord):
    x, y, z, w = coord
    result = []
    for x_n in range(x-1, x+2):
        for y_n in range(y-1, y+2):
            for z_n in range(z-1, z+2):
                for w_n in range(w-1, w+2):
                    coord_n = (x_n, y_n, z_n, w_n)
                    if coord_n not in coords_to_state:
                        coords_to_state[coord_n] = '.'
                    if coord_n != coord:
                        result.append(coord_n)
    return result


def eval_coord(coord):
    x, y, z, w = coord
    neighbors = get_coord_neighbors(coord)
    # print(neighbors)
    active_neighbors = 0
    for neighbor in neighbors:
        if coords_to_state[neighbor] == '#':
            active_neighbors += 1
    if coords_to_state[(x, y, z, w)] == '.':
        # currently inactive, if three neighbors are active, turn active
        if active_neighbors == 3:
            result = '#'
        else:
            result = '.'
    else:
        # currently active, if 2 or 3 neighbors are active, keep active, else turn inactive
        if active_neighbors != 2 and active_neighbors != 3:
            result = '.'
        else:
            result = '#'
    return result


def count_active():
    result = 0
    for state in list(coords_to_state.keys()):
        if coords_to_state[state] == '#':
            result += 1
        else:
            del coords_to_state[state]
    print(result)


for row, v1 in enumerate(arr):
    for col, v2 in enumerate(arr):
        coords_to_state[(row, col, 0, 0)] = arr[row][col]
print("first count = ")
count_active()

for cycle in range(6):
    new_states = {}
    for coord in list(coords_to_state.keys()):
        get_coord_neighbors(coord)
    for coord in list(coords_to_state.keys()):
        new_states[coord] = eval_coord(coord)
    for state in new_states:
        coords_to_state[state] = new_states[state]
    count_active()

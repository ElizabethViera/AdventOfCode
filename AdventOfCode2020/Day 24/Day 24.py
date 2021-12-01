import operator
fileContents = open("Day 24/input")

arr = fileContents.read().split('\n')


tiles = {}

for line in arr:
    lastN = False
    lastS = False
    pos = (0, 0)
    for c in line:
        if c == 's':
            lastS = True
        elif c == 'n':
            lastN = True
        elif c == 'w':
            if not lastS and not lastN:
                pos = tuple(map(operator.add, pos, (-1, 0)))
            else:
                if lastS:
                    pos = tuple(map(operator.add, pos, (-1, -1)))
                else:  # lastN
                    pos = tuple(map(operator.add, pos, (0, 1)))
            lastS = False
            lastN = False

        elif c == 'e':
            if not lastS and not lastN:
                pos = tuple(map(operator.add, pos, (1, 0)))
            else:
                if lastS:
                    pos = tuple(map(operator.add, pos, (0, -1)))
                else:  # lastN
                    pos = tuple(map(operator.add, pos, (1, 1)))
            lastS = False
            lastN = False
    if pos in tiles:
        tiles[pos] += 1
    else:
        tiles[pos] = 1

result = 0


def get_neighbors(pos):
    result = []
    neighbors_offset = [(-1, 0), (-1, -1), (0, 1), (1, 0), (0, -1), (1, 1)]
    for offset in neighbors_offset:
        result.append(tuple(map(operator.add, pos, offset)))
    return result


grid_pos = set()

for tile in tiles:
    if tiles[tile] % 2 == 1:
        grid_pos.add(tile)

print(len(grid_pos))


def print_set(s):
    for row in range(-5, 5):
        for i in range(20-row):
            print("|", end="")
        for col in range(-5, 5):
            if (row, col) in s:
                print(" x", end="")
            else:
                print(" .", end="")
        print('')


def flip_tiles(n):
    for i in range(n):
        remove_pos = set()
        add_pos = set()
        for pos in grid_pos:
            neighbors = get_neighbors(pos)
            neighbor_count = 0
            for neighbor in neighbors:
                if neighbor in grid_pos:
                    neighbor_count += 1

            if neighbor_count > 2 or neighbor_count == 0:
                remove_pos.add(pos)
            for neighbor in neighbors:
                if neighbor not in grid_pos:
                    white_tile_neighbors = get_neighbors(neighbor)
                    white_tile_neighbors_neighbor_count = 0
                    for white_tile_neighbor in white_tile_neighbors:
                        if white_tile_neighbor in grid_pos:
                            white_tile_neighbors_neighbor_count += 1

                    if white_tile_neighbors_neighbor_count == 2:
                        add_pos.add(neighbor)
        for pos in remove_pos:
            grid_pos.remove(pos)
        for pos in add_pos:
            grid_pos.add(pos)
    return len(grid_pos)


print(flip_tiles(100))

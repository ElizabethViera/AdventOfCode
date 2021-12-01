import numpy as np
fileContents = open("Day 20/input")
arr = fileContents.read().split('\n')


def print_tile(B):
    print('\n')
    for row in B:
        print(row)
    print('\n')


def get_neighbors(edge_collection):
    neighbor_list = {}
    # dictionary from string to list [a,b]
    # return dict [a] -> [b, c, d] neighbors
    for s in edge_collection:
        for piece in edge_collection[s]:
            for neighbor in edge_collection[s]:
                if piece != neighbor:
                    if piece in neighbor_list:
                        neighbor_list[piece].add(neighbor)
                    else:
                        neighbor_list[piece] = set([neighbor])
    return neighbor_list


def rotate_tile(matrix):
    # m = [[], [], ...]
    # return top, right, bottom, left
    top = matrix[0]
    right = ''.join([m[-1] for m in matrix])
    bottom = matrix[-1]
    left = ''.join([m[0] for m in matrix])
    return right, bottom, left, top


tiles = {}
tile_name = False
for line in arr:
    if line.startswith("Tile "):
        if tile_name:
            tiles[tile_name] = tile
        tile_name = int(line.split(" ")[-1][:-1])
        tile = []
    elif line == "":
        continue
    else:
        tile.append(line)
tiles[tile_name] = tile

edges_to_tiles = {}

for tile in tiles:
    for row in rotate_tile(tiles[tile]):
        if row in edges_to_tiles:
            edges_to_tiles[row].append(tile)
            edges_to_tiles[row[::-1]].append(tile)
        else:
            edges_to_tiles[row] = [tile]
            edges_to_tiles[row[::-1]] = [tile]

counts = {}

for key in edges_to_tiles:
    if len(edges_to_tiles[key]) == 1:
        if edges_to_tiles[key][0] in counts:
            counts[edges_to_tiles[key][0]] += 1
        else:
            counts[edges_to_tiles[key][0]] = 1

result = 1
for k in counts:
    if counts[k] == 4:
        result *= k
print(result)

neighbor_list = get_neighbors(edges_to_tiles)

#####################
# Produce Grid
#####################

grid = [[3023]]
next_neighbor = 2477
grid[0].append(next_neighbor)
found_first_row = False
placed_tiles = set([3023, 2477])
while(not found_first_row):
    for candidate_neighbor in neighbor_list[next_neighbor]:
        if candidate_neighbor not in placed_tiles and len(neighbor_list[candidate_neighbor]) == 2:
            grid[0].append(candidate_neighbor)
            placed_tiles.add(candidate_neighbor)
            found_first_row = True
            break
        elif candidate_neighbor not in placed_tiles and len(neighbor_list[candidate_neighbor]) == 3:
            grid[0].append(candidate_neighbor)
            placed_tiles.add(candidate_neighbor)
            next_neighbor = candidate_neighbor


next_neighbor = 3583
placed_tiles.add(3583)
grid.append([next_neighbor])
found_first_col = False
while(not found_first_col):
    for candidate_neighbor in neighbor_list[next_neighbor]:
        if candidate_neighbor not in placed_tiles and len(neighbor_list[candidate_neighbor]) == 2:
            grid.append([candidate_neighbor])
            placed_tiles.add(candidate_neighbor)
            found_first_col = True
            break
        elif candidate_neighbor not in placed_tiles and len(neighbor_list[candidate_neighbor]) == 3:
            grid.append([candidate_neighbor])
            placed_tiles.add(candidate_neighbor)
            next_neighbor = candidate_neighbor


next_neighbor = 1039
placed_tiles.add(1039)
grid[-1].append(next_neighbor)
found_last_row = False
while(not found_last_row):
    for candidate_neighbor in neighbor_list[next_neighbor]:
        if candidate_neighbor not in placed_tiles and len(neighbor_list[candidate_neighbor]) == 2:
            grid[-1].append(candidate_neighbor)
            placed_tiles.add(candidate_neighbor)
            found_last_row = True
            break
        elif candidate_neighbor not in placed_tiles and len(neighbor_list[candidate_neighbor]) == 3:
            grid[-1].append(candidate_neighbor)
            placed_tiles.add(candidate_neighbor)
            next_neighbor = candidate_neighbor

for row in grid:
    while len(row) != 12:
        row.append(0)

for row in range(1, 11):
    for col in range(1, 12):
        for candidate_neighbor in neighbor_list[grid[row][col-1]]:
            if (candidate_neighbor not in placed_tiles and candidate_neighbor in neighbor_list[grid[row-1][col]]):
                grid[row][col] = candidate_neighbor
                placed_tiles.add(candidate_neighbor)


######################
# Flip tiles
######################


np_matrices = {}

for m in tiles:
    new_matrix = []
    for row in tiles[m]:
        new_row = [c for c in row]
        new_matrix.append(new_row)
    new_matrix = np.array(new_matrix)
    np_matrices[m] = new_matrix

correct_orientation = 0
for row in range(len(grid)-1):
    for col in range(len(grid)-1):
        for i in range(8):
            bottom_neighbor = grid[row+1][col]
            right_neighbor = grid[row][col+1]
            right_side = ''.join([r[-1] for r in np_matrices[grid[row][col]]])
            bottom_side = ''.join(np_matrices[grid[row][col]][-1])
            if (right_neighbor in edges_to_tiles[right_side] and
                    bottom_neighbor in edges_to_tiles[bottom_side]):
                correct_orientation += 1
                break

            np_matrices[grid[row][col]] = np.rot90(
                np_matrices[grid[row][col]])
            if i == 3:
                np_matrices[grid[row][col]] = np.fliplr(
                    np_matrices[grid[row][col]])


for row in range(11):
    for i in range(8):
        left_neighbor = grid[row][-2]
        bottom_neighbor = grid[row+1][-1]
        left_side = ''.join([r[0] for r in np_matrices[grid[row][-1]]])
        bottom_side = ''.join(np_matrices[grid[row][-1]][-1])
        if (left_neighbor in edges_to_tiles[left_side] and
                bottom_neighbor in edges_to_tiles[bottom_side]):
            correct_orientation += 1
            break

        np_matrices[grid[row][-1]] = np.rot90(
            np_matrices[grid[row][-1]])
        if i == 3:
            np_matrices[grid[row][-1]] = np.fliplr(
                np_matrices[grid[row][-1]])

# print(np_matrices)

for col in range(11):
    for i in range(8):
        right_neighbor = grid[-1][col+1]
        top_neighbor = grid[-2][col]
        right_side = ''.join([r[-1] for r in np_matrices[grid[-1][col]]])
        top_side = ''.join(np_matrices[grid[-1][col]][0])
        if (right_neighbor in edges_to_tiles[right_side] and
                top_neighbor in edges_to_tiles[top_side]):
            correct_orientation += 1
            break

        np_matrices[grid[-1][col]] = np.rot90(
            np_matrices[grid[-1][col]])
        if i == 3:
            np_matrices[grid[-1][col]] = np.fliplr(
                np_matrices[grid[-1][col]])
# print(np_matrices)

for i in range(8):
    top_neighbor = grid[-1][-2]
    left_neighbor = grid[-2][-1]
    top_side = ''.join(np_matrices[grid[-1][-1]][0])
    left_side = ''.join([r[0] for r in np_matrices[grid[-1][-1]]])
    if (left_neighbor in edges_to_tiles[left_side] and
            top_neighbor in edges_to_tiles[top_side]):
        correct_orientation += 1
        break

    np_matrices[grid[-1][-1]] = np.rot90(
        np_matrices[grid[-1][-1]])
    if i == 3:
        np_matrices[grid[-1][-1]] = np.fliplr(
            np_matrices[grid[-1][-1]])

print(correct_orientation)

################
# Remove borders
################
for row in grid:
    for tile in row:
        np_matrices[tile] = np.array([r[1:9] for r in np_matrices[tile][1:9]])

final_grid = {}
for row in range(len(grid)):
    for col in range(len(grid)):
        final_grid[(row, col)] = np_matrices[grid[row][col]]

output = {}
for row, col in final_grid:
    tile = final_grid[(row, col)]
    for x in range(len(tile)):
        for y in range(len(tile)):
            output[(8*col+y, 8*row+x)] = tile[x][y]


nessie_count = 0
nessie = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17),
          (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
for x in range(8*12):
    for y in range(8*12):
        found_nessie = True
        for offset_x, offset_y in nessie:
            if (x+offset_x, y + offset_y) not in output or output[(x + offset_x, y+offset_y)] != '#':
                found_nessie = False
        if found_nessie:
            nessie_count += 1
print(nessie_count * 15)

hashtags = 0
for x in range(8*12):
    for y in range(8*12):
        if output[x, y] == '#':
            hashtags += 1
print(hashtags - 270)

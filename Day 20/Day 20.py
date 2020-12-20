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

f = open("Day 20/output", "a")
for edge in neighbor_list:
    f.write(str(edge))
    f.write('\n')
    f.write(str(neighbor_list[edge]))
    f.write('\n')
    f.write('\n')
f.close()

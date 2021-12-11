fileContents = open("Day 11/input.txt")
arr = fileContents.read().split('\n')
arr = [[int(i) for i in line] for line in arr]
# print(arr)

dirs = [(0, 1), (0, -1),
        (1, 0), (1, 1), (1, -1),
        (-1, 0), (-1, 1), (-1, -1)]

coords_to_value = {}

for row in range(len(arr)):
    for col in range(len(arr[0])):
        coords_to_value[(row, col)] = arr[row][col]


def coords_to_neighbors(coords):
    results = []
    for direction in dirs:
        neighbor = (coords[0]+direction[0], coords[1]+direction[1])
        if neighbor in coords_to_value:
            results.append(neighbor)
    return results


def make_neighbors_flash(neighbors):
    flashes = 0
    for neighbor in neighbors:
        coords_to_value[neighbor] += 1
        if coords_to_value[neighbor] == 10:
            coords_to_value[neighbor] += 1
            flashes += 1
            flashes += make_neighbors_flash(coords_to_neighbors(neighbor))
    return flashes


flashes = 0
i_seen_at_step = set()

for i in range(1000):
    # Go through each item and increment
    for key in coords_to_value:
        coords_to_value[key] += 1
        if coords_to_value[key] == 10:
            coords_to_value[key] += 1
            flashes += 1
            neighbors = coords_to_neighbors(key)
            flashes += make_neighbors_flash(neighbors)

    for key in coords_to_value:
        if coords_to_value[key] >= 10:
            coords_to_value[key] = 0
        else:
            i_seen_at_step.add(i)

i_seen_at_step = sorted(i_seen_at_step)
print(i_seen_at_step)
for result in range(1, len(i_seen_at_step)):
    if result != i_seen_at_step[result]:
        print(result)
        break
print(flashes)

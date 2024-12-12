listsContents = open("AdventOfCode2024/Day 12/input.txt")
plant_list = listsContents.read().split("\n")

plants: dict[str, set[tuple[int, int]]] = dict()

for r, row in enumerate(plant_list):
    for c, p in enumerate(row):
        if p not in plants:
            plants[p] = set()
        plants[p].add((r, c))


def add_pts(a, b):
    return a[0] + b[0], a[1] + b[1]


def getNeighbors(p):
    result = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in dirs:
        new_pt = add_pts(dir, p)
        result.append(new_pt)
    return result


def get_region(p, plant):
    queue = [p]
    seen = set()
    while queue != []:
        current = queue.pop(0)
        if current in seen:
            continue
        seen.add(current)
        neighbors = getNeighbors(current)
        for neighbor in neighbors:
            if neighbor in plant:
                queue.append(neighbor)
    return seen


def floodPlants(plant):
    seen = set()
    partitions = dict()
    part = 0
    for p in plant:
        if p in seen:
            continue
        else:
            p_region = get_region(p, plant)
            partitions[part] = []
            for n in p_region:
                seen.add(n)
                partitions[part].append(n)
            part += 1
    return partitions


keys_to_delete = []
keys_to_add = dict()
for plant in plants:
    partitions_of_plant = floodPlants(plants[plant])
    if len(partitions_of_plant) > 1:
        for i in range(len(partitions_of_plant)):
            keys_to_add[plant + str(i)] = partitions_of_plant[i]
        keys_to_delete.append(plant)

for k in keys_to_delete:
    del plants[k]

for k in keys_to_add:
    plants[k] = keys_to_add[k]


def calculateFence(veg: set[tuple[int, int]]):
    perimeter = 0
    area = 0
    for v in veg:
        neighbors = getNeighbors(v)
        area += 1
        for neighbor in neighbors:
            if neighbor not in veg:
                perimeter += 1
    return area * perimeter


result = 0
for plant in plants:
    fences = calculateFence(plants[plant])
    result += fences
print(result)

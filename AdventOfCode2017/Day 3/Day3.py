dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def add_pts(a,b):
    return (a[0] + b[0], a[1] + b[1])

def generate():
    target = 1000
    total = 1
    previous_amount = 0
    amount = 1
    current_dir = 0
    current_coords = (0,0)
    yield current_coords
    coords_seen = set()

    while total < target:
        for i in range(amount):
            total += 1
            current_coords = add_pts(current_coords, dirs[current_dir])
            coords_seen.add(current_coords)
            yield current_coords
            if total == target:
                break
        temporary_amount = amount
        if amount == previous_amount:
            amount += 1
        current_dir += 1
        current_dir %= 4
        previous_amount = temporary_amount
        
    print(current_coords)

neighbors = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,0), (1,1), (1,-1)]

def getNeighbors(p):
    total = 0
    for neighbor in neighbors:
        nc = add_pts(p, neighbor)
        if nc in seen_coords:
            total += seen_coords[nc]
    return total

seen_coords = dict()
seen_coords[(0,0)] = 1
seen_coords[(0,1)] = 1
for coord in generate():
    if coord not in seen_coords:
        seen_coords[coord] = getNeighbors(coord)
        if seen_coords[coord] > 312051:
            break
print(coord)
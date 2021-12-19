import heapq
fileContents = open("Day 15/input.txt")
arr = fileContents.read().split('\n')
arr = [[int(i) for i in line] for line in arr]


def get_value_from_coords(coord):
    x, y = coord[0], coord[1]
    offset = x//len(arr) + y//len(arr)
    corresponding_value = arr[x % len(arr)][y % len(arr)]
    result = corresponding_value + offset
    if result > 9:
        result -= 9
    return result


def getNeighbors(node):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []
    for direction in dirs:
        if (node[0]+direction[0], node[1]+direction[1]) in coords:
            result.append((node[0]+direction[0], node[1]+direction[1]))
    return result


coords = set([(row, col) for row in range(5*len(arr))
              for col in range(5*len(arr))])


def calculate_risk():

    start = (0, 0)
    target = (5*len(arr)-1, 5*len(arr)-1)

    distances = {coord: 100000 for coord in coords}

    visited = set()

    q = [(0, start)]

    while len(q) != 0:
        distance, coord = heapq.heappop(q)
        if coord == target:
            return distance
        if coord in visited:
            continue

        visited.add(coord)
        for neighbor in getNeighbors(coord):
            if neighbor in visited:
                continue
            neighborDistance = distance + get_value_from_coords(neighbor)
            if neighborDistance < distances[neighbor]:
                distances[neighbor] = neighborDistance
                heapq.heappush(q, (neighborDistance, neighbor))


print(calculate_risk())

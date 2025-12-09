fileContents = open("AdventOfCode2025/Day 9/input.txt")
arr = fileContents.read().split("\n")

tiles = []

for line in arr:
    x, y = int(line.split(",")[0]), int(line.split(",")[1])
    # print((x, y))
    tiles.append((x, y))


def getArea(a, b):
    return (abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1)


def constructPerimeter(tiles):
    perimeterTiles = set()
    current = tiles[0]
    for tile in tiles[1:]:
        # print("new tile")
        # add current to tile to set
        while current != tile:
            # print(current, tile)
            perimeterTiles.add(current)
            if current[0] != tile[0]:
                if current[0] < tile[0]:
                    current = (current[0] + 1, current[1])
                else:
                    current = (current[0] - 1, current[1])
            else:
                if current[1] < tile[1]:
                    current = (current[0], current[1] + 1)
                else:
                    current = (current[0], current[1] - 1)
    while current != tiles[0]:
        # print(current, tiles[0])
        perimeterTiles.add(current)
        if current[0] != tiles[0][0]:
            if current[0] < tiles[0][0]:
                current = (current[0] + 1, current[1])
            else:
                current = (current[0] - 1, current[1])
        else:
            if current[1] < tiles[0][1]:
                current = (current[0], current[1] + 1)
            else:
                current = (current[0], current[1] - 1)
    return perimeterTiles


def isValidRectangle(a, b, perimeter):
    # left side
    # top left is sorted a[0], b[0], sorted a[1], b[1]
    top_left_row = min(a[0], b[0])
    top_left_col = min(a[1], b[1])
    bottom_right_row = max(a[0], b[0])
    bottom_right_col = max(a[1], b[1])

    # Walk Left Side
    for i in range(1, bottom_right_row - top_left_row):
        first, second = (
            (top_left_row + i, top_left_col),
            (top_left_row + i, top_left_col + 1),
        )
        if first in perimeter and second in perimeter:
            return False

    # Walk Right Side
    for i in range(1, bottom_right_row - top_left_row):
        first, second = (
            (top_left_row + i, bottom_right_col),
            (top_left_row + i, bottom_right_col - 1),
        )
        if first in perimeter and second in perimeter:
            return False

    # Walk Top Side
    for i in range(1, bottom_right_col - top_left_col):
        first, second = (
            (top_left_row, top_left_col + i),
            (top_left_row + 1, top_left_col + i),
        )
        if first in perimeter and second in perimeter:
            return False

    # Walk Bottom Side
    for i in range(1, bottom_right_col - top_left_col):
        first, second = (
            (bottom_right_row, top_left_col + i),
            (bottom_right_row - 1, top_left_col + i),
        )
        if first in perimeter and second in perimeter:
            return False
    return True


largestArea = 0
perimeter = constructPerimeter(tiles)
print("Constructed!")
for tile1 in tiles:
    for tile2 in tiles:
        if tile1 == tile2:
            continue
        else:
            area = getArea(tile1, tile2)
            if area > largestArea:
                if isValidRectangle(tile1, tile2, perimeter):
                    print("New Area!", area)
                    largestArea = area
                    coords = tile1, tile2
print(largestArea, coords)

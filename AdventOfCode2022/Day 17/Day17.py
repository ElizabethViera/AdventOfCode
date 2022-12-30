horizLine = [(2,0), (3,0), (4,0), (5,0)]
cross = [(3,-2), (2,-1), (3,-1), (4,-1), (3,0)]
bigL = [(2,0), (3,0), (4,0), (4,-1), (4,-2)]
vertLine = [(2,-3), (2,-2), (2,-1), (2,0)]
box = [(2,0), (3,0), (2,-1), (3,-1)]

tetris_pieces = [horizLine, cross, bigL, vertLine, box]

def make_piece(i):
    if i > 4:
        i %= 5
    return tetris_pieces[i]

def collides_with_existing_floor(coords, existing_floor):
    for coord in coords:
        if coord in existing_floor:
            return True
    return False

def air_push_piece(dir, piece_coords):
    new_piece_coords = []
    # print("dir = ", dir)
    if dir == '>':
        # push right
        for piece_coord in piece_coords:
            # print("piece_coord", piece_coord)
            new_x = piece_coord[0] + 1
            new_y = piece_coord[1]
            new_piece_coords.append((new_x, new_y))
    
    if dir == '<':
        # push left
        for piece_coord in piece_coords:
            new_x = piece_coord[0] - 1
            new_y = piece_coord[1]
            new_piece_coords.append((new_x, new_y))
    for new_piece in new_piece_coords:
        if new_piece[0] < 0 or new_piece[0] > 6:
            return piece_coords
    return new_piece_coords

def piece_falls(piece_coords, floor_coords):
    result = []
    for piece_coord in piece_coords:
        new_location = (piece_coord[0], piece_coord[1] - 1)
        if new_location in floor_coords:
            return piece_coords
        result.append(new_location)
    # print("after falling, ", result)
    return result
    

def place_piece(piece, highest_point):
    result = []
    for coord in piece:
        result.append( (coord[0], coord[1] + highest_point + 3))
    # print(result)
    return result

def getNewHighestPoint(highest_point, piece):
    for piece_coords in piece:
        if piece_coords[1] > highest_point:
            highest_point = piece_coords[1]
    return highest_point


fileContents = open("AdventOfCode2022/Day 17/input.txt")
arr = fileContents.read().split("\n")
arr = arr[0]
wind = 0
floor_coords = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (0,0)]
highest_point = 0
for i in range(2022):
    piece = make_piece(i)
    piece = place_piece(piece, highest_point)
    # print("piece = ", piece)
    while (True):
        direction = arr[wind%len(arr)]
        wind += 1
        piece = air_push_piece(direction, piece)
        # print("after air push", piece)
        new_location_piece = piece_falls(piece, floor_coords)
        if new_location_piece == piece: 
            break
        piece = new_location_piece
    for coord in piece:
        floor_coords.append(coord)
    highest_point = getNewHighestPoint(highest_point, new_location_piece)


print(highest_point)
horizLine = [(2,0), (3,0), (4,0), (5,0)]
cross = [(3,-2), (2,-1), (3,-1), (4,-1), (3,0)]
bigL = [(2,0), (3,0), (4,0), (4,-1), (4,-2)]
vertLine = [(2,-3), (2,-2), (2,-1), (2,0)]
box = [(2,0), (3,0), (2,-1), (3,-1)]

existing_floor = set([(0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4)])

tetris_pieces = [horizLine, cross, bigL, vertLine, box]

def make_piece(i):
    if i > 4:
        i %= 5
    return tetris_pieces[i]

def collides_with_existing_floor(coords):
    for coord in coords:
        if coord in existing_floor:
            return True
    return False

def push_floor_down(piece_coords):
    global existing_floor
    for coord in piece_coords:
        if coord[1] < 4:
            move_by = 4 - coord[1]
            new_floor = set()
            for coord in existing_floor:
                new_x = coord[0]
                new_y = coord[1] + move_by
                new_floor.add((new_x, new_y))
    existing_floor = new_floor

def air_push_piece(dir, piece_coords):
    new_piece_coords = []
    print("dir = ", dir)
    if dir == '>':
        # push right
        for piece_coord in piece_coords:
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

def gravity_push_piece(piece_coords):
    new_piece_coords = []
    
    for piece_coord in piece_coords:
        new_x = piece_coord[0]
        new_y = piece_coord[1] + 1
        new_piece_coords.append((new_x, new_y))
    for piece_coord in new_piece_coords:
        if collides_with_existing_floor(new_piece_coords):
            for piece in piece_coords:
                existing_floor.add(piece)
            push_floor_down(piece_coords)
            return 
    return new_piece_coords


fileContents = open("AdventOfCode2022/Day 17/input.txt")
arr = fileContents.read().split("\n")
arr = arr[0]
wind = 0
for i in range(1):
    piece = make_piece(i)
    print("piece = ", piece)
    while (piece):
        direction = arr[wind%len(arr)]
        wind += 1
        piece = air_push_piece(direction, piece)
        print("after air push", piece)
        piece = gravity_push_piece(piece)
print("existing floor = ", existing_floor)



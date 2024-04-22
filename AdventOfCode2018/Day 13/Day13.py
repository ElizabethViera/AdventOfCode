fileContents = open("AdventOfCode2018/Day 13/input.txt")
map_of_carts = fileContents.read().split("\n")

from dataclasses import dataclass

def createDirs():
    dirs = dict()
    dirs[('N', 'L')] = 'W'
    dirs[('N', 'F')] = 'N'
    dirs[('N', 'R')] = 'E'
    dirs[('S', 'L')] = 'E'
    dirs[('S', 'F')] = 'S'
    dirs[('S', 'R')] = 'W'
    dirs[('E', 'L')] = 'N'
    dirs[('E', 'F')] = 'E'
    dirs[('E', 'R')] = 'S'
    dirs[('W', 'L')] = 'S'
    dirs[('W', 'F')] = 'W'
    dirs[('W', 'R')] = 'N'
    return dirs

@dataclass
class Coord():
    row: int
    col: int
    character: str
    north: tuple[int,int]
    south: tuple[int,int]
    east: tuple[int,int] 
    west: tuple[int,int]


@dataclass
class MineCart():
    row: int
    col: int
    direction: str
    turns: int = 0

all_coords = dict() # from (row,col) to Coord
minecarts = dict() # from (row,col) to Minecart
dirs = createDirs()

def get_new_direction(t: int, d: str):
    match t%3:
        case 0:
            lrf = 'L'
        case 1:
            lrf = 'F'
        case 2:
            lrf = 'R'
    return dirs[(d, lrf)]

# parse input
for row, line in enumerate(map_of_carts):
    for col, c in enumerate(line):
        match c:
            case '-':
                new_coord = Coord(row=row, col=col, character='-', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                all_coords[(row,col)] = new_coord
            case '|':
                new_coord = Coord(row=row, col=col, character='|', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                all_coords[(row,col)] = new_coord
            case '/':
                new_coord = Coord(row=row, col=col, character='/', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                all_coords[(row,col)] = new_coord
            case '\\':
                new_coord = Coord(row=row, col=col, character='\\', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                all_coords[(row,col)] = new_coord
            case '+':
                new_coord = Coord(row=row, col=col, character='+', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                all_coords[(row,col)] = new_coord
            case '>':
                new_coord = Coord(row=row, col=col, character='-', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                new_minecart = MineCart(row=row, col=col, direction='E')
                all_coords[(row,col)] = new_coord
                minecarts[(row,col)] = new_minecart
            case '<':
                new_coord = Coord(row=row, col=col, character='-', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                new_minecart = MineCart(row=row, col=col, direction='W')
                all_coords[(row,col)] = new_coord
                minecarts[(row,col)] = new_minecart
            case '^':
                new_coord = Coord(row=row, col=col, character='|', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                new_minecart = MineCart(row=row, col=col, direction='N')
                all_coords[(row,col)] = new_coord
                minecarts[(row,col)] = new_minecart
            case 'v':
                new_coord = Coord(row=row, col=col, character='|', east=(row, col+1), west=(row, col-1), north=(row-1,col), south=(row+1,col))
                new_minecart = MineCart(row=row, col=col, direction='S')
                all_coords[(row,col)] = new_coord
                minecarts[(row,col)] = new_minecart

def moveMinecarts(mcs):
    old_minecarts = sorted(list(mcs.keys()))
    new_minecarts = dict()
    counts = dict() # coords to number
    while old_minecarts != []:
        minecart = old_minecarts.pop(0)
        new_direction = 'N'
        new_location = None
        new_turn_count = mcs[minecart].turns
        match mcs[minecart].direction:
            case 'N':
                new_location = all_coords[(mcs[minecart].row, mcs[minecart].col)].north
                if all_coords[new_location].character == '/':
                    new_direction = 'E'
                elif all_coords[new_location].character == '\\':
                    new_direction = 'W'
                elif all_coords[new_location].character == '|':
                    new_direction = 'N'
                elif all_coords[new_location].character == '+':
                    new_direction = get_new_direction(mcs[minecart].turns, 'N')
                    new_turn_count += 1
                else:
                    raise(ValueError)
            case 'S':
                new_location = all_coords[(mcs[minecart].row, mcs[minecart].col)].south
                if all_coords[new_location].character == '/':
                    new_direction = 'W'
                elif all_coords[new_location].character == '\\':
                    new_direction = 'E'
                elif all_coords[new_location].character == '|':
                    new_direction = 'S'
                elif all_coords[new_location].character == '+':
                    new_direction = get_new_direction(mcs[minecart].turns, 'S')
                    new_turn_count += 1
                else:
                    raise(ValueError)
            case 'E':
                new_location = all_coords[(mcs[minecart].row, mcs[minecart].col)].east
                if all_coords[new_location].character == '/':
                    new_direction = 'N'
                elif all_coords[new_location].character == '\\':
                    new_direction = 'S'
                elif all_coords[new_location].character == '-':
                    new_direction = 'E'
                elif all_coords[new_location].character == '+':
                    new_direction = get_new_direction(mcs[minecart].turns, 'E')
                    new_turn_count += 1
                else:
                    raise(ValueError)
            case 'W':
                new_location = all_coords[(mcs[minecart].row, mcs[minecart].col)].west
                if all_coords[new_location].character == '/':
                    new_direction = 'S'
                elif all_coords[new_location].character == '\\':
                    new_direction = 'N'
                elif all_coords[new_location].character == '-':
                    new_direction = 'W'
                elif all_coords[new_location].character == '+':
                    new_direction = get_new_direction(mcs[minecart].turns, 'W')
                    new_turn_count += 1
                else:
                    raise(ValueError)
            case _:
                raise(ValueError)
        if new_direction == None:
            raise(ValueError)
        
        if new_location in old_minecarts: 
            old_minecarts.remove(new_location)   
        elif new_location in new_minecarts:
            del new_minecarts[new_location]
        else:
            new_minecarts[new_location] = MineCart(row=new_location[0], col=new_location[1], direction=new_direction, turns=new_turn_count)
        
    for c in counts:
        if counts[c] > 1:
            print(c, counts[c])
            del new_minecarts[c]
    return new_minecarts

while len(minecarts) > 1:
    minecarts = moveMinecarts(minecarts)
for key in minecarts:
    print(key[1], key[0])
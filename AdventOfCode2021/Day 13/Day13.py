fileContents = open("Day 13/input.txt")
coords = fileContents.read().split('\n')

fileContents = open("Day 13/input2.txt")
folds = fileContents.read().split('\n')

coords = [[int(x.split(',')[0]), int(x.split(',')[1])] for x in coords]
# print(coords)


def translate_to_new_spot(coord, axis, value):
    if axis == 'y':
        new_x = coord[0]
        new_y = value - abs(value - coord[1])
    if axis == 'x':
        new_x = value - abs(value - coord[0])
        new_y = coord[1]
    return [new_x, new_y]


for fold in folds:
    instructions = fold.split(' ')
    axis, value = instructions[-1].split(
        '=')[0], int(instructions[-1].split('=')[1])
    new_coords = []
    for coord in coords:
        if axis == 'y':
            if coord[1] > value:
                new_coord = translate_to_new_spot(coord, axis, value)
            else:
                new_coord = coord
        else:
            # axis is x
            if coord[0] > value:
                new_coord = translate_to_new_spot(coord, axis, value)
            else:
                new_coord = coord
        new_coords.append(new_coord)
    coords = new_coords

result = [tuple(i) for i in coords]
result = (set(result))

for y in range(6):
    for x in range(40):
        if (x, y) in result:
            print('x', end='')
        else:
            print(' ', end='')
    print('')

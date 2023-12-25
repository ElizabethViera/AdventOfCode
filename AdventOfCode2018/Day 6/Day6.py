fileContents = open("AdventOfCode2018/Day 6/input.txt")
lines = fileContents.read().split("\n")

coords = set()
for line in lines:
    r, c = int(line.split(', ')[0]), int(line.split(', ')[1])
    coords.add((r,c))


min_y, max_y = min(p[0] for p in coords), max(p[0] for p in coords)
 
min_x, max_x = min(p[0] for p in coords), max(p[0] for p in coords)

answer_candidates = [p for p in coords if p[0] != min_x and p[0] != max_x and p[1] != min_y and p[1] != max_y]


def getManhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

def getClosestCoord(x,y):
    min_manhattan = 500000
    closest_coord = None
    for coord in coords:
        if getManhattan(coord, (x,y)) < min_manhattan:
            min_manhattan = getManhattan(coord, (x,y))
            closest_coord = coord
        elif getManhattan(coord, (x,y)) == min_manhattan:
            closest_coord = 'Tie'
    return closest_coord

ultimate_dictionary = dict()
for coord in coords:
    ultimate_dictionary[coord] = set()
ultimate_dictionary['Tie'] = set()
for x in range(min_x-100, max_x+100):
    for y in range(min_y-100, max_y+100):
        coord = getClosestCoord(x,y)
        ultimate_dictionary[coord].add((x,y))

candidate_lengths = []
for candidate in answer_candidates:
    candidate_lengths.append(len(ultimate_dictionary[candidate]))

print(sorted(candidate_lengths))
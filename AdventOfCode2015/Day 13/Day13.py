import itertools

fileContents = open("AdventOfCode2015/Day 13/input.txt")
arr = fileContents.read().split('\n')

happiness_dict = {}
for line in arr:
    line_contents = line.split(' ')
    guest, neighbor, sign, happiness = line_contents[0], line_contents[-1][:-1], line_contents[2], line_contents[3], 

    if guest not in happiness_dict:
        happiness_dict[guest] = {}
    multiplier = 1 if sign == 'gain' else -1
    happiness_dict[guest][neighbor] = int(happiness)*multiplier
print(happiness_dict)

guests = ['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory', 'Blando']
all_seatings = list(itertools.permutations(guests))

def calculate_happiness(group):
    result = 0
    for i, guest in enumerate(group):
        neighbor_left = group[i-1]
        neighbor_right = group[(i+1)%9]
        result += happiness_dict[guest][neighbor_right]
        result += happiness_dict[guest][neighbor_left]
    return result

max_happiness = 0
for seating in all_seatings:
    happiness = calculate_happiness(seating)
    if happiness > max_happiness:
        max_happiness = happiness
print(max_happiness)
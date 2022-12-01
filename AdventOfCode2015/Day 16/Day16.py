fileContents = open("AdventOfCode2015/Day 16/input.txt")
arr = fileContents.read().split('\n')

sues_dict = {}
for line in arr:
    items = line.split(' ')
    number, item1, item2, item3, count1, count2, count3 = items[1][:-1], items[2][:-1], items[4][:-1], items[6][:-1], items[3][:-1], items[5][:-1], items[7]
    sues_dict[number] = {item1: count1, item2: count2, item3: count3}
print(sues_dict['25'])

clues = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

possible_aunts = set(range(1,500))
for clue in clues:
    for sue in sues_dict:
        if clue in sues_dict[sue]:
            if clue == 'cats' or clue == 'trees':
                if int(sues_dict[sue][clue]) <= clues[clue]:
                    if int(sue) in possible_aunts:
                        possible_aunts.remove(int(sue))
            elif clue == 'pomeranians' or clue == 'goldfish':
                if int(sues_dict[sue][clue]) >= clues[clue]:
                    if int(sue) in possible_aunts:
                        possible_aunts.remove(int(sue))
            else:    
                if int(sues_dict[sue][clue]) != clues[clue]:
                    if int(sue) in possible_aunts:
                        possible_aunts.remove(int(sue))
print(possible_aunts)

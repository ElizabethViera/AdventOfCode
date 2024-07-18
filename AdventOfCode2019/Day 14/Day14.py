fileContents = open("AdventOfCode2019/Day 14/input.txt")
instructions = fileContents.read().split("\n")

menu = dict()

for ins in instructions:
    left, right = ins.split(' => ')[0], ins.split(' => ')[1]
    number, item = int(right.split(' ')[0]), right.split(' ')[1]
    menu[(item, number)] = []

    materials = left.split(', ')
    for material in materials:
        n, m = int(material.split(' ')[0]), material.split(' ')[1]
        menu[(item, number)].append((m, n))

def roundUpDiv(a,b):
    if a%b == 0:
        return a//b
    else:
        return a//b + 1

def find_inventory_match(item):
    for candidate in menu:
        if candidate[0] == item:
            return candidate
    raise(ValueError)

def simplify_inventory(inventory):
    names_to_numbers = dict()
    for (i,n) in inventory:
        if i not in names_to_numbers:
            names_to_numbers[i] = 0
        names_to_numbers[i] += n
    return [(name, names_to_numbers[name]) for name in names_to_numbers]


def update_inventory(inventory):
    new_inventory = []
    for (i, n) in inventory:
        if i == 'ORE':
            new_inventory.append((i, n))
            continue
        match = find_inventory_match(i)
        conversion_number = match[1]
        multiply_left_side_by = roundUpDiv(n, conversion_number)
        for result in menu[match]:
            new_inventory.append((result[0], result[1]*multiply_left_side_by))
    return simplify_inventory(new_inventory)

inventory = [('FUEL', 1)]
while len(inventory) != 1 or inventory[0][0] != 'ORE':
    print(inventory)
    inventory = update_inventory(inventory)
print(inventory)
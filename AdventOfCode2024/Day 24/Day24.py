from itertools import permutations

listsContents = open("AdventOfCode2024/Day 24/input.txt")
lines = listsContents.read().split("\n")

rulesContents = open("AdventOfCode2024/Day 24/rules.txt")
rules = rulesContents.read().split("\n")


all_rules = dict()
for rule in rules:
    left, operator, right = (
        rule.split(" ")[0],
        rule.split(" ")[1],
        rule.split(" ")[2],
    )
    value = rule.split(" -> ")[1]
    all_rules[(left, operator, right)] = value


def calc(rules):
    values = dict()

    for line in lines:
        left, right = line.split(": ")
        values[left] = int(right)

    while True:
        all_done = True
        change_made = False
        for rule in rules:
            left, operator, right = (
                rule[0],
                rule[1],
                rule[2],
            )
            if left not in values or right not in values:
                all_done = False
                continue
            else:
                value = rules[rule]
                if value in values:
                    continue
                change_made = True
                match operator:
                    case "AND":
                        values[value] = values[left] and values[right]
                    case "OR":
                        values[value] = values[left] or values[right]
                    case "XOR":
                        values[value] = values[left] != values[right]
        if all_done:
            return values
        if not change_made:
            return None


values = calc(all_rules)
all_combos = permutations(all_rules.keys(), 8)

for i, combo in enumerate(all_combos):
    if i % 100000 == 0:
        print(i)
    rules = all_rules
    rules[combo[0]], rules[combo[1]] = rules[combo[1]], rules[combo[0]]
    rules[combo[2]], rules[combo[3]] = rules[combo[3]], rules[combo[2]]
    rules[combo[4]], rules[combo[5]] = rules[combo[5]], rules[combo[4]]
    rules[combo[6]], rules[combo[7]] = rules[combo[7]], rules[combo[6]]
    values = calc(rules)
    if values is None:
        continue

    x_value = ""
    y_value = ""
    z_value = ""
    for value in sorted(values)[::-1]:
        if value.startswith("z"):
            z_value += "1" if values[value] else "0"
        if value.startswith("x"):
            x_value += "1" if values[value] else "0"
        if value.startswith("y"):
            y_value += "1" if values[value] else "0"
    if int(x_value, base=2) + int(y_value, base=2) == int(z_value, base=2):
        print(combo)
        break

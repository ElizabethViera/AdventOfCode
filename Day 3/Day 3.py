fileContents = open("AdventOfCode/Day 3/input")
arr = fileContents.read().split('\n')

current_index = 0
total_trees = 1
slopeList = [1, 3, 5, 7]
downList = [1, 1, 1, 1]

for slope in slopeList:
    current_index = 0
    trees = 0
    for line in arr:
        length_of_line = len(line)

        if line[current_index] == "#":
            trees += 1
        current_index += slope
        if current_index >= length_of_line:
            current_index %= length_of_line
    total_trees *= trees
    print(total_trees)

trees = 0
current_index = 0
for i, line in enumerate(arr):
    if (i % 2) == 1:
        continue
    length_of_line = len(line)

    if line[current_index] == "#":
        trees += 1
    current_index += 1
    if current_index >= length_of_line:
        current_index %= length_of_line
total_trees *= trees
print(total_trees)

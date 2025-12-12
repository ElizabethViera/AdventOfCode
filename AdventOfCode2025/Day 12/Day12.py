fileContents = open("AdventOfCode2025/Day 12/input.txt")
arr = fileContents.read().split("\n\n")
# print(arr)

total = 0
trees = arr[-1]
trees = trees.split("\n")
tree_list = []
for tree in trees:
    dimensions = tree.split(": ")[0].split("x")
    dimensions = [int(x) for x in dimensions]
    # print(dimensions)
    goals = tree.split(": ")[1].split(" ")
    goals = [int(x) for x in goals]
    # print(goals)
    tree_list.append((dimensions, goals))
    print(sum(goals), dimensions[0] * dimensions[1])
    if sum(goals) * 7 < dimensions[0] * dimensions[1]:
        total += 1
print(total)

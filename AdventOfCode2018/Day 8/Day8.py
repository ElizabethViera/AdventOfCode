# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
fileContents = open("AdventOfCode2018/Day 8/input.txt")
nodes = fileContents.read().split(" ")
nodes = [int(x) for x in nodes]

def process(list_of_nodes):
    result = 0
    length = 2
    children = list_of_nodes.pop(0)
    metadata = list_of_nodes.pop(0)
    child_values = []
    for child in range(children):
        child_length, child_result = process(list_of_nodes)
        child_values.append(child_result)
    if children == 0:
        for meta in range(metadata):
            length += 1
            result += list_of_nodes.pop(0)
        return length, result
    for meta in range(metadata):
        length += 1
        index = list_of_nodes.pop(0)-1
        if index in range(len(child_values)):
            result += child_values[index]
    return length, result

print(process(nodes))
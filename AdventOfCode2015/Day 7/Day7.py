from functools import lru_cache


fileContents = open("AdventOfCode2015/Day 7/input.txt")
arr = fileContents.read().split('\n')

directions_dict = dict()
for direction in arr:
    left_side, output_wire = direction.split(' -> ')
    directions_dict[output_wire] = left_side.split(' ')
print(len(directions_dict))

for key in directions_dict:
    directions_dict[key] = tuple(directions_dict[key])


@lru_cache(maxsize=128)
def calc(instruct):
    if isinstance(instruct, int):
        return instruct
    if len(instruct) == 1:
        if instruct[0].isnumeric():
            return int(instruct[0])
        else:
            return calc(directions_dict[instruct[0]])
    if instruct[0] == "NOT":
        not_piece = instruct[1] if instruct[1].isnumeric() else directions_dict[instruct[1]]
        return ~calc(not_piece)

    left_piece = int(instruct[0]) if instruct[0].isnumeric() else directions_dict[instruct[0]]
    right_piece = int(instruct[2]) if instruct[2].isnumeric() else directions_dict[instruct[2]]
    if instruct[1] == "OR":
        return calc(left_piece) | calc(right_piece)
    if instruct[1] == "AND":
        return calc(left_piece) & calc(right_piece)
    if instruct[1] == "LSHIFT":
        return calc(left_piece) << calc(right_piece)
    if instruct[1] == "RSHIFT":
        return calc(left_piece) >> calc(right_piece)

result = calc(tuple(directions_dict["a"]))
print(result)


fileContents = open("AdventOfCode2023/Day 25/input.txt")
arr = fileContents.read().split("\n")

ver = set()

for line in arr:
    left = line.split(':')[0]
    right = line.split(':')[1].strip().split(' ')
    for r in right:
        ver.add(tuple(sorted([r, left])))

import itertools
things_to_remove = list(itertools.combinations(ver, 3))

print(len(things_to_remove))

def construct_graphs(v_copy) -> list[list[str]]:
    return []

for r in things_to_remove:
    a, b, c = r[0], r[1], r[2]
    v_copy = ver
    v_copy.remove(a)
    v_copy.remove(b)
    v_copy.remove(c)
    if len(construct_graphs(v_copy)) == 2:
        pass
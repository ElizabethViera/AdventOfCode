from itertools import combinations

listsContents = open("AdventOfCode2024/Day 23/input.txt")
connections = listsContents.read().split("\n")

cons = dict()

for c in connections:
    left, right = c.split("-")
    if left not in cons:
        cons[left] = set()
    if right not in cons:
        cons[right] = set()
    cons[left].add(right)
    cons[right].add(left)
    cons[left].add(left)
    cons[right].add(right)
#####
# I did some stuff manually inspecting the dictionary with graphviz
# I ran dot -Tsvg -Ksfdp AdventOfCode2024/Day\ 23/cons.dot -o output.svg
# and then visually looked for a cluster. I made a list of candidates, redacted below, and then did some printing to verify this was right

candidates = [
    # redacted
]
for c in candidates:
    for b in candidates:
        if c not in cons[b]:
            print(c, b, cons[b])

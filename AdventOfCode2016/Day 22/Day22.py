fileContents = open("AdventOfCode2016/Day 22/input.txt")
arr = fileContents.read().split('\n')

nodes = dict()

for line in arr:
    x,y = int(line.split(' ')[0].split('-')[-2][1:]), int(line.split(' ')[0].split('-')[-1][1:])
    used, avail = int(line.split(' ')[2][:-1]), int(line.split(' ')[3][:-1])
    nodes[(x,y)] = (used,avail)
    if y == 0:
        print(x, used, avail, used+avail)

results = set()

for a in nodes:
    for b in nodes:
        if a == b:
            continue
        if nodes[a][0] != 0 and nodes[a][0] <= nodes[b][1]:
            results.add((a,b))

def cpy(a,b, nodes):
    if (a,b) in results:
        nodes[a], nodes[b] = (0, a[0] + a[1]), (a[1 + b[0]], b[1]-a[1])
    return nodes


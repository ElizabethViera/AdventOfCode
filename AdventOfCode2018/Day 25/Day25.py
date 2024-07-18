fileContents = open("AdventOfCode2018/Day 25/input.txt")
rows = fileContents.read().split("\n")

constellations: list[list[tuple[int,...]]] = []

for row in rows:
    vals = tuple([int(x) for x in row.split(',')])
    constellations.append([vals])

def get_manhattan(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2]) + abs(c1[3] - c2[3])


def compare_constellations(a,b):
    for c1 in a:
        for c2 in b:
            if get_manhattan(c1, c2) <= 3:
                return True
    return False

def merge_constellations(a,b):
    result = []
    for c in a:
        result.append(c)
    for c in b:
        result.append(c)
    return result

def collapse_constellations(old):
    copy_old = list(old)
    new = []
    merged = []
    for i in copy_old:
        for j in copy_old:
            for a in i:
                for b in j:
                    if i != j and i not in merged and j not in merged and get_manhattan(a,b) <= 3:
                        merging = merge_constellations(i,j)
                        new.append(merging)
                        merged.append(i)
                        merged.append(j)
                        if i in new:
                            new.remove(i)
                        if j in new:
                            new.remove(j)
            if j not in merged and j not in new and i not in merged:
                new.append(j)
        if i not in merged and i not in new and j not in merged:
            new.append(i)
    return new

old_constellations = constellations
print(len(constellations))
new_constellations = collapse_constellations(old_constellations)
while len(old_constellations) > len(new_constellations):
    print(len(old_constellations))
    old_constellations = new_constellations
    new_constellations = collapse_constellations(old_constellations)
print(len(new_constellations))

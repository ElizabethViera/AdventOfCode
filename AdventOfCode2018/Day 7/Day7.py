fileContents = open("AdventOfCode2018/Day 7/sampleInput.txt")
lines = fileContents.read().split("\n")

dependencies = dict()
opposite_direction = dict()
for line in lines:
    left, right = line.split(' ')[1], line.split(' ')[-3]
    if left not in dependencies:
        dependencies[left] = []
    if right not in opposite_direction:
        opposite_direction[right] = []
    dependencies[left].append(right)
    opposite_direction[right].append(left)

print(dependencies)
print(opposite_direction)

def removeFromList(l, n):
    print(l,n)
    for i,v in enumerate(l):
        if v == n:
            return l[:i] + l[i+1:]

def cleanUpOppositeDirection(i):
    cleaned = dict()
    for k in opposite_direction:
        print(k)
        clean = removeFromList(opposite_direction[k], i)
        if clean != []:
            cleaned[k] = clean
    return cleaned

def getNextAvailable():
    next_available = []
    for k in dependencies:
        if k not in opposite_direction:
            next_available.append(k)
    return next_available

result = ''
while len(dependencies) > 0:
    next_available = getNextAvailable()
    print(next_available)
    for n in sorted(next_available):
        del dependencies[n]
        opposite_direction = cleanUpOppositeDirection(n)
        result += n

print(result)
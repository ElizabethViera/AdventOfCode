fileContents = open("AdventOfCode2023/Day 15/input.txt")
grid = fileContents.read().split(",")

'''
for line in grid:
    currentValue = 0
    for c in line:
        asci = int(ord(c))
        currentValue += asci
        currentValue *= 17
        currentValue %= 256
    total += currentValue
'''

def getHash(s):
    currentValue = 0
    for c in s:
        asci = int(ord(c))
        currentValue += asci
        currentValue *= 17
        currentValue %= 256
    return currentValue

def addHashToHashBox(box, t):
    if box == []:
        return [t]
    else:
        for i in range(len(box)):
            if box[i][0] == t[0]:
                box[i] = t
                return box
        box.append(t)
        return box

def removeHashFromHashBox(box, h):
    for i in range(len(box)):
        if box[i][0] == h:
            return box[:i] + box[i+1:]
    return box

hashBoxes = dict()

for line in grid:
    if '=' in line:
        h, v = line.split('=')[0], int(line.split('=')[1])
        hashOfH = getHash(h)
        if hashOfH not in hashBoxes:
            hashBoxes[hashOfH] = []
        hashBoxes[getHash(h)] = addHashToHashBox(hashBoxes[getHash(h)], (h, v))
    if '-' in line:
        h = line[:-1]
        hHash = getHash(h)
        if hHash not in hashBoxes:
            continue
        hashBoxes[hHash] = removeHashFromHashBox(hashBoxes[hHash], h)

    
############## After obtaining HashBoxes, Calculate Focus Power ##########
total = 0
for hashBox in hashBoxes:
    if len(hashBoxes[hashBox]) == 0:
        continue
    for i, lens in enumerate(hashBoxes[hashBox]):
        total += (hashBox+1) * (i+1) * lens[1]
print(total)
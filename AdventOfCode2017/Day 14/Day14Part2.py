fileContents = open("AdventOfCode2017/Day 14/input2.txt")
arr = fileContents.read().split('\n')

chars = dict()
for r, row in enumerate(arr):
    for c, char in enumerate(row):
        chars[(r,c)] = char

def findAsterisk(characters):
    for key in characters:
        if characters[key] == '*':
            return key
    return None

def addPts(a,b):
   return a[0] + b[0], a[1] + b[1]

def getNeighbors(point, characters, visited):
    n = [(-1,0), (1,0), (0,1), (0, -1)]
    results = []
    for neighbor in n:
        candidate = addPts(point, neighbor)
        if characters[candidate] == '*' and candidate not in visited:
            results.append(candidate)
    return results

visited = set()
regions = 0
while '*' in chars.values():
    regions += 1
    asterisk = findAsterisk(chars)
    toSearch = [asterisk]
    while toSearch != []:
        current = toSearch.pop()
        visited.add(current)
        chars[current] = regions
        neighbors = getNeighbors(current, chars, visited)
        for neighbor in neighbors:
            toSearch.append(neighbor)

print(regions)
fileContents = open("AdventOfCode2017/Day 12/input.txt")
arr = fileContents.read().split('\n')

links = dict()

for line in arr:
    left, right = line.split(' <-> ')[0], line.split(' <-> ')[1].split(', ')
    if left not in links:
        links[left] = set()
    for r in right:
        if r not in links:
            links[r] = set()
        links[left].add(r)
        links[r].add(left)

def findUnvisited(s, k):
    for key in k:
        if key not in s:
            return key
    return None
    
visited = set()
results = 1
queue = ['0']
while queue != []:
    current = queue.pop()
    if current not in visited:
        visited.add(current)
        for neighbor in links[current]:
            queue.append(neighbor)
    if queue == [] and len(visited) < len(set(links.keys())):
        nextKey = findUnvisited(visited, links.keys())
        if nextKey is not None:
            queue.append(nextKey)
            results += 1

print(results)
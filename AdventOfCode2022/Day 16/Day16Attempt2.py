fileContents = open("AdventOfCode2022/Day 16/input.txt")
arr = fileContents.read().split("\n")
import functools
import itertools
import datetime

print(datetime.datetime.now())
start = datetime.datetime.now()

rates = {}
neighbors = {}
openableValves = set()
for line in arr:
    node, rate = line.split(' ')[1], int(line.split(' ')[4].split('=')[-1][:-1])
    get_neighbors = line.split('valve')[-1].split(' ')[1:]
    get_neighbors = [neighbor.strip(',') for neighbor in get_neighbors]
    if rate != 0:
        openableValves.add(node)


    rates[node] = rate
    neighbors[node] = get_neighbors

def powerset(s):
    allSets = []
    for n in range(len(s)):
        allSets.extend(itertools.combinations(s,n))
    return allSets

def openValve(valve, remainingTime):
    return rates[valve] * remainingTime

@functools.cache
def dynamicProgramming(openValves, timeRemaining, currentNode):
    if len(openValves) == len(openableValves):
        return 0
    if timeRemaining == 0:
        return 0
    maxScore = 0
    for neighbor in neighbors[currentNode]:
        score = dynamicProgramming(openValves, timeRemaining-1, neighbor)
        maxScore = max(score, maxScore)
    if rates[currentNode] != 0 and currentNode not in openValves:
        newOpenValves = tuple(sorted((* openValves, currentNode)))
        score = openValve(currentNode, timeRemaining-1)
        score += dynamicProgramming(newOpenValves, timeRemaining-1, currentNode)
        maxScore = max(score, maxScore)
    return maxScore

maxScore = 0
for subset in powerset(openableValves):
    elephant = []
    me = []
    for valve in openableValves:
        if valve in subset:
            elephant.append(valve)
        else:
            me.append(valve)
    score = 0
    score += dynamicProgramming(tuple(sorted(elephant)), 26, 'AA')
    score += dynamicProgramming(tuple(sorted(me)), 26, 'AA')
    maxScore = max(score, maxScore)
print(maxScore)
print(datetime.datetime.now() - start)





fileContents = open("AdventOfCode2023/Day 5/input.txt")
arr = fileContents.read().split("\n")

seeds = arr[0]
maplist = []
maps = []
for line in arr[2:]:
    if line == '':
        continue
    if 'map' in line:
        maps.append(maplist)
        maplist = [line]
    else:
        maplist.append(line)
maps.append(maplist)

fancydict = dict()
for entry in maps[1:]:
    fancydict[entry[0]] = [x.split(' ') for x in entry[1:]]
    
for key in fancydict: 
    for i in range(len(fancydict[key])):

        fancydict[key][i] = [int(x) for x in fancydict[key][i]]

def getRelevantRange(i, r):
    for specialRange in r:
        if i >= specialRange[1] and i < specialRange[1] + specialRange[2]: 
            return specialRange[0] + (i - specialRange[1]), specialRange[1] + (specialRange[2] - i)
    minimum_distance = 102345600000
    for specialRange in r:
        if specialRange[1] - i < minimum_distance and specialRange[1] > i:
            minimum_distance = specialRange[1] - i
    return i, minimum_distance

def seedMap(seed):
    currentKey = seed
    relevantRange = 1008908000000
    for key in fancydict:
        currentKey, candidateRange = getRelevantRange(currentKey, fancydict[key])
        
        relevantRange = min(candidateRange, relevantRange)
        #print('after', currentKey, relevantRange)
    return currentKey, relevantRange

seeds = [int(x) for x in seeds.split(' ')[1:]]
allLocations = []
for s in range(0, len(seeds), 2):
    seed_start, r = seeds[s], seeds[s+1]
    currentSeed = seed_start
    while currentSeed < seed_start + r:
        #print("words", currentSeed)
        location, relevantRange = seedMap(currentSeed)
        allLocations.append(location)
        currentSeed += relevantRange
        #print("location", location)
    #print('\n')

#print(allLocations)
print(sorted(allLocations)[0])

print()





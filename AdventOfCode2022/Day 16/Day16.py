fileContents = open("AdventOfCode2022/Day 16/input.txt")
arr = fileContents.read().split("\n")
TIME_LIMIT = 30


rates = {}
neighbors = {}
for line in arr:
    node, rate = line.split(' ')[1], int(line.split(' ')[4].split('=')[-1][:-1])
    get_neighbors = line.split('valve')[-1].split(' ')[1:]
    get_neighbors = [neighbor.strip(',') for neighbor in get_neighbors]

    rates[node] = rate
    neighbors[node] = get_neighbors

total = 0
count = 0
bestCase = sorted(rates, key=rates.get)
for  k in bestCase[::-1]:
    total += rates[k]
    print(rates[k])
    if rates[k] != 0:
        count += 1
print(total, count)

def isRidiculous(path, bestFound):
    remaining_steps = 30 - len(path)
    #if currentRateAt30(path) + remaining_steps*total < bestFound:
        #return True
    return False

def isSilly(path):
    lastItem = path[-1]
    for item in path[::-1][1:]:
        if item == 'OPEN':
            return False
        if item == lastItem:
            return True
    return False
        

def getOpens(currentPath):
    open = {}
    currentLocation = 'AA'
    for c in currentPath:
        if c == 'OPEN':
            open[currentLocation] = 0
        else:
            currentLocation = c
    return open.keys()


def getPossibleNextSteps(current_location, current_path):
    possibleNextSteps = []
    if current_location not in getOpens(current_path):
        possibleNextSteps.append("OPEN")
    for neighbor in neighbors[current_location]:
        possibleNextSteps.append(neighbor)
    return possibleNextSteps

def incrementOpen(open):
    for key in open:
        open[key] += 1
    return open

def calculateTotalPressure(open):
    total = 0
    for key in open:
        time = open[key]
        rate = rates[key]
        total += time*rate
    return total
    

def calculateSolution(currentPath):
    open = {}
    # we have 30 items here
    currentLocation = 'AA'
    for c in currentPath:
        open = incrementOpen(open)
        if c == 'OPEN':
            open[currentLocation] = 0
        else:
            currentLocation = c
    return calculateTotalPressure(open)

def dynamicProgramming(currentPath, time):
    if isDumb(currentPath):
        return -5000
    if time == TIME_LIMIT:
        return calculateSolution(currentPath)
    else:
        current_location = currentPath[-1] if currentPath[-1] != 'OPEN' else currentPath[-2]
        possibleNextSteps = getPossibleNextSteps(current_location, currentPath)
        best_answer = 0
        for step in possibleNextSteps:
            ans = dynamicProgramming(currentPath+[step], time+1)
            if ans > best_answer:
                best_answer = ans
        return best_answer

# print(dynamicProgramming(['AA'], 0))
    
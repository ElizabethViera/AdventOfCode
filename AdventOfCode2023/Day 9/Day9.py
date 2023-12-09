fileContents = open("AdventOfCode2023/Day 9/input.txt")
arr = fileContents.read().split("\n")

def onlyZerosIn(listONumbers):
    for i in listONumbers:
        if i != 0:
            return False
    return True

def oasisRecurse(listONumbers):
    if onlyZerosIn(listONumbers):
        return listONumbers[-1]
    else:
        prev = listONumbers[0]
        nextLevel = []
        for i in listONumbers[1:]:
            nextLevel.append(i - prev)
            prev = i
        return oasisRecurse(nextLevel) + listONumbers[-1]

results = []
for line in arr:
    line = [int(x) for x in line.split(' ')][::-1]
    results.append(oasisRecurse(line))
print(len(results))
print(sum(results))

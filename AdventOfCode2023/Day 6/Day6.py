fileContents = open("AdventOfCode2023/Day 6/input.txt")
arr = fileContents.read().split("\n")


Times = [int(x) for x in arr[0].split()[1:]]
Distances = [int(x) for x in arr[1].split()[1:]]


def getDistanceFromHeldAmount(amount, totalTime):
    timeForDistance = totalTime - amount
    return timeForDistance*amount

totals = []
for race in range(len(Times)):
    time = Times[race]
    distance = Distances[race]
    permutations = 0
    for i in range(distance//time, time):
        if getDistanceFromHeldAmount(i, time) > distance:
            permutations += 1
    totals.append(permutations)

begin = 1

for total in totals:
    begin *= total

print(begin)


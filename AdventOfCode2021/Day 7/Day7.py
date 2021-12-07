from collections import defaultdict
fileContents = open("Day 7/input.txt")
arr = fileContents.read().split(',')
arr = [int(x) for x in arr]

print(arr)

minRange = 10000000000000
answer = -1
for i in range(0, 2600):
    totalRange = 0
    for crab in arr:
        totalRange += sum(range(abs(crab - i)+1))
        # print(totalRange)
    if totalRange < minRange:
        minRange = totalRange
        answer = i
print(minRange, answer)

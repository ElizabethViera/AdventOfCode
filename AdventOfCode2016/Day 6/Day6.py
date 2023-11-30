fileContents = open("AdventOfCode2016/Day 6/input.txt")
arr = fileContents.read().split("\n")

lettersDict = dict()

for line in arr:
    for c in range(len(line)):
        if c not in lettersDict:
            lettersDict[c] = dict()
        if line[c] not in lettersDict[c]:
            lettersDict[c][line[c]] = 0
        lettersDict[c][line[c]] += 1
print(len(lettersDict))

result = ''
for i in range(len(lettersDict)):
    resultsAtIndex = lettersDict[i]
    result += sorted(resultsAtIndex.items(), key=lambda x:x[1])[0][0]
print(result)
from typing import Iterable


fileContents = open("AdventOfCode2023/Day 11/input.txt")
arr = fileContents.read().split("\n")

def hasOnly(line: Iterable[str], char: str):
    for c in line:
        if c != char and c != '*':
            return False
    return True

doubledGridStr: list[str] = []

for row in arr:
    if hasOnly(row, '.'):
        doubledGridStr.append(row.replace('.', '*'))
    else:
        doubledGridStr.append(row)

doubledGrid = [[row[i] for row in doubledGridStr] for i in range(len(doubledGridStr[0]))]

doubledGrid2 = []

for row in doubledGrid:
    if hasOnly(row, '.'):
        doubledGrid2.append(['*' for i in row])
    else:
        doubledGrid2.append(row)

doubledGrid = [[row[i] for row in doubledGrid2] for i in range(len(doubledGrid2[0]))]

hashtags = []

for i, row in enumerate(doubledGrid):
    for j, c in enumerate(row):
        if doubledGrid[i][j] == '#':
            hashtags.append((i,j))
print(len(hashtags))

def countStars(one, two):
    stars = 0
    for i in range(one[0], two[0]):
        if doubledGrid[i][one[1]] == '*':
            stars += 1
    for i in range(two[0], one[0]):
        if doubledGrid[i][one[1]] == '*':
            stars += 1
    for i in range(one[1], two[1]):
        if doubledGrid[one[0]][i] == '*':
            stars += 1
    for i in range(two[1], one[1]):
        if doubledGrid[one[0]][i] == '*':
            stars += 1
    return stars


def getDistance(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1]) + (1000000-1)*countStars(one,two)

sum = 0

for i in range(len(hashtags)):
    for j in range(i, len(hashtags)):
        if i != j:
            hashtag1 = hashtags[i]
            hashtag2 = hashtags[j]
            sum += getDistance(hashtag1, hashtag2)

print(sum)
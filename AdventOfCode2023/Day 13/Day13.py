fileContents = open("AdventOfCode2023/Day 13/input.txt")
allInput = fileContents.read().split("\n\n")

total = 0

def processBlock(a, oldResult=None):
    for i in range(1, len(a)):
        mirrorSize = min(i, len(a)-i)
        if mirrorSize == i:
            leftHalf = a[:i]
            rightHalf = a[i:2*i]
        else:
            leftHalf = a[i-mirrorSize:i]
            rightHalf = a[i:]
        if leftHalf == rightHalf[::-1] and i*100 != oldResult:
            return i*100

    transposedArr = [[row[i] for row in a] for i in range(len(a[0]))]

    for i in range(1, len(transposedArr)):
        mirrorSize = min(i, len(transposedArr)-i)
        if mirrorSize == i:
            leftHalf = transposedArr[:i]
            rightHalf = transposedArr[i:2*i]
        else:
            leftHalf = transposedArr[i-mirrorSize:i]
            rightHalf = transposedArr[i:]
        if leftHalf == rightHalf[::-1] and i != oldResult:
            return i
    return -1

import copy

def replaceInBlocks(b) -> int:
    oldResult = processBlock(b)
    for i in range(len(b)):
        for c in range(len(b[i])):
            copyOfArr = copy.deepcopy(b)
            if b[i][c] == '#':
                copyOfArr[i] = copyOfArr[i][:c] + '.' + copyOfArr[i][c+1:]
            else:
                copyOfArr[i] = copyOfArr[i][:c] + '#' + copyOfArr[i][c+1:]
            result = processBlock(copyOfArr, oldResult)
            if  result != -1:
                return result
    return 0

n = 0
for thisBlock in allInput:
    n+=1
    print("processed", n)
    arr = thisBlock.split('\n')
    total += replaceInBlocks(arr)
    

    
print(total)
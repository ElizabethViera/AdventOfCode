fileContents = open("AdventOfCode2023/Day 13/input.txt")
allInput = fileContents.read().split("\n\n")

total = 0

for thisBlock in allInput:
    arr = thisBlock.split('\n')
    for i in range(1, len(arr)):
        mirrorSize = min(i, len(arr)-i)
        if mirrorSize == i:
            leftHalf = arr[:i]
            rightHalf = arr[i:2*i]
        else:
            leftHalf = arr[i-mirrorSize:i]
            rightHalf = arr[i:]
        if leftHalf == rightHalf[::-1]:
            total += i*100

    transposedArr = [[row[i] for row in arr] for i in range(len(arr[0]))]

    for i in range(1, len(transposedArr)):
        mirrorSize = min(i, len(transposedArr)-i)
        if mirrorSize == i:
            leftHalf = transposedArr[:i]
            rightHalf = transposedArr[i:2*i]
        else:
            leftHalf = transposedArr[i-mirrorSize:i]
            rightHalf = transposedArr[i:]
        if leftHalf == rightHalf[::-1]:
            total += i
print(total)
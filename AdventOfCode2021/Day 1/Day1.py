fileContents = open("AdventOfCode2021/Day 1/input.txt")
arr = fileContents.read().split('\n')
arr = [int(i) for i in arr]
print(arr)

result = 0
previous0 = arr[0]
previous1 = arr[1]
previous2 = arr[2]
sumOfprevious = previous0 + previous1 + previous2

for i in range(2, len(arr)):
    newSum = sumOfprevious - arr[i-3] + arr[i]
    if newSum > sumOfprevious:
        result += 1
    sumOfprevious = newSum
print(result)

fileContents = open("AdventOfCode2015/Day 1/input.txt")
arr = fileContents.read().split('\n')
result = 0
print(len(arr[0]))
for floor, c in enumerate(arr[0]):
    if result == -1:
        print(floor)
        break
    if c == '(':
        result += 1
    else:
        result -= 1
print(result)

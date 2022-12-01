fileContents = open("AdventOfCode2015/Day 8/input.txt")
outputContents = open("AdventOfCode2015/Day 8/output.txt", "a")

arr = fileContents.read().split('\n')

total_length_result = 6310
result = 0
for line in arr:
    result += len(line)+2
print(result - total_length_result)
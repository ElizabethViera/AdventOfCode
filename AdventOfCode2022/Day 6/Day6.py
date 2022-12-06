fileContents = open("AdventOfCode2022/Day 6/input.txt")
arr = list(fileContents.read())

seen = []
for i,c in enumerate(arr):
    seen.append(c)
    if len(seen) == 15:
        seen = seen[1:]
    if len(set(seen)) == 14:
        print(i)
        print(seen)
        break
fileContents = open("AdventOfCode2022/Day 3/input")
arr = fileContents.read().split('\n')

new_arr = []
arr_item = ""
count = 0

results = ""
for index, line in enumerate(arr):
    if index%3 == 0:
        set1 = set(line)
    if index%3 == 1:
        set2 = set(line)
    if index%3 == 2:
        set3 = set(line)
        for c in set3:
            if c in set1 and c in set2:
                results += c


total = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in results:
    total += letters.index(char) + 1

print(total)

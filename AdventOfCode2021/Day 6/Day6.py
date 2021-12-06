from collections import defaultdict
fileContents = open("Day 6/input.txt")
arr = fileContents.read().split(',')
arr = [int(x) for x in arr]

fishAges = dict()
for fishAge in arr:
    if fishAge not in fishAges:
        fishAges[fishAge] = 0
    fishAges[fishAge] += 1
print(fishAges)


def default_zero():
    return 0


for i in range(256):
    newFishAges = defaultdict(default_zero)
    for age in fishAges:
        newAge = age-1
        if newAge < 0:
            newAge = 6
            newFishAges[8] += fishAges[age]
        newFishAges[newAge] += fishAges[age]
    fishAges = newFishAges
print(fishAges)

result = 0
for resultAge in fishAges:
    result += fishAges[resultAge]
print(result)

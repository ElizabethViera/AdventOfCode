fileContents = open("AdventOfCode2023/Day 8/input.txt")
arr = fileContents.read().split("\n")

sample_lrlrlr = "RL"
lrlrlrlr = "This is where my lefts and rights go"

print(len(lrlrlrlr))
dirs = dict()
for direction in arr:
    key, L, R = direction.split(" ")[0], direction.split(" ")[2][1:-1], direction.split(" ")[3][:-1]
    #print(key, L, R)
    dirs[key] = dict()
    dirs[key]["L"] = L
    dirs[key]["R"] = R
    if key.endswith('A'):
        print(key)

count = 0
current_keys = [
    # 'DFA', 
    #'BLA', 
    'TGA',
    # 'AAA', 
    # 'PQA', 
    # 'CQA', 
]

lcms = [
    # This is where I put all the cycles for each key
    ]

import math

result = 1
for i in lcms:
    result = math.lcm(result, i)
print(result, "is the result")


def notDoneYet(k:list[str], count):
    # use this to get the cycle numbers in the above array
    for key in k:
        if key.endswith("Z"):
            print(count)
            return True
    if count < 1000000:
        return True
    return False

while notDoneYet(current_keys, count):
    new_current_keys = []
    for key in current_keys:
        new_current_keys.append(dirs[key][lrlrlrlr[count%len(lrlrlrlr)]])
    current_keys = new_current_keys
    count += 1


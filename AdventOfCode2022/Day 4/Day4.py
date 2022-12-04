fileContents = open("AdventOfCode2022/Day 4/input.txt")
arr = fileContents.read().split('\n')

total = 0
for line in arr:
    line_0 = line.split(',')
    left, right = line_0[0].split('-'), line_0[1].split('-')
    left, right = [int(x) for x in left], [int(x) for x in right]
    left, right = sorted([left,right])[0], sorted([left,right])[1]
    if right[0] == left[0] or right[1] == left[1]:
        total += 1
    # we know left[0] < right[0], so if 
    elif left[1] >= right[0]:
        total += 1
   
    
print(total)
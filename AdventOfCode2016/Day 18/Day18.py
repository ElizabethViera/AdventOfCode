fileContents = open("AdventOfCode2016/Day 18/input.txt")
line = fileContents.read()


traps = dict()

traps[0] = line

def getNewItem(left, center, right) -> str :
    if left == '^' and center == '^' and right == '.':
        new_item = '^'
    elif left == '.' and center == '^' and right == '^':
        new_item = '^'
    elif left == '^' and center == '.' and right == '.':
        new_item = '^'
    elif left == '.' and center == '.' and right == '^':
        new_item = '^'
    else:
        new_item = '.'
    return new_item

for i in range(1,400000):
    traps[i] = []
    for c in range(len(line)):
        if c == 0:
            left = '.'
        else:
            left = traps[i-1][c-1]
        center = traps[i-1][c]
        if c == len(line)-1:
            right = '.'
        else:
            right = traps[i-1][c+1]
        traps[i].append(getNewItem(left,center,right))
count = 0
for r in traps:
    count += len([i for i in traps[r] if i == '.'])
print(count)
        
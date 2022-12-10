fileContents = open("AdventOfCode2022/Day 10/input.txt")
arr = fileContents.read().split("\n")

def checkCycle():
    current = cycle%40
    if (register-1 == current 
        or register == current 
        or register+1 == current):
        print('#', end='')
    else:
        print('.', end='')
    if current == 0:
        print('')

def drawGrid():
    for row in range(6):
        for col in range(40):
            print('.', end='')
        print('')

# drawGrid()
cycle = 0
register = 1
for line in arr:
    #Cycle Begins
    cycle += 1
    if line.startswith('addx'):
        total = checkCycle()
        cycle += 1 
        register += int(line.split(' ')[-1])
        total = checkCycle()
    else:
        # noOp
        total = checkCycle()



fileContents = open("AdventOfCode2019/Day 2/input.txt")
arr = fileContents.read().split(",")

instructions = dict()
for i, v in enumerate(arr):
    instructions[i] = int(v)

def intCode(ins, input, output):
    current_value = 0
    while ins[current_value] != 99 :
        if ins[current_value] == 1:
            left = ins[ins[current_value+1]]
            right = ins[ins[current_value+2]]
            target = ins[current_value+3]
            ins[target] = left+right
            current_value += 4
        if ins[current_value] == 2:
            left = ins[ins[current_value+1]]
            right = ins[ins[current_value+2]]
            target = ins[current_value+3]
            ins[target] = left*right
            current_value += 4
        if ins[current_value] == 3:
            # input
            target = ins[current_value+1]
            ins[target] = input()
            current_value += 2
        if ins[current_value] == 3:
            # input
            readfrom = ins[current_value+1]
            output(readfrom)
            current_value += 2
        

    return ins


def getInput(n):

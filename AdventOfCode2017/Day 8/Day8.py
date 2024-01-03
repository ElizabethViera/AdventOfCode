from dis import Instruction


fileContents = open("AdventOfCode2017/Day 8/input.txt")
arr = fileContents.read().split('\n')

registers = dict()
instructions = dict()
for e,ins in enumerate(arr):
    register = ins.split(' ')[0]
    if register not in registers:
        registers[register] = 0
    inc = ins.split(' ')[1] == 'inc'
    amount = int(ins.split(' ')[2])
    condition = ins.split(' ')[4:]
    left, c, right = condition[0], condition[1], int(condition[2])
    if left not in registers:
        registers[left] = 0
    instructions[e] = (left, c, right, register, inc, amount)


def compare(left, c, right)-> bool:
    match c:
        case '<':
            return left < right    
        case '<=':
            return left <= right
        case '>':
            return left > right
        case '>=':
            return left >= right
        case '==':
            return left == right
        case '!=':
            return left != right
    raise ValueError
biggest = 0
for i in range(len(instructions)):
    if compare(registers[instructions[i][0]], instructions[i][1], instructions[i][2]):
        if instructions[i][4]:
            registers[instructions[i][3]] += instructions[i][5]
        else:
            registers[instructions[i][3]] -= instructions[i][5]
        for register in registers:
            if registers[register] > biggest:
                biggest = registers[register]



print(biggest)
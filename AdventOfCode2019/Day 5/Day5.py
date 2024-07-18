def runIntCode(program, input):
    registers = dict()
    for i, val in enumerate(program):
        registers[i] = val
    
    index = 0
    while True:
        opcode, parameters = readIns(registers[index])
        match opcode:
            case 1:
                while len(parameters) < 3:
                    parameters.append(0)
                # adds
                left = index + 1 if parameters[0] else registers[index + 1]
                right = index + 2 if parameters[1] else registers[index + 2]
                result = index + 3 if parameters[2] else registers[index + 3]
                registers[result] = registers[left] + registers[right]
                index += 4
            case 2:
                while len(parameters) < 3:
                    parameters.append(0)
                # multiplies
                left = index + 1 if parameters[0] else registers[index + 1]
                right = index + 2 if parameters[1] else registers[index + 2]
                result = index + 3 if parameters[2] else registers[index + 3]
                registers[result] = registers[left] * registers[right]
                index += 4
            case 3:
                while len(parameters) < 1:
                    parameters.append(0)
                result = index + 1 if parameters[0] else registers[index + 1]
                registers[result] = input.pop(0)
                index += 2
            case 4:
                while len(parameters) < 1:
                    parameters.append(0)
                result = index + 1 if parameters[0] else registers[index + 1]
                return(registers[result])
            case 5:
                # jump if true
                while len(parameters) < 2:
                    parameters.append(0)
                left = index + 1 if parameters[0] else registers[index + 1]
                right = index + 2 if parameters[1] else registers[index + 2]
                if registers[left] != 0:
                    index = registers[right]
                else:
                    index += 3
            case 6:
                # jump if false
                while len(parameters) < 2:
                    parameters.append(0)
                left = index + 1 if parameters[0] else registers[index + 1]
                right = index + 2 if parameters[1] else registers[index + 2]
                if registers[left] == 0:
                    index = registers[right]
                else:
                    index += 3
            case 7:
                # less than
                while len(parameters) < 3:
                    parameters.append(0)
                # adds
                left = index + 1 if parameters[0] else registers[index + 1]
                right = index + 2 if parameters[1] else registers[index + 2]
                result = index + 3 if parameters[2] else registers[index + 3]
                if registers[left] < registers[right]:
                    registers[result] = 1
                else:
                    registers[result] = 0
                index += 4
            case 8:
                # less than
                while len(parameters) < 3:
                    parameters.append(0)
                # adds
                left = index + 1 if parameters[0] else registers[index + 1]
                right = index + 2 if parameters[1] else registers[index + 2]
                result = index + 3 if parameters[2] else registers[index + 3]
                if registers[left] == registers[right]:
                    registers[result] = 1
                else:
                    registers[result] = 0
                index += 4
            case 99:
                return registers
            

def readIns(instruction):
    instruction = str(instruction)
    if len(instruction) < 2:
        return int(instruction[-1]), []
    opcode = int(instruction[-2] + instruction[-1])
    parameters = list(instruction[:-2])[::-1]
    return opcode, [int(x) for x in parameters]

fileContents = open("AdventOfCode2019/Day 5/input.txt")
program = fileContents.read().split(",")
program = [int(x) for x in program]

import itertools

max_output = 0

all_combos = itertools.permutations([0, 1, 2, 3, 4])
for combo in all_combos:
    output = 0
    for i in combo:
        fresh_program = program
        input = [i, output]
        output = runIntCode(fresh_program, input)
    if output > max_output:
        max_output = output
print(max_output)

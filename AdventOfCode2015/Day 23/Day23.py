storage = {'a': 1, 'b': 0}


fileContents = open("AdventOfCode2015/Day 23/input.txt")
instructions = fileContents.read().split("\n")

nextInstruction = 0

while(True):
    if nextInstruction >= len(instructions):
        break
    instruction = instructions[nextInstruction].split(' ')
    #if nextInstruction == 41:
        #print('hi')
        # print(nextInstruction, instruction)
    match instruction[0]:
        case 'hlf':
            storage[instruction[1]] //= 2
            nextInstruction += 1
        case 'tpl':
            storage[instruction[1]] *= 3
            nextInstruction += 1
        case 'inc':
            storage[instruction[1]] += 1
            nextInstruction += 1
        case 'jmp':
            nextInstruction += int(instruction[1])
        case 'jie':
            if storage['a']%2 == 0:
                nextInstruction += int(instruction[2])
                print(storage['a'])
            else:
                nextInstruction += 1
        case 'jio':
            if storage['a'] == 1:
                nextInstruction += int(instruction[2])
                print(storage['a'])
            else:
                nextInstruction += 1
        case other:
            break

print(storage['a'], storage['b'])
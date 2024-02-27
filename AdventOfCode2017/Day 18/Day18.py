fileContents = open("AdventOfCode2017/Day 18/input.txt")
arr = fileContents.read().split('\n')

answer = None
registers = dict()
registers['p'] = 0
registers['i'] = 0
registers['a'] = 0
registers['b'] = 0
registers['f'] = 0

instructions = dict()

instruct = 0

for i, c in enumerate(arr):
    instructions[i] = c

while instruct in instructions:
    ins = instructions[instruct]
    print(ins)
    if ins.startswith('snd'):
        if ins.split(' ')[1] in registers:
            answer = registers[ins.split(' ')[1]]
        else:
            answer = ins.split(' ')[1]
    elif ins.startswith('set'):
        x,y = ins.split(' ')[1], ins.split(' ')[2]
        if y in registers:
            y = registers[y]
        registers[x] = int(y)
    elif ins.startswith('add'):
        x,y = ins.split(' ')[1], ins.split(' ')[2]
        if y in registers:
            y = registers[y]
        y = int(y)
        registers[x] += y
    elif ins.startswith('mul'):
        x,y = ins.split(' ')[1], ins.split(' ')[2]
        if y in registers:
            y = registers[y]
        y = int(y)
        registers[x] = registers[x]*y
    elif ins.startswith('mod'):
        x,y = ins.split(' ')[1], ins.split(' ')[2]
        if y in registers:
            y = registers[y]
        y = int(y)
        registers[x] = registers[x]%y
    elif ins.startswith('rcv'):
        x = ins.split(' ')[1]
        if x in registers:
            x = registers[x]
        if x != 0:
            print(answer)
            break
    elif ins.startswith('jgz'):
        x = ins.split(' ')[1]
        if x in registers:
            x = registers[x]
        x = int(x)
        if x > 0:
            instruct += int(ins.split(' ')[2])-1
    instruct += 1
print(registers)
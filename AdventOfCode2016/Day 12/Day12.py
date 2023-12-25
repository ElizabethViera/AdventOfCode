assembunny_registers = dict()
assembunny_registers['a'] = 0
assembunny_registers['b'] = 0
assembunny_registers['c'] = 1
assembunny_registers['d'] = 0

def do_assembunny(instruct:str):
    if instruct.startswith('inc'):
        assembunny_registers[instruct.split(' ')[1]] += 1
        return 1
    if instruct.startswith('dec'):
        assembunny_registers[instruct.split(' ')[1]] -= 1
        return 1
    if instruct.startswith('cpy'):
        source = instruct.split(' ')[1]
        target = instruct.split(' ')[2]
        if source in assembunny_registers:
            source = assembunny_registers[source]
        assembunny_registers[target] = int(source)
        return 1
    if instruct.startswith('jnz'):
        source = instruct.split(' ')[1]
        target = int(instruct.split(' ')[2])
        if source in assembunny_registers:
            source = assembunny_registers[source]
        if source != 0:
            return target
        else:
            return 1
    raise(ValueError)


fileContents = open("AdventOfCode2016/Day 12/input.txt")
lines = fileContents.read().split("\n")

ins = dict()
for i,line in enumerate(lines):
    ins[i] = line

current_ins = 0
while current_ins in ins:
    current_ins += do_assembunny(ins[current_ins])
print(assembunny_registers['a'])
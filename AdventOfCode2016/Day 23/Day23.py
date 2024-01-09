assembunny_registers = dict()
assembunny_registers['a'] = 12
assembunny_registers['b'] = 0
assembunny_registers['c'] = 0
assembunny_registers['d'] = 0

def toggle(inst):
    print('toggle')
    if inst.startswith('inc'):
        return 'dec' + inst[3:]
    if inst.startswith('dec'):
        return 'inc' + inst[3:]
    if inst.startswith('cpy'):
        return 'jnz' + inst[3:]
    if inst.startswith('jnz'):
        return 'cpy' + inst[3:]
    if inst.startswith('tgl'):
        return 'inc' + inst[3:]
    
def do_assembunny(instruct:str, current_ins):
    print(instruct)
    if instruct == 'nop':
        return 1
    if instruct.startswith('muladd'):
        source = instruct.split(' ')[1]
        source2 = instruct.split(' ')[2]
        target = instruct.split(' ')[3]
        assembunny_registers[target] += assembunny_registers[source]*assembunny_registers[source2]
        return 1
    if instruct.startswith('add'):
        source = instruct.split(' ')[1]
        target = instruct.split(' ')[2]
        assembunny_registers[target] += assembunny_registers[source]
        return 1
    if instruct.startswith('adz'):
        source = instruct.split(' ')[1]
        target = instruct.split(' ')[2]
        assembunny_registers[source] += assembunny_registers[target]
        assembunny_registers[target] = 0
        return 1
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
        if target in assembunny_registers:
            assembunny_registers[target] = int(source)
        return 1
    if instruct.startswith('jnz'):
        source = instruct.split(' ')[1]
        target = instruct.split(' ')[2]
        if source in assembunny_registers:
            source = assembunny_registers[source]
        else:
            source = int(source)
        if target in assembunny_registers:
            target = assembunny_registers[target]
        else:
            target = int(target)
        if source != 0:
            return target
        else:
            return 1
    if instruct.startswith('tgl'):
        target = instruct.split(' ')[1]
        if target in assembunny_registers:
            target = assembunny_registers[target]
        else:
            target = int(target)
        if current_ins+target not in ins:
            return 1
        ins[current_ins+target] = toggle(ins[current_ins+target])
        return 1
    raise(ValueError)


fileContents = open("AdventOfCode2016/Day 23/input.txt")
lines = fileContents.read().split("\n")

ins = dict()
for i,line in enumerate(lines):
    ins[i] = line


current_ins = 0
while current_ins in ins:
    #print(ins[current_ins], assembunny_registers, ins)
    current_ins += do_assembunny(ins[current_ins], current_ins)
print(assembunny_registers['a'])
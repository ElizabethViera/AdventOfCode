assembunny_registers = dict()

def do_assembunny(instruct:str, result: str) -> tuple[int, str]:
    if instruct.startswith('add'):
        source = instruct.split(' ')[1]
        target = instruct.split(' ')[2]
        assembunny_registers[source] += int(target)
        return (1, result)
    if instruct.startswith('nop'):
        return (1, result)
    if instruct.startswith('inc'):
        assembunny_registers[instruct.split(' ')[1]] += 1
        return (1, result)
    if instruct.startswith('dec'):
        assembunny_registers[instruct.split(' ')[1]] -= 1
        return (1, result)
    if instruct.startswith('cpy'):
        source = instruct.split(' ')[1]
        target = instruct.split(' ')[2]
        if source in assembunny_registers:
            source = assembunny_registers[source]
        assembunny_registers[target] = int(source)
        return (1, result)
    if instruct.startswith('jnz'):
        source = instruct.split(' ')[1]
        target = int(instruct.split(' ')[2])
        if source in assembunny_registers:
            source = assembunny_registers[source]
        if int(source) != 0:
            return (target,result)
        else:
            return (1, result)
    if instruct.startswith('out'):
        source = source = instruct.split(' ')[1]
        if source in assembunny_registers:
            source = assembunny_registers[source] 
        result += str(source)
        return (1, result)
    raise(ValueError)


fileContents = open("AdventOfCode2016/Day 25/input.txt")
lines = fileContents.read().split("\n")

ins = dict()
for i,line in enumerate(lines):
    ins[i] = line

for i in range(100000):
    if i%10 == 0:
        print(i)
    assembunny_registers['a'] = i
    assembunny_registers['b'] = 0
    assembunny_registers['c'] = 0
    assembunny_registers['d'] = 0

    result = ''
    current_ins = 0
    while current_ins in ins and len(result) < 30:
        next_ins, result = do_assembunny(ins[current_ins], result)
        current_ins += next_ins
        if result == '010101010101010101010101':
            print(i)
            raise(ValueError)

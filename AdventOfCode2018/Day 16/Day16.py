from copy import deepcopy


def addr(a,b,r,init):
    init[r] = init[a] + init[b]
    return init

def addi(a,b,r,init):
    init[r] = init[a] + b
    return init

def mulr(a,b,r,init):
    init[r] = init[a] * init[b]
    return init

def muli(a,b,r,init):
    init[r] = init[a] * b
    return init

def banr(a,b,r,init):
    init[r] = init[a] & init[b]
    return init

def bani(a,b,r,init):
    init[r] = init[a] & b
    return init

def borr(a,b,r,init):
    init[r] = init[a] | init[b]
    return init

def bori(a,b,r,init):
    init[r] = init[a] | b
    return init

def setr(a,b,r,init):
    init[r] = init[a]
    return init

def seti(a,b,r,init):
    init[r] = a
    return init

def gtir(a,b,r,init):
    if a > init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init

def gtri(a,b,r,init):
    if init[a] > b:
        init[r] = 1
    else:
        init[r] = 0
    return init

def gtrr(a,b,r,init):
    if init[a] > init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init

def eqir(a,b,r,init):
    if a == init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init

def eqri(a,b,r,init):
    if init[a] == b:
        init[r] = 1
    else:
        init[r] = 0
    return init

def eqrr(a,b,r,init):
    if init[a] == init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init

all_functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

function_map = dict()

fileContents = open("AdventOfCode2018/Day 16/input.txt")
cases = fileContents.read().split("\n\n")

total = 0
for case in cases:
    init = case.split('\n')[0][:-1].split(': [')[1].split(', ')
    init = [int(x) for x in init]

    program = case.split('\n')[1]
    program_contents = [int(x) for x in program.split(' ')]
    p,a,b,r = program_contents[0], program_contents[1], program_contents[2], program_contents[3]

    result = case.split('\n')[2][:-1].split('[')[1].split(', ')
    result = [int(x) for x in result]

    count = 0
    for f in all_functions:
        copy = deepcopy(init)
        if f(a,b,r,copy) == result:
            count += 1
            resulting_f = f
    if count == 1:
        function_map[p] = resulting_f
        all_functions.remove(resulting_f)

programContents = open("AdventOfCode2018/Day 16/program.txt")
program = programContents.read().split("\n")

state = [0, 0, 0, 0]

for ins in program:
    print(ins)
    instructions = [int(x) for x in ins.split(' ')]
    p,a,b,r = instructions[0], instructions[1], instructions[2], instructions[3]
    f = function_map[p]
    state = f(a,b,r, state)

print(state)



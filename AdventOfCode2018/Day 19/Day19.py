from copy import deepcopy


def addr(a, b, r, init):
    init[r] = init[a] + init[b]
    return init


def addi(a, b, r, init):
    init[r] = init[a] + b
    return init


def mulr(a, b, r, init):
    init[r] = init[a] * init[b]
    return init


def muli(a, b, r, init):
    init[r] = init[a] * b
    return init


def banr(a, b, r, init):
    init[r] = init[a] & init[b]
    return init


def bani(a, b, r, init):
    init[r] = init[a] & b
    return init


def borr(a, b, r, init):
    init[r] = init[a] | init[b]
    return init


def bori(a, b, r, init):
    init[r] = init[a] | b
    return init


def setr(a, b, r, init):
    init[r] = init[a]
    return init


def seti(a, b, r, init):
    init[r] = a
    return init


def gtir(a, b, r, init):
    if a > init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init


def gtri(a, b, r, init):
    if init[a] > b:
        init[r] = 1
    else:
        init[r] = 0
    return init


def gtrr(a, b, r, init):
    if init[a] > init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init


def eqir(a, b, r, init):
    if a == init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init


def eqri(a, b, r, init):
    if init[a] == b:
        init[r] = 1
    else:
        init[r] = 0
    return init


def eqrr(a, b, r, init):
    if init[a] == init[b]:
        init[r] = 1
    else:
        init[r] = 0
    return init


all_functions = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
}


fileContents = open("AdventOfCode2018/Day 19/input.txt")
arr = fileContents.read().split("\n")


program: dict[int, list[str | int]] = dict()
for i, line in enumerate(arr):
    p, a, b, r = line.split()
    a, b, r = int(a), int(b), int(r)
    program[i] = [p, a, b, r]

state = [1, 0, 0, 10551355, 0, 0]
ip = 2

counter = None

startPrinting = 40

while True:
    startPrinting -= 1
    if startPrinting < 0:
        break
    # for ins in program:
    if state[ip] not in program:
        break
    ins = program[state[ip]]
    print(ins, state)
    p, a, b, r = ins[0], ins[1], ins[2], ins[3]
    p = str(p)
    f = all_functions[p]
    state = f(a, b, r, state)
    state[ip] += 1

print(state)

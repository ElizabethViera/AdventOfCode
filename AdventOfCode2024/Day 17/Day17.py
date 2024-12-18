def combo(n):
    if n < 4:
        return n
    if n == 4:
        return registers["A"]
    if n == 5:
        return registers["B"]
    if n == 6:
        return registers["C"]
    if n == 7:
        raise (ValueError)
    else:
        raise (ValueError)


def adivision(n):
    global instruction
    numerator = registers["A"]
    denominator = 2 ** (combo(n))
    registers["A"] = numerator // denominator
    instruction += 2


def xorregb(n):
    global instruction
    registers["B"] = registers["B"] ^ n
    instruction += 2


def shortenregb(n):
    global instruction
    registers["B"] = combo(n) % 8
    instruction += 2


def jumpnotzero(n):
    global instruction
    if registers["A"] == 0:
        instruction += 2
    else:
        instruction = n


def bitwisexorBnC(n):
    global instruction
    registers["B"] = registers["B"] ^ registers["C"]
    instruction += 2


def out(n):
    global instruction
    instruction += 2
    return combo(n) % 8


def bdivision(n):
    global instruction
    numerator = registers["A"]
    denominator = 2 ** (combo(n))
    registers["B"] = numerator // denominator
    instruction += 2


def cdivision(n):
    global instruction
    numerator = registers["A"]
    denominator = 2 ** (combo(n))
    registers["C"] = numerator // denominator
    instruction += 2


functions = [
    adivision,
    xorregb,
    shortenregb,
    jumpnotzero,
    bitwisexorBnC,
    out,
    bdivision,
    cdivision,
]


def run_program(k, ins):
    global registers
    global instruction
    registers = dict()

    registers["A"] = k
    registers["B"] = 0
    registers["C"] = 0
    registers["output"] = []

    instruction = 0

    while instruction in range(len(ins)):
        f = functions[int(ins[instruction])]
        n = int(ins[instruction + 1])
        print(functions[int(ins[instruction])].__name__, n)
        result = f(n)
        if result is not None:
            registers["output"].append(result)
        if result == ins:
            return k
    print(registers["output"])
    return None


listsContents = open("AdventOfCode2024/Day 17/input.txt")
ins = listsContents.read().split(",")

run_program(240005441111111, ins)

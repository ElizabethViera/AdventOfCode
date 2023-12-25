fileContents = open("AdventOfCode2017/Day 7/input.txt")
lines = fileContents.read().split("\n")

program_pointers = dict()
program_weights = dict()

for line in lines:
    name = line.split(' ')[0]
    weight = int(line.split(' ')[1][1:-1])
    program_weights[name] = weight
    if len(line.split(' ')) > 2:
        subPrograms = line.split('-> ')[1].split(', ')
        program_pointers[name] = subPrograms

def getWeightOfProgram(p):
    total = program_weights[p]
    if p not in program_pointers:
        return total
    childWeights = []
    for child in program_pointers[p]:
        if p == 'jdxfsa':
            print(child, getWeightOfProgram(child))
        childWeights.append(getWeightOfProgram(child))
    if len(set(childWeights)) != 1:
        print(set(childWeights), childWeights, p)
    total += sum(childWeights)
    return total

getWeightOfProgram('fbgguv')
print(2548 - 3*228)


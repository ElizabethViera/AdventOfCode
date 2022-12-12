fileContents = open("AdventOfCode2022/Day 11/input.txt")
arr = fileContents.read().split("\n")
import math
# print(arr)

consts = [2, 17, 7, 11, 19, 5, 13, 3]
big_number = math.prod(consts)

def operate(operation, worryLevel):
    operand = operation.split(' ')[-2]
    value = int(operation.split(' ')[-1]) if operation.split(' ')[-1].isnumeric() else worryLevel
    if operand == '+':
        return worryLevel + value
    if operand == '*':
        return worryLevel * value

def testWorry(test, worryLevel):
    divisor = int(test.split(' ')[-1])
    return worryLevel%divisor == 0

def processMonkey(name):
    for item in monkeyList[name]['items']:
        monkeyList[name]['inspects'] += 1
        operation = monkeyList[name]['operation']
        newWorryLevel = operate(operation, item)
        newWorryLevel %= big_number
        test = monkeyList[name]['test']
        if testWorry(test, newWorryLevel):
            monkeyList[monkeyList[name]['true']]['items'].append(newWorryLevel)
        else:
            monkeyList[monkeyList[name]['false']]['items'].append(newWorryLevel)
    monkeyList[name]['items'] = []

monkeyList = {}
currentMonkey = {}
for index, line in enumerate(arr):
    if index%7 == 0:
        currentMonkey['number'] = line[7]
        currentMonkey['inspects'] = 0
    if index%7 == 1:
        currentMonkey['items'] = line.split(': ')[-1].split(', ')
        currentMonkey['items'] = [int(x) for x in currentMonkey['items']]
    if index%7 == 2:
        currentMonkey['operation'] = line.split(': ')[-1]
    if index%7 == 3:
        currentMonkey['test'] = line.split(': ')[-1]
    if index%7 == 4:
        currentMonkey['true'] = line.split(' ')[-1]
    if index%7 == 5:
        currentMonkey['false'] = line.split(' ')[-1]
    if index%7 == 6:
        monkeyList[currentMonkey['number']] = currentMonkey
        currentMonkey = {}


for i in range(10000):
    for monkey in monkeyList:
        processMonkey(monkey)

results = []
for monkey in monkeyList:    
    print(monkey)
    results.append(monkeyList[monkey]['inspects'])

print(sorted(results))

fileContents = open("AdventOfCode2018/Day 12/rules.txt")
rules = fileContents.read().split("\n")

rule_dict = dict()

for rule in rules:
    left, right = rule.split(' => ')
    rule_dict[left] = right

initial_state = 'this is where my input would go'
state = dict()
for i,c in enumerate(initial_state):
    state[i] = c

def updateState(s):
    newDict = dict()

    for k in range(-1000, 1000):
        this_string = ''
        for i in range(k-2, k+3):
            if i not in s:
                this_string += '.'
            else:
                this_string += s[i]
        if this_string in rule_dict:
            newDict[k] = rule_dict[this_string]
        else:
            newDict[k] = '.'
    return newDict

for i in range(50000000000):
    if i%500000000 == 0:
        print(i)
    state = updateState(state)

def scoreState(s):
    total = 0
    for k in s:
        if s[k] == '#':
            total += k
    return total
print(scoreState(state))

fileContents = open("AdventOfCode2018/Day 12/rules.txt")
rules = fileContents.read().split("\n")

rule_dict = dict()

for rule in rules:
    left, right = rule.split(' => ')
    rule_dict[left] = right

initial_state = '#..#####.#.#.##....####..##.#.#.##.##.#####..####.#.##.....#..#.#.#...###..#..###.##.#..##.#.#.....#'
state = dict()
for i,c in enumerate(initial_state):
    state[i] = c

def updateState(s):
    newDict = dict()
    keys = sorted(s.keys())
    for k in range(keys[0]-2, keys[-1]+2):
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


def scoreState(s):
    total = 0
    for k in s:
        if s[k] == '#':
            total += k
    return total

target = 10005

states_seen = dict()
for i in range(target+1):
    if i%1000 == 0:
        print(i)
    state = updateState(state)
    states_seen[i+1] = scoreState(state)

# print("made dict")

# for i in range(9400, 9500):
#         if states_seen[i+5] - states_seen[i] == states_seen[i+10] - states_seen[i+5]:
#             print(states_seen[i+5] - states_seen[i], i, states_seen[i])

    
'''
105 9494 199875
105 9495 199896
105 9496 199917
105 9497 199938
105 9498 199959
105 9499 199980
'''

example = 9495

print(states_seen[target], "should be: ")
print((105*(50000000000 - example)//5) + states_seen[example]) # 1050000000501
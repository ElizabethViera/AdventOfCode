fileContents = open("AdventOfCode2025/Day 6/input.txt")
arr = fileContents.read().split("\n")

problems = dict()

for i, line in enumerate(arr):
    for j, val in enumerate(line.split()):
        if j not in problems:
            problems[j] = []
        problems[j].append(val)

# print(problems)

total = 0
for problem in problems:
    print(problems[problem])
    operand = problems[problem][-1]
    ints = problems[problem][:-1]
    ints = [int(x) for x in ints]
    if operand == "+":
        total += sum(ints)
    else:
        local_total = 1
        for i in ints:
            local_total *= i
        total += local_total

print(total)

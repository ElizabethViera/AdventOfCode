fileContents = open("AdventOfCode2025/Day 6/input.txt")
arr = fileContents.read().split("\n")

stuff = dict()  # from column to item

for line in arr:
    for i, col in enumerate(line):
        if i not in stuff:
            stuff[i] = []
        stuff[i].append(col)


def mult(arr):
    t = 1
    for a in arr:
        t *= a
    return t


def createNum(arr):
    n = ""
    for i in arr:
        if i != " ":
            n += i
    return int(n)


def computeProblem(problem):  # array of arrays, one of the arrays will have an op
    nums = []
    # print("problem = ", problem)
    operand = None
    for item in problem:
        number = createNum(item[:-1])
        nums.append(number)
        if item[-1] != " ":
            operand = item[-1]
    # print(operand, nums)
    if operand == "+":
        return sum(nums)
    else:
        return mult(nums)


problem = []

total = 0
for k in stuff:
    if stuff[k] == [" ", " ", " ", " ", " "]:
        # problem end
        total += computeProblem(problem)
        problem = []
    else:
        problem.append(stuff[k])

total += computeProblem(problem)
print(total)

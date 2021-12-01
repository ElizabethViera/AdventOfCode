fileContents = open("Day 18/input")
arr = fileContents.read().split('\n')


def solveLeftToRight(math_arr):
    s = []
    for m in math_arr:
        if isinstance(m, int):
            s.append(m)
        if m in ['(', '+', '*']:
            s.append(m)
        if m == ')':
            number = s.pop()
            while len(s) >= 2 and s[-1] == '*':
                op = s.pop()
                num2 = s.pop()
                number = number * num2
            paren_throwaway = s.pop()
            s.append(number)
        if len(s) >= 3:
            if isinstance(s[-1], int) and s[-2] in ['+']:
                num = s.pop()
                op = s.pop()
                num2 = s.pop()
                s.append(num + num2 if op == '+' else num * num2)
    return s[0]


total = 0
for mathProblem in arr:
    mathProblem = mathProblem.replace("(", " ( ")
    mathProblem = mathProblem.replace(")", " ) ")
    mathProblem = [item for item in mathProblem.split(" ") if item != '']
    mathProblem = [
        int(item) if item in '0123456789' else item for item in mathProblem]
    # print(mathProblem)
    mathProblem = ['('] + mathProblem + [')']
    total += solveLeftToRight(mathProblem)
print(total)

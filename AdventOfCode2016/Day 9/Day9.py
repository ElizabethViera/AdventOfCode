def getIndexOfCloseParens(s,c) -> int:
    for i in range(c, len(s)):
        if s[i] == ')':
            return i
    raise(ValueError)


def getLength(s) -> int:
    total = 0
    c = 0
    while c < len(s):
        if s[c] != '(':
            total += 1
            c += 1
        elif s[c] == '(':
            next_c = getIndexOfCloseParens(s,c)
            markers = s[c+1:next_c].split('x')
            characters, numbers = int(markers[0]), int(markers[1])
            total += numbers*getLength(s[next_c+1:next_c+characters+1])
            c = next_c+characters+1
    return total

fileContents = open("AdventOfCode2016/Day 9/input.txt")
arr = fileContents.read()

print(getLength(arr))
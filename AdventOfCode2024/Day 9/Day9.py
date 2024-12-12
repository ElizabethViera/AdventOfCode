listsContents = open("AdventOfCode2024/Day 9/input.txt")
files = listsContents.read()

s = ""

characters = dict()

f = 65
for i, c in enumerate(files):
    n = int(c)
    if i % 2 == 0:
        s += chr(f) * n
        f += 1
    else:
        s += "." * n

s = list(s)

print(s)


i = len(s) - 1


result = 0

for i, c in enumerate(s):
    if c != ".":
        result += i * (ord(c) - 65)

print(result)

listsContents = open("AdventOfCode2024/Day 9/input.txt")
files = listsContents.read()

s = ""

f = 65
for i, c in enumerate(files):
    n = int(c)
    if i % 2 == 0:
        s += chr(f) * n
        f += 1
    else:
        s += "." * n

s = list(s)


def get_next_dot(s, i):
    while i < len(s) and s[i] != ".":
        i += 1
    # print(i, s[i])
    return i


def get_next_c(s, j):
    while j > 0 and s[j] == ".":
        j -= 1
    # print(j, s[j])
    return j


def swap(s, a, b):
    s[a], s[b] = s[b], s[a]
    return s


i = 0
j = len(s) - 1

while i < j:
    i, j = get_next_dot(s, i), get_next_c(s, j)
    if s[i] == "." and s[j] != "." and i < j:
        s = swap(s, i, j)


result = 0

for i, c in enumerate(s):
    if c != ".":
        result += i * (ord(c) - 65)

print(result)

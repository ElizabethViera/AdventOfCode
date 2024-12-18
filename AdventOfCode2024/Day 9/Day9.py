listsContents = open("AdventOfCode2024/Day 9/input.txt")
files = listsContents.read()

s = ""

characters = dict()
stack = []

f = 65
for i, c in enumerate(files):
    n = int(c)
    if i % 2 == 0:
        s += chr(f) * n
        stack.append((n, chr(f), len(s) - n))
        f += 1
    else:
        s += "." * n

s = list(s)

# print(stack)


def get_gap(l, leng):
    for i, item in enumerate(l):
        if item == ".":
            found = True
            for j in range(leng):
                if i + j >= len(l) or l[i + j] != ".":
                    found = False
                    break
            if found:
                return i
    return None


def reorder(l, st):
    st = st[::-1]
    for item in st:
        # print(item)
        length = item[0]
        gap = get_gap(l, length)
        if gap is not None and gap < item[2]:
            for i in range(length):
                l[gap + i] = item[1]
                l[item[2] + i] = "."
    return l


s = reorder(s, stack)

# print("".join(s))
result = 0

for i, c in enumerate(s):
    if c != ".":
        result += i * (ord(c) - 65)

print(result)

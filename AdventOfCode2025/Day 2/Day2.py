fileContents = open("AdventOfCode2025/Day 2/input.txt")
arr = fileContents.read().split(",")
print(arr)


def is_repeaty(s):
    if len(s) == 0:
        return False
    for i, c in enumerate(s):
        init_seg = s[:i]
        if init_seg == "":
            continue
        subsection = init_seg
        while len(subsection) < len(s):
            subsection += init_seg
            if subsection == s:
                return True
    return False


print(is_repeaty("11"), is_repeaty("22"), is_repeaty("123123"))

total = 0
for r in arr:
    left, right = int(r.split("-")[0]), int(r.split("-")[1])
    for i in range(left, right + 1):
        string_rep = str(i)
        if is_repeaty(string_rep):
            total += i
print(total)

fileContents = open("AdventOfCode2025/Day 3/input.txt")
arr = fileContents.read().split("\n")
print(arr)


def wow_recursion(input_str, len):
    if len == 0:
        return []
    # print(f"{len=} {input_str=}")
    if len == 1:
        at_least_len = input_str
    else:
        at_least_len = input_str[: -len + 1]
    # print(at_least_len)
    highest = 0
    highest_index = 0
    for i, c in enumerate(at_least_len):
        if int(c) > highest:
            highest = int(c)
            highest_index = i
    return [highest] + wow_recursion(input_str[highest_index + 1 :], len - 1)


total = 0
for line in arr:
    best_stuff = wow_recursion(line, 12)
    for i, digit in enumerate(best_stuff[::-1]):
        total += digit * (10**i)
print(total)

from functools import cache

listsContents = open("AdventOfCode2024/Day 19/input.txt")
towels = listsContents.read().split("\n")

colorContents = open("AdventOfCode2024/Day 19/colors.txt")
colors = set(colorContents.read().split(", "))


@cache
def isPossible(towel) -> int:
    result = 0
    for color in colors:
        if towel == color:
            result += 1

        if towel.startswith(color) and towel != color:
            result += isPossible(towel[len(color) :])

    return result


result = 0
for towel in towels:
    result += isPossible(towel)

print(result)

listsContents = open("AdventOfCode2024/Day 11/input.txt")
stones = listsContents.read().split(" ")


def blink(rocks):
    result = []
    for rock in rocks:
        if rock == 0:
            result.append(1)
        elif len(str(rock)) % 2 == 0:
            string_rock = str(rock)
            left, right = (
                string_rock[: len(string_rock) // 2],
                string_rock[len(string_rock) // 2 :],
            )
            result.append(int(left))
            result.append(int(right))
        else:
            result.append(rock * 2024)
    return result

def blink_2()

stones = [int(x) for x in stones]

for i in range(55):
    stones = blink(stones)
    print(len(stones))

print(len(stones))

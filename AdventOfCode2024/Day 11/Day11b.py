listsContents = open("AdventOfCode2024/Day 11/input.txt")
stones = listsContents.read().split(" ")

rock_dict = dict()

for stone in stones:
    if int(stone) not in rock_dict:
        rock_dict[int(stone)] = 0
    rock_dict[int(stone)] += 1


def blink(rocks: dict[int, int]):
    result = dict()
    for rock in rocks:
        if rock == 0:
            if 1 not in result:
                result[1] = 0
            result[1] += rocks[rock]
        elif len(str(rock)) % 2 == 0:
            string_rock = str(rock)
            left, right = (
                string_rock[: len(string_rock) // 2],
                string_rock[len(string_rock) // 2 :],
            )
            if int(left) not in result:
                result[int(left)] = 0
            if int(right) not in result:
                result[int(right)] = 0
            result[int(left)] += rocks[rock]
            result[int(right)] += rocks[rock]
        else:
            if (rock * 2024) not in result:
                result[rock * 2024] = 0
            result[rock * 2024] += rocks[rock]

    return result


for i in range(75):
    rock_dict = blink(rock_dict)

total = 0
for rock in rock_dict:
    total += rock_dict[rock]
print(total)

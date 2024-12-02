fileContents = open("AdventOfCode2024/Day 1/input.txt")
arr = fileContents.read().split("\n")

left_numbers: list[int] = []
right_numbers: list[int] = []

for line in arr:
    left, right = int(line.split("   ")[0]), int(line.split("   ")[1])
    left_numbers.append(left)
    right_numbers.append(right)

left_numbers = sorted(left_numbers)
right_numbers = sorted(right_numbers)


total = 0
for i in range(len(left_numbers)):
    total += left_numbers[i] * len([j for j in right_numbers if j == left_numbers[i]])

print(total)

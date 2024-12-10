from itertools import product

from datetime import datetime

start = datetime.now()


listsContents = open("AdventOfCode2024/Day 7/input.txt")
equations = listsContents.read().split("\n")


result = 0

for line in equations:
    left, right = line.split(": ")[0], line.split(": ")[1]
    nums = right.split(" ")
    left, nums = int(left), [int(x) for x in nums]
    gaps = len(nums) - 1
    ops = [0, 1, 2]
    all_ops = product(ops, repeat=gaps)

    found_combo = False
    for op_tuple in all_ops:
        total = nums[0]
        apply_ops = list(op_tuple)
        for num in nums[1:]:
            op = apply_ops.pop(0)
            if op == 0:
                total += num
            elif op == 1:
                total *= num
            else:
                total = int(str(total) + str(num))

        if total == left:
            found_combo = True
            break

    if found_combo:
        result += left

print(result)

end = datetime.now()
print(end - start)

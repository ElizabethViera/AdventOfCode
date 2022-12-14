fileContents = open("AdventOfCode2022/Day 13/input.txt")
arr = fileContents.read().split("\n")
import functools
import json

def compare(left, right):
    match left, right:
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case int(), int():
            return left - right
        case list(), list():
            for left_contents, right_contents in zip(left,right):
                comparison = compare(left_contents, right_contents)
                if comparison != 0:
                    return comparison
            return len(left) - len(right)
    
all_lines = []
for line in arr:
    if line == "":
        continue
    else:
        all_lines.append(json.loads(line))

# print(all_lines)

result = sorted(all_lines, key=functools.cmp_to_key(compare))

result1 = result.index([[2]])+1
result2 = result.index([[6]])+1

print(result1 * result2)

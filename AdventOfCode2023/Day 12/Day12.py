fileContents = open("AdventOfCode2023/Day 12/input.txt")
arr = fileContents.read().split("\n")
import functools


@functools.cache
def recursiveAssignment(graph, nums) -> int:
    if len(graph) == 0 and len(nums) == 0:
        return 1
    if len(graph) == 0 and len(nums) != 0:
        return 0
    if graph[0] == '?':
        return recursiveAssignment('#' + graph[1:], nums) + recursiveAssignment('.' + graph[1:], nums)
    if graph[0] == '#':
        if len(nums) == 0:
            return 0
        num = nums[0]
        if '.' in graph[:num]:
            return 0
        if len(graph) == num and len(nums) == 1:
            return 1
        if len(graph) == num and len(nums) != 1:
            return 0
        if len(graph) < num:
            return 0
        if graph[num] == '#':
            return 0
        return recursiveAssignment(graph[num+1:], nums[1:])

    if graph[0] == '.':
        return recursiveAssignment(graph[1:], nums)
    else:
        raise(ValueError())

total = 0
for line in arr:
    [graph, nums] = line.split(' ')
    nums = [int(x) for x in nums.split(',')]
    graph = graph + '?' + graph + '?' + graph + '?' + graph + '?' + graph
    nums = nums*5
    total += recursiveAssignment(graph, tuple(nums))

print(total)


 
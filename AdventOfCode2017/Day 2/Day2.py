fileContents = open("AdventOfCode2017/Day 2/input.txt")
lines = fileContents.read().split("\n")

def evenDivide(i,j):
    #print(i, j, j//i == j/i)
    return j//i == j/i

total = 0
for line in lines:
    nums = line.split(" ")
    nums = sorted([int(x) for x in nums])
    for i in range(len(nums)):
        for j in (nums[i+1:]):
            if evenDivide(nums[i], j) and nums[i] != j:
                total += j//nums[i]
                #print(nums[i], j)

print(total)
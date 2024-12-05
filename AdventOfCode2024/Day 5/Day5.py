fileContents = open("AdventOfCode2024/Day 5/input.txt")
arr = fileContents.read().split("\n")

rules = dict()

for rule in arr:
    left, right = int(rule.split("|")[0]), int(rule.split("|")[1])
    if left not in rules:
        rules[left] = []
    rules[left].append(right)


def is_ordered(nums: list[int]):
    # 75,47,61,53,29
    for i_ind, i in enumerate(nums):
        for j_ind, j in enumerate(nums):
            if i_ind == j_ind:
                continue
            if i_ind < j_ind:
                if j in rules and i in rules[j]:
                    return False
            else:
                if i in rules and j in rules[i]:
                    return False
    return True


def get_order(l):
    for i_ind, i in enumerate(nums):
        for j_ind, j in enumerate(nums):
            if i_ind == j_ind:
                continue
            if i_ind < j_ind:
                if j in rules and i in rules[j]:
                    l[i_ind], l[j_ind] = j, i
                    return get_order(l)
            else:
                if i in rules and j in rules[i]:
                    l[i_ind], l[j_ind] = j, i
                    return get_order(l)
    return l


listsContents = open("AdventOfCode2024/Day 5/lists.txt")
lists = listsContents.read().split("\n")

total = 0

for l in lists:
    nums = l.split(",")
    nums = [int(x) for x in nums]
    if not is_ordered(nums):
        new_nums = get_order(nums)
        total += new_nums[len(new_nums) // 2]
print(total)

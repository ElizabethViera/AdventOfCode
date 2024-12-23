listsContents = open("AdventOfCode2024/Day 22/input.txt")
nums = listsContents.read().split("\n")


def mix(n, mix):
    return n ^ mix


def prune(n):
    return n % 16777216


def get_secret(n: int) -> int:  # -> Any:
    times_64 = n * 64
    mixed = mix(n, times_64)
    pruned = prune(mixed)
    divided = pruned // 32
    mixed_two = mix(divided, pruned)
    pruned_two = prune(mixed_two)
    multiplied = pruned_two * 2048
    mixed_three = mix(multiplied, pruned_two)
    pruned_three = prune(mixed_three)
    return pruned_three


result = 0

for num in nums:
    secret = int(num)
    for i in range(2000):
        secret = get_secret(secret)
    result += secret

print(result)

fileContents = open("Day 10/input")
arr = fileContents.read().split('\n')

arr = [int(arr[i]) for i in range(len(arr))]
arr.sort()

plus_one = 1
plus_three = 1
for i in range(1, len(arr)):
    if arr[i-1] + 1 == arr[i]:
        plus_one += 1
    elif arr[i-1] + 3 == arr[i]:
        plus_three += 1

print(plus_one*plus_three)
seen_x = {}


def count_combinations_up_to(x):
    if x in seen_x:
        return seen_x[x]
    if x == 0:
        return 1
    if x < 0:
        return 0
    if x-1 in arr:
        xminus1 = 1
    else:
        xminus1 = 0
    if x-2 in arr:
        xminus2 = 1
    else:
        xminus2 = 0
    if x-3 in arr:
        xminus3 = 1
    else:
        xminus3 = 0
    result = xminus1 * count_combinations_up_to(x - 1) + xminus2 * count_combinations_up_to(
        x-2) + xminus3 * count_combinations_up_to(x-3)
    seen_x[x] = result
    return result


print(count_combinations_up_to(175))

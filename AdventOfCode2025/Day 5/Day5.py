fileContents = open("AdventOfCode2025/Day 5/input.txt")
arr = fileContents.read().split("\n\n")

ranges = arr[0].split("\n")
ingredients = arr[1].split("\n")

# print(ranges)

# print(ingredients)
ingredients = [int(x) for x in ingredients]


all_ranges = []
for r in ranges:
    left, right = r.split("-")[0], r.split("-")[1]
    all_ranges.append((int(left), int(right)))

all_ranges = sorted(all_ranges)

# total = 0
# for ingredient in ingredients:
#     rotten = True
#     for r in all_ranges:
#         if ingredient < r[0]:
#             continue
#         elif ingredient > r[1]:
#             continue
#         elif ingredient >= r[0] and ingredient <= r[1]:
#             # print(ingredient, r)
#             rotten = False
#             break
#     if not rotten:
#         # print("fresh, ", ingredient)
#         total += 1
# print(total)

# 5, 8
# 6, 10

collapsed_ranges = []

current_range = all_ranges[0]

for i, r in enumerate(all_ranges[1:]):
    if current_range[1] >= r[0] and r[1] >= current_range[1]:
        current_range = (current_range[0], r[1])
    elif current_range[1] >= r[0]:
        continue
    else:
        collapsed_ranges.append(current_range)
        current_range = r
collapsed_ranges.append(current_range)

total = 0
for r in collapsed_ranges:
    total += r[1] - r[0] + 1

print(collapsed_ranges)
print(total)

fileContents = open("input")
arr = fileContents.read().split('\n')

max_id = 0
min_id = 978
r_nums = [128, 64, 32, 16, 8, 4, 2]
c_nums = [8, 4, 2]
all_seats = set()
for line in arr:
    row = 0
    for i, c in enumerate(line[:7]):
        if c == "B":
            row += r_nums[i]
    row //= 2
    column = 0
    for i, c in enumerate(line[7:]):
        if c == "R":
            column += c_nums[i]
    column //= 2
    max_id = max(max_id, row*8+column)
    min_id = min(min_id, row*8+column)
    all_seats.add(row*8+column)

for i in range(min_id, max_id):
    if i not in all_seats:
        print(i)
print(max_id, min_id)

top = 0
bottom = 0
left = 0
right = 0

target = 23

dirs = [right, top, left, bottom]

current_dir = 0
i = 0
total = 0
while total < target:
    while i <= dirs[current_dir]:
        i += 1
        total += 1
    dirs[current_dir] = i
    i = 0
    current_dir += 1
    current_dir %= 4

print(dirs, i, total)
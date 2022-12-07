fileContents = open("AdventOfCode2022/Day 7/input.txt")
arr = fileContents.read().split("\n")

files = {}

current_path = []
for line in arr:
    if line.startswith("$ cd .."):
        current_path.pop()
    elif line.startswith("$ cd"):
            current_path.append(line.split()[-1])
    elif line.startswith("dir"):
        # named directory
        if tuple(current_path) not in files:
            files[tuple(current_path)] = {}
        files[tuple(current_path)][line.split()[-1]] = {}
    elif line.startswith("$"):
        pass
    else:
        #file, has a size
        if tuple(current_path) not in files:
            files[tuple(current_path)] = {}
        if "file_sizes" not in files[tuple(current_path)]:
            files[tuple(current_path)]["file_sizes"] = 0
        files[tuple(current_path)]["file_sizes"] += int(line.split(" ")[0])
# print(files)

def total_size(dir):
    current = files[dir]
    total = current["file_sizes"] if "file_sizes" in current else 0
    for key in current:
        if key == "file_sizes":
            continue
        total += total_size(tuple(list(dir) + [key]))
    return total

final_total = 0

for key in files:
    if total_size(key) <= 100000:
        final_total += total_size(key)

space_to_free_up = 30000000 - (70000000 - total_size(('/',)))

best_answer = 30000000
for key in files:
    if total_size(key) > space_to_free_up:
        best_answer = min(best_answer, total_size(key))
print(best_answer)


fileContents = open("Day 6/input")
arr = fileContents.read().split('\n')

answer = {}
total = 0
count = 0

for line in arr:
    if line == "":
        for k in answer:
            if answer[k] == count:
                total += 1
        answer = {}
        count = 0
    else:
        count += 1
        for c in line:
            if c in answer:
                answer[c] += 1
            else:
                answer[c] = 1

for k in answer:
    if answer[k] == count:
        total += 1

print(total)

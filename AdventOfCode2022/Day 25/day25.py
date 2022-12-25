fileContents = open("AdventOfCode2022/Day 25/input.txt")
arr = fileContents.read().split("\n")

def make_int(k):
    match k:
        case '1':
            return 1
        case '2':
            return 2
        case '0':
            return 0
        case '-':
            return -1
        case '=':
            return -2

results = []
for line in arr:
    sum_arr = []
    #print(len(line))
    for i in range(len(line)-1, 0, -1):
        sum_arr.append((5**i)*(make_int(line[len(line)-i-1])))
    sum_arr.append(make_int(line[-1]))
    results.append(sum(sum_arr))

answer = sum(results)
for i in range(20):
    if 5**i > answer:
        print(i)
        break

print(answer)

character_string = ['=', '-', '0', '1', '2']
solution = ""
while answer > 0:
    digit = (answer + 2) % 5
    answer = (answer + 2) // 5
    solution += character_string[digit]

print(solution[::-1])
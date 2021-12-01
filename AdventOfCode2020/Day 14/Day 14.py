fileContents = open("Day 14/input")
arr = fileContents.read().split('\n')


def reverse_binary_string(s):
    s = s[::-1]
    for c in range(len(s)):
        if s[c] == "1":
            return s[c:]


memory_dict = {}
mask_dict = {}
for line in arr:
    if line.startswith("mask"):
        mask_dict = {}
        mask = line[7:].strip()
        for i, c in enumerate(mask[::-1]):
            if c == 'X':
                continue
            else:
                mask_dict[i] = c
    else:
        memory = int(line.split("]")[0][4:])
        value = bin(int(line.split(" ")[-1]))[2:][::-1]
        for key in mask_dict:
            if key > len(value) - 1:
                value += '0' * key
            value_arr = []
            for c in value:
                value_arr.append(c)
            value_arr[key] = mask_dict[key]
            value = ''.join(value_arr)
        memory_dict[memory] = int(reverse_binary_string(value), 2)

total = 0
for key in memory_dict:
    total += memory_dict[key]

print(total)

final_dict = {}


def memory_values_from_bitmask(memory, mask_1_set, mask_X_set):
    memory = bin(memory)[2:][::-1]
    mem_arr = list(memory)
    for i in mask_1_set:
        while i >= len(mem_arr):
            mem_arr.append('0')
        print(i, mem_arr)
        mem_arr[i] = '1'
    for k in mask_X_set:
        while k >= len(mem_arr):
            mem_arr.append('0')
        mem_arr[k] = 'X'
    frontier = [mem_arr]
    while len(frontier) < 2**len(mask_X_set):
        current_arr = frontier.pop(0)
        for i, v in enumerate(current_arr):
            if v == 'X':
                frontier.append(current_arr[:i] + ['0'] + current_arr[i+1:])
                frontier.append(current_arr[:i] + ['1'] + current_arr[i+1:])
                break
    result = []
    for mem in frontier:
        result.append(''.join(c for c in mem))
    return [reverse_binary_string(s) for s in result]


for line in arr:
    if line.startswith("mask"):
        mask_1_set = set()
        mask_X_set = set()
        mask = line[7:].strip()
        for i, c in enumerate(mask[::-1]):
            if c == 'X':
                mask_X_set.add(i)
            elif c == '1':
                mask_1_set.add(i)
    else:
        memory = int(line.split("]")[0][4:])
        value = int(line.split(" ")[-1])
        memories = memory_values_from_bitmask(memory, mask_1_set, mask_X_set)
        for mem in memories:
            key = int(mem, 2)
            final_dict[key] = value
total = 0
for d in final_dict:
    total += final_dict[d]
print(total)

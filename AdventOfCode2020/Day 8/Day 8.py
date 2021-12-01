fileContents = open("Day 8/input")
arr = fileContents.read().split('\n')


def runTest(new_arr):
    acc = 0
    current_index = 0
    visited_indices = set()
    while (True):
        if current_index in visited_indices:
            return False
        visited_indices.add(current_index)
        current_instruction = new_arr[current_index]
        if current_instruction == "done!":
            print("acc = ", acc)
            return True
        value = current_instruction.split(" ")[1][1:]
        sign = current_instruction.split(" ")[1][:1]
        if current_instruction.split(" ")[0] == "nop":
            current_index += 1
        elif current_instruction.split(" ")[0] == "acc":
            if sign == "+":
                acc += int(value)
            else:
                acc -= int(value)
            current_index += 1
        else:  # current_instruction.split(" ")[0] == "jmp":
            if sign == "+":
                current_index += int(value)
            else:
                current_index -= int(value)


for i in range(len(arr)):
    if arr[i].startswith("acc"):
        continue
    elif arr[i].startswith("nop"):
        if(runTest(arr[:i] + ["jmp" + arr[i][3:]] + arr[i+1:])):
            print(i)
    else:
        if(runTest(arr[:i] + ["nop" + arr[i][3:]] + arr[i+1:])):
            print(i)

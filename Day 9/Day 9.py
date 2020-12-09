fileContents = open("Day 9/input")
arr = fileContents.read().split('\n')

start_index = 0
numbers = []


def check_number(current_number, start_index, numbers):
    for i in numbers[start_index:]:
        for j in numbers[(start_index+1):]:
            if i + j == current_number:
                return True
    return False


for line in arr:
    current_number = int(line)
    if len(numbers) > 25:
        if (check_number(current_number, start_index, numbers)):
            numbers.append(current_number)
            start_index += 1
        else:
            print(current_number)
            break
    else:
        numbers.append(current_number)

magic_number = 393911906


def sum_of_arr(array_of_nums):
    total = 0
    for i in array_of_nums:
        total += int(i)
    return total


def rando():
    for i in range(650):
        for j in range(i+1, 650):
            if sum_of_arr(arr[i:j]) >= magic_number:
                if sum_of_arr(arr[i:j]) == magic_number:
                    print("hello!", i, j)
                    return
    print("done")


rando()  # my result of rando is the range 517-534

max_num = int(arr[534])
min_num = int(arr[517])
for num in arr[517:534]:
    if int(num) < min_num:
        min_num = int(num)
    if int(num) > max_num:
        max_num = int(num)
print(max_num + min_num)

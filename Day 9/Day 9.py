fileContents = open("Day 9/input")
arr = fileContents.read().split('\n')

start_index = 0
numbers = []

arr = [int(arr[i]) for i in range(len(arr))]


def check_number(current_number, start_index, numbers):
    for i in numbers[start_index:]:
        for j in numbers[(start_index+1):]:
            if i + j == current_number:
                return True
    return False


for line in arr:
    current_number = line
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


def get_magic_range():
    for i in range(650):
        for j in range(i+1, 650):
            if sum(arr[i:j]) >= magic_number:
                if sum(arr[i:j]) == magic_number:
                    print("hello!", i, j)
                    return
    print("done? No range?")


get_magic_range()  # my result is the range 517-534

max_num = arr[534]
min_num = arr[517]
for num in arr[517:534]:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print(max_num + min_num)

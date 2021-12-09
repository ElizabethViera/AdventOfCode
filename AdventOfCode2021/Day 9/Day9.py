fileContents = open("Day 9/input.txt")
arr = fileContents.read().split('\n')
arr = [[i for i in line] for line in arr]


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
rows_len = len(arr)
cols_len = len(arr[0])


def is_in_bounds(row, col):
    if row < 0 or row >= rows_len:
        return False
    if col < 0 or col >= cols_len:
        return False
    if arr[row][col] != ',':
        return False
    return True


def floodfill(arr, row, col, num):
    arr[row][col] = num
    for direction in dirs:
        if is_in_bounds(row + direction[0], col + direction[1]):
            floodfill(arr, row+direction[0], col+direction[1], num)


num = 0
for row in range(rows_len):
    for col in range(cols_len):
        if arr[row][col] == ',':
            floodfill(arr, row, col, num)
            num += 1

results = []
for i in range(250):
    result = 0
    for row in range(rows_len):
        for col in range(cols_len):
            if arr[row][col] == i:
                result += 1
    results.append(result)
print(sorted(results, reverse=True))

print(108*103*101)

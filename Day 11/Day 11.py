fileContents = open("Day 11/input")
arr = fileContents.read().split('\n')
new_matrix = []
for line in arr:
    new_matrix_row = []
    for c in line:
        new_matrix_row.append(c)
    new_matrix.append(new_matrix_row)
arr = new_matrix

new_matrix = []
new_matrix_row = []

print("LENGTH = ", len(arr), len(arr[0]))


def is_L_to_O(row, col, array_at_time):
    dirs = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]]
    for dir in dirs:
        try:
            magnitude = 1
            while(True):
                dir_row = row + (dir[0]*magnitude)
                dir_col = col + (dir[1]*magnitude)
                if dir_row < 0 or dir_col < 0:
                    break
                if array_at_time[dir_row][dir_col] == "#":
                    return False
                elif array_at_time[dir_row][dir_col] == "L":
                    break
                elif array_at_time[dir_row][dir_col] == ".":
                    magnitude += 1
        except:
            continue
    return True


def is_O_to_L(row, col, array_at_time):
    count = 0
    dirs = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]]
    for dir in dirs:
        magnitude = 1
        try:
            while True:
                dir_row = row + (dir[0]*magnitude)
                dir_col = col + (dir[1]*magnitude)
                if dir_row < 0 or dir_col < 0:
                    break
                if array_at_time[dir_row][dir_col] == "#":
                    count += 1
                    if count >= 5:
                        return True
                    break
                elif array_at_time[dir_row][dir_col] == "L":
                    break
                if array_at_time[dir_row][dir_col] == ".":
                    magnitude += 1
        except:
            continue
    return False


def count_occupied(a):
    occupied_count = 0
    for row in a:
        for col in row:
            if col == "#":
                occupied_count += 1
    return occupied_count


def get_occupied_seats(arr):
    while True:
        new_matrix = []
        # for row in range(10):
        for row in range(93):
            new_line = []
            # for col in range(10):
            for col in range(97):
                if arr[row][col] == ".":
                    new_line.append(".")
                elif arr[row][col] == "L":
                    if is_L_to_O(row, col, arr):
                        new_line.append("#")
                    else:
                        new_line.append("L")
                elif arr[row][col] == "#":
                    if is_O_to_L(row, col, arr):
                        new_line.append("L")
                    else:
                        new_line.append("#")
            new_matrix.append(new_line)
        # print(new_matrix)
        # print("count = ", count_occupied(new_matrix))
        if arr == new_matrix:
            return count_occupied(arr)
        arr = new_matrix


print(get_occupied_seats(arr))

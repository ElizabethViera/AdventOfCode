fileContents = open("AdventOfCode2022/Day 8/input.txt")
arr = fileContents.read().split("\n")

total_arr = []
for line in arr:
    line_arr = [int(i) for i in line]
    total_arr.append(line_arr)



dirs = [(-1, 0), (1,0), (0,1), (0,-1)]

def in_bounds(row,col):
    if row < 0 or col < 0 or row >= len(total_arr) or col >= len(total_arr[0]):
        return False
    return True

def visibile_until_blocked(row,col):
    direction_visibility = []
    for direction in dirs:
        found_limiting_tree_in_this_direction = False
        current_row = row + direction[0]
        current_col = col + direction[1]
        while (in_bounds(current_row, current_col)):
            if total_arr[current_row][current_col] >= total_arr[row][col]:
                distance = abs((current_col - col) + (current_row - row))
                direction_visibility.append(distance)
                found_limiting_tree_in_this_direction = True
                break
            current_col = current_col + direction[1]
            current_row = current_row + direction[0]
        if not found_limiting_tree_in_this_direction:
            distance = abs((current_col - col) + (current_row - row))
            direction_visibility.append(distance-1)
    return direction_visibility
            
            

best_result = 0
for row in range(len(total_arr)):
    for col in range(len(total_arr[0])):
        if row == 0 or col == 0 or row == len(total_arr)-1 or col == len(total_arr[0])-1:
            continue
        scenic_score = visibile_until_blocked(row, col)
        # print(scenic_score, row, col)
        result = 1
        for score in scenic_score:
            result *= score
        if result > best_result:
            best_result = result
print(best_result)

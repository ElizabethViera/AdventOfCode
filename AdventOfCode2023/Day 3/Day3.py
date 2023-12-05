fileContents = open("AdventOfCode2023/Day 3/input.txt")
arr = fileContents.read().split("\n")

found = set() # coordinates of number locations
region_start = dict() # dictionary from a single coordinate to a value

def find_number_at(start_r: int, start_c: int) -> list[tuple[int, int]]:
    r, c = start_r, start_c
    result: list[tuple[int, int]] = []
    while arr[r][c] in '1234567890':
        result.append((r, c))
        c += 1
    return result
    

for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col] in '1234567890':
            if (row, col) not in found:
                found.add((row,col))
                digits = region_start[(row,col)] = find_number_at(row,col)
                numStr = ''
                for digit in digits:
                    found.add(digit)
                    numStr += arr[digit[0]][digit[1]]
                region_start[(row, col)] = numStr
                
print(len(region_start))

def hasSpecialCharacterInPerimeter(start, width) -> bool:
    for i in range(start[1]-1, start[1]+width+1):
        # should be row above the number
        if arr[start[0]-1][i] != '.':
            return True
    if arr[start[0]][start[1]-1] != '.':
        return True
    if arr[start[0]][start[1]+width] != '.':
        return True
    for i in range(start[1]-1, start[1]+width+1):
        if arr[start[0]+1][i] != '.':
            return True
    return False

print('\n')
total = 0
for coord in region_start:
    numLength = len(region_start[coord])
    if hasSpecialCharacterInPerimeter(coord, numLength):
        #print(region_start[coord])
        total += int(region_start[coord])
print(total)
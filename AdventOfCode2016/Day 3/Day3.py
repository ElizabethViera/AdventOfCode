fileContents = open("AdventOfCode2016/Day 3/input.txt")
arr = fileContents.read().split("\n")

def isValid(arrOfPoints):
    zero, one, two = arrOfPoints[0], arrOfPoints[1], arrOfPoints[2]
    return not(zero + one <= two or zero + two <= one or one + two <= zero)

def transpose(matrix):
    return [ [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        

count = 0
all_points = []
for triangle in arr:
    triangle_points = []
    for point in triangle.split(" "):
        if point != "":
            triangle_points.append(int(point))
    all_points.append(triangle_points)

transposed_points = transpose(all_points)

for row in range(3):
    while len(transposed_points[row]) != 0:
        a = transposed_points[row].pop()
        b = transposed_points[row].pop()
        c = transposed_points[row].pop()
        if isValid([a,b,c]):
            count += 1

print(transposed_points)

print(count)

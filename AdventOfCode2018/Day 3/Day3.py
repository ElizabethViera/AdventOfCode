fileContents = open("AdventOfCode2018/Day 3/input.txt")
claims = fileContents.read().split("\n")

squares = set()
results = set()
unique_squares = set()

for claim in claims:
    found_overlap = False
    segments = claim.split(' ')
    segment_id = segments[0]
    start_row, start_col = int(segments[2][:-1].split(',')[0]), int(segments[2][:-1].split(',')[1])
    width, height = int(segments[3].split('x')[0]), int(segments[3].split('x')[1])

    for row in range(start_row, start_row+width):
        for col in range(start_col, start_col+height):
            if (row, col) in squares:
                results.add((row,col))
            squares.add((row,col))
            unique_squares.add((row,col, segment_id))
 
number_of_times = dict()   
for square in unique_squares:
    if (square[0], square[1]) not in number_of_times:
        number_of_times[(square[0], square[1])] = 0
    number_of_times[(square[0], square[1])] += 1

filtered_results = set([x for x in number_of_times if number_of_times[x] == 1])

print(len(filtered_results))
    
for claim in claims:
    found_overlap = False
    segments = claim.split(' ')
    segment_id = segments[0]
    start_row, start_col = int(segments[2][:-1].split(',')[0]), int(segments[2][:-1].split(',')[1])
    width, height = int(segments[3].split('x')[0]), int(segments[3].split('x')[1])

    for row in range(start_row, start_row+width):
        for col in range(start_col, start_col+height):
            if (row, col) not in filtered_results:
                found_overlap = True
                break
    if found_overlap == False:
        print(segment_id)




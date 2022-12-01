fileContents = open("AdventOfCode2015/Day 6/input.txt")
arr = fileContents.read().split('\n')

light_dict = dict()

for instruction in arr:
    instruction_pieces = instruction.split(' ')

    # toggle case
    if instruction_pieces[0] == 'toggle':
        # print(instruction_pieces)
        left_side = instruction_pieces[1].split(',')
        right_side = instruction_pieces[-1].split(',')

        for row in range(int(left_side[0]), int(right_side[0])+1):
            for col in range(int(left_side[1]), int(right_side[1])+1):
                if (row, col) not in light_dict:
                    light_dict[(row, col)] = 2
                else:
                    light_dict[(row, col)] += 2

    # turn off or on case
    else:
        light_amount = 1 if instruction_pieces[1] == 'on' else -1

        left_side = instruction_pieces[2].split(',')
        right_side = instruction_pieces[-1].split(',')
        for row in range(int(left_side[0]), int(right_side[0])+1):
            for col in range(int(left_side[1]), int(right_side[1])+1):
                if (row, col) not in light_dict:
                    light_dict[(row, col)] = 0
                light_dict[(row, col)] += light_amount
                if light_dict[(row, col)] < 0:
                    light_dict[(row, col)] = 0


print(sum(light_dict.values()))

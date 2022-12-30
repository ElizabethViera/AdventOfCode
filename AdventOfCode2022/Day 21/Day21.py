fileContents = open("AdventOfCode2022/Day 21/input.txt")
arr = fileContents.read().split("\n")

monkey_dict = {}
for line in arr:
    spaced_line = line.split(' ')
    monkey_name = spaced_line[0][:-1]
    monkey_dict[monkey_name] = {}
    match len(spaced_line):
        case 4:
            monkey_dict[monkey_name]['Role'] = 'friendly'
            monkey_dict[monkey_name]['Left_Friend'] = spaced_line[1]
            monkey_dict[monkey_name]['Right_Friend'] = spaced_line[3]
            monkey_dict[monkey_name]['Operator'] = spaced_line[2]
        case 2:
            monkey_dict[monkey_name]['Role'] = 'alone'
            monkey_dict[monkey_name]['num'] = int(spaced_line[1])

def operate(operator, left, right):
    match operator:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case '/':
            return left / right
        case '==':
            return left == 23440423968672

def get_left_right(left, right, operator, trying_this_number):
    if monkey_dict[left]['Role'] == 'alone':
        left_calc = monkey_dict[left]['num']
    else:
        left_calc = get_left_right(monkey_dict[left]['Left_Friend'], monkey_dict[left]['Right_Friend'], monkey_dict[left]['Operator'], trying_this_number)
    if monkey_dict[right]['Role'] == 'alone':
        right_calc = monkey_dict[right]['num']
    else:
        right_calc = get_left_right(monkey_dict[right]['Left_Friend'], monkey_dict[right]['Right_Friend'], monkey_dict[right]['Operator'], trying_this_number)
    if left == 'humn':
        left_calc = trying_this_number
    if right == 'humn':
        right_calc = trying_this_number
    return operate(operator, left_calc, right_calc)

for i in range(3296135415000, 3296135420000, 1):
    left_result = get_left_right('rhtg', 'nmms', '*', i)
    right_result = get_left_right('ccwj', 'wqmc', '*', i)
    # print(left_result - right_result)
    if abs(left_result - right_result) == 0:
        print(i)
        
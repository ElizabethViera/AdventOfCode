fileContents = open("Day 16/input.txt")
stackContents = open("Day 16/input2.txt")

# stackarr = stackContents.read().split('\n')
arr = fileContents.read().split('\n')
global_result = []

packet_types = {0: 'sum', 1: 'product', 2: 'minimum', 3: 'maximum',
                4: 'literal', 5: 'greater_than', 6: 'less_than', 7: 'equal'}

hex_to_bin = {'0': '0000',
              '1': '0001',
              '2': '0010',
              '3': '0011',
              '4': '0100',
              '5': '0101',
              '6': '0110',
              '7': '0111',
              '8': '1000',
              '9': '1001',
              'A': '1010',
              'B': '1011',
              'C': '1100',
              'D': '1101',
              'E': '1110',
              'F': '1111'
              }

binary_string = ''
for line in arr:
    for c in line:
        binary_string += hex_to_bin[c]


def update(bstring, n):
    return (bstring[:n], bstring[n:])


tokens = []


def parse_packet(bstring):
    packet_version, bstring = update(bstring, 3)
    packet_type, bstring = update(bstring, 3)
    print(packet_types[int(packet_type, 2)])
    global_result.append(int(packet_version, 2))
    packet_contents = [packet_version, packet_type]
    if packet_type == '100':
        literal_value = ''
        while(True):
            packet_value, bstring = update(bstring, 5)
            literal_value += packet_value[1:]
            packet_contents.append(packet_value)
            if packet_value[0] == '0':
                print("literal = ", int(literal_value, 2))
                tokens.append(int(literal_value, 2))
                return packet_contents, bstring
    else:
        # packet is operator
        tokens.append(packet_types[int(packet_type, 2)] + "(")
        operator_type, bstring = update(bstring, 1)
        packet_contents.append(operator_type)
        if operator_type == '0':
            print("[operator start: ")
            packet_length, bstring = update(bstring, 15)
            sub_b_string, bstring = update(bstring, int(packet_length, 2))
            while (sub_b_string != ''):
                subpacket_contents, sub_b_string = parse_packet(sub_b_string)
                packet_contents.append(subpacket_contents)
            print(" operator end.]")

            tokens.append(")")
            return packet_contents, bstring
        else:
            print("[operator start: ")
            number_of_subpackets, bstring = update(bstring, 11)
            for _ in range(int(number_of_subpackets, 2)):
                subpacket_contents, bstring = parse_packet(bstring)
                packet_contents.append(subpacket_contents)
            print(" operator end.] ")
            tokens.append(")")
            return packet_contents, bstring


parse_packet(binary_string)

operators = ['sum(', 'product(', 'minimum(', 'maximum(',
             'less_than(', 'greater_than(', 'equal(']


def get_last_operator(stack_of_items):
    for index, item in enumerate(stack_of_items[::-1]):
        if item in operators:
            return len(stack_of_items) - index - 1


def my_safe_eval(expression):
    operator = expression[0]
    if operator == 'sum(':
        result = 0
        for operand in expression[1:]:
            result += int(operand)
        return result
    if operator == 'product(':
        result = 1
        for operand in expression[1:]:
            result *= int(operand)
        return result
    if operator == 'minimum(':
        result = 10000000000000
        for operand in expression[1:]:
            if int(operand) < result:
                result = int(operand)
        return result
    if operator == 'maximum(':
        result = 0
        for operand in expression[1:]:
            if int(operand) > result:
                result = int(operand)
        return result
    if operator == 'less_than(':
        return 1 if int(expression[1]) < int(expression[2]) else 0
    if operator == 'greater_than(':
        return 1 if int(expression[1]) > int(expression[2]) else 0
    if operator == 'equal(':
        return 1 if int(expression[1]) == int(expression[2]) else 0

    raise Exception("invalid operator")


fancy_stack = []
for item in tokens:
    if item in operators:
        fancy_stack.append(item)
    elif item == ')':
        index_of = get_last_operator(fancy_stack)
        items_to_evaluate, fancy_stack = fancy_stack[index_of:], fancy_stack[:index_of]
        print(items_to_evaluate)
        fancy_stack.append(my_safe_eval(items_to_evaluate))
    else:
        fancy_stack.append(item)

print(fancy_stack)

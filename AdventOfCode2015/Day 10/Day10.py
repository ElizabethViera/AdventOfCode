current_number = '1321131112'

for i in range(50):
    current_digit = current_number[:1]
    current_count = 1
    result = ""
    for c in current_number[1:]:
        if current_digit == c:
            current_count += 1
        else:
            result += str(current_count) + current_digit
            current_count = 1
            current_digit = c
    result += str(current_count) + current_digit
    # print(result)
    current_number = result
print(len(current_number))




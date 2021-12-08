unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}

fileContents = open("Day 8/input.txt")
arr = fileContents.read().split('\n')
result = 0


def get_number_from_letters(letters, letters_to_numbers):
    for digit in letters_to_numbers:
        if letters_to_numbers[digit] == set(letters):
            return digit


for line in arr:
    letters_to_numbers = {}
    letters_to_numbers[1] = set()
    letters_to_numbers[8] = set()
    letters_to_numbers[4] = set()
    letters_to_numbers[7] = set()
    lhs, rhs = line.split(' | ')[0], line.split(' | ')[1]
    lhs, rhs = lhs.split(' '), rhs.split(' ')

    #print(lhs, rhs)
    for digit in lhs + rhs:
        if len(digit) in unique_lengths:
            letters_to_numbers[unique_lengths[len(digit)]] = set(digit)
    for digit in lhs + rhs:
        if len(digit) == 5 and letters_to_numbers[1].intersection(digit) == letters_to_numbers[1]:
            letters_to_numbers[3] = set(digit)
    aaaa = letters_to_numbers[7] - letters_to_numbers[1]
    dddd = letters_to_numbers[3].intersection(
        letters_to_numbers[4] - letters_to_numbers[1])
    bbbb = (letters_to_numbers[4] - letters_to_numbers[1]) - set(dddd)

    for digit in lhs + rhs:
        if len(digit) == 5 and set(digit) != letters_to_numbers[3]:
            if bbbb.intersection(digit) == set():
                letters_to_numbers[2] = set(digit)
            else:
                letters_to_numbers[5] = set(digit)
        if len(digit) == 6:
            if set(digit).intersection(set(dddd)) == set():
                letters_to_numbers[0] = set(digit)
            elif set(digit).intersection(letters_to_numbers[1]) == letters_to_numbers[1]:
                letters_to_numbers[9] = set(digit)
            else:
                letters_to_numbers[6] = set(digit)
    # decode RHS
    local_result = ''
    for r in rhs:
        local_result += str(get_number_from_letters(r, letters_to_numbers))
    print(local_result)
    result += int(local_result)

print(result)

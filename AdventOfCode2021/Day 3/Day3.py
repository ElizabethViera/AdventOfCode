fileContents = open("AdventOfCode2021/Day 3/input.txt")
start_arr = fileContents.read().split('\n')
print(start_arr)


def findMostPopularDigits(arr: "list[str]"):
    # calculate the most and least popular digits
    number_of_digits = len(arr[0])
    digit_popularity = dict()
    for i in range(len(arr)):
        for j in range(number_of_digits):
            if j not in digit_popularity:
                digit_popularity[j] = 0
            if arr[i][j] == '1':
                digit_popularity[j] += 1
            else:
                digit_popularity[j] -= 1

    # build the result strings
    result1 = ''
    result2 = ''
    for d in digit_popularity:
        if digit_popularity[d] < 0:
            result1 = result1 + '0'
            result2 = result2 + '1'
        else:
            result1 = result1 + '1'
            result2 = result2 + '0'

    return result1, result2


def compareInitialSegments(s1, s2):
    count = 0
    for char_index in range(len(s1)):
        if s1[char_index] == s2[char_index]:
            count += 1
        else:
            return count
    return count


remaining_strings = {key: key for key in start_arr}
while len(remaining_strings) > 1:
    new_remaining_strings = {}
    most_popular, least_popular = findMostPopularDigits(
        [remaining_strings[v] for v in remaining_strings])
    for candidate in remaining_strings:
        if remaining_strings[candidate][0] == most_popular[0]:
            new_remaining_strings[candidate] = remaining_strings[candidate][1:]
    remaining_strings = new_remaining_strings
resultLeft = list(key for key in remaining_strings)[0]

remaining_strings = {key: key for key in start_arr}
while len(remaining_strings) > 1:
    new_remaining_strings = {}
    most_popular, least_popular = findMostPopularDigits(
        [remaining_strings[v] for v in remaining_strings])
    for candidate in remaining_strings:
        if remaining_strings[candidate][0] == least_popular[0]:
            new_remaining_strings[candidate] = remaining_strings[candidate][1:]
    remaining_strings = new_remaining_strings
resultRight = list(key for key in remaining_strings)[0]

print(resultLeft, resultRight)
print(int(resultLeft, 2) * int(resultRight, 2))

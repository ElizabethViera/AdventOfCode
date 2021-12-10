fileContents = open("Day 10/input.txt")
arr = fileContents.read().split('\n')
arr = [[i for i in line] for line in arr]
# print(arr)

opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']

result = []


def is_corrupt(line):
    syntax_stack = []
    for char in line:
        if char in opening_brackets:
            syntax_stack.append(char)
        if char in closing_brackets:
            matching_bracket = syntax_stack.pop()
            if opening_brackets.index(matching_bracket) != closing_brackets.index(char):
                return (True, [])
    return (False, syntax_stack)


def calculate_incomplete_stack(syntax_stack):
    result_stack = []
    for i in syntax_stack[::-1]:
        result_stack.append(closing_brackets[opening_brackets.index(i)])
    score = 0
    for j in result_stack:
        score *= 5
        score += closing_brackets.index(j) + 1
    return score


result_scores = []
for line in arr:
    corrupted, syntax_stack = is_corrupt(line)
    if not corrupted:
        score = calculate_incomplete_stack(syntax_stack)
        result_scores.append(score)

print(sorted(result_scores)[len(result_scores)//2])


'''
score = 0
for wrong_character in result:
    if wrong_character == ')':
        score += 3
    elif wrong_character == '}':
        score += 1197
    elif wrong_character == '>':
        score += 25137
    else:
        score += 57

print(score)
'''

fileContents = open("AdventOfCode2015/Day 3/input.txt")
arr = fileContents.read().split('\n')


current_state1 = (0, 0)
current_state2 = (0, 0)
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

result1 = set([current_state1])
result2 = set([current_state2])
for i, c in enumerate(arr[0]):
    if i % 2 == 0:
        current_state = current_state1
    else:
        current_state = current_state2
    if c == '^':
        current_state = (current_state[0] + dirs[0][0],
                         current_state[1] + dirs[0][1])
    if c == 'v':
        current_state = (current_state[0] + dirs[1][0],
                         current_state[1] + dirs[1][1])
    if c == '>':

        current_state = (current_state[0] + dirs[2][0],
                         current_state[1] + dirs[2][1])
    if c == '<':

        current_state = (current_state[0] + dirs[3][0],
                         current_state[1] + dirs[3][1])
    if i % 2 == 0:
        result1.add(current_state)
        current_state1 = current_state
    else:
        result2.add(current_state)
        current_state2 = current_state

final_result = set()
for item in result1:
    final_result.add(item)
for item in result2:
    final_result.add(item)
print(len(final_result))

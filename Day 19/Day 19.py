fileContents = open("Day 19/input")
arr = fileContents.read().split('\n')

file2Contents = open("Day 19/input2")
arr2 = file2Contents.read().split('\n')


def no_pipes(pipe_arr):
    if '|' in pipe_arr:
        arr1 = pipe_arr[:pipe_arr.index('|')]
        arr2 = pipe_arr[pipe_arr.index('|')+1:]
        return [arr1, arr2]
    else:
        return [pipe_arr]


rules = {}
for line in arr:
    line_arr = line.split(" ")
    rule = [
        int(item) if item[0] != 'a' and item[0] != 'b' and item[0] != '|' else item for item in line_arr[1:]]
    rules[int(line_arr[0][:-1])] = no_pipes(rule)
print(rules)


def canStringBeMade(string):
    frontier = [[0]]
    final_frontier = []
    while frontier != []:
        current_rule = frontier.pop()
        if len(current_rule) > len(string):
            continue
        bad = False
        for i in range(len(current_rule)):
            if current_rule[i] == 'a' or current_rule[i] == 'b':
                if string[i] != current_rule[i]:
                    bad = True
                    break
            else:
                break
        if bad:
            continue
        # print("printing...", current_rule, string)
        # [4, 1, 5]
        for i, next_rule in enumerate(current_rule):
            # 1
            if isinstance(next_rule, int):
                next_options = rules[next_rule]
                # [[2,3], [3,2]]
                for option in next_options:
                    new_rule = current_rule[:i] + option + current_rule[i+1:]
                    frontier.append(new_rule)
                break
        else:
            final_frontier.append("".join(current_rule))
    return string in final_frontier


count = 0
for line in arr2:
    print("line = ", line, count)
    if canStringBeMade(line):
        count += 1
print(count)

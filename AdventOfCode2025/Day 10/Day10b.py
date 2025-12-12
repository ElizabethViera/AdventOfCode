fileContents = open("AdventOfCode2025/Day 10/input.txt")
arr = fileContents.read().split("\n")


def disqualified(current_state, goal, best):
    for i, num in enumerate(current_state[0]):
        if num > goal[i]:
            return True
    if current_state[1] > best:
        return True
    return False


def apply_button(current_state: list[int], button: tuple[int, ...]):
    copy_current = current_state.copy()
    for num in button:
        copy_current[num] += 1
    return copy_current


def getLowestPresses(goal, buttons):
    goal_parsed = goal[1:-1].split(",")
    goal_parsed = [int(x) for x in goal_parsed]
    zeros = [0 for x in goal_parsed]
    to_visit = [(zeros, 0)]
    best = 600000000
    while to_visit != []:
        current = to_visit.pop()
        if current[0] == goal_parsed:
            if current[1] < best:
                best = current[1]
        if disqualified(current, goal_parsed, best):
            continue
        print(current)
        for button in buttons:
            new_state = apply_button(current[0], button)
            visiting_next = (new_state, current[1] + 1)
            to_visit.append(visiting_next)
    return best


for i, machine in enumerate(arr):
    # print(i)
    machine_parts = machine.split()
    goal = machine_parts[-1]
    bts = machine_parts[1:-1]
    buttons = [tuple([int(x) for x in button[1:-1].split(",")]) for button in bts]
    print(getLowestPresses(goal, buttons))

fileContents = open("AdventOfCode2025/Day 10/input.txt")
arr = fileContents.read().split("\n")


def apply(button, state):
    # print(button, state)
    state_set = set(state)
    for num in button:
        if num not in state_set:
            state_set.add(num)
        else:
            state_set.remove(num)
    return tuple(sorted(list(state_set)))


def getBest(goal, buttons):
    goal_state = []
    for i, c in enumerate(goal[1:-1]):
        if c == "#":
            goal_state.append(i)
    goal_state = tuple(goal_state)

    button_states = dict()
    for i, button in enumerate(buttons):
        nums = button[1:-1].split(",")
        nums = [int(x) for x in nums]
        button_states[i] = nums

    # print(goal_state, button_states)

    visited = dict()
    visiting = [((), 0)]
    while goal_state not in visited:
        current = visiting.pop(0)
        visited[current[0]] = current[1]
        for button in button_states:
            # print("button ", button)
            neighbor_state = apply(button_states[button], current[0])
            if neighbor_state not in visited:
                visiting.append((neighbor_state, current[1] + 1))
    return visited[goal_state]


totes = 0
for i, machine in enumerate(arr):
    print(i)
    machine_parts = machine.split()
    goal = machine_parts[0]
    buttons = machine_parts[1:-1]

    lowestButtons = getBest(goal, buttons)
    totes += lowestButtons

print(totes)

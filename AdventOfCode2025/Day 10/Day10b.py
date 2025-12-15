fileContents = open("input.txt")
arr = fileContents.read().split("\n")
import scipy.optimize

total = 0
for i, machine in enumerate(arr):
    # print(i)
    machine_parts = machine.split()
    goal = machine_parts[-1]
    goal = [int(x) for x in goal[1:-1].split(",")]
    bts = machine_parts[1:-1]
    buttons = [tuple([int(x) for x in button[1:-1].split(",")]) for button in bts]
    # print(goal, buttons)
    matrix = []
    for i, n in enumerate(goal):
        result = []
        for button in buttons:
            if i in button:
                result.append(1)
            else:
                result.append(0)
        matrix.append(result)
    # print("optimizing")
    optimized = scipy.optimize.milp(
        c=[1 for x in range(len(buttons))],
        integrality=[1 for x in range(len(buttons))],
        constraints=scipy.optimize.LinearConstraint(
            A=matrix,
            lb=goal,
            ub=goal,
        ),
    )
    for i in list(optimized.x.tolist()):
        total += i

print(total)

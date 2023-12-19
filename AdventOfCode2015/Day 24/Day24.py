fileContents = open("AdventOfCode2015/Day 24/input.txt")
arr = fileContents.read().split("\n")
arr = [int(x) for x in arr][::-1]

sum_of_all = sum(arr)//4

set_of_assignments = set()

def quantumEntanglement(s):
    result = 1
    for i in s:
        result *= i
    return result
bestQE = 72050270

def recursiveAssignment(assigned, toAssign):
    global bestQE
    QE = quantumEntanglement(assigned[0])
    if len(assigned[0]) > 5 or quantumEntanglement(assigned[0]) >= bestQE:
        return 0
    if (sum_of_all - sum(assigned[0])-1)*QE >= bestQE:
        return 0
    
    #print(assigned, toAssign, sum(assigned[0]), sum(assigned[1]), sum_of_all, bestQE, QE)
    if len(toAssign) == 0:
        if sum(assigned[0]) == sum_of_all and sum(assigned[1]) == sum_of_all and sum(assigned[2]) == sum_of_all:
            if len(assigned[0]) < 6:
                if quantumEntanglement(assigned[0]) < bestQE:
                    bestQE = quantumEntanglement(assigned[0])
                if len(assigned[0]) < 5:
                    raise(ValueError)
                print("found", quantumEntanglement(assigned[0]))
                set_of_assignments.add(quantumEntanglement(assigned[0]))
            return 1
        else:
            return 0
    
    if sum(assigned[0]) > sum_of_all or sum(assigned[1]) > sum_of_all or sum(assigned[2]) > sum_of_all or sum(assigned[3]) > sum_of_all:
        return 0
    else:
        toAssign = tuple(toAssign)
        new_assignment = (toAssign[0],)
        new_first = assigned[0]+new_assignment
        new_second = assigned[1]+new_assignment
        new_third = assigned[2] + new_assignment
        new_fourth = assigned[3] + new_assignment
        return recursiveAssignment((new_first, assigned[1], assigned[2], assigned[3]), toAssign[1:]) +\
            recursiveAssignment((assigned[0], new_second, assigned[2], assigned[3]), toAssign[1:]) + \
            recursiveAssignment((assigned[0], assigned[1], new_third, assigned[3]), toAssign[1:]) + \
            recursiveAssignment((assigned[0], assigned[1], assigned[2], new_fourth), toAssign[1:])


recursiveAssignment(assigned=((),(), (), ()), toAssign=tuple(arr))

def get_len_of_tuple(t):
    return len(t)

for s in sorted(set_of_assignments, key=get_len_of_tuple)[:2]:
    print(s)
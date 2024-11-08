fileContents = open("AdventOfCode2019/Day 24/input.txt")
rows = fileContents.read().split("\n")

state = set()
for row, r in enumerate(rows):
    for col, c in enumerate(r):
        if c == '#':
            state.add((row,col))

print(state)

def addpts(a,b,n):
    return (a+n[0], b+n[1])

def hasExactlyOneNeighbor(x,y,s):
    result = 0
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    for neighbor in neighbors:
        if addpts(x,y,neighbor) in s:
            result += 1
    return result == 1

def hasOneOrTwoNeighbors(x,y,s):
    result = 0
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    for neighbor in neighbors:
        if addpts(x,y,neighbor) in s:
            result += 1
    return result == 1 or result == 2


def update_state(s):
    new_state = set()
    for i in range(5):
        for j in range(5):
            if (i,j) in s:
                if hasExactlyOneNeighbor(i,j,s):
                    new_state.add((i,j))
            else:
                if hasOneOrTwoNeighbors(i,j,s):
                    new_state.add((i,j))
    return new_state

current_state = state
seen_states = set()
while tuple(current_state) not in seen_states:
    seen_states.add(tuple(current_state))
    current_state = update_state(current_state)

duplicated_state = current_state

total = 0
biodiversity_multiple = 1
for i in range(25):
    r = i // 5
    c = i % 5
    if (r,c) in duplicated_state:
        total += biodiversity_multiple
    biodiversity_multiple *= 2
print(total)
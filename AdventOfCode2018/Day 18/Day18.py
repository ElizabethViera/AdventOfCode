fileContents = open("AdventOfCode2018/Day 18/input.txt")
rows = fileContents.read().split("\n")

trees = set()
lumberyard = set()

for r,row in enumerate(rows):
    for c,col in enumerate(row):
        if col == '.':
            continue
        if col == '|':
            trees.add((r,c))
        if col == '#':
            lumberyard.add((r,c))
        
def add_pts(x,y):
    return x[0] + y[0], x[1] + y[1]

neighbors = [(-1,-1), (-1, 0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]


def update(t,l):
    new_t = set()
    new_l = set()
    for r in range(50):
        for c in range(50):
            current_point = (r,c)
            if current_point in t:
                # tree logic
                count = 0
                for neighbor in neighbors:
                    n = add_pts(neighbor, current_point)
                    if n in l:
                        count += 1
                if count >= 3:
                    new_l.add(current_point)
                else:
                    new_t.add(current_point)
            elif current_point in l:
                # lumber logic
                found_neighbor_tree = False
                found_neighbor_lumber = False
                for neighbor in neighbors:
                    n = add_pts(neighbor, current_point)
                    if n in l:
                        found_neighbor_lumber = True
                    elif n in t:
                        found_neighbor_tree = True
                if found_neighbor_lumber and found_neighbor_tree:
                    new_l.add(current_point)
            else:
                # open logic
                count = 0
                for neighbor in neighbors:
                    n = add_pts(neighbor, current_point)
                    if n in t:
                        count += 1
                if count >= 3:
                    new_t.add(current_point)
    return new_t, new_l

states_seen = dict()

for i in range(10):
    trees, lumberyard = update(trees, lumberyard)

print(len(trees)*len(lumberyard))


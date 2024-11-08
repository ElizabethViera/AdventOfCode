fileContents = open("AdventOfCode2023/Day 17/input.txt")
plot = fileContents.read().split("\n")
from queue import PriorityQueue

# dict from (row,col) to value
heatloss_map: dict[tuple[int,int], int] = dict()

for r, row in enumerate(plot):
    for c, col in enumerate(row):
        heatloss_map[(r,c)] = int(col)

directions = {
    'U': (0,-1),
    'D': (0,1),
    'R': (1,0),
    'L': (-1,0),
}

neighbors = {
    'U': ['U', 'L', 'R'],
    'D': ['D', 'L', 'R'],
    'L': ['U', 'D', 'L'],
    'R': ['U', 'D', 'R'],
}

def add_pts(a,b):
    return a[0] + b[0], a[1] + b[1]

def get_neighbors(row,col,dir):
    results = []
    neighbor_dirs = neighbors[dir]
    for n in neighbor_dirs:
        new_pt = add_pts((row,col), directions[n])
        if new_pt in heatloss_map:
            results.append((new_pt[0], new_pt[1], n))
    return results

def shortest_path():
    visited = set()
    best_distances: dict[tuple[int,int,str,int],int] = dict() #[row,col, direction, time_since_last_turn] to distance
    to_visit = PriorityQueue[tuple[int, tuple[int,int,str,int]]]()
    to_visit.put((0, (0,0,'D',0))) 
    to_visit.put((0, (0,0,'R',0)))
    while to_visit.qsize() > 0:
        current_node = to_visit.get()
        if current_node[1] in visited:
            continue
        visited.add(current_node[1])
        n = get_neighbors(current_node[1][0], current_node[1][1], current_node[1][2])
        for neighbor in n:
            if neighbor[2] == current_node[1][2]:
                if current_node[1][3] == 9:
                    continue
                since_last = current_node[1][3] + 1
            else:
                if current_node[1][3] < 3:
                    continue
                since_last = 0
            heatloss = current_node[0] + heatloss_map[(neighbor[0], neighbor[1])]
            if (neighbor[0], neighbor[1], neighbor[2], since_last) not in best_distances or heatloss < best_distances[(neighbor[0], neighbor[1], neighbor[2], since_last)]:
                best_distances[(neighbor[0], neighbor[1], neighbor[2], since_last)] = heatloss
            to_visit.put((heatloss, (neighbor[0], neighbor[1], neighbor[2], since_last)))
    return best_distances

best = 100000000
best_dist = shortest_path()
for k in best_dist:
    if k[0] == 140 and k[1] == 140:
        if best_dist[k] < best:
            best = best_dist[k]
print(best)

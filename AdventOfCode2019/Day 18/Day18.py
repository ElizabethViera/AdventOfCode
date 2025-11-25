from collections import deque


def parseGrid(s: str):
    walls: set[tuple[int,int]] = set() 
    keys = dict()
    doors = dict()
    keys_filtered = dict()
    for r, row in enumerate(s.split('\n')):
        for c, char in enumerate(row):
            coords = (r,c)
            if char == '#':
                walls.add(coords)
            elif char in 'abcdefghijklmnopqrstuvwxyz@':
                keys[coords] = char
                keys[char] = coords
                keys_filtered[char] = coords
            elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                doors[coords] = char
                doors[char] = coords
            else:
                continue
    return walls, keys, doors, keys_filtered

def add_pts(a,b):
    return a[0] + b[0], a[1] + b[1]

def getNeighbors(visiting, key_set, walls, doors, keys):
    neighbor_candidates = [(1,0), (0,1), (-1,0), (0,-1)]
    results = []
    for cand_dir in neighbor_candidates:
        cand = add_pts(cand_dir, visiting)
        if cand in walls:
            continue
        elif cand in keys:
            results.append(cand)
        elif cand in doors:
            if doors[cand].lower() in key_set:
                results.append(cand)
            else:
                continue
        else:
            results.append(cand)
    return results

def shortestPathWithKeys(key_set, source, target, walls, doors, keys):
    memoize_key = (tuple(sorted(key_set)), source, target)
    if memoize_key in found_dists:
        return found_dists[memoize_key]
    visited = dict()
    visited[source] = 0
    to_visit = deque([source])
    while target not in visited and to_visit:
        visiting = to_visit.popleft()
        neighbors = getNeighbors(visiting, key_set, walls, doors, keys)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = visited[visiting] + 1
                to_visit.append(neighbor)
    if target in visited:
        found_dists[memoize_key] = visited[target]
        return visited[target]
    else:
        found_dists[memoize_key] = None
        return None
    
def getNextOptionsWithCurrentPath(current_path, distance_so_far, source, walls, doors, keys):
    results = []
    for key in keys:
        if isinstance(key, str):
            if key not in current_path:
                dist = shortestPathWithKeys(current_path, source, keys[key], walls, doors, keys)
                if  dist != None:
                    results.append((current_path + [key], key, distance_so_far + dist))
    return results

def get_distance(path):
    return path[2]

def buildPath(s: str):
    count = 0
    all_visited = dict()
    shortest_complete = 4705
    walls, keys, doors, keys_filtered = parseGrid(s)
    all_results = []
    path_queue = [(['@'], '@', 0)]
    while path_queue != []:
        count += 1
        if count % 10000000 == 0:
            print(count // 10000000)
        # pruning
        current_path = path_queue.pop()
        if current_path[2] > shortest_complete:
            continue
        min_remaining = len(keys_filtered) - len(current_path[0])
        if current_path[2] + min_remaining > shortest_complete:
            continue
        current_location, current_key_set = current_path[1], tuple(sorted(current_path[0]))
        if (current_location, current_key_set) in all_visited and all_visited[(current_location, current_key_set)] < current_path[2]:
            continue
        else:
            all_visited[(current_location, current_key_set)] = current_path[2]
        # done pruning

        next_options = getNextOptionsWithCurrentPath(current_path[0], current_path[2], keys[current_path[1]], walls, doors, keys)
        if len(next_options) == 0:
            if len(current_path[0]) == len(keys_filtered):
                dist = get_distance(current_path)
                if dist < shortest_complete:
                    shortest_complete = dist
                    print("shortest so far: ", shortest_complete)
                all_results.append(dist)
        else:
            for option in next_options:
                path_queue.append(option)
    return sorted(all_results)[0]

fileContents = open("input.txt")
arr = fileContents.read()
found_dists = dict()
print(buildPath(arr))

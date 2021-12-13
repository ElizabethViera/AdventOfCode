fileContents = open("Day 12/input.txt")
arr = fileContents.read().split('\n')

nodes = set()
links = {}  # dictionary from nodes to nodes

for line in arr:
    left, right = line.split('-')[0], line.split('-')[1]
    nodes.add(left)
    nodes.add(right)
    if left not in links:
        links[left] = set()
    if right not in links:
        links[right] = set()
    links[left].add(right)
    links[right].add(left)

currentNode = 'start'
targetNode = 'end'

path_queue = [[currentNode]]
result_paths = 0

while path_queue != []:
    current_path = path_queue.pop()
    # print(path_queue)
    neighbors = links[current_path[-1]]
    for neighbor in neighbors:
        if neighbor == targetNode:
            result_paths += 1
            # print(current_path + [neighbor])
            continue
        if neighbor == 'start':
            continue
        if neighbor.lower() == neighbor and neighbor in current_path:
            if 'visited_twice' in current_path:
                continue
            else:
                path_queue.append(
                    current_path + ['visited_twice'] + [neighbor])
                continue
        path_queue.append(current_path + [neighbor])
        # print(len(path_queue))


print(result_paths)

fileContents = open("AdventOfCode2025/Day 8/input.txt")
arr = fileContents.read().split("\n")
# print(arr)

BOX_NUMBER = 1000

boxes = set()
box_dists = dict()

for box in arr:
    coords = box.split(",")
    x, y, z = coords[0], coords[1], coords[2]
    boxes.add((int(x), int(y), int(z)))


def getDist(b1, b2):
    x = (b2[0] - b1[0]) ** 2
    y = (b2[1] - b1[1]) ** 2
    z = (b2[2] - b1[2]) ** 2
    import math

    return math.sqrt(x + y + z)


for box in boxes:
    for box2 in boxes:
        if box == box2:
            continue

        distance = getDist(box, box2)
        distance_key = tuple(sorted([box, box2]))
        box_dists[distance_key] = distance
print(len(box_dists))


def makeConnections(distances):
    sorted_distances = sorted(distances.items(), key=lambda dist: dist[1])
    edges = set()
    for i in range(BOX_NUMBER):
        edges.add(sorted_distances[i])

    edge_dict = dict()
    for edge in edges:
        left = edge[0][0]
        right = edge[0][1]
        if left not in edge_dict:
            edge_dict[left] = []
        if right not in edge_dict:
            edge_dict[right] = []
        edge_dict[left].append(right)
        edge_dict[right].append(left)
    return edge_dict


edges = makeConnections(box_dists)


def getClustersAndSizes(nodes, edges):
    clusters = 0
    cluster_sizes = []
    visited = set()
    for node in nodes:
        if node not in edges:
            clusters += 1
            print(node)
        elif node not in visited:
            neighbors = [node]
            newly_visited = set()
            while neighbors != []:
                current = neighbors.pop()
                visited.add(current)
                newly_visited.add(current)
                new_neighbors = edges[current]
                for neighbor in new_neighbors:
                    if neighbor not in visited:
                        neighbors.append(neighbor)
            cluster_sizes.append(len(newly_visited))
            clusters += 1
        else:
            continue
    return clusters, cluster_sizes


clusters, sizes = getClustersAndSizes(boxes, edges)
print(clusters)

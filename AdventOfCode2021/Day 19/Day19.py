from os import write


fileContents = open("AdventOfCode2021/Day 19/input.txt")
arr = fileContents.read().split('\n')


def getOrientations(x, y, z):
    # Reflections are ruled out, so xyz has six orders (first six items), and then there are three additional ways for this to rotate without reflections. 1.Negative xy. 2. Negative xz. 3. Negative yz. This makes (6 x 4) = 24 possible orientations.
    return [
        [x, y, z], [-x, -z, -y], [-y, -x, -z], [y, z, x], [-z, -y, -x], [z, x, y],
        [-x, -y, z], [x, -z, y], [y, x, -z], [-y,
                                              z, -x], [-z, y, x], [z, -x, -y],
        [-x, y, -z], [x, z, -y],
        [-y, x, z], [y, -z, -x], [z, -y, x], [-z, -x, y],
        [x, -y, -z], [-x, z, y],
        [y, -x, z], [y, z, -x], [z, y, -x], [-z, x, -y]
    ]


scanners = []
scanner = []
for line in arr:
    if line == '':
        scanners.append(scanner)
        scanner = []
        continue
    if line.startswith('---'):
        continue
    beacon_coords = line.split(',')
    beacon_coords = [int(i) for i in beacon_coords]
    scanner.append(beacon_coords)


def rotateScanner(scanner):
    rotations = {}
    for beacon in scanner:
        a, b, c = beacon[0], beacon[1], beacon[2]
        beaconOrientations = getOrientations(a, b, c)
        for number, orientation in enumerate(beaconOrientations):
            if number not in rotations:
                rotations[number] = []
            rotations[number].append(orientation)
    return rotations


possibleMatches = set()
rotationDictionaries = {}
# rotationDictionaries[n] will return 24 sets of possible beacon coordinates for scanner n
for scannerNumber, scanner in enumerate(scanners):
    rotationDictionaries[scannerNumber] = rotateScanner(scanner)

# for baseScanner in rotationDictionaries:
#     baseDistances = set()
#     for rotation in [0]:
#         for i in range(len(rotationDictionaries[baseScanner][rotation])):
#             for j in range(len(rotationDictionaries[baseScanner][rotation])):
#                 if i == j:
#                     continue
#                 dx, dy, dz = rotationDictionaries[baseScanner][rotation][i][0] - rotationDictionaries[baseScanner][rotation][j][0], rotationDictionaries[baseScanner][rotation][i][1] - \
#                     rotationDictionaries[baseScanner][rotation][j][1], rotationDictionaries[baseScanner][rotation][i][2] - \
#                     rotationDictionaries[baseScanner][rotation][j][2]
#                 baseDistances.add((dx, dy, dz))
#     for comparisonScanner in range(0, len(rotationDictionaries)):
#         if comparisonScanner == baseScanner:
#             continue
#         for rotation in rotationDictionaries[comparisonScanner]:
#             comparisonCount = 0
#             for i in range(len(rotationDictionaries[comparisonScanner][rotation])):
#                 for j in range(len(rotationDictionaries[comparisonScanner][rotation])):
#                     if i == j:
#                         continue
#                     dx, dy, dz = rotationDictionaries[comparisonScanner][rotation][i][0] - rotationDictionaries[comparisonScanner][rotation][j][0], rotationDictionaries[comparisonScanner][rotation][i][1] - \
#                         rotationDictionaries[comparisonScanner][rotation][j][1], rotationDictionaries[comparisonScanner][rotation][i][2] - \
#                         rotationDictionaries[comparisonScanner][rotation][j][2]
#                     if (dx, dy, dz) in baseDistances:
#                         comparisonCount += 1
#                         if comparisonCount == 125:
#                             possibleMatches.add(
#                                 (baseScanner, comparisonScanner, rotation))


# outputFile = open("AdventOfCode2021/Day 19/output.txt", "a")
# deduplicateMatches = set()
# for match in possibleMatches:
#     if (match[0], match[1]) in deduplicateMatches or (match[1], match[0]) in deduplicateMatches:
#         continue
#     deduplicateMatches.add((match[0], match[1]))
#     outputFile.write(str(match))
#     outputFile.write("\n")

def create_opposite_rotation_dict():
    resultDictionary = {}
    rotationList = getOrientations(1, 2, 3)
    for rotation in rotationList:
        x, y, z = rotationList[rotation]
        oppositeRotationList = getOrientations[x, y, z]
        for oppositeRotation in oppositeRotationList:
            if oppositeRotationList[oppositeRotation] == (1, 2, 3):
                resultDictionary[rotation] = oppositeRotation
    print(resultDictionary)


def add_tuples(p, q):
    return (p[0] + q[0], p[1] + q[1], p[2] + q[2])


def subtract_tuples(p, q):
    return (p[0] - q[0], p[1] - q[1], p[2] - q[2])


def checkOffset(offset, leftSet, rightSet):
    count = 0
    for item_left in leftSet:
        if add_tuples(item_left, offset) in rightSet:
            count += 1
            if count == 12:
                return True
    return False


def getOffset(leftSet, rightSet):
    for leftItem in leftSet:
        for rightItem in rightSet:
            possible_offset = subtract_tuples(rightItem, leftItem)
            if checkOffset(possible_offset, leftSet, rightSet):
                return possible_offset
    return None

##### Part 1 Part 2 ######


fileContents = open("AdventOfCode2021/Day 19/output.txt")
possibleMatches = fileContents.read().split('\n')

offsets = {}
neighbors = {}


def getOppositeRotation(rotation):
    pass


def getNegativeOffset(offset):
    x, y, z = offset
    return (-x, -y, -z)


secondOutputFile = open("AdventOfCode2021/Day 19/output2.txt", "a")
for possibleMatch in possibleMatches:
    stripParents = possibleMatch[1:-1]
    candidate = stripParents.split(", ")
    left, right, rotation = int(candidate[0]), int(
        candidate[1]), int(candidate[2])
    leftList, rightList = rotationDictionaries[left][0], rotationDictionaries[right][rotation]
    leftSet, rightSet = set([tuple(triplet) for triplet in leftList]), set(
        [tuple(triplet) for triplet in rightList])
    offset = getOffset(leftSet, rightSet)
    if offset is not None:
        if left not in neighbors:
            neighbors[left] = []
        if right not in neighbors:
            neighbors[right] = []
        neighbors[left].append(right)
        neighbors[right].append(left)
        offsets[(left, right)] = (rotation, offset)
        offsets[(right, left)] = (getOppositeRotation(
            rotation), getNegativeOffset(offset))
        offsets[offset] = (left, right, rotation)


secondOutputFile.write(str(offsets))

create_opposite_rotation_dict()


def buildBeaconGraph(neighborGraph, offsetDict):
    visitedNodes = (0)
    visitedNodesBeacons = set(rotationDictionaries[0][0])

    neighbor_queue = neighbors[0]
    while neighbor_queue != []:
        current_node = neighbor_queue.pop()
        for neighbor in neighborGraph[current_node]:
            if neighbor in visitedNodes:
                continue

fileContents = open("AdventOfCode2022/Day 12/input.txt")
arr = fileContents.read().split("\n")
import string

heightMap = []
possibleStart = []
for row, line in enumerate(arr):
    currentArr = []
    for column, letter in enumerate(line):
        if letter == 'a':
            possibleStart.append( (row,column))
        if letter == 'S':
            startCoords = (row,column)
            currentArr.append('a')
            continue
        if letter == 'E':
            endCoords = (row,column)
            currentArr.append('z')
            continue
        currentArr.append(letter)
    heightMap.append(currentArr)

# print(heightMap)
print(startCoords, endCoords)

# index into this
alphabet = [i for i in string.ascii_lowercase]

connections = {}

dirs = [(-1, 0), (1,0), (0,1), (0,-1)]

def move(direction, row, col):
    return direction[0] + row, direction[1] + col

def inBounds(neighborRow, neighborCol):
    return neighborRow >= 0 and neighborRow < len(heightMap) and neighborCol >= 0 and neighborCol < len(heightMap[0])

def getNeighbors(row, col):
    result = []
    for direction in dirs:
        neighborRow, neighborCol = move(direction, row, col)
        if inBounds(neighborRow, neighborCol):
            if alphabet.index(heightMap[neighborRow][neighborCol]) <= alphabet.index(heightMap[row][col]) + 1:
                result.append((neighborRow, neighborCol))
            
    return result

for row in range(len(heightMap)):
    for col in range(len(heightMap[0])):
        connections[(row,col)] = getNeighbors(row,col)
'''
for connection in connections:
    print(connection)
    print(connections[connection])
'''

def findShortestPath(startCoords):
    distance_from_start = {}
    distance_from_start[startCoords] = 0

    nodes_to_check = [startCoords]
    visited = set()
    while nodes_to_check != []:
        current_node = nodes_to_check.pop(0)
        if current_node in visited:
            continue
        else:
            visited.add(current_node)
            neighbors = connections[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    nodes_to_check.append(neighbor)
                    if neighbor in distance_from_start:
                        distance_from_start[neighbor] = min(distance_from_start[current_node]+1, distance_from_start[neighbor]) 
                    else:
                        distance_from_start[neighbor] = distance_from_start[current_node] + 1
    if endCoords in distance_from_start:
        return distance_from_start[endCoords]
    else:
        return 100000

    '''
    for distance in distance_from_start:
        print(distance)
        print(distance_from_start[distance])
    '''

answers = []
for start in possibleStart:
    answers.append(findShortestPath(start))

print(sorted(answers))
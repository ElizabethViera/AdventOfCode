fileContents = open("AdventOfCode2022/Day 24/input.txt")
arr = fileContents.read().split("\n")

walls = set()
blizzards = {}
blizzards[0] = {}
width = 120
height = 26
for row, line in enumerate(arr):
    for col, c in enumerate(line):
        if c == '#':
            walls.add((row,col))
        if c == '>':
            blizzards[0][(row,col, '>')] = '>'
        if c == '<':
            blizzards[0][(row,col, '<')] = '<'
        if c == 'v':
            blizzards[0][(row,col, 'v')] = 'v'
        if c == '^':
            blizzards[0][(row,col, '^')] = '^'

def getNextBlizzardSpot(point, direction):
    match direction:
        case '>':
            if (point[0], point[1]+1) in walls:
                return (point[0], 1)
            else:
                return (point[0], point[1]+1)
        
        case '<':
            if (point[0], point[1]-1) in walls:
                return (point[0], width)
            else:
                return (point[0], point[1]-1)

        
        case '^':
            if (point[0]-1, point[1]) in walls:
                return (height, point[1])
            else:
                return (point[0]-1, point[1])
        
        case 'v':
            if (point[0]+1, point[1]) in walls:
                return (2, point[1])
            else:
                return (point[0]+1, point[1])

def setBlizzardArray(blizzards):
    for i in range(1, 3000):
        blizzards[i] = {}
        for blizzard in blizzards[i-1]:
            newpoint = getNextBlizzardSpot(blizzard[:2], blizzard[2])
            blizzards[i][newpoint + (blizzard[2],)] = blizzard[2]
    return blizzards
#print(blizzards)

setBlizzardArray(blizzards)

blizzard_dirs = ['>', '<', '^', 'v']

def getNeighbors(point, i):
    neighbors = set()
    neighbor_dirs = [(-1,0), (0,-1), (1,0), (0,1), (0,0)]
    for direction in neighbor_dirs:
        neighbor = (point[0] + direction[0], point[1] + direction[1])
        if neighbor in walls or any(neighbor + (direction,) in blizzards[i+1] for direction in blizzard_dirs):
            continue
        neighbors.add(neighbor)
    return neighbors



def findPath(start):
    queue = set([start])
    for step in range(0,1000):
        next_queue = set()
        for item in queue:
            neighbors = getNeighbors(item, step)
            for neighbor in neighbors:
                if neighbor == destination:
                    return step + 1, blizzards[step+1]
                next_queue.add(neighbor)
        queue = next_queue
        
        print(step+1, queue)
        '''
        for blizzard in blizzards[step]:
            print(blizzard)
        '''

start = (1,1)
destination = (27,120)

result1, blizzard_config = findPath(start)

blizzards = {}
blizzards[0] = blizzard_config
setBlizzardArray(blizzards)

destination = (1,1)
start = (27,120)

result2, blizzard_config = findPath(start)

blizzards = {}
blizzards[0] = blizzard_config
setBlizzardArray(blizzards)

start = (1,1)
destination = (27,120)

result3, blizzard_config = findPath(start)

print(result1 + result2 + result3)


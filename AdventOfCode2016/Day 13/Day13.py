def isWall(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += 1362
    n = str(bin(n))
    ones = 0
    for c in n:
        if c == '1':
            ones += 1
    return ones%2 == 1

def addpts(x, y):
    return (x[0] + y[0], x[1] + y[1])

neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
def getNeighbors(pt):
    results = []
    for neighbor in neighbors:
        n = addpts(neighbor, pt)
        if not isWall(*n) and n[0] >= 0 and n[1] >= 0:
            results.append(n)
    return results



lets_walk = set()
queue: list[tuple[int, tuple[int,int]]] = [(0, (1,1))]

while True:
    queue = sorted(queue)
    current = queue.pop(0)
    steps = current[0]
    if steps > 50:
        print(queue)
        break
    if current[1] in lets_walk:
        continue
    lets_walk.add(current[1])
    for neighbor in getNeighbors(current[1]):
        queue.append((steps+1, neighbor))
        
print(len(lets_walk), lets_walk)

fileContents = open("AdventOfCode2017/Day 20/input.txt")
arr = fileContents.read().split('\n')

#p=<-1027,-979,-188>, v=<7,60,66>, a=<9,1,-7>

coords = dict()
for i, particle in enumerate(arr):
    p,v,a = particle.split(', ')[0], particle.split(', ')[1], particle.split(', ')[2]
    pcoords = tuple([int(x) for x in p[3:-1].split(',')])
    vcoords = tuple([int(x) for x in v[3:-1].split(',')])
    acoords = tuple([int(x) for x in a[3:-1].split(',')])
    coords[i] = dict()
    coords[i]['pos'] = pcoords
    coords[i]['vel'] = vcoords
    coords[i]['acc'] = acoords

def addTriple(a: tuple[int,int,int],b: tuple[int,int,int]):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def takeStep(i):
    coords[i]['vel'] = addTriple(coords[i]['vel'], coords[i]['acc'])
    coords[i]['pos'] = addTriple(coords[i]['vel'], coords[i]['pos'])


for _ in range(10000):
    currentPositions = dict()
    for i in coords:
        takeStep(i)
        if coords[i]['pos'] not in currentPositions:
            currentPositions[coords[i]['pos']] = []
        currentPositions[coords[i]['pos']].append(i)
    for k in currentPositions:
        if len(currentPositions[k]) > 1:
            for particle in currentPositions[k]:
                del coords[particle]

print(len(coords))
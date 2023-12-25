from dataclasses import dataclass

fileContents = open("AdventOfCode2021/Day 19/sampleInput.txt")
arr = fileContents.read().split("\n")

pos3 = tuple[int, int, int]

def parseScanners(arr) -> dict[str, list[pos3]]:
    scanners = dict()
    scanner = []
    current_scanner = [-1]
    for line in arr:
        if line.startswith('--- scanner'):
            scanner = []
            current_scanner = line.split(' ')[-2]
        elif line == '':
            scanners[current_scanner] = scanner
        else:
            left, right, forward = int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])
            scanner.append((left,right, forward))
    return scanners

def dotProduct(u:pos3,v:pos3) -> int:
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def crossProduct(u:pos3, v:pos3) -> pos3:
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

def getOrientations(p: pos3) -> list[pos3]:
    '''
    Reflections are ruled out, so xyz has six orders (first six items), and then there are three additional ways for this to rotate without reflections. 1.Negative xy. 2. Negative xz. 3. Negative yz. This makes (6 x 4) = 24 possible orientations.
    '''
    x, y, z = p
    a = [
        (x, y, z), (-x, -z, -y), (-y, -x, -z), (y, z, x), (-z, -y, -x), (z, x, y),
        (-x, -y, z), (x, -z, y), (y, x, -z), (-y, z, -x), (-z, y, x), (z, -x, -y),
        (-x, y, -z), (x, z, -y),
        (-y, x, z), (y, -z, -x), (z, -y, x), (-z, -x, y),
        (x, -y, -z), (-x, z, y),
        (y, -x, z), (y, z, -x), (z, y, -x), (-z, x, -y)
    ]
    
    axis = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
    outputs = []
    for a1 in axis:
        for a2 in axis:
            if dotProduct(a1, a2) == 0:
                a3 = crossProduct(a1,a2)
                outputs.append((dotProduct(a1,p), dotProduct(a2,p), dotProduct(a3,p)))
    if sorted(a) != sorted(outputs):
        print(sorted(a), '\n', '\n', sorted(outputs))
        raise(ValueError)
    return outputs

    

def getAllOrientationsForScanner(s: list[pos3]) -> list[list[pos3]]:
    results : list[list[pos3]] = [[] for i in range(24)]
    for beacon in s:
        orientations = getOrientations(beacon)
        for i, orientation in enumerate(orientations):
            results[i].append(orientation)
    return results


@dataclass
class Scanner():
    position: pos3
    name: str

@dataclass
class Region():
    scanners: list[Scanner]
    beacons: set[pos3]


def subtractPts(a:pos3,b:pos3)-> pos3:
    return a[0]-b[0], a[1]-b[1], a[2]-b[2]

def addPts(a:pos3,b:pos3)-> pos3:
    return a[0]+b[0], a[1]+b[1], a[2]+b[2]

def OrientationHasSoManyThingsInCommon(o: list[pos3], becons:list[pos3])-> pos3|None:
    all_offsets_count = dict()
    for p in o:
        for b in becons:
            possibleOffset = subtractPts(p,b)
            if possibleOffset not in all_offsets_count:
                all_offsets_count[possibleOffset] = 0
            all_offsets_count[possibleOffset] += 1
    for offset in all_offsets_count:
        if all_offsets_count[offset] >= 6:
            return offset
    return None

def addScannerToRegion(scanner_name: str, scanner_with_orientation: list[list[pos3]], region: Region)-> Region | None:
    for orientation in scanner_with_orientation:
        offset = OrientationHasSoManyThingsInCommon(orientation, list(region.beacons))
        if offset is not None:
            for b in orientation:
                region.beacons.add(addPts(b, offset))
            s = Scanner(name=scanner_name, position=offset)
            region.scanners.append(s)
            return region
    return None

scanner_dict = parseScanners(arr)

scanner_dict_with_orientations: dict[str, list[list[pos3]]] = dict()


for scanner in scanner_dict:
    beacons_at_ith_orientation = getAllOrientationsForScanner(scanner_dict[scanner])
    for i in beacons_at_ith_orientation:
        scanner_dict_with_orientations[scanner] = beacons_at_ith_orientation

the_ultimate_answer = Region(
    scanners=list([Scanner(name='0', position=(0,0,0))]),
    beacons=set(scanner_dict_with_orientations['0'][0]),
)


for scanner,orientations in scanner_dict_with_orientations.items():
    if scanner not in [s.name for s in the_ultimate_answer.scanners]:
        possible_addition = addScannerToRegion(scanner, orientations, the_ultimate_answer)
        if possible_addition is not None:
            the_ultimate_answer = possible_addition

    

print(the_ultimate_answer.scanners)
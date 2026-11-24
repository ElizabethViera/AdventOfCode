from dataclasses import dataclass

fileContents = open("AdventOfCode2021/Day 19/input.txt")
arr = fileContents.read().split("\n\n")


NUMBER_OF_ROTATIONS = 24


@dataclass
class Transform:
    transformations: "list[Rotation | pt]"

    def applyTransformation(self, p: "pt") -> "pt":
        resultP = p
        for t in self.transformations:
            if isinstance(t, Rotation):
                resultP = t.rotatePoint(resultP)
            else:
                assert isinstance(t, pt), t
                resultP = resultP.offset(t.negativeOffset())
        return resultP

    def reverseTransformation(self) -> "Transform":
        reversedTransformationList: list[Rotation | pt] = []
        for t in self.transformations[::-1]:
            if isinstance(t, Rotation):
                reversedTransformationList.append(t.getInverse())
            else:
                reversedTransformationList.append(t.negativeOffset())
        return Transform(transformations=reversedTransformationList)


@dataclass
class Rotation:
    perms: tuple[int, int, int]  # location of original thing
    negations: tuple[int, int, int]  # plus or minus 1

    def rotatePoint(self, o: "pt") -> "pt":

        permedPoint = pt(
            x=o.getCoord(self.perms[0]),
            y=o.getCoord(self.perms[1]),
            z=o.getCoord(self.perms[2]),
        )
        negatedPoint = pt(
            x=permedPoint.x * self.negations[0],
            y=permedPoint.y * self.negations[1],
            z=permedPoint.z * self.negations[2],
        )
        return negatedPoint

    def getInverse(self):
        perms = tuple([self.perms.index(i) for i in range(3)])
        negations = tuple([self.negations[i] for i in perms])
        inverse = Rotation(perms=perms, negations=negations)  # pyright: ignore
        return inverse


@dataclass(frozen=True)
class pt:
    x: int
    y: int
    z: int

    def getCoord(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        if i == 2:
            return self.z
        raise (ValueError)

    def negativeOffset(self) -> "pt":
        return pt(x=-self.x, y=-self.y, z=-self.z)

    def __repr__(self) -> str:
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)

    def offset(self, other: "pt") -> "pt":
        return pt(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def selfPlusOffsetInOtherBeacons(self: "pt", other: set["pt"], offset: "pt"):
        toCheck = pt(x=self.x - offset.x, y=self.y - offset.y, z=self.z - offset.z)
        return toCheck in other

    def rotate(self) -> list["pt"]:
        results = []
        for r in rotationsList:
            results.append(r.rotatePoint(self))
        return results


@dataclass
class Scanner:
    beacons: list[pt]

    def __repr__(self) -> str:
        result = "\n\n"
        for i, beacon in enumerate(self.beacons):
            result += str(i) + ": " + repr(beacon) + "\n"
        result += "\n\n"
        return result

    def rotateScanner(self) -> list["Scanner"]:
        rotations: dict[int, list[pt]] = dict()
        for beacon in self.beacons:
            twentyFourRotatedBeacons = beacon.rotate()
            for j in range(NUMBER_OF_ROTATIONS):
                if j not in rotations:
                    rotations[j] = []
                rotations[j].append(twentyFourRotatedBeacons[j])
        result: list[Scanner] = []
        for i in rotations:
            result.append(Scanner(rotations[i]))
        return result

    def isOverlap(self, other: "Scanner") -> Transform | None:

        selfRotations = self.rotateScanner()
        for i, s1 in enumerate(selfRotations):
            result = (
                someAmountSubtractedOrAddedMakesTheseHaveAtLeastTwelveMatchingBeacons(
                    s1, other
                )
            )
            if result is not None:
                resultTransformation = Transform(
                    [rotationsList[i], result.negativeOffset()]
                )
                return resultTransformation
        return None


def parseInput(textInput: list[str]) -> list[Scanner]:
    scannersList = []
    for scanner in textInput:
        beacons = []
        for beacon in scanner.split("\n")[1:]:
            x, y, z = beacon.split(",")
            newPt = pt(x=int(x), y=int(y), z=int(z))
            beacons.append(newPt)
        newScanner = Scanner(beacons=beacons)
        scannersList.append(newScanner)
    return scannersList


def someAmountSubtractedOrAddedMakesTheseHaveAtLeastTwelveMatchingBeacons(
    s1: Scanner, s2: Scanner
) -> pt | None:
    offsetCounts = dict()
    for s1Beacon in s1.beacons:
        for s2Beacon in s2.beacons:
            offset = s1Beacon.offset(s2Beacon)
            if offset not in offsetCounts:
                offsetCounts[offset] = 0
            offsetCounts[offset] += 1
            if offsetCounts[offset] == 12:
                return offset
    return None


def isNegated(s):
    return s[0] == "-"


def parseRotations(s):
    rotationsList = []
    for rotation in s:
        first, second, third = rotation.split(", ")
        firstNegated, secondNegated, thirdNegated = (
            -1 if isNegated(first) else 1,
            -1 if isNegated(second) else 1,
            -1 if isNegated(third) else 1,
        )
        negations = (firstNegated, secondNegated, thirdNegated)
        threeItemList = [first[-1], second[-1], third[-1]]
        perms = (
            threeItemList.index("x"),
            threeItemList.index("y"),
            threeItemList.index("z"),
        )
        rotationsList.append(Rotation(perms, negations))  # pyright: ignore
    return rotationsList


input2Contents = open("AdventOfCode2021/Day 19/input2.txt")
arr2 = input2Contents.read().split("\n")
rotationsList = parseRotations(arr2)


parsed = parseInput(arr)
overlaps: list[tuple[int, int, Transform]] = []
for i in range(len(parsed)):
    for j in range(len(parsed)):
        if i < j:
            result = parsed[i].isOverlap(parsed[j])
            if result is not None:
                overlaps.append((i, j, result))

testOverlap = overlaps[0]
testScanner = parsed[testOverlap[1]]
for beacon in testScanner.beacons:
    reversedTransformation = testOverlap[2].reverseTransformation()
    newBeacon = reversedTransformation.applyTransformation(beacon)


def getNeighbors(
    i: int, overlaps: list[tuple[int, int, Transform]]
) -> list[tuple[int, Transform]]:
    results: list[tuple[int, Transform]] = []
    for n in overlaps:
        if n[0] == i:
            results.append((n[1], n[2]))
        elif n[1] == i:
            results.append((n[0], n[2].reverseTransformation()))
    return results


homeTransforms: dict[int, list[Transform]] = dict()
# j (index into parsed) to list of transforms
homeTransforms[0] = []
while len(homeTransforms) < len(parsed):
    for i, scanner in enumerate(parsed):
        if i in homeTransforms:
            continue
        neighbors: list[tuple[int, Transform]] = getNeighbors(i, overlaps)
        for neighbor in neighbors:
            if neighbor[0] in homeTransforms:
                homeTransforms[i] = homeTransforms[neighbor[0]] + [neighbor[1]]


bigResultSet: set[pt] = set()
for h in homeTransforms:
    theseBeacons = parsed[h].beacons
    theseTransforms = homeTransforms[h][::-1]
    for b in theseBeacons:
        newBeacon = b
        for t in theseTransforms:
            newBeacon = t.applyTransformation(newBeacon)
        bigResultSet.add(newBeacon)

# Calculate Manhattan Distance
largestDistance = 0


def calculateManhattan(
    p1, p2
) -> int:  # Shamelessly stolen from my own Day6.py of 2018 and adapted to this
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)


for b1 in bigResultSet:
    for b2 in bigResultSet:
        if b1 == b2:
            continue
        dist = calculateManhattan(b1, b2)
        if dist > largestDistance:
            print(b1, b2, dist)
            largestDistance = dist
print(dist)

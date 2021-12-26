fileContents = open("AdventOfCode2021/Day 18/input.txt")
arr = fileContents.read().split('\n')
numsToAdd = []
for line in arr:
    numToAdd = []
    for c in line:
        if c in '0123456789':
            numToAdd.append(int(c))
        else:
            numToAdd.append(c)
    numsToAdd.append(numToAdd)


def addNums(x, y):
    return reduceNum(['['] + x + [','] + y + [']'])


def stringifyNum(x):
    result = ""
    for c in x:
        result += str(c)
    return result


def splittingNums(x):
    for i, c in enumerate(x):
        if isinstance(c, int) and c > 9:
            return x[:i] + ['['] + [c//2] + \
                    [','] + [(1+c)//2] + [']'] + x[i+1:]
    return x


def isExplodingNums(x):
    depth = 0
    for i, c in enumerate(x):
        if c == '[':
            depth += 1
        if c == ']':
            depth -= 1
        if depth == 5:
            return i
    return None


def explodeNums(x, i):
    rightmost_left_number = None
    leftmost_right_number = None
    # get num to left
    for left in range(i-1, 0, -1):
        if isinstance(x[left], int):
            rightmost_left_number = left
            break
    # get num to right
    for right in range(i+4, len(x)):
        if isinstance(x[right], int):
            leftmost_right_number = right
            break
    if leftmost_right_number is not None:
        x[leftmost_right_number] += x[i+3]
    if rightmost_left_number is not None:
        x[rightmost_left_number] += x[i+1]
    x = x[:i] + [0] + x[i+5:]
    return x


def reduceNum(x):
    new_x = list(x)
    i = isExplodingNums(x)
    if i is not None:
        # print("explodes")
        new_x = explodeNums(new_x, i)
        # print(stringifyNum(x), '\n', stringifyNum(new_x))
        return reduceNum(new_x)
    else:
        # print("splits")
        new_x = splittingNums(x)
        # print(stringifyNum(x), '\n', stringifyNum(new_x))
    return x if new_x == x else reduceNum(new_x)


def getMagnitude(x):
    times_three = 0
    times_two = 0
    result = 0
    for c in x:
        if c == '[':
            times_three += 1
        elif c == ',':
            times_three -= 1
            times_two += 1
        elif c == ']':
            times_two -= 1
        else:
            result += 3**times_three * 2**times_two * c
    return result


greatestMagnitude = 0
for i in range(len(numsToAdd)):
    for j in range(len(numsToAdd)):
        if i != j:
            magnitude = getMagnitude(addNums(numsToAdd[i], numsToAdd[j]))
            if magnitude > greatestMagnitude:
                greatestMagnitude = magnitude
print(greatestMagnitude)

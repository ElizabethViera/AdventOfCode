fileContents = open("AdventOfCode2016/Day 7/input.txt")
arr = fileContents.read().split("\n")

def getABAs(s):
    results = []
    first_character = s[0]
    second_character = s[1]
    for third_character in s[2:]:
        if first_character == third_character and first_character != second_character:
            results.append([first_character, second_character])
        first_character = second_character
        second_character = third_character
    
    return results

def isABABAB(line):
    # print(line)
    foundABABAB = False
    outsideContents: list[list[str]] = []
    segment: list[str] = []
    for c in line:
        if c == '[':
            outsideContents.append(segment)
            segment = []
        elif c == ']':
            segment = []
        else:
            segment.append(c)
    outsideContents.append(segment)

    segment = []
    insideContents: list[list[str]] = []
    for c in line:
        if c == '[':
            segment = []
        elif c == ']':
            insideContents.append(segment)
            segment = []
        else:
            segment.append(c)

    #print(outsideContents)
    for segment in outsideContents:
        abas = getABAs(segment)
        for aba in abas:
            bab: str = aba[1] + aba[0] + aba[1]
            for insegment in insideContents:
                if bab in ''.join(insegment):
                    foundABABAB = True
                    break
            if foundABABAB:
                break
        if foundABABAB:
            break
    return foundABABAB

total = 0
for line in arr:
    if isABABAB(line):
        #print(line)
        total += 1
print(total)
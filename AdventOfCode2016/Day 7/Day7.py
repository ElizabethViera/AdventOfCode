def searchWholeStringForReverse(s, s2):
    expected1 = s2[0]
    expected2 = s2[1]
    expected3 = s2[0]
    first = s[0]
    second = s[1]
    for third in s[2:]:
        if first == expected1 and second == expected2 and third == expected3:
            return True
        else:
            first = second
            second = third
    return False

def searchExteriorOfBrackets(s):
    first = s[0]
    second = s[1]
    for third in s[2:]:
        if first == third and first != second:
            return True
        else:
            first = second
            second = third
    return False

fileContents = open("AdventOfCode2016/Day 7/input.txt")
arr = fileContents.read().split("\n")

result = 0

for line in arr:
    segments = line.split('[')
    segments[0]
        
    for segment in segments[1:]:
        interior, exterior = segment.split(']')[0], segment.split(']')[1]
        if searchInteriorOfBrackets(interior):
            hasInnerString = True
        if searchExteriorOfBrackets(exterior):
            hasOutterString = True
    if hasOutterString and not hasInnerString:
        result += 1

print(result)
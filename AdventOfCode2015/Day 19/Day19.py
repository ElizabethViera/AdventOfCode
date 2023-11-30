goalString = 'CRSRGPIMYGPIRFDSTFDGSTSTPBGGSRSRIIMDPBGPMYPIRFDFDGSRBPMDPRGPIRFDGSTGGFDPBGGPIIRFDGSRSAYSTRFDDGSRBFDGGSRSTGGGFYGPIBGSTGSTPMDSRGPBFYGGFDGGGGSTGSRPRFDPBSTPRFDSRMDGFYFDGSRSADIIIIIIIRPMDPIIIBSRSADIIRPMDGFYBPBPIRSRMDSTGFDGSTFDPRFDGSRIBSTSRSAYGFDPRFDSTGFDGGSTGGGSRPRGFDFYPMDGPBGPBSRFYPBGFDGSA'

fileContents = open("AdventOfCode2015/Day 19/input.txt")
replacementRules = fileContents.read().split("\n")

rulesDict = dict()

for replacementRule in replacementRules:
    key = replacementRule.split(' ')[0]
    value = replacementRule.split(' ')[-1]
    if key not in rulesDict:
        rulesDict[key] = []
    rulesDict[key].append(value)
# print(rulesDict)


def replaceKeyWithValueAll(stringToBeReplaced, key, value):
    segments = stringToBeReplaced.split(key)
    results = set()
    if len(segments) > 1:
        for segment in range(1, len(segments)):
            fixedResult = key.join(segments[:segment])
            unfixedResult = value + key.join(segments[segment:])
            results.add((fixedResult, unfixedResult))
    return results

def getNextSetOfValues(setOfValues):
    results = set()
    for value in setOfValues:
        for rule in rulesDict:
            for replacementValue in rulesDict[rule]:
                allReplacementsForValue = replaceKeyWithValueAll(value[1], rule, replacementValue)
                for resultValue in allReplacementsForValue:
                       results.add((value[0] + resultValue[0], resultValue[1]))
    return results

def isValid(result):
    return goalString.startswith(result[0]) and len(result[0]) + len(result[1]) <= len(goalString)


initSetOfValues = set([('','e')])
total = 0
currentSetOfValues = initSetOfValues
print(len(getNextSetOfValues(initSetOfValues)))
print(getNextSetOfValues(initSetOfValues))
while goalString not in currentSetOfValues:
    currentSetOfValues = getNextSetOfValues(currentSetOfValues)
    currentSetOfValues = set([i for i in currentSetOfValues if isValid(i)])
    total += 1
    print(currentSetOfValues)
    print(total)
    if total == 3:
        break
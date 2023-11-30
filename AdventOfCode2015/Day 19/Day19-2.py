goalString = 'CRSRGPIMYGPIRFDSTFDGSTSTPBGGSRSRIIMDPBGPMYPIRFDFDGSRBPMDPRGPIRFDGSTGGFDPBGGPIIRFDGSRSAYSTRFDDGSRBFDGGSRSTGGGFYGPIBGSTGSTPMDSRGPBFYGGFDGGGGSTGSRPRFDPBSTPRFDSRMDGFYFDGSRSADIIIIIIIRPMDPIIIBSRSADIIRPMDGFYBPBPIRSRMDSTGFDGSTFDPRFDGSRIBSTSRSAYGFDPRFDSTGFDGGSTGGGSRPRGFDFYPMDGPBGPBSRFYPBGFDGSA'

fileContents = open("AdventOfCode2015/Day 19/input.txt")
replacementRules = fileContents.read().split("\n")

rulesDict = dict()

import sys
sys.setrecursionlimit(20000)

for replacementRule in replacementRules:
    key = replacementRule.split(' ')[0]
    value = replacementRule.split(' ')[-1]
    if key not in rulesDict:
        rulesDict[key] = []
    rulesDict[key].append(value)
# print(rulesDict)

from functools import cache

@cache
def minRules(s, t):
    if s == t:
        return 0
    if len(s) >= len(t):
        return None
    if s == '':
        return None
    if len(s) == 1:
        if s not in rulesDict:
            return None
        transformations = rulesDict[s]
        minTransformation = None
        for transformation in transformations:
            candidate = minRules(transformation, t)
            if candidate == None:
                continue
            if minTransformation is not None:
                minTransformation = min(candidate + 1, minTransformation)
            else:
                minTransformation = candidate + 1
        return minTransformation
    
    minimumReturn = None
    for n in range(1,len(t)):
        leftHand = minRules(s[0], t[:n])
        rightHand = minRules(s[1:], t[n:])
        if leftHand == None or rightHand == None:
            continue
        candidate = leftHand + rightHand 
        if minimumReturn == None:
            minimumReturn = candidate
        else:
            minimumReturn = min(minimumReturn, candidate)
    return minimumReturn

print(minRules('e', goalString))


    
    
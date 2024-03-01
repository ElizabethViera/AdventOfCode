from typing import cast


fileContents = open("AdventOfCode2017/Day 24/input.txt")
dominos = fileContents.read().split('\n')

all_dominos: set[tuple[int,int]] = set()
for domino in dominos:
    left, right = domino.split('/')
    all_dominos.add(cast(tuple[int,int], tuple(sorted([int(left),int(right)]))))

def getNextCandidates(unusedItems, rightMost) -> set[str]:
    result = set()
    for left,right in unusedItems:
        if left == rightMost:
            result.add(right)
        if right == rightMost:
            result.add(left)
    return result

def score(chain):
    return (len(chain), sum(chain))

def extendSelf(chain, rightMost, unusedItems) -> tuple[str, ...]:
    candidates = getNextCandidates(unusedItems, rightMost)
    bestCandidate = chain
    bestCandidateScore = score(chain)
    for candidate in candidates:
        nextChain = chain + (rightMost,) + (candidate,)
        nextUnusedItems = set(unusedItems)
        nextUnusedItems.remove(tuple(sorted([rightMost, candidate])))
        bestExtension = extendSelf(nextChain, candidate, nextUnusedItems)
        bestExtensionScore = score(bestExtension)
        if bestExtensionScore > bestCandidateScore:
            bestCandidate = bestExtension
            bestCandidateScore = bestExtensionScore
    return bestCandidate

starting_set = [(0,45), (0,39), (0,43)]
best = None
for start in starting_set:
    best = extendSelf((start), start[1], all_dominos)
    print(best)
    print(score(best))
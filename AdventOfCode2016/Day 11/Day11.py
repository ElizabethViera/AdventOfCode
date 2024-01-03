from dataclasses import dataclass
import itertools
from collections import deque


@dataclass(frozen=True)
class Configuration:
    items: tuple[tuple[str, int],...]
    me: int

    def itemsAsDict(self) -> dict[str, int]:
        return dict(self.items)
    
    def replaceItem(self, str, floor) -> "Configuration":
        newDict = self.itemsAsDict()
        newDict[str] = floor
        newMe = floor
        return Configuration(items=tuple(newDict.items()), me=newMe)


def getMatchingPairFloor(s, c: Configuration):
    if s[1] == 'G':
        i = s[0] + 'M'
    else:
        #if s[1] == 'M':
        i = s[0] + 'G'

    return c.itemsAsDict()[i]


def isValidConfiguration(c: Configuration) -> bool:
    for i, floor in c.items:
        if i[1] == 'G':
            continue
        # in 'M case'
        if getMatchingPairFloor(i, c) == floor:
            continue
        for j, floor2 in c.items:
            if floor2 == floor and j[1] == 'G' and j[0] != i[0]:
                return False
    return True

def isDone(c: Configuration) -> bool:
    for i,floor in c.items:
        if floor != 4:
            return False
    return True

def getMoves(c: Configuration):
    possibleMovableItems: list[str] = []
    for i,floor in c.items:
        if floor == c.me:
            possibleMovableItems.append(i)
    for itemsToMove in list(itertools.combinations(possibleMovableItems, 2)) +  list(itertools.combinations(possibleMovableItems, 1)):
        for f in [c.me-1, c.me+1]:
            if f == 0 or f == 5:
                continue
            newConfig = c
            for itemToMove in itemsToMove:
                newConfig = newConfig.replaceItem(itemToMove, f)
            if isValidConfiguration(newConfig):
                yield newConfig


first = Configuration(
    items=(
        ("EG", 1),
        ("EM", 1),
        ("DG", 1),
        ("DM", 1),
        ("SG", 1),
        ("SM", 1),
        ("PG", 1),
        ("PM", 1),
        ("TG", 2),
        ("RG", 2),
        ("RM", 2),
        ("CG", 2),
        ("CM", 2),
        ("TM", 3),
    ), 
    me=1,
)

configsToDist: dict[Configuration, int] = dict()
configsToDist[first] = 0

states:deque[Configuration] = deque([first])

while states != deque():
    current = states.popleft()
    print("deque, dist ", len(states), configsToDist[current])
    if isDone(current):
        print(configsToDist[current])
        raise(ValueError)
    else:
        moves = getMoves(current)
        for move in moves:
            if move not in configsToDist:
                configsToDist[move] = configsToDist[current] + 1
                states.append(move)
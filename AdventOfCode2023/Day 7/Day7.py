fileContents = open("AdventOfCode2023/Day 7/input.txt")
arr = fileContents.read().split("\n")

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

handTypes = ["five", "four", "full", "three", "2pair", "pair", "high"]

def classifyHand(h):
    d = dict()
    for card in h:
        if card not in d:
            d[card] = 0
        d[card] += 1
    for card in d:
        if d[card] == 5:
            return "five"
        if d[card] == 4:
            return "four"
        if d[card] == 3:
            if len(d) == 2:
                return "full"
            else:
                return "three"
        if d[card] == 2:
            if len(d) == 2:
                return "full"
            if len(d) == 3:
                return "2pair"
            else:
                return "pair"
    return "high" 

def getKeyForHand(hand, originalHand):
    return(handTypes.index(classifyHand(hand)), cards.index(originalHand[0]), cards.index(originalHand[1]), cards.index(originalHand[2]), cards.index(originalHand[3]), cards.index(originalHand[4]))

def handleJ(hand):
    d = dict()
    for card in h:
        if card not in d:
            d[card] = 0
        d[card] += 1
    if "J" not in d:
        return getKeyForHand(hand, hand)
    numberOfJokers = d["J"]
    if numberOfJokers == 5:
        return getKeyForHand(hand, hand)
    else:
        bestHand = getKeyForHand(hand, hand)
        handWithOutJ = hand.replace("J", "")
        for letter in cards:
            addLetters = handWithOutJ + (letter * numberOfJokers)
            candidateHand = getKeyForHand(addLetters, hand)
            
            if candidateHand < bestHand:
                bestHand = candidateHand
        return bestHand

def printHandFromKey(key):
    print(handTypes[key[0]], cards[key[1]], cards[key[2]], cards[key[3]],cards[key[4]],cards[key[5]])

handToBid = dict()
for hand in arr:
    h, bid = hand.split(" ")[0], int(hand.split(" ")[1])
    handToBid[handleJ(h)] = bid

total = 0
for i, key in enumerate(sorted(handToBid)[::-1]):
    total += handToBid[key]*(i+1)
print(total)
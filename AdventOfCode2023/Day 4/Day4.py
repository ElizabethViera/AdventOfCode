
fileContents = open("AdventOfCode2023/Day 4/input.txt")
arr = fileContents.read().split("\n")



total_points = 0
copies = dict()
cards = dict()
for scratchcard in arr:
    scratchcard_total = 0
    card_number = int(scratchcard.split(' ')[1][:-1])
    winningNumbers = scratchcard.split(':')[1].split('|')[0].strip().split(' ')
    winningNumbers = set([int(x) for x in winningNumbers])
    yourNumbers = scratchcard.split(':')[1].split('|')[1].strip().split(' ')
    yourNumbers = [int(x) for x in yourNumbers]
    #print(winningNumbers, yourNumbers)
    for number in yourNumbers:
        if number in winningNumbers:
            scratchcard_total += 1
    cards[card_number] = scratchcard_total
    copies[card_number] = 1
    
def computeWinnings(card_number):
    results = []
    total = cards[card_number]
    for i in range(1,total+1):
        results.append(card_number + i)
    return results

print(cards)

for i in cards:
    winnings = computeWinnings(i)
    for winning in winnings:
        copies[winning] += copies[i]
print(sum(copies.values()))



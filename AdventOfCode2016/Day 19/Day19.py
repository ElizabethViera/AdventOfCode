elves = [i for i in range(1,3005291)]
currentElfIndex = 0
while len(elves) > 1:
    if len(elves)%50000 == 0:
        print(len(elves))
    offset = len(elves)//2
    removeElf = (currentElfIndex+offset)%len(elves)
    del elves[removeElf]
    if currentElfIndex < removeElf:
        currentElfIndex += 1
    currentElfIndex %= len(elves)
print(elves)


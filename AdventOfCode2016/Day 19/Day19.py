elves = [i for i in range(1,3005291)]
currentElfIndex = 0
while len(elves) > 1:
    if len(elves)%10000 == 0:
        print(len(elves))
    offset = len(elves)//2
    removeElf = elves[(currentElfIndex+offset)%len(elves)]
    if removeElf > currentElfIndex:
        currentElfIndex += 1
    elves = elves[:removeElf-1] + elves[removeElf:]
print(elves)


from queue import PriorityQueue

bigNumber = 29000000

priority_queue = PriorityQueue[tuple[int,int]]()

def removeElvesAtCurrentNumber(i:int, priority_queue) -> tuple[tuple[int, int], list[tuple[int, int]]]:
    results = []
    currentElement = priority_queue.get()
    while currentElement[0] < i:
        results.append(currentElement)
        currentElement = priority_queue.get()
    priority_queue.put(currentElement)
    return priority_queue, results
# elves = (nextN, n)

for i in range(1, bigNumber):
    priority_queue.put((i, i))
    priority_queue, currentElves = removeElvesAtCurrentNumber(i, priority_queue)
    sumOfElvesNumbers = sum([currentElf[1]*11 for currentElf in currentElves])
    if sumOfElvesNumbers >= bigNumber:
        print(i)
        break
    else:
        for elf in currentElves:
            if elf[0] + elf[1] <= elf[1]*50:
                priority_queue.put((elf[0]+elf[1], elf[1]))
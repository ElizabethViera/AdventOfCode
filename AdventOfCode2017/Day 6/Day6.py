fileContents = open("AdventOfCode2017/Day 6/input.txt")
lines = fileContents.read().split(" ")
lines = [int(line) for line in lines]
print(lines)

memory_banks = dict()

for e,i in enumerate(lines):
    memory_banks[e] = i

print(memory_banks)

def cycle() -> None:
    largest_number = 0
    bank = -1
    for m in memory_banks:
        if memory_banks[m] > largest_number:
            bank = m
            largest_number = memory_banks[m]
    memory_banks[bank] = 0
    for i in range(largest_number):
        bank += 1
        if bank >= len(memory_banks):
            bank = 0
        memory_banks[bank] += 1

halting = 0
states = set()
cycles = 0
while True:
    cycle()
    cycles += 1
    state = ''
    for i in range(len(memory_banks)):
        state += str(memory_banks[i]) + ','
    if state == '1,1,14,13,12,11,10,9,8,7,7,5,5,3,3,0,':
        print("Found", cycles)
        halting += 1
    if halting == 4:
        break



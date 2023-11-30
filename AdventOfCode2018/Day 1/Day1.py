fileContents = open("AdventOfCode2018/Day 1/input.txt")
digits = fileContents.read().split("\n")
digits = [int(x) for x in digits]

result = set()
total = 0
while(True):
    for digit in digits:
        total += digit
        if total in result:
            print(total)
            raise(KeyError)
        result.add(total)

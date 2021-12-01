fileContents = open("AdventOfCode/Day 2/input")
arr = fileContents.read().split('\n')
valid = 0
valid2 = 0
for l in arr:
    Halves = l.split(':')
    firstHalf = Halves[0]
    secondHalf = Halves[1]
    lowerBound = firstHalf.split('-')[0]
    upperBound = firstHalf.split('-')[1][:-2]
    letter = firstHalf.split('-')[1][-1:]
    letter_count = 0
    for c in secondHalf:
        if c == letter:
            letter_count += 1
    if letter_count <= int(upperBound) and letter_count >= int(lowerBound):
        valid += 1

    if (secondHalf[int(lowerBound)] == letter) != (secondHalf[int(upperBound)] == letter):
        valid2 += 1
print(valid, valid2)

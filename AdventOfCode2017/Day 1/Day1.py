fileContents = open("AdventOfCode2017/Day 1/input.txt")
digits = list(fileContents.read())
digits = [int(x) for x in digits]
indexIntoDigits = len(digits)//2
total = 0

previousDigit = digits[indexIntoDigits]
for d in digits:
    print(d, previousDigit, indexIntoDigits)
    if d == previousDigit:
        total += d
    indexIntoDigits += 1
    if indexIntoDigits >= len(digits):
        indexIntoDigits -= len(digits)
    previousDigit = digits[indexIntoDigits]
print(total)
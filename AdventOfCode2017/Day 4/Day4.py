fileContents = open("AdventOfCode2017/Day 4/input.txt")
arr = fileContents.read().split("\n")

def hasDuplicateWords(words):
    s = set()
    for word in words:
        if ''.join(sorted(word)) in s:
            return True
        s.add(''.join(sorted(word)))
    return False

total = 0
for passphrase in arr:
    if not hasDuplicateWords(passphrase.split(' ')):
        total += 1
print(total)
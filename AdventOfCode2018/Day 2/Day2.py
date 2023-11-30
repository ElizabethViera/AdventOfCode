
fileContents = open("AdventOfCode2018/Day 2/input.txt")
lines = fileContents.read().split("\n")

dictionary = dict()

for line in lines:
    for i in range(len(line)):
        if i not in dictionary:
            dictionary[i] = set()
        word_without_char = line[:i] + line[i+1:]
        if word_without_char in dictionary[i]:
            print(word_without_char, i)
        dictionary[i].add(word_without_char)

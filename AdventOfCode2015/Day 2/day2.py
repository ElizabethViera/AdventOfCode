fileContents = open("AdventOfCode2015/Day 2/input.txt")
arr = fileContents.read().split('\n')

result = 0

for gift in arr:
    l, w, h = map(int, gift.split('x'))
    min1, min2 = sorted([l, w, h])[0], sorted([l, w, h])[1]
    ribbon = 2*(min1+min2)
    bow = l*w*h
    result += ribbon + bow

print(result)

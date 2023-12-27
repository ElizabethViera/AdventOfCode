fileContents = open("AdventOfCode2023/Day 25/input.txt")
arr = fileContents.read().split("\n\n")

left = set()
right = set()

for l in arr[0].strip().split('\n'):
    left.add(l.strip().split(' -- ')[0])
    left.add(l.strip().split(' -- ')[1][:-1])
    
for r in arr[1].strip().split('\n'):
    right.add(r.strip().split(' -- ')[0])
    right.add(r.strip().split(' -- ')[1][:-1])
print(len(left)*len(right))
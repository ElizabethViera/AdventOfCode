fileContents = open("AdventOfCode2022/Day 5/input.txt")
arr = fileContents.read().split('\n')

'''
[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9 
'''
rowStacks = {
             '1': ['F','H','B','V','R','Q','D','P'],
             '2': ['L','D','Z','Q','W','V'],
             '3': ['H','L','Z','Q','G','R','P','C'],
             '4': ['R','D','H','F','J','V','B'],
             '5': ['Z','W','L','C'],
             '6': ['J','R','P','N','T','G','V','M'],
             '7': ['J','R','L','V','M','B','S'],
             '8': ['D','P','J'],
             '9': ['D','C','N','W','V']}

def moveBoxes(columnOld, columnNew, number):
    
        topBoxes, rowStacks[columnOld] = rowStacks[columnOld][-1*number:], rowStacks[columnOld][:-1*number]
        rowStacks[columnNew] += topBoxes

for direction_line in arr:
    directions = direction_line.split(' ')
    moveBoxes(directions[3], directions[5], int(directions[1]))
result = ""
for stack in rowStacks:
    result += rowStacks[stack][-1]
print(result)
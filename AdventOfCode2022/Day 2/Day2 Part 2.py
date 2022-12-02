# Day2 Part 2

fileContents = open("AdventOfCode2022/Day 2/input.txt")
arr = fileContents.read().split('\n')


# X = Rock Y = Paper Z = Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
#  A for Rock, B for Paper, and C for Scissors
'''
A X = tie
A Y = Win
A Z = Lose
B X = Lose
B Y = Tie
B Z = Win
C X = Win
C Y = Lose
C Z = Tie
'''

points = {'X':1, 'Y': 2, 'Z': 3}

lose = {'A': 'Z', 'B': 'X', 'C':'Y'}
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
tie = {'A': 'X', 'B': 'Y', 'C': 'Z'}

totes = 0
for line in arr:
    strat = line.split(' ')
    opponent, you = strat[0], strat[1]
    if you == 'X':
        #lose
        totes += points[lose[opponent]]
        #no other points
    if you == 'Y':
        #draw
        totes += 3
        totes += points[tie[opponent]]
    if you == 'Z':
        #win
        totes += 6
        totes += points[win[opponent]]
    
print(totes)
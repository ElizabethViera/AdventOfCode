fileContents = open("AdventOfCode2022/Day 2/input.txt")
arr = fileContents.read().split('\n')

print(arr)

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

points = 0
for line in arr:
    strat = line.split(' ')
    opponent, you = strat[0], strat[1]
    if you == 'X':
        points += 1
    if you == 'Y':
        points += 2
    if you == 'Z':
        points += 3
    if line in ['A Y', 'B Z', 'C X']:
        # win
        points += 6
    if line in ['A X', 'B Y', 'C Z']:
        # tie
        points += 3
    # else no points you lose
print(points)

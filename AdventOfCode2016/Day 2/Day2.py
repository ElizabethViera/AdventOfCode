'''
1 2 3
4 5 6
7 8 9
'''

neighbors = {
    1: {
        "D": 3
    },
    2: {
        "R": 3,
        "D": 6,
    },
    3: {
        "U": 1,
        "R": 4,
        "L": 2,
        "D": 7,
    },
    4: {
        "L": 3,
        "D": 8
    },
    5: {
        "R": 6,
    },
    6: {
        "U": 2,
        "L": 5,
        "R": 7,
        "D": "A"
    },
    7: {
        "U": 3,
        "L": 6,
        "D": "B",
        "R": 8
    },
    8: {
        "D": "C",
        "U": 4,
        "R": 9,
        "L": 7,
    },
    9: {
        "L": 8
    },
    "A": {
        "U": 6,
        "R": "B"
    },
    "B": {
        "U": 7,
        "L": "A",
        "R": "C",
        "D": "D",
    },
    "C": {
        "U": 8,
        "L": "B"
    },
    "D": {
        "U": "B"
    }
}

currentNumber = 5

fileContents = open("AdventOfCode2016/Day 2/input.txt")
arr = fileContents.read().split("\n")

for line in arr:
    for c in line:
        if c in neighbors[currentNumber]:
            currentNumber = neighbors[currentNumber][c]
    print(currentNumber)

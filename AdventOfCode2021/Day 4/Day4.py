fileContents = open("AdventOfCode2021/Day 4/input.txt")
arr = fileContents.read().split('\n')
numbersToCall = arr[0].split(',')
numbersToCall = [int(x) for x in numbersToCall]
bingoLines = [x for x in arr[1:] if x != '']

count = 0
bingoBoards = []
for bingoLine in bingoLines:
    if count == 0:
        bingoBoard = []
    bingoLine = [int(x) for x in bingoLine.split(' ') if x != ' ' and x != '']
    bingoBoard.append(tuple(bingoLine))
    count += 1
    if count == 5:
        count = 0
        bingoBoards.append(tuple(bingoBoard))

    row1 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    row2 = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
    row3 = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
    row4 = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    row5 = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    col1 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    col2 = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
    col3 = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
    col4 = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
    col5 = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

    winners = [row1, row2, row3, row4, row5, col1, col2, col3, col4, col5]


def isWinner(board, calledNumbers):
    coords = set()
    width = len(board)
    height = len(board[0])
    for row in range(width):
        for col in range(height):
            if board[row][col] in calledNumbers:
                coords.add((row, col))
    for winner in winners:
        if all(w in coords for w in winner):
            return True
    return False


def mainFunction(numbersToCall, bingoBoards):
    calledNumbers = set()
    boardsThatHaveWon = set()
    for number in numbersToCall:
        calledNumbers.add(number)
        for board in bingoBoards:
            if board in boardsThatHaveWon:
                continue
            if isWinner(board, calledNumbers):
                boardsThatHaveWon.add(board)
                if len(boardsThatHaveWon) == len(bingoBoards):
                    print("found a winning board after ", number)
                    return calculateScore(board, number, calledNumbers)


def calculateScore(board, number, calledNumbers):
    result = 0
    for row in board:
        for item in row:
            if item not in calledNumbers:
                result += item
    return result*number


print(mainFunction(numbersToCall, bingoBoards))

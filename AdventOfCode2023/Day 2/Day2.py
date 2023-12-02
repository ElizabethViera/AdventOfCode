fileContents = open("AdventOfCode2023/Day 2/input.txt")
arr = fileContents.read().split("\n")
total = 0

def getMin(game, d):
    answer = dict()

    rightGame = game.strip().split(',')

    results = [x.strip().split(' ') for x in rightGame]

    for rest in results:
        answer[rest[1]] = int(rest[0])
    
    if 'red' not in answer: 
        answer['red'] = 0
    if 'blue' not in answer:
        answer['blue'] = 0
    if 'green' not in answer:
        answer['green'] = 0
    print(d, answer)
    return {
        'red': max(answer['red'], d['red']),
        'blue': max(answer['blue'], d['blue']),
        'green': max(answer['green'], d['green']),
    }

for game in arr:
    print(game)
    unreasonableD = {
        'red': 0,
        'blue': 0,
        'green': 0,
    }
    game_id = game.split(' ')[1][:-1]
    game2 = game.split(':')[1]
    minVals = unreasonableD
    for i in range(len(game2.split(';'))):
        minVals = getMin(game2.split(';')[i], minVals)
          
    total += minVals['red'] * minVals['blue'] * minVals['green']
        
    

print(total)
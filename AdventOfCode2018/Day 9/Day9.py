from collections import defaultdict

PLAYERS = 11 # fake number
LAST_MARBLE = 11 # fake number

game = [0,1]
index = 1
player = 2
players = defaultdict(list)

for i in range(2, LAST_MARBLE*100):
    if i % 100000 == 0:
        print(i)
    if i % 23 == 0:
        players[player].append(i)
        index -= 7
        index += len(game)
        index %= len(game)
        players[player].append(game.pop(index))
    else:
        index += 2
        index %= len(game)
        game = game[:index] + [i] + game[index:]
    player += 1
    player %= PLAYERS

max_score = 0
for player in players:
    if sum(players[player]) > max_score:
        max_score = sum(players[player])

print(max_score)
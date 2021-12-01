fileContents = open("Day 22/input")
deck1 = fileContents.read().split('\n')
deck1 = [int(x) for x in deck1]

fileContents = open("Day 22/input2")
deck2 = fileContents.read().split('\n')
deck2 = [int(x) for x in deck2]


def playGame(player1, player2, depth=0):
    print("new game! Depth = ", depth)
    previous_decks = set()
    while len(player1) > 0 and len(player2) > 0:
        if tuple(player1 + [" "] + player2) in previous_decks:
            return "player1", player1

        previous_decks.add(tuple(player1 + [" "] + player2))

        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 <= len(player1) and card2 <= len(player2):
            winner, tmp = playGame(
                list(player1[:card1]), list(player2[:card2]), depth+1)
            if winner == "player1":
                player1.append(card1)
                player1.append(card2)
            elif winner == "player2":
                player2.append(card2)
                player2.append(card1)
            else:
                raise("why")
        else:
            if card1 > card2:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
    if player1 == []:
        return "player2", player2
    elif player2 == []:
        return "player1", player1
    else:
        raise("wat")


winner, result = playGame(deck1, deck2)
print(winner, result)

score = 0
for i in range(len(result)):
    score += (i+1)*(result[::-1][i])
print(score)

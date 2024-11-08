fileContents = open("AdventOfCode2019/Day 22/input.txt")
ins = fileContents.read().split("\n")

deck_length = 119315717514047
cards = [i for i in range(deck_length)]

def get_new_order(c: list[int], inc: int) -> list[int]:
    if inc < 0: 
        print(inc)
        raise(ValueError)
    index = 0
    new_deck = [-1 for i in range(deck_length)]
    for card in c:
        if new_deck[index] != -1:
             print(new_deck[index], card, inc)
             raise(ValueError)
        new_deck[index] = card
        index += inc
        index %= deck_length
    return new_deck

for line in ins:
    if line.startswith('cut'):
        amount = int(line.split(' ')[1])
        cards = cards[amount:] + cards[:amount]
    elif line.startswith('deal into'):
        cards = cards[::-1]
    elif line.startswith('deal with'):
            increment = int(line.split(' ')[-1])
            cards = get_new_order(cards, increment)
    else:
        raise(ValueError)
print(cards.index(2019))
score_1 = 0
score_2 = 0

pos_1 = 4
pos_2 = 1

die = 1
dice_rolls = 0

def getDiceResult(d):
    if d == 98:
        return 199+98, 1 
    if d == 99:
        return 200, 2
    if d == 100:
        return 103, 3
    else:
        return (3*d)+3, d+3

def myMod(value):
    while value > 10:
        value -= 10
    return value

def playerTurn(d, pos):
    move_forward, new_dice_value = getDiceResult(d)
    new_place = myMod(pos + move_forward)
    return new_dice_value, new_place

while True:
    die, pos_1 = playerTurn(die, pos_1)
    dice_rolls += 3
    score_1 += pos_1
    if score_1 >= 1000:
        print(score_2 * dice_rolls)
        break
    die, pos_2 = playerTurn(die, pos_2)
    dice_rolls += 3
    score_2 += pos_2
    if score_2 >= 1000:
        print(score_1 * dice_rolls)
        break
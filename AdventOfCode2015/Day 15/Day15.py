ingredients = {
    'sprinkles': {
        'capacity': 2,
        'durability': 0,
        'flavor': -2,
        'texture':0, 
        'calories': 3
    },
    'butterscotch': {
        'capacity': 0,
        'durability': 5,
        'flavor': -3,
        'texture':0, 
        'calories': 3
    },
    'chocolate': {
        'capacity': 0,
        'durability': 0,
        'flavor': 5,
        'texture':-1, 
        'calories': 8,
    },
    'candy': {
        'capacity': 0,
        'durability': -1,
        'flavor': 0,
        'texture': 5, 
        'calories': 8
    }
}

def calculateScore(ratios):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for ingredient in ingredients:
        capacity += ingredients[ingredient]['capacity']*ratios[ingredient]
        durability += ingredients[ingredient]['durability']*ratios[ingredient]
        flavor += ingredients[ingredient]['flavor']*ratios[ingredient]
        texture += ingredients[ingredient]['texture']*ratios[ingredient]
    return max(0, capacity) * max(0, durability) * max(0,flavor) * max(0, texture)

def calculateCalories(ratios):
    calories = 0
    for ingredient in ingredients:
        calories += ratios[ingredient] * ingredients[ingredient]['calories']
    return calories

def getAllRatios():
    maxScore = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                for l in range(100):
                    if i+j+k+l == 100:
                        ratios = {
                            'sprinkles': i,
                            'butterscotch': j,
                            'chocolate': k,
                            'candy': l,
                        }
                        if calculateCalories(ratios) == 500:
                            score = calculateScore(ratios)
                            if score > maxScore:
                                maxScore = score
    return maxScore

print (getAllRatios())
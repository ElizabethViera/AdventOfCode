fileContents = open("Day 21/input")
arr = fileContents.read().split('\n')
candidates = {}
ing = set()
aller = set()
ingredient_count = {}


for line in arr:
    ingredients = line.split("(")[0].split(" ")[:-1]
    allergens = line.split("contains ")[1].split(", ")
    allergens[-1] = allergens[-1][:-1]

    for allergen in allergens:
        aller.add(allergen)
        if allergen in candidates:
            candidates[allergen].append(ingredients)
        else:
            candidates[allergen] = ([ingredients])

    for ingredient in ingredients:
        ing.add(ingredient)
        if ingredient in ingredient_count:
            ingredient_count[ingredient] += 1
        else:
            ingredient_count[ingredient] = 1


cant_be = {}

for ingredient in ing:
    for allergen in aller:
        for label in candidates[allergen]:
            if ingredient not in label:
                if ingredient not in cant_be:
                    cant_be[ingredient] = set([allergen])
                else:
                    cant_be[ingredient].add(allergen)
result = 0
for ingredient in cant_be:
    if len(cant_be[ingredient]) == len(aller):
        ing.remove(ingredient)
        result += ingredient_count[ingredient]
print(ing)
for ingredient in ing:
    print('ingredient ', ingredient, " can't be ", cant_be[ingredient])
print(result)

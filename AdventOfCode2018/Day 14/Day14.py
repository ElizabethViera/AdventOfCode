recipes = [3,7]

elf1_index = 0
elf2_index = 1

def newRecipes(recipes):
    new_recipes = recipes[elf1_index] + recipes[elf2_index]
    if new_recipes >= 10:
        recipes.append(1)
    recipes.append(new_recipes%10)
    return recipes

def updateElves(recipes):
    first_elf = (elf1_index + recipes[elf1_index] + 1) % len(recipes)
    second_elf = (elf2_index + recipes[elf2_index] + 1) % len(recipes)

    return first_elf, second_elf

def isSubArray(t, r):
    if len(r) < len(t):
            return False
    return recipes[len(r)-len(t):] == t or recipes[len(r)-len(t)-1:-1] == t

# target = [0,1,2,4,5] # 5
# target = [5,1,5,8,9] # 9
# target = [9,2,5,1,0] # 18
# target = [5,9,4,1,4] # 2018
target = [8,2,5,4,0,1]
i = 0
while not isSubArray(target, recipes):
    i += 1
    if i % 10000000 == 0:
        print(i)
    recipes = newRecipes(recipes)
    elf1_index, elf2_index = updateElves(recipes)

print(len(recipes)-len(target))




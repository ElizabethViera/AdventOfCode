from dataclasses import dataclass

'''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
'''

@dataclass
class Item:
    name: str
    cost: int = 0
    damage: int = 0
    armor: int = 0

weaponsList = [
    Item(name="Dagger", cost=8, damage=4),
    Item(name="Shortsword", cost=10, damage=5),
    Item(name="Warhammer", cost=25, damage=6),
    Item(name="Longsword", cost=40, damage=7),
    Item(name="Greataxe", cost=74, damage=8),
     ]

'''
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''

armorList = [
    Item(name="None", cost=0),
    Item(name="Leather", cost=13, armor=1),
    Item(name="Chainmail", cost=31, armor=2),
    Item(name="Splitmail", cost=53, armor=3),
    Item(name="Bandedmail", cost=75, armor=4),
    Item(name="Platemail", cost=102, armor=5),
     ]

'''
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''
ringList = [
    Item(name="A1", cost=25, damage=1),
    Item(name="A2", cost=50, damage=2),
    Item(name="A3", cost=100, damage=3),
    Item(name="De1", cost=20, armor=1),
    Item(name="De2", cost=40, armor=2),
    Item(name="De3", cost=80, armor=3),
     ]

def combineItems(item1: Item, item2: Item):
    return Item(name=item1.name + item2.name, cost = item1.cost + item2.cost, damage=item1.damage + item2.damage, armor = item1.armor + item2.armor)

def simulateFight(items: Item):
    yourHP = 100
    yourDamage = items.damage
    yourArmor = items.armor
    bossHP = 109
    bossDamage = 8
    bossArmor = 2
    youHit = max(1, yourDamage - bossArmor)
    bossHit = max(1, bossDamage - yourArmor)
    turn = 1
    while yourHP > 0 and bossHP > 0:
        if turn == 1:
            bossHP -= youHit
        else:
            yourHP -= bossHit
        turn = 1 - turn
    return yourHP > 0

ringComboList = list(ringList)
ringComboList.append(Item(name="none"))
for ring in ringList:
    for ring2 in ringList:
        if ring.name == ring2.name:
            break
        ringComboList.append(combineItems(ring,ring2))

maxCost = 0
for weapon in weaponsList:
    for armor in armorList:
        for ringCombos in ringComboList:
            weaponArmor = combineItems(weapon, armor)
            weaponArmorRings = combineItems(weaponArmor, ringCombos)
            if not simulateFight(weaponArmorRings):
                if weaponArmorRings.cost > maxCost:
                    maxCost = weaponArmorRings.cost

print(maxCost)
        
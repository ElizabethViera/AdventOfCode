from collections import defaultdict
from dataclasses import dataclass
from copy import deepcopy
from queue import PriorityQueue
from unittest import result

@dataclass()
class Player:
    hp: int = 0
    mana: int = 0
    armor: int = 0

@dataclass()
class Boss:
    hp: int = 0
    damage: int = 0

@dataclass
class Spell:
    name: str
    turns_remaining: int
    cost: int
    damage: int = 0
    heals: int = 0
    armor: int = 0
    poison: int = 0
    recharge: int = 0

spellList = [
    Spell(name="Magic Missile", cost=53, turns_remaining=0, damage=4),
    Spell(name="Drain", cost=73, damage=2, heals=2, turns_remaining=0),
    Spell(name="Shield", cost=113, turns_remaining=6, armor=7),
    Spell(name="Poison", turns_remaining=6, cost=173, damage=3),
    Spell(name="Recharge", cost=229, turns_remaining=5, recharge=101),
]

@dataclass()
class TurnState:
    player: Player
    boss: Boss
    effects: dict[str, int]
    totalManaSpent: int
    turn: int # 0 if player 1 if boss
    def __lt__(self, a):
        return a.totalManaSpent > self.totalManaSpent

def gameIsOver(s: TurnState):
    return s.player.hp <= 0 or s.boss.hp <= 0

def chooseSpell(turnState: TurnState) -> list[TurnState]:
    returnStates: list[TurnState] = []
    for spell in spellList:
        newTurnState = deepcopy(turnState)
        if spell.cost > turnState.player.mana:
            continue
        newTurnState.player.mana -= spell.cost
        newTurnState.totalManaSpent += spell.cost
        match spell.name:
            case "Magic Missile":
                newTurnState.boss.hp -= 4
            case "Drain":
                newTurnState.boss.hp -= 2
                newTurnState.player.hp += 2
            case "Shield":
                if newTurnState.effects['Shield'] > 0:
                    continue
                newTurnState.effects['Shield'] = 6
                newTurnState.player.armor += 7
            case "Poison":
                if newTurnState.effects['Poison'] > 0:
                    continue
                newTurnState.effects['Poison'] = 6
            case "Recharge":
                if newTurnState.effects['Recharge'] > 0:
                    continue
                newTurnState.effects['Recharge'] = 5
        returnStates.append(newTurnState)
    return returnStates

    
def takeTurn(turnState: TurnState) -> list[TurnState]:
    turnState = deepcopy(turnState)
    if turnState.effects['Poison'] > 0:
            turnState.effects['Poison'] -= 1
            turnState.boss.hp -= 3
            if turnState.boss.hp <= 0:
                return [turnState]
    if turnState.effects['Shield'] > 0:
            turnState.effects['Shield'] -= 1
            if turnState.effects['Shield'] == 0:
                turnState.player.armor -= 7
    if turnState.effects['Recharge'] > 0:
        turnState.effects['Recharge'] -= 1
        turnState.player.mana += 101
    if turnState.turn == 1:
        turnState.player.hp -= max(turnState.boss.damage - turnState.player.armor, 1)
        return [turnState]
    else:
        #player turn
        #check effects
        turnState.player.hp -= 1
        if turnState.player.hp <= 0:
            return [turnState]
        
        return(chooseSpell(turnState))

def findLeastMana():
    initial = TurnState(Player(hp= 50, mana= 500), Boss(damage=8, hp=55),effects=defaultdict(int), totalManaSpent=0, turn=0)
    states = PriorityQueue[TurnState]()
    states.put(initial)
    while True:
        leastManaState = states.get()
        if gameIsOver(leastManaState):
            if leastManaState.boss.hp <= 0:
                return leastManaState.totalManaSpent
            else:
                continue
        resultantStates = takeTurn(leastManaState)
        for resultantState in resultantStates:
            resultantState.turn = 1-resultantState.turn
            states.put(resultantState)


        
print(findLeastMana())



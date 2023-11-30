from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    hp: int = 0
    mana: int = 0
    armor: int = 0

@dataclass(frozen=True)
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
    Spell(name="Magic Missle", cost=53, turns_remaining=0, damage=4),
    Spell(name="Drain", cost=73, damage=2, heals=2, turns_remaining=0),
    Spell(name="Shield", cost=113, turns_remaining=6, armor=7),
    Spell(name="Poison", turns_remaining=6, cost=173, damage=3),
    Spell(name="Recharge", cost=229, turns_remaining=5, recharge=101),
]

@dataclass(frozen=True)
class TurnState:
    player: Player
    boss: Boss
    effects: dict[str, int]
    totalManaSpent: int
    turn: int # 0 if player 1 if boss

def gameIsOver(s: TurnState):
    return s.player.hp <= 0 or s.player.mana < 53 or s.boss.hp <= 0

    
def takeTurn(turnState: TurnState) -> set[TurnState]:
    for spell in spellList:


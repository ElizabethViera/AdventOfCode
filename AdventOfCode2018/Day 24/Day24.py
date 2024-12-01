from dataclasses import dataclass


@dataclass
class GroupOfUnits:
    hp: int
    attack: int
    attack_type: str
    initiative: int
    quantity: int
    weaknesses: list[str]
    immunities: list[str]

    def get_effective_power(self):
        return attack * quantity


IllnessFile = open("AdventOfCode2018/Day 24/illness.txt")
illness_groups = IllnessFile.read().split("\n")

infections: dict[int, GroupOfUnits] = dict()

for i, illness_group in enumerate(illness_groups):
    atts = illness_group.split(", ")
    quantity = int(atts[0])
    hp = int(atts[1])
    attack = int(atts[2].split(" ")[0])
    attack_type = atts[2].split(" ")[1]
    initiative = int(atts[3])
    immunities = []
    weaknesses = []
    if len(atts) > 4:
        if atts[4].split("=")[0] == "weak":
            all_weaknesses = atts[4].split("=")[1][1:-1]
            weaknesses = all_weaknesses.split("| ")
        elif atts[4].split("=")[0] == "immune":
            all_immunities = atts[4].split("=")[1][1:-1]
            immunities = all_immunities.split("| ")
        else:
            print(atts[4], atts)
            raise (ValueError())
    if len(atts) > 5:
        if atts[5].split("=")[0] == "weak":
            all_weaknesses = atts[4].split("=")[1][1:-1]
            weaknesses = all_weaknesses.split("| ")
        elif atts[5].split("=")[0] == "immune":
            all_immunities = atts[4].split("=")[1][1:-1]
            immunities = all_immunities.split("| ")
        else:
            print(atts[5], atts)
            raise (ValueError())
    infections[i] = GroupOfUnits(
        hp, attack, attack_type, initiative, quantity, weaknesses, immunities
    )


ImmunityFile = open("AdventOfCode2018/Day 24/immune.txt")
immunity_groups = ImmunityFile.read().split("\n")

immune_defenses: dict[int, GroupOfUnits] = dict()

for i, immunity_group in enumerate(immunity_groups):
    atts = immunity_group.split(", ")
    quantity = int(atts[0])
    hp = int(atts[1])
    attack = int(atts[2].split(" ")[0])
    attack_type = atts[2].split(" ")[1]
    initiative = int(atts[3])
    immunities = []
    weaknesses = []
    if len(atts) > 4:
        if atts[4].split("=")[0] == "weak":
            all_weaknesses = atts[4].split("=")[1][1:-1]
            weaknesses = all_weaknesses.split("| ")
        elif atts[4].split("=")[0] == "immune":
            all_immunities = atts[4].split("=")[1][1:-1]
            immunities = all_immunities.split("| ")
        else:
            print(atts[4])
            raise (ValueError())
    if len(atts) > 5:
        if atts[5].split("=")[0] == "weak":
            all_weaknesses = atts[4].split("=")[1][1:-1]
            weaknesses = all_weaknesses.split("| ")
        elif atts[5].split("=")[0] == "immune":
            all_immunities = atts[4].split("=")[1][1:-1]
            immunities = all_immunities.split("| ")
        else:
            print(atts[5])
            raise (ValueError())
    immune_defenses[i] = GroupOfUnits(
        hp, attack, attack_type, initiative, quantity, weaknesses, immunities
    )


def sort_inf(i):
    return infections[i].get_effective_power(), infections[i].initiative


def sort_imm(i):
    return immune_defenses[i].get_effective_power(), immune_defenses[i].initiative


def get_targets(infections, immune_defenses):
    infections_order = sorted(infections, key=sort_inf)
    imm_targeted = set()
    inf_targets: dict[int, int] = dict()
    for inf in infections_order:
        best_target = None
        best_attack = 0
        for imm in immune_defenses:
            if imm not in imm_targeted:
                attack = get_attack(infections[inf], immune_defenses[imm])
                if attack > best_attack:
                    best_attack = attack
                    best_target = imm
        if best_target is not None:
            imm_targeted.add(best_target)
            inf_targets[inf] = best_target

    immune_defenses_order = sorted(immune_defenses, key=sort_imm)


get_targets(infections, immune_defenses)

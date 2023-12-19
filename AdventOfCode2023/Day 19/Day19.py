
fileContents = open("AdventOfCode2023/Day 19/input.txt")
arr = fileContents.read().split("\n\n")

rules = arr[0].split('\n')
gears = arr[1].split('\n')

rules_dict = dict()

for rule in rules:
    rule_name = rule.split('{')[0]
    interior_contents = rule.split('{')[1][:-1]
    cases = interior_contents.split(',')
    rules_dict[rule_name] = cases

    

from dataclasses import dataclass

@dataclass
class Range:
    start: int
    end_inclusive: int

    def intersect(self, other: "Range") -> "Range":
        return Range(start=max(self.start, other.start), end_inclusive=min(self.end_inclusive, other.end_inclusive))

    def isEmptyRange(self):
        return self.start > self.end_inclusive

    def count(self):
        return self.end_inclusive - self.start + 1

@dataclass
class GearRanges:
    x: Range
    m: Range
    a: Range
    s: Range

    def intersect(self, other: "GearRanges"):
        return GearRanges(
            x=self.x.intersect(other.x),
            m=self.m.intersect(other.m),
            a=self.a.intersect(other.a),
            s=self.s.intersect(other.s),
            )
    
    def isEmptyRange(self):
        return self.x.isEmptyRange() or self.m.isEmptyRange() or self.a.isEmptyRange() or self.s.isEmptyRange() 

    def count(self):
        return self.x.count() * self.m.count() * self.a.count() * self.s.count()


def ifCondition(condition, gearRange):
    gear_index = condition[0]
    operator = condition[1]
    if operator == '<':
        resultRange = Range(start = 1, end_inclusive=int(condition[2:])-1)
        oppositeRange = Range(start = int(condition[2:]), end_inclusive=4000)
    else: # operator == '>':
        resultRange = Range(start = int(condition[2:])+1, end_inclusive=4000)
        oppositeRange = Range(start = 1, end_inclusive= int(condition[2:]))
    from copy import deepcopy
    gearRangeTrue = deepcopy(gearRange)
    setattr(gearRangeTrue, gear_index, getattr(gearRangeTrue, gear_index).intersect(resultRange))

    gearRangeFalse = deepcopy(gearRange)
    setattr(gearRangeFalse, gear_index, getattr(gearRangeFalse, gear_index).intersect(oppositeRange))

    return gearRangeTrue, gearRangeFalse


def eval_rule(gearRange, single_rule_list):
    result = []
    for single_rule in single_rule_list[:-1]:
        condition, state = single_rule.split(':')[0], single_rule.split(':')[1]
        rTrue, rFalse = ifCondition(condition, gearRange)
        gearRange = rFalse
        result.append((state, rTrue))
    result.append((single_rule_list[-1], gearRange))
    result = [r for r in result if not r[1].isEmptyRange()]
    return result

def rejectOrFail():
    current_index = [('in', GearRanges(
        x=Range(start=1, end_inclusive=4000),
        m=Range(start=1, end_inclusive=4000),
        a=Range(start=1, end_inclusive=4000),
        s=Range(start=1, end_inclusive=4000),
        ))]
    results = []
    while current_index != []:
        c = current_index.pop()
        if c[0] == 'A':
            results.append(c[1])
            continue
        if c[0] == 'R':
            continue
        evaled = eval_rule(c[1], rules_dict[c[0]])
        for ev in evaled:
            current_index.append(ev)
    return results

print(sum([g.count() for g in rejectOrFail()]))
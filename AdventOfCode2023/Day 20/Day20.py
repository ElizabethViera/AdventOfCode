fileContents = open("AdventOfCode2023/Day 20/input.txt")
conf = fileContents.read().split("\n")

# map from name to object with type and destinations

import dataclasses

@dataclasses.dataclass
class Module:
    type: str
    destinations: list[str]
    memory: dict = dataclasses.field(default_factory = dict)
    on: bool = False


modules: dict[str, Module] = dict()

for line in conf:
    left, right = line.split(' -> ')[0], line.split(' -> ')[1]
    destinations = right.split(', ')
    if left == 'broadcaster':
        modules['broadcaster'] = Module('broadcaster', destinations)
    else:
        modules[left[1:]] = Module(left[0], destinations)

empty_modules: dict[str, Module] = dict()

for m in modules:
     mod = modules[m]
     for d in mod.destinations:
         if d not in modules:
             empty_modules[d] = Module(type='empty', destinations=[])
             continue
         modules[d].memory[m] = False

for e in empty_modules:
    modules[e] = empty_modules[e]

def processPulse(m, isHigh, sent, i):
    module = modules[m]
    match module.type:
        case 'broadcaster':
            results = []
            for d in module.destinations:
                results.append((d, isHigh, m))
            return results
        case '%':
            if isHigh:
                return []
            else:
                module.on = not module.on
                results = []
                for d in module.destinations:
                    results.append((d, module.on, m))
                return results
        case '&':
            module.memory[sent] = isHigh
            newLow = True
            for mem in module.memory:
                if not module.memory[mem]:
                    newLow = False
            results = []
            for d in module.destinations:
                results.append((d, not newLow, m))
            return results
        case 'empty':
            if not isHigh:
                print(buttonPress)
                raise(ValueError)
            return []
        case _:
            raise(ValueError)
   
pulses = []
'''
for buttonPress in range(1000000):
    if buttonPress%1000000 == 0:
        print(buttonPress)
    pulses.append(('broadcaster', False, 'button'))

    while pulses != []:
        (m, isHigh, sent) = pulses.pop(0)
        new_pulses = processPulse(m, isHigh, sent, buttonPress)
        for n in new_pulses:
            if n[0] in ['js', 'qs', 'dt', 'ts'] and not n[1]:
                print(n[0], buttonPress, n[1])
            pulses.append(n)
'''
print(3943*3947*4007*4019)
from dataclasses import dataclass

@dataclass
class Unit:
    type: str
    health: int = 200
    attack: int = 3
    died: bool = False

    

    def attacks(self, opponent):
        opponent.health -= self.attack
        if opponent.health <= 0:
            opponent.died = True

GAME_OVER = 'GAME OVER'
walls = set() # (row,col)

units: dict[tuple[int, int], 'Unit'] = dict()
# tuple row, col to Unit

neighbors = [(-1,0), (0, -1), (0,1), (1,0)]

def addPts(a,b):
    return a[0] + b[0], a[1] + b[1]

def isReachable(a,b, pending_units, new_units, walls):
    visited = set()
    to_visit = [a]
    while to_visit != []:
        current_unit = to_visit.pop(0)
        if current_unit in visited:
            continue
        visited.add(current_unit)
        local_neighbors = [addPts(neighbor, current_unit) for neighbor in neighbors]
        for local_neighbor in local_neighbors:
            if local_neighbor == b:
                return True
            if local_neighbor in pending_units:
                continue
            if local_neighbor in new_units:
                continue
            if local_neighbor in walls:
                continue
            to_visit.append(local_neighbor)
    return False

def getDistance(a,b, pending_units, new_units, walls):
    blocks = set()
    for p in pending_units:
        blocks.add(p)
    for p in new_units:
        blocks.add(p)
    for p in walls:
        blocks.add(p)
    distances = dict()
    distances[a] = 0
    visited = set()
    to_visit = [a]
    while to_visit != []:
        current_unit = to_visit.pop(0)
        if current_unit in visited:
            continue
        visited.add(current_unit)
        local_neighbors = [addPts(neighbor, current_unit) for neighbor in neighbors]
        for local_neighbor in local_neighbors:
            if local_neighbor in blocks:
                continue
            to_visit.append(local_neighbor)
            if local_neighbor not in distances or distances[current_unit] + 1 < distances[local_neighbor]:
                distances[local_neighbor] = distances[current_unit] + 1
    return distances[b]

def getTarget(t: dict[tuple[int,int], 'Unit']):
    leastHealthSeen = 204
    unitWithLeastHealth = (-1, -1)
    for k in t:
        if t[k].health < leastHealthSeen:
            leastHealthSeen = t[k].health
            unitWithLeastHealth = k
        elif t[k].health == leastHealthSeen:
            if k < unitWithLeastHealth:
                unitWithLeastHealth = k
    return t[unitWithLeastHealth]


def getStep(b,a, pending_units, new_units, walls):
    blocks = set()
    for p in pending_units:
        blocks.add(p)
    for p in new_units:
        blocks.add(p)
    for p in walls:
        blocks.add(p)
    distances = dict()
    distances[b] = 0
    visited = set()
    visited.add(b)
    to_visit = [b]
    while to_visit != []:
        current_unit = to_visit.pop(0)
        if current_unit in visited:
            continue
        visited.add(current_unit)
        local_neighbors = [addPts(neighbor, current_unit) for neighbor in neighbors]
        for local_neighbor in local_neighbors:
            if local_neighbor in blocks:
                continue
            to_visit.append(local_neighbor)
            if local_neighbor not in distances or distances[current_unit] + 1 < distances[local_neighbor]:
                distances[local_neighbor] = distances[current_unit] + 1
    local_neighbors = [addPts(neighbor, a) for neighbor in neighbors]
    for local_neighbor in local_neighbors:
        print("local_neighbor = ", local_neighbor, distances)
        if local_neighbor in blocks:
            continue
        if local_neighbor in distances and distances[local_neighbor] == distances[a]-1:
            return local_neighbor
    raise(ValueError)

def takeTurn(units):
    pending_units = sorted(units.keys())
    new_unit_locations: dict[tuple[int, int], 'Unit'] = dict()
    while pending_units != []:
        # get a unit
        # check that unit is alive
        # get targets
        # check if has a target that is already hittable
        # if not, move to a hittable target
        unit = pending_units.pop(0)
        if units[unit].died:
            continue
        targets: list[tuple[int,int]] = []
        for x in pending_units:
            if units[x].type != units[unit].type:
                targets.append(x)

        for x in new_unit_locations:
            if new_unit_locations[x].type != units[unit].type:
                targets.append(x)

        if targets == []:
            return GAME_OVER
        already_in_range = False
        for neighbor in neighbors:
            to_check = addPts(unit, neighbor)
            if to_check in targets:
                new_unit_locations[unit] = units[unit]
                already_in_range = True
                current_location = unit

        if not already_in_range:
            enemy_hit_boxes = []
            for target in targets:
                #identify open slots
                for neighbor in neighbors:
                    to_check = addPts(target,neighbor)
                    if to_check in walls or to_check in units:
                        continue
                    else:
                        enemy_hit_boxes.append(to_check)
            
            
            reachable = []
            for hit_box in enemy_hit_boxes:
                if isReachable(unit, hit_box, pending_units, new_unit_locations, walls):
                    reachable.append(hit_box)
            if len(reachable) == 0:
                new_unit_locations[unit] = units[unit]
                continue
            
            distances_to_reachable = dict()
            for reachable_block in reachable:
                d = getDistance(unit, reachable_block, pending_units, new_unit_locations, walls)
                if d not in distances_to_reachable:
                    distances_to_reachable[d] = []
                distances_to_reachable[d].append(reachable_block)
            distances_to_reachable_keys = sorted(distances_to_reachable)

            destination_distance = distances_to_reachable_keys[0]
            destination_block = sorted(distances_to_reachable[destination_distance])[0]
            step_to_block = getStep(unit, destination_block, pending_units, new_unit_locations, walls)
            new_unit_locations[step_to_block] = units[unit]
            current_location = step_to_block

        
        print("unit ", unit, " moving to ", current_location)
        # find and attack target
        targets_in_range: dict[tuple[int,int], 'Unit'] = dict()
        for n in neighbors:
            in_range = addPts(current_location,n)
            if in_range in targets:
                targets_in_range[in_range] = new_unit_locations[in_range] if in_range in new_unit_locations else units[in_range]
        if len(targets_in_range) == 0:
            continue
        else:
            print('attacking')
            new_unit_locations[current_location].attacks(getTarget(targets_in_range))
    return new_unit_locations

           
fileContents = open("AdventOfCode2018/Day 15/input.txt")
contents = fileContents.read().split("\n")

for r, row in enumerate(contents):
    for c, char in enumerate(row):
        if char == '#':
            walls.add((r,c))
        if char == 'G':
            units[(r,c)] = Unit('G')
        if char == 'E':
            units[(r,c)] = Unit('E')

result = units
turns = 0
while turns <= 1:
    turns += 1
    result = takeTurn(result)

print(turns)
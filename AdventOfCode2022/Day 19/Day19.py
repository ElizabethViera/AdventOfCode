fileContents = open("AdventOfCode2022/Day 19/input.txt")
arr = fileContents.read().split("\n")

TIMELIMIT = 32
blueprint_dict = {}

for i, blueprint in enumerate(arr):
    sentences = blueprint.split('.')
    blueprint_dict[i+1] = {}
    blueprint_dict[i+1]['Ore Robot'] = { 'Ore': int(sentences[1].split(' ')[-2]) }
    blueprint_dict[i+1]['Clay Robot'] = { 'Ore': int(sentences[2].split(' ')[-2]) }
    blueprint_dict[i+1]['Obsidian Robot'] = {}

    blueprint_dict[i+1]['Obsidian Robot']['Ore'] = int(sentences[3].split(' ')[5])

    blueprint_dict[i+1]['Obsidian Robot']['Clay'] = int(sentences[3].split(' ')[8])

    blueprint_dict[i+1]['Geode Robot'] = {}

    blueprint_dict[i+1]['Geode Robot']['Ore'] = int(sentences[4].split(' ')[5])

    blueprint_dict[i+1]['Geode Robot']['Obsidian'] = int(sentences[4].split(' ')[8])

    blueprint_dict[i+1]['None Robot'] = {}

def buyPossibleNewRobots(inventory, blueprint):
    options = ['Ore Robot', 'Clay Robot', 'Obsidian Robot', 'Geode Robot']
    results = set(['None Robot'])
    for option in options:
        
        if all( blueprint[option][material] <= inventory[material] for material in blueprint[option]):
            results.add(option)
    return results

def getNewRobot(robot, robot_dict):
    match robot:
        case 'Ore Robot':
            robot_dict['Ore Robot'] += 1
        case 'Clay Robot':
            robot_dict['Clay Robot'] += 1
        case 'Obsidian Robot':
            robot_dict['Obsidian Robot'] += 1
        case 'Geode Robot':
            robot_dict['Geode Robot'] += 1
        case 'None Robot':
            pass

def calculateMaxMaterials(blueprint):
    materials = {}
    for robot in blueprint:
        for material in blueprint[robot]:
            if material not in materials:
                materials[material] = blueprint[robot][material]
            else:
                if blueprint[robot][material] > materials[material]:
                    materials[material] = blueprint[robot][material]
    return materials

def gatherMaterials(inventory, robots):
    for robot in robots:
        inventory_type = robot.split(' ')[0]
        inventory[inventory_type] += robots[robot]

def subtractRobotCosts(inventory, costs):
    for cost in costs:
        inventory[cost] -= costs[cost]

def is_equal_or_worse(state1, state2):
    for key in state1[0]:
        if state1[0][key] > state2[0][key]:
            return False
    for key in state1[1]:
        if state1[1][key] > state2[1][key]:
            return False
    return True 

def reduce_state(state, max_materials_required, days_remaining):
    for material in max_materials_required:
        if state[0][material + " Robot"] > max_materials_required[material]:
            state[0][material + " Robot"] = max_materials_required[material]
    for material in max_materials_required:
        if state[1][material] > max_materials_required[material]*days_remaining:
            state[1][material] = max_materials_required[material]*days_remaining
    return state

def prune_duplicates(list_of_states):
    output_list = []
    for state in list_of_states:
        if any(is_equal_or_worse(state, output) for output in output_list):
           continue
        output_list = [output for output in output_list if not is_equal_or_worse(output, state)]
        output_list.append(state)
    return output_list

def calculate_quality(blueprint):
    max_materials_blueprint = calculateMaxMaterials(blueprint)
    init_robot_dict = {
        'Ore Robot': 1,
        'Clay Robot': 0,
        'Obsidian Robot': 0,
        'Geode Robot': 0,
    }
    init_inventory_dict = {
        'Ore': 0,
        'Clay': 0,
        'Obsidian': 0,
        'Geode': 0
    }
    possible_states = [(init_robot_dict, init_inventory_dict)]
    for i in range(TIMELIMIT):
        days_remaining = TIMELIMIT - i - 1
        new_possible_states = []
        for robot_dict, inventory_dict in possible_states:
            robot_options = buyPossibleNewRobots(inventory_dict, blueprint)
            gatherMaterials(inventory_dict, robot_dict)
            for robot in robot_options:
                new_inventory = dict(inventory_dict)
                new_robot_dict = dict(robot_dict)
                getNewRobot(robot, new_robot_dict)
                subtractRobotCosts(new_inventory, blueprint[robot])
                new_possible_states.append((new_robot_dict, new_inventory))
        new_possible_states = [reduce_state(state, max_materials_blueprint, days_remaining) for state in new_possible_states]
        possible_states = prune_duplicates(new_possible_states)
    return (sorted([possible_state[1]['Geode'] for possible_state in possible_states])[-1])
result = 0
for i, blueprint in enumerate(blueprint_dict):
    blueprint_result = calculate_quality(blueprint_dict[blueprint])
    result += blueprint_result*(i+1)
    print(blueprint_result, i+1)
print(result)
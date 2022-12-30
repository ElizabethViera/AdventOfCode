fileContents = open("AdventOfCode2022/Day 19/input.txt")
arr = fileContents.read().split("\n")

TIMELIMIT = 24
blueprint_dict = {}

for blueprint in arr:
    sentences = blueprint.split('.')
    blueprint_dict[sentences[0][-1]] = {}
    blueprint_dict[sentences[0][-1]]['Ore Robot'] = int(sentences[1].split(' ')[-2])
    blueprint_dict[sentences[0][-1]]['Clay Robot'] = int(sentences[2].split(' ')[-2])
    blueprint_dict[sentences[0][-1]]['Obsidian Robot'] = {}

    blueprint_dict[sentences[0][-1]]['Obsidian Robot']['Ore'] = int(sentences[3].split(' ')[5])

    blueprint_dict[sentences[0][-1]]['Obsidian Robot']['Clay'] = int(sentences[3].split(' ')[8])

    blueprint_dict[sentences[0][-1]]['Geode Robot'] = {}

    blueprint_dict[sentences[0][-1]]['Geode Robot']['Ore'] = int(sentences[4].split(' ')[5])

    blueprint_dict[sentences[0][-1]]['Geode Robot']['Obsidian'] = int(sentences[4].split(' ')[8])

def buyNewRobot(inventory):
    robot = 'Ore'
    #help
    return robot, inventory

def getNewRobot(robot, robot_dict):
    match robot:
        case 'Ore':
            robot_dict['Ore Robot'] += 1
        case 'Clay':
            robot_dict['Clay Robot'] += 1
        case 'Obsidian':
            robot_dict['Obsidian Robot'] += 1
        case 'Geode':
            robot_dict['Geode Robot'] += 1
        case 'None':
            pass
    return robot_dict

def gatherMaterials(inventory, robots):
    for robot in robots:
        inventory_type = robot.split(' ')[0]
        inventory[inventory_type] += robots[robot]
    return inventory

def calculate_quality(blueprint):
    robot_dict = {
        'Ore Robot': 1,
        'Clay Robot': 0,
        'Obsidian Robot': 0,
        'Geode Robot': 0,
    }
    inventory_dict = {
        'Ore': 0,
        'Clay': 0,
        'Obsidian': 0,
        'Geode': 0
    }
    for i in range(TIMELIMIT):
        robot, inventory_dict = buyNewRobot(inventory_dict)
        inventory_dict = gatherMaterials(inventory_dict, robot_dict)
        robot_dict = getNewRobot(robot, robot_dict)
    return inventory_dict['Geode']

for blueprint in blueprint_dict:
    quality = calculate_quality(blueprint_dict[blueprint])
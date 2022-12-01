reindeer_speeds = {
    'vixen': {
        'fly': 7,
        'speed': 19,
        'rest': 124
    },
    'rudolph': {
        'fly': 15,
        'speed': 3,
        'rest': 28
    },
    'donner': {
        'fly': 9,
        'speed': 19,
        'rest': 164
    },
    'cupid': {
        'fly': 6,
        'speed': 25,
        'rest': 145
    },
    'dasher': {
        'fly': 3,
        'speed': 14,
        'rest': 48
    },
    'dancer': {
        'fly': 16,
        'speed': 3,
        'rest': 37
    },
    'prancer': {
        'fly': 6,
        'speed': 25,
        'rest': 143
    },
    'blitzen': {
        'fly': 9,
        'speed': 19,
        'rest': 158
    },
    'comet': {
        'fly': 7,
        'speed': 13,
        'rest': 82
    },

}

state_dict = {}
for reindeer in reindeer_speeds:
    state_dict[reindeer] = {}
    state_dict[reindeer]['is_flying'] = True
    state_dict[reindeer]['time_remaining'] = reindeer_speeds[reindeer]['fly']
    state_dict[reindeer]['distance'] = 0
    state_dict[reindeer]['points'] = 0

length = 2503
for second in range(length):
    for reindeer in state_dict:
        state_dict[reindeer]['time_remaining'] -= 1
        if state_dict[reindeer]['is_flying']:
            state_dict[reindeer]['distance'] += reindeer_speeds[reindeer]['speed']
        
        if state_dict[reindeer]['time_remaining'] == 0:
            
            if state_dict[reindeer]['is_flying']:
                state_dict[reindeer]['time_remaining'] = reindeer_speeds[reindeer]['rest']
            else:
                state_dict[reindeer]['time_remaining'] = reindeer_speeds[reindeer]['fly']
            state_dict[reindeer]['is_flying'] = not state_dict[reindeer]['is_flying']
    max_dist = 0
    for reindeer in state_dict:
        current_distance = state_dict[reindeer]['distance']
        if current_distance > max_dist:
            max_dist = current_distance
    for reindeer in state_dict:
        if max_dist == state_dict[reindeer]['distance']:
            state_dict[reindeer]['points'] += 1

for key in state_dict:
    print(key, state_dict[key]['points'])


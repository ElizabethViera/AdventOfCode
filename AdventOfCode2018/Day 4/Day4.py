fileContents = open("AdventOfCode2018/Day 4/input.txt")
data = fileContents.read().split("\n")

data_structure = dict() # guard -> minute -> number of dates asleep

dates = set()
guards = set()

event_queue = []
for event in data:
    # [1518-11-01 00:00] Guard #10 begins shift
    segments = event.split(' ')
    date = segments[0][1:]
    time = segments[1][:-1]
    event_type = segments[2]
    if event_type == 'Guard':
        guard_number = segments[3]
    else: 
        guard_number = ''
    event_queue.append((date, time, event_type, guard_number))
    dates.add(date)
    if guard_number != '':
        guards.add(guard_number)

sleep_queue = dict()
currentGuard = -1
asleep = False
for event in sorted(event_queue):
    date = event[0]
    if event[2] == 'Guard':
        currentGuard = event[3]
        if currentGuard not in sleep_queue:
            sleep_queue[currentGuard] = []
    if event[2] == 'falls':
        sleep_queue[currentGuard].append((event[0], event[1], 'sleep'))
    if event[2] == 'wakes':
        sleep_queue[currentGuard].append((event[0], event[1], 'awake'))
 
sleep_map = dict()
for guard in guards:
    sleep_map[guard] = dict()
    guard_total = 0
    awake = True
    while len(sleep_queue[guard]) > 0:
        sleep_event = sleep_queue[guard].pop(0) # date, time, awake or asleep
        awake_event = sleep_queue[guard].pop(0)
        #('1518-03-07', '00:15', 'sleep')
        for i in range(int(sleep_event[1][3:]), int(awake_event[1][3:])):
            if i not in sleep_map[guard]:
                sleep_map[guard][i] = 0
            sleep_map[guard][i] += 1

#for guard in sleep_map:
    #print(guard, sleep_map[guard])

max_seen = 0
max_minute = None
max_guard = None
for guard in sleep_map:
    for minute in sleep_map[guard]:
        if sleep_map[guard][minute] > max_seen:
            max_guard = guard
            max_seen = sleep_map[guard][minute]
            max_minute = minute


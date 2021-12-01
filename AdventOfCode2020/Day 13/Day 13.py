fileContents = open("Day 13/input")
arr = fileContents.read().split('\n')

earliest_time = int(arr[0])
bus_ids = arr[1].split(",")

result = 200000000

for bus_id in bus_ids:
    if bus_id == 'x':
        continue
    bus_int = int(bus_id)
    leq_time = (earliest_time // bus_int) * bus_int
    print(leq_time)
    if leq_time == 0:
        result = leq_time
        result_bus = bus_int
        break
    else:
        possible_time = leq_time + bus_int
        if possible_time < result:
            result = possible_time
            result_bus = bus_int
print(result_bus*(result - earliest_time))


def check_if_t_works(bus_ids, t):
    for i in range(len(bus_ids)):
        bus_id = bus_ids[i]
        if bus_id == 'x':
            continue
        bus_int = int(bus_id)
        if ((t + i) % bus_int) != 0:
            return False
    return True


result = 1
for bus_id in bus_ids:
    if bus_id != 'x':
        result *= int(bus_id)
print(result)

# t % bus_int == -i % bus_int
# 1936728611590279


def combine_eq(eq1, eq2):
    c1, m1 = eq1
    c2, m2 = eq2
    candidate = c2
    while True:
        if candidate % m1 == c1 and candidate % m2 == c2:
            return candidate, m1*m2
        candidate += m2


combine_arr = []
for i in range(len(bus_ids)):
    bus_id = bus_ids[i]
    if bus_id == 'x':
        continue
    bus_int = int(bus_id)
    #t % bus_int == -i % bus_int
    m = bus_int
    c = -i
    combine_arr.append((c % m, m))

result = (0, 1)
for combine in combine_arr:
    print(combine)
    result = combine_eq(combine, result)

print(result)

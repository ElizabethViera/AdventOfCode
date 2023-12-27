fileContents = open("AdventOfCode2016/Day 20/input.txt")
ranges = fileContents.read().split('\n')

min_ip = 0
max_ip = 

parsed_ranges = []
for r in ranges:
    left, right = int(r.split('-')[0]), int(r.split('-')[1])
    parsed_ranges.append((left, 's'))
    parsed_ranges.append((right, 'e'))
parsed_ranges.append((max_ip, 's'))
parsed_ranges = sorted(parsed_ranges)

total = 0
all_ips = 0
for r in range(len(parsed_ranges)):
    if parsed_ranges[r][1] == 's':
        total += 1
    if parsed_ranges[r][1] == 'e':
        total -= 1
    if total == 0:
        all_ips += parsed_ranges[r+1][0] - parsed_ranges[r][0] -1
print(all_ips)
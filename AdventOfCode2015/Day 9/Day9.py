fileContents = open("AdventOfCode2015/Day 9/input.txt")

arr = fileContents.read().split('\n')

distance_dict = {}
cities = set()
for dist in arr:
    dist_split = dist.split(' ')
    left_city, right_city, distance = dist_split[0], dist_split[2], int(dist_split[-1])

    cities.add(left_city) 
    cities.add(right_city)
    
    if left_city not in distance_dict:
        distance_dict[left_city] = {}
    if right_city not in distance_dict:
        distance_dict[right_city] = {}

    distance_dict[left_city][right_city] = distance
    distance_dict[right_city][left_city] = distance


import itertools
all_paths = list(itertools.permutations(cities))
best_distance = 0
for path in all_paths:
    distance = 0
    current_city = path[0]
    for next_city in path[1:]:
        distance += distance_dict[current_city][next_city]
        current_city = next_city
    best_distance = max(best_distance, distance)
print(best_distance)
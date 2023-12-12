fileContents = open("AdventOfCode2019/Day 6/input.txt")
arr = fileContents.read().split("\n")

orb_map = dict()

for orb in arr:
    left, right = orb.split(')')[0], orb.split(')')[1]
    orb_map[right] = left

you_orbits = []
current = 'YOU'
while current in orb_map:
    you_orbits.append(current)
    current = orb_map[current]

san_orbits = []
current = 'SAN'
while current in orb_map:
    san_orbits.append(current)
    current = orb_map[current]

print(len(you_orbits), len(san_orbits))
answer = -1
for i in range(len(san_orbits)):
    if you_orbits[::-1][i] == san_orbits[::-1][i]:
        continue
    else:
        answer = i
        break
print(len(you_orbits) - (answer + 1) + len(san_orbits) - (answer))


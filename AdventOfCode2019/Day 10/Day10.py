fileContents = open("AdventOfCode2019/Day 10/input.txt")
map_of_space = fileContents.read().split("\n")
import math

asteroids = set()

for r, row in enumerate(map_of_space):
    for c, col in enumerate(row):
        if col == "#":
            asteroids.add((r, c))


def get_slopes(a, all):
    all_slopes = set()
    for other in all:
        num, den = other[0] - a[0], other[1] - a[1]
        if num == 0 and den == 0:
            continue
        if num == 0:
            if den > 0:
                all_slopes.add((0, 1))
                continue
            if den < 0:
                all_slopes.add((0, -1))
                continue
        if den == 0:
            if num > 0:
                all_slopes.add((1, 0))
                continue
            if num < 0:
                all_slopes.add((-1, 0))
                continue

        gcd = math.gcd(num, den)
        result = (num / gcd, den / gcd)
        if result == (-1.0, -9.0):
            print("found!", other)
        all_slopes.add(result)
    return all_slopes


def get_quadrants(slopes):
    result = set()
    q1, q2, q3, q4, s = 0, 0, 0, 0, 0
    for slope in slopes:
        if slope[0] > 0 and slope[1] > 0:
            q1 += 1
        elif slope[0] > 0 and slope[1] < 0:
            q2 += 1
        elif slope[0] < 0 and slope[1] < 0:
            q3 += 1
            result.add(slope)
        elif slope[0] < 0 and slope[1] > 0:
            q4 += 1
        else:
            s += 1
    return [q1, q2, q3, q4, s, result]


answer = (11, 19)
all_slopes = get_slopes(answer, asteroids)
quadrants = get_quadrants(all_slopes)
print(sorted(quadrants[5])[-8])

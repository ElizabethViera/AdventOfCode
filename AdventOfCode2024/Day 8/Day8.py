listsContents = open("AdventOfCode2024/Day 8/input.txt")
antennas = listsContents.read().split("\n")

antenna_locs: dict[str, list[tuple[int, int]]] = dict()
all_locs = set()

for r, row in enumerate(antennas):
    for c, char in enumerate(row):
        all_locs.add((r, c))
        if char != ".":
            if char not in antenna_locs:
                antenna_locs[char] = []
            antenna_locs[char].append((r, c))


def get_slope(a: tuple[int, int], b: tuple[int, int]):
    result = []
    rise = a[0] - b[0]
    run = a[1] - b[1]
    for i in range(1, 70):
        result.append((a[0] + i * rise, a[1] + i * run))
        result.append((b[0] - i * rise, b[1] - i * run))
    return result


antinodes = set()

for character in antenna_locs:
    node_count = len(antenna_locs[character])
    if node_count == 1:
        continue
    else:
        for i in antenna_locs[character]:
            for j in antenna_locs[character]:
                if i != j:
                    antinodes.add(i)
                    antinodes.add(j)
                    s = sorted([i, j])
                    antinode_s = get_slope(s[0], s[1])
                    for a in antinode_s:
                        if a in all_locs:
                            antinodes.add(a)
print(len(antinodes))

# 3,4 and 5,5
# 1,3 and 7,6

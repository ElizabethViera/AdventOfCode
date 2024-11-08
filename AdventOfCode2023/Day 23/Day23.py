fileContents = open("AdventOfCode2023/Day 23/input.txt")
lines = fileContents.read().split("\n")

Pos = tuple[int, int]
neighbors: dict[Pos, list[Pos]] = dict()
paths: dict[Pos, str] = dict()


def add_pts(a: Pos, b: Pos) -> Pos:
  return a[0] + b[0], a[1] + b[1]


def get_neighbors(p: Pos, t: str):
  # point, type
  results: list[Pos] = []
  if t in ".<>v^":
    neighbor_list = [(-1, 0), (1, 0), (0, 1), (0, -1)]
  for n in neighbor_list:
    if add_pts(n, p) in paths:
      results.append(add_pts(n, p))
  return results


for r, row in enumerate(lines):
  for c, col in enumerate(row):
    if col != "#":
      paths[(r, c)] = col

for p in paths:
  neighbors[p] = get_neighbors(p, paths[p])

start = (0, 1)
end = (140, 139)

print(paths[end])


def find_all_paths():
  paths: list[list[Pos]] = [[start]]
  completed_paths: list[list[Pos]] = []
  while paths != []:
    current_path = paths.pop()
    n_list = neighbors[current_path[-1]]
    for n in n_list:
      if n in current_path:
        continue
      if n == end:
        completed_paths.append(current_path + [n])
        continue
      paths.append(current_path + [n])
  return completed_paths


def find_longest_path():
  best_path = max(find_all_paths(), key=len)
  return len(best_path)


print(find_longest_path() - 1)

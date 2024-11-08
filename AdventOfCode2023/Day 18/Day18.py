fileContents = open("AdventOfCode2023/Day 18/input.txt")
ins = fileContents.read().split("\n")

Pos = tuple[int, int]
points: list[Pos] = []

dirs = {3: (-1, 0), 1: (1, 0), 2: (0, -1), 0: (0, 1)}


def add_pts(a: Pos, b: Pos) -> Pos:
  return a[0] + b[0], a[1] + b[1]


def get_dist_travelled(dis, direct):
  d = dirs[direct]
  return d[0] * dis, d[1] * dis


loc = (0, 0)
points.append(loc)
for i in ins:
  left, right = i.split("(")[0], i.split("(")[1][1:-1]
  hex_code = right[:5]
  dirr = int(right[-1])
  dist = int(hex_code, 16)
  loc = add_pts(loc, get_dist_travelled(dist, dirr))
  points.append(loc)
print(points)

points = sorted(points)

overall_total = 0
last_x = points[0][0]
last_y = points[0][1]
in_bounds = True
local_total = 0
for p in points[1:]:
  if p[0] != last_x:
    overall_total += local_total * (p[0] - last_x)
    last_x = p[0]
    local_total = 0
    last_y = p[1]
  else:
    if in_bounds:
      local_total += p[1] - last_y  # TODO handle negative values
    else:
      pass
    last_y = p[1]
    in_bounds = not in_bounds

overall_total += local_total * (p[0] - last_x)
last_x = p[0]
local_total = 0
last_y = p[1]

print(overall_total - 952408144115)

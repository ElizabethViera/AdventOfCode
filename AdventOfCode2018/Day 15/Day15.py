from dataclasses import dataclass

pos = tuple[int, int]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


@dataclass
class Unit:
  type: str
  location: pos
  health: int = 200
  attack: int = 3
  died: bool = False

  def attacks(self, opponent: "Unit"):
    opponent.health -= self.attack
    if opponent.health <= 0:
      opponent.died = True


def add_pts(a: pos, b: pos):
  return (a[0] + b[0], a[1] + b[1])


def get_neighbors(p: pos) -> list[pos]:
  result: list[pos] = []
  for d in directions:
    candidate_loc = add_pts(p, d)
    if candidate_loc not in walls:
      result.append(candidate_loc)
  return result


def distanceToLoc(s: pos, t: pos) -> int | None:
  distances = [(s)]
  all_distances: dict[pos, int] = dict()
  all_distances[s] = 0
  while distances != []:
    to_check = distances.pop(0)
    neighbors = get_neighbors(to_check)
    for n in neighbors:
      if n == t:
        return all_distances[to_check] + 1
      if n in all_unit_locations or n in all_distances:
        continue
      else:
        distances.append(n)
        all_distances[n] = all_distances[to_check] + 1
  return None  # no path to target


def distanceToEverything(s: pos) -> dict[pos, int]:
  distances = [(s)]
  all_distances: dict[pos, int] = dict()
  all_distances[s] = 0
  while distances != []:
    to_check = distances.pop(0)
    neighbors = get_neighbors(to_check)
    for n in neighbors:
      if n in all_unit_locations or n in all_distances:
        continue
      else:
        distances.append(n)
        all_distances[n] = all_distances[to_check] + 1
  return all_distances


def inRangeOfTarget(unit: Unit, targets: list[Unit]):
  unit_range: list[pos] = []
  for d in directions:
    unit_range.append(add_pts(unit.location, d))
  for t in targets:
    if t.died:
      continue
    if t.location in unit_range:
      return True
  return False


def getInRangeTargets(unit: Unit, targets: list[Unit]):
  unit_range: list[pos] = []
  for d in directions:
    unit_range.append(add_pts(unit.location, d))
  in_range_targets: list[Unit] = []
  for t in targets:
    if t.died:
      continue
    if t.location in unit_range:
      in_range_targets.append(t)
  return in_range_targets


def getAllTargetHitBoxes(targets: list[Unit]) -> list[pos]:
  result: list[pos] = []
  targets = [t for t in targets if not t.died]
  for t in targets:
    for d in directions:
      candidate = add_pts(t.location, d)
      if candidate not in walls and candidate not in all_unit_locations:
        result.append(candidate)
  return result


#####################
# Parse Initial State
#####################
fileContents = open("AdventOfCode2018/Day 15/input.txt")
contents = fileContents.read().split("\n")
walls: set[pos] = set()
all_unit_locations: set[pos] = set()
elves: list[Unit] = []
goblins: list[Unit] = []

for row, line in enumerate(contents):
  for col, c in enumerate(line):
    location = (row, col)
    if c == "#":
      walls.add(location)
    if c == "E":
      elf = Unit("E", location)
      elves.append(elf)
      all_unit_locations.add(location)
    if c == "G":
      goblin = Unit("G", location)
      goblins.append(goblin)
      all_unit_locations.add(location)


def get_next_step(unit_location: pos, destination: pos) -> pos:
  all_distances = distanceToEverything(destination)
  steps_from_unit_location = [
    add_pts(d, unit_location)
    for d in directions
    if add_pts(d, unit_location) in all_distances
  ]

  def next_step_key(step: pos) -> tuple[int, tuple[int, int]]:
    return (all_distances[step], step)

  return min(steps_from_unit_location, key=next_step_key)


def get_destination(unit_location: pos, battle_spaces: list[pos]):
  all_distances = distanceToEverything(unit_location)
  battle_spaces = [
    battle_space for battle_space in battle_spaces if battle_space in all_distances
  ]

  if battle_spaces == []:
    return None

  def battle_space_key(battle_space: pos) -> tuple[int, tuple[int, int]]:
    return (all_distances[battle_space], battle_space)

  return min(battle_spaces, key=battle_space_key)


def sortByLocation(u: Unit):
  return u.location


def takeTurn():
  all_units_at_start_of_turn = sorted(elves + goblins, key=sortByLocation)
  for unit in all_units_at_start_of_turn:
    if unit.died:
      continue
    if unit.type == "E":
      targets = goblins
    elif unit.type == "G":
      targets = elves
    else:
      raise (ValueError)
    targets = [t for t in targets if not t.died]
    if len(targets) == 0:
      print("Game Over")
      return True
    if inRangeOfTarget(unit, targets):
      # don't move
      pass
    else:
      # decide if/how to move
      targetHitBoxes = getAllTargetHitBoxes(targets)
      destination = get_destination(unit.location, targetHitBoxes)
      if destination:
        new_location = get_next_step(unit.location, destination)
        all_unit_locations.remove(unit.location)
        unit.location = new_location
        all_unit_locations.add(new_location)
    if inRangeOfTarget(unit, targets):
      in_range_targets = getInRangeTargets(unit, targets)
      if in_range_targets != []:
        getting_thwacked = min(in_range_targets, key=lambda x: x.health)
        unit.attacks(getting_thwacked)
        if getting_thwacked.died:
          all_unit_locations.remove(getting_thwacked.location)
  return False


def calculateScore(e: list[Unit], g: list[Unit], round: int) -> int:
  sum_of_alive_team = 0
  for elf in e:
    if not elf.died:
      sum_of_alive_team = sum([i.health for i in e if not i.died])
  for gob in g:
    if not gob.died:
      sum_of_alive_team = sum([i.health for i in g if not i.died])
  return sum_of_alive_team * round


def print_board(g: list[Unit], e: list[Unit], w: set[pos]):
  for i in range(8):
    for j in range(7):
      goblin_pos = [p.location for p in g if not p.died]
      elf_pos = [p.location for p in e if not p.died]
      if (i, j) in w:
        print("#", end="")
      elif (i, j) in goblin_pos:
        print("G", end="")
      elif (i, j) in elf_pos:
        print("E", end="")
      else:
        print(".", end="")
    print("")


round = 0
while True:
  print(round)
  round += 1
  gameOver = takeTurn()
  # print(elves, goblins)
  # print_board(goblins, elves, walls)
  if gameOver:
    print(calculateScore(elves, goblins, round - 1))
    raise (ValueError())

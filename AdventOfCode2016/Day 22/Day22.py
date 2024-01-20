fileContents = open("AdventOfCode2016/Day 22/input.txt")
arr = fileContents.read().split('\n')
width = 34
height = 30
nodes = dict()
allowed_spots: set[tuple[int,int]] = set()
empty = -1,-1
for line in arr:
    x,y = int(line.split(' ')[0].split('-')[-2][1:]), int(line.split(' ')[0].split('-')[-1][1:])
    used, avail = int(line.split(' ')[2][:-1]), int(line.split(' ')[3][:-1])
    nodes[(x,y)] = (used,avail)
    if used == 0:
        empty = (x,y)
    if used < 200:
        allowed_spots.add((x,y))

import dataclasses

dirs = [(-1, 0), (1,0), (0,1), (0,-1)]

def add(a: tuple[int,int],b:tuple[int,int]):
    return a[0] + b[0], a[1] + b[1]

@dataclasses.dataclass(frozen=True)
class State:
    data: tuple[int,int]
    blank: tuple[int,int]

    def moveBlank(self, d: tuple[int,int]) -> "State | None":
        if add(d, self.blank) in allowed_spots:
            if add(d, self.blank) == self.data:
                return State(data=self.blank, blank=self.data)
            else:
                return State(data=self.data, blank=add(d,self.blank))
        else:
            return None
        
starting_state = State(data=(width-1,0), blank=empty)
states = [starting_state]
distances: dict[State, int] = dict()
distances[starting_state] = 0
while states != []:
    current_state = states.pop(0)
    if current_state.data == (0,0):
        print(distances[current_state])
        raise ValueError()
    for d in dirs:
        next_state = current_state.moveBlank(d)
        if next_state != None and next_state not in distances:
                distances[next_state] = distances[current_state] + 1
                states.append(next_state)
            
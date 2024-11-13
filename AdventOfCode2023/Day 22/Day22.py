from dataclasses import dataclass
import copy
from typing import Mapping

fileContents = open("AdventOfCode2023/Day 22/input.txt")
lines = fileContents.read().split("\n")

pos3 = tuple[int, int, int]


@dataclass
class Brick:
    bricks: list[tuple[int, int, int]]
    moved: bool

    def shift_down(self) -> list[pos3]:
        new_bricks: list[pos3] = []
        for b in self.bricks:
            new_bricks.append((b[0], b[1], b[2] - 1))
        return new_bricks

    def collides(self, other: "Brick"):
        for b in self.bricks:
            if b in other.bricks:
                return True
        return False


all_bricks: dict[int, Brick] = dict()

i = 0
for brick in lines:
    [left, right] = brick.split("~")
    lx, ly, lz = (
        int(left.split(",")[0]),
        int(left.split(",")[1]),
        int(left.split(",")[2]),
    )
    rx, ry, rz = (
        int(right.split(",")[0]),
        int(right.split(",")[1]),
        int(right.split(",")[2]),
    )
    if lx != rx:
        assert ly == ry
        assert lz == rz
        # x coordinate is different
        bricks = [(x, ly, lz) for x in range(lx, rx + 1)]
    elif ly != ry:
        assert lx == rx
        assert lz == rz
        # x coordinate is different
        bricks = [(lx, y, lz) for y in range(ly, ry + 1)]
    elif lz != rz:
        assert lx == rx
        assert ly == ry
        # z coordinate is different
        bricks = [(lx, ly, z) for z in range(lz, rz + 1)]
    else:
        bricks = [(lx, ly, lz)]
    all_bricks[i] = Brick(bricks=bricks, moved=False)
    i += 1


def is_valid(new_brick: Brick, state: dict[int, Brick], i: int):
    for coord in new_brick.bricks:
        if coord[2] < 1:
            return False

    for b in state:
        if i != b:
            collides = new_brick.collides(state[b])
            if collides:
                return False
    return True


def drop_all_bricks(bricks: Mapping[int, Brick]) -> dict[int, Brick]:
    bricks_copy = dict(bricks)
    while True:
        state_updated = 0
        for i in bricks_copy:
            new_brick = Brick(bricks_copy[i].shift_down(), moved=True)
            if is_valid(new_brick, bricks_copy, i):
                bricks_copy[i] = new_brick
                state_updated += 1
        if state_updated == 0:
            return bricks_copy


alph = "ABCDEFGHIJK"


def print_bricks(bricks: dict[int, Brick]):
    map_of_bricks: dict[tuple[int, int], str] = dict()

    for b in bricks:
        for block in bricks[b].bricks:
            if (block[2], block[0]) in map_of_bricks and map_of_bricks[
                (block[2], block[0])
            ] != alph[b]:
                map_of_bricks[(block[2], block[0])] = "?"
            else:
                map_of_bricks[(block[2], block[0])] = alph[b]

    for row in range(10, -1, -1):
        for col in range(2, -1, -1):
            if (row, col) in map_of_bricks:
                print(map_of_bricks[(row, col)], end="")
            else:
                print(".", end="")
        print("")


all_bricks = drop_all_bricks(all_bricks)
for i in all_bricks:
    all_bricks[i].moved = False

print("dropped")
# print_bricks(all_bricks)

total = 0
for i, _ in enumerate(all_bricks):
    print(i)
    bricks_minus_one = copy.deepcopy(all_bricks)
    del bricks_minus_one[i]
    new_bricks = drop_all_bricks(bricks_minus_one)
    for j in new_bricks:
        if new_bricks[j].moved:
            total += 1
print(total)

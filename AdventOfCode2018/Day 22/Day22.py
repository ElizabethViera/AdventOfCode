from dataclasses import dataclass
from typing import Literal

fileContents = open("AdventOfCode2018/Day 22/input.txt")
rows = fileContents.read().split("\n")


@dataclass
class Region:
    x: int
    y: int
    terrain_type: Literal["rocky", "wet", "narrow"]
    erosion_level: int
    geological_index: int


regions: dict[tuple[int, int], Region] = dict()


def get_geo_ind(row: int, col: int) -> int:
    if row == 0 and col == 0:
        return 0
    if row == TARGET[1] and col == TARGET[0]:
        return 0
    if row == 0:
        return col * 16807
    if col == 0:
        return row * 48271
    left, up = (row - 1, col), (row, col - 1)
    return regions[left].erosion_level * regions[up].erosion_level


def get_ero_lev(geo_ind: int) -> int:
    DEPTH = 0
    MODULO = 20183
    return (geo_ind + DEPTH) % MODULO


def get_terrain_type(ero_level: int):
    match ero_level % 3:
        case 0:
            return "rocky"
        case 1:
            return "wet"
        case 2:
            return "narrow"
        case _:
            raise (ValueError)


for row in range(TARGET[0] + 1):
    for col in range(TARGET[1] + 1):
        geo_ind = get_geo_ind(row, col)
        ero_lev = get_ero_lev(geo_ind)
        terrain_typ = get_terrain_type(ero_lev)
        regions[(row, col)] = Region(
            x=row,
            y=col,
            terrain_type=terrain_typ,
            erosion_level=ero_lev,
            geological_index=geo_ind,
        )

score = 0
for region in regions:
    if regions[region].terrain_type == "rocky":
        score += 0
    if regions[region].terrain_type == "wet":
        score += 1
    if regions[region].terrain_type == "narrow":
        score += 2
print(score)

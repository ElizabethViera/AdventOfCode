from dataclasses import dataclass
from typing import Any, Callable, cast

@dataclass
class Grid[T]:
    items: list[list[T]]

    def size(self):
        for row in self.items:
            assert len(row) == len(self.items)
        return len(self.items[0])

    def __getitem__(self, i: tuple[int, int]) -> T:
        return self.items[i[0]][i[1]]
    
    def map[S](self, func: Callable[[T], S]) -> "Grid[S]":
        return Grid([[func(j) for j in i] for i in self.items])
    
    def countHashtags(self):
        count = 0
        for i in self.items:
            for j in i:
                if j == '#':
                    count += 1
        return count

def breakIntoSquares[T](g: Grid[T], n: int) -> Grid[Grid[T]]:
    size = g.size()
    chunks: list[list[Grid[T]]] = []
    for i in range(0, size, n):
        row = []
        for j in range(0, size, n):
            chunk = Grid(
                [[g[l, k] for k in range(j, j+n)] for l in range(i, i+n)])
            row.append(chunk)
        chunks.append(row)
    return Grid(chunks)

def flipGrid(g):
    newGrid = []
    for row in g:
        row = row[::-1]
        newGrid.append(row)
    return newGrid

def rotate(g):
    return [[g[j][i] for j in range(len(g))] for i in range(len(g[0])-1,-1,-1)]

def getAllEightRotationsAndFlips(g):
    result = []
    grid = g
    for i in range(4):
        result.append(grid)
        result.append(flipGrid(grid))
        grid = rotate(grid)
    return result

def turnGridIntoString(g):
    return '/'.join(''.join(r) for r in g)

def enhance(grid: Grid[str])-> Grid[str]:
    g = grid.items
    allRotates = getAllEightRotationsAndFlips(g)
    for r in allRotates:
        if turnGridIntoString(r) in rules:
            return Grid(stringToGrid(rules[turnGridIntoString(r)]))
    print(allRotates)
    raise ValueError('Rule Not Found For grid')

def stringToGrid(s):
    rows = s.split('/')
    return [[c for c in row] for row in rows]

def collapseOfCivilization[T](g: Grid[Grid[T]]) -> Grid[T]:
    k = g.size() * g[0,0].size()
    outArray: list[list[T]] = [[cast(Any,...) for __ in range(k)] for _ in range(k)]
    grid = g.items
    for outerRow in range(len(grid)):
        for outerCol in range(len(grid)):
            for innerRow in range(g[0,0].size()):
                for innerCol in range(g[0,0].size()):
                    outArray[outerRow*g[0,0].size() + innerRow][outerCol*g[0,0].size() + innerCol] = g[outerRow,outerCol][innerRow,innerCol]
    return Grid(outArray)

fileContents = open("AdventOfCode2017/Day 21/input.txt")
arr = fileContents.read().split('\n')

rules = dict()
for rule in arr:
    left, right = rule.split(' => ')[0], rule.split(' => ')[1]
    rules[left] = right

start = stringToGrid('.#./..#/###')

def step(g: Grid[str]):
    if g.size()%2 == 0:
        chunks = breakIntoSquares(g, 2)
    elif g.size()%3 == 0:
        chunks = breakIntoSquares(g, 3)
    else:
        raise ValueError('ugh')
    newChunks = chunks.map(enhance)
    return collapseOfCivilization(newChunks)

g = Grid(start)
for i in range(5):
    print(i)
    g = step(g)

print(g.countHashtags())

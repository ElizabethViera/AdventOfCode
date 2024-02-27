import functools
from operator import indexOf


fileContents = open("AdventOfCode2017/Day 16/input.txt")
arr = fileContents.read().split(',')

line_dance = 'abcdefghijklmnop'

def spin(s, n):
    z = [c for c in s]
    z = s[-n:] + s[:-n]
    return ''.join(z)

def exchange(s: str, l:int, r:int):
    a: list[str] = [c for c in s]
    a[l], a[r] = a[r], a[l]
    return ''.join(a)

def partner(s, l, r):
    left = s.index(l)
    right = s.index(r)
    return exchange(s, left, right)

from functools import cache

@cache
def dance(line_dance):
    for ins in arr:
        if ins.startswith('s'):
            n = int(ins[1:])
            line_dance = spin(line_dance, n)
        elif ins.startswith('x'):
            l,r = ins[1:].split('/')[0], ins[1:].split('/')[1]
            line_dance = exchange(line_dance, int(l), int(r))
        elif ins.startswith('p'):
            l,r = ins[1:].split('/')[0], ins[1:].split('/')[1]
            line_dance = partner(line_dance, l, r)
    return line_dance

for i in range(1000000000):
    if i % 100000000 == 0:
        print(i)
    line_dance = dance(line_dance)

print(line_dance)
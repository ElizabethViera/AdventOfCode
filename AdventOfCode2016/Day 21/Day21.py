pw = 'fbgdceah'

def swapPos(p,x,y):
    p[x], p[y] = p[y], p[x]
    return p

def swapLet(p,x,y):
    p = ''.join(p)
    p = p.replace(x, '*')
    p = p.replace(y, '&')
    p = p.replace('*', y)
    p = p.replace('&', x)
    p = [c for c in p]
    return p

def rotateLeft(p, n):
    for i in range(n):
        k = p.pop(0)
        p.append(k)
    return p

def rotateRight(p,n):
    for i in range(n):
        k = p.pop()
        p = [k] + p
    return p

def rotatePosRight(p,x):
    r = None
    for i in range(len(p)):
        if p[i] == x:
            r = i
    if r is None:
        raise(ValueError)
    if r >= 4:
        r += 1
    return rotateRight(p,r+1)

def rev(p,x,y):
    return p[:x] + p[x:y+1][::-1] + p[y+1:]

def move(p,x,y):
    i = p[x]
    p = p[:x] + p[x+1:]
    p = p[:y] + [i] + p[y:]
    return p


def parseLine(l:str, p):
    if l.startswith('swap position'):
        x, y = int(l.split(' ')[2]), int(l.split(' ')[-1])
        return swapPos(p,x,y)
    if l.startswith('swap letter'):
        x,y = l.split(' ')[2], l.split(' ')[-1]
        return swapLet(p,x,y)
    if l.startswith('rotate left'):
        n = int(l.split(' ')[2])
        return rotateLeft(p,n)
    if l.startswith('rotate right'):
        n = int(l.split(' ')[2])
        return rotateRight(p,n)
    if l.startswith('rotate based'):
        x = l.split(' ')[-1]
        return rotatePosRight(p,x)
    if l.startswith('reverse'):
        x,y = int(l.split(' ')[2]), int(l.split(' ')[-1])
        return rev(p,x,y)
    if l.startswith('move position'):
        x,y = int(l.split(' ')[2]), int(l.split(' ')[-1])
        return move(p,x,y)
    raise(ValueError)

fileContents = open("AdventOfCode2016/Day 21/input.txt")
arr = fileContents.read().split('\n')

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
import itertools
for perm in itertools.permutations(chars):
    result = list(perm)
    for line in arr:
        result = parseLine(line, result)
    if ''.join(result) == pw:
        print(perm)
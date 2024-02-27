fileContents = open("AdventOfCode2017/Day 11/input.txt")
arr = fileContents.read().split(',')
s = set()
dirs_in_order = ['n', 'nw', 'sw', 's', 'se', 'ne']

def atInitialSegment(l):
    dirs = dict()
    dirs['s'] = 0
    dirs['n'] = 0
    dirs['sw'] = 0
    dirs['se'] = 0
    dirs['nw'] = 0
    dirs['ne'] = 0

    for a in l:
        dirs[a] += 1

    def sub(s,n):
        subtr = min(dirs[s], dirs[n])
        dirs[s], dirs[n] = dirs[s] - subtr, dirs[n] - subtr
        return subtr
    
    sub('s', 'n')
    sub('sw', 'ne')
    sub('se', 'nw')

    for i in range(6):
        a,b,c = dirs_in_order[i], dirs_in_order[i-1], dirs_in_order[i-2]
        if dirs[a] > 0 and dirs[c] > 0:
            dirs[b] += sub(a,c)
    dist = sum(dirs.values())
    return dist
    
for i in range(len(arr)):
    s.add(atInitialSegment(arr[:i]))

print(sorted(s)[-1])


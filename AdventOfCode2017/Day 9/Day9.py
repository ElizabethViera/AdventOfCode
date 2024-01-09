#{{<a>},{<a>},{<a>},{<a>}}


fileContents = open("AdventOfCode2017/Day 9/input.txt")
stream = fileContents.read()

nests = 0
garbage = False
canceled = False
score = 0
for c in stream:
    if not garbage and not canceled:
        if c == '{':
            nests += 1
        if c == '}':
            nests -= 1
        if c == '<':
            garbage = True
    elif not canceled:
        if c == '>':
            garbage = False
        elif c == '!':
            canceled = True
        else:
            score += 1
    else:
        canceled = False

        
print(score)
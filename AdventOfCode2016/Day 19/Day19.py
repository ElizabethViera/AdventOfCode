elves = [i for i in range(1,3005291)]
while len(elves) > 1:
    print(elves)
    if len(elves)%2 == 0:
        elves = [i for e,i in enumerate(elves) if e%2 == 0]
    else:
        elves = [i for e,i in enumerate(elves) if e%2 == 0 and e != 0]
print(elves)

# 1816277
# 2097151
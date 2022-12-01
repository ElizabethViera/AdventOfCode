capacities = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

all_capacities = powerset(capacities)

total = 0
min_capacity = 20
for capacity in all_capacities:
    if sum(capacity) == 150:
        if len(capacity) < min_capacity:
            total = 1
            min_capacity = len(capacity)
        elif len(capacity) == min_capacity:
            total += 1

print(total)
new_value = [1,2,3,4,5] #my input as a comma separated array
perms = [0,1,0,-1]

def do_thing(val, perms):
    # calculate digit
    result = []
    for i, v in enumerate(val):
        total = 0
        created_indexes = []
        for a in perms:
            for b in range(i+1):
                created_indexes.append(a)
        while len(created_indexes) < len(val)+1:
            created_indexes = created_indexes + created_indexes
        created_indexes = created_indexes[:len(val)+1]
        created_indexes = created_indexes[1:]
        for j, u in enumerate(val):
            #print(u, created_indexes[j])
            total += u*created_indexes[j]
        if total < 0:
            total *= -1
        total %= 10
        result.append(total)
    return result

for i in range(100):
    new_value = do_thing(new_value, perms)
print(new_value[:8])
target = [] #specific to me
limits = [] 
current = [] 

t = 0
while current != target:
    t += 1
    for i in range(len(current)):
        current[i] += 1
        if current[i] == limits[i]:
            current[i] = 0
print(t)
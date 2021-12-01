for i in range(len(ar)):
    for j in range(i, len(ar)):
        if ar[i] + ar[j] == 2020:
            print(ar[i] * ar[j])

for i in range(len(ar)):
    for j in range(i, len(ar)):
        for k in range(j, len(ar)):
            if ar[i] + ar[j] + ar[k] == 2020:
                print(ar[i] * ar[j] * ar[k])

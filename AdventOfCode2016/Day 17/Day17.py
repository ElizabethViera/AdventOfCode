dirs = [(-1,0), (1,0), (0,-1), (0,1)]
dirs_letters = ['U', 'D', 'L', 'R']
rows = 4
cols = 4

import hashlib
def get_neighbors(pathSoFar: str) -> list[bool]:
    hashthis = special_hash + pathSoFar
    result = hashlib.md5(hashthis.encode())
    result = str(result.hexdigest())
    u, d, l, r = result[0], result[1], result[2], result[3] 
    opens = []
    for c in [u,d,l,r]:
        opens.append(c in 'bdcef')
    return opens

def add_pts(a,b):
    return a[0] + b[0], a[1] + b[1]

locations: list[tuple[tuple[int, int], str]] = [((0,0), '')]

while True:
    current_location = locations.pop(0)
    if current_location[0] == (3,3):
        continue
    neighbors = get_neighbors(current_location[1])
    for i,neighbor in enumerate(neighbors):
        if neighbor:
            newLocation = add_pts(current_location[0], dirs[i])
            if newLocation[0] >= 0 and newLocation[0] < rows and newLocation[1] >= 0 and newLocation[1] < cols:
                newPath = current_location[1] + dirs_letters[i]
                locations.append((newLocation, newPath))
    
1
fileContents = open("AdventOfCode2018/Day 7/sampleInput.txt")
lines = fileContents.read().split("\n")

dependencies = dict()

for dependency in lines:
    left, right = dependency.split(' ')[1], dependency.split(' ')[7]
    if left not in dependencies:
        dependencies[left] = []
    if right not in dependencies:
        dependencies[right] = []
    dependencies[right].append(left)

full_list = dict()

def collapseNode(key):
    global full_list
    if key in full_list:
        return full_list[key]
    children = dependencies[key]
    results = set()
    for child in children:
        results.add(child)
        child_results = collapseNode(child)
        for child_result in child_results:
            results.add(child_result)
    results = list(results)
    full_list[key] = results
    return results

for key in dependencies:
    collapseNode(key)

def sortBy(k):
    return len(full_list[k]), k

def completed(full_list, l):
    for k in full_list:
        if l in full_list[k]:
           full_list[k].remove(l)
    return full_list

def getNextItemForWorker(full_list):
    if len(full_list) == 0:
        return None, full_list
    keys = sorted(full_list, key=sortBy)
    if full_list[keys[0]] == []:
        letter = keys[0]
        print(letter)
        time = all_letters.index(letter) + 1
        del full_list[letter]
        return [time, letter], full_list
    else:
        return None, full_list

answer = ''

workers = dict()
workers[0] = None
workers[1] = None
# workers[2] = None
# workers[3] = None
# workers[4] = None

all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

t = 0
while len(full_list) > 0:
    t += 1
    print(workers)
    for worker in workers:
        if workers[worker] != None:
            workers[worker][0] -= 1
            if workers[worker][0] == 0:
                full_list = completed(full_list, workers[worker][1])
                workers[worker] = None
    for worker in workers:
        if workers[worker] == None:
            workers[worker], full_list = getNextItemForWorker(full_list)
    
print(t, workers) # add the workers to t

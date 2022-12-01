
import json

fileContents = open("AdventOfCode2015/Day 12/input.json")

arr = json.load(fileContents)

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                if x[a] == 'red':
                    return

            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

flattened_arr = flatten_json(arr)

print(flattened_arr)
result = 0
for key in flattened_arr: 
    if type(flattened_arr[key]) is int:
        result += flattened_arr[key]
print(result)

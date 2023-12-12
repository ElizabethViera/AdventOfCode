fileContents = open("AdventOfCode2019/Day 8/input.txt")
arr = fileContents.read().split("\n")[0]

# 0 black, 1 white, 2 transparent

rows = 6
cols = 25

layers = []
layer = []
for i,c in enumerate(arr):
    if i%(rows*cols) == 0:
        layers.append(layer)
        layer = []
    layer.append(c)
layers.append(layer)

layers = layers[1:]

def findColor(n, l):
    for layer in l:
        print(layer[n])
        if layer[n] == '0':
            return '#'
        if layer[n] == '1':
            return '.'
    return ''
color_map = ''

for i in range(len(layers[0])):
    color = findColor(i,layers)
    print(color)
    color_map += color
    if i%25 == 0:
        color_map += '\n'

print(color_map)
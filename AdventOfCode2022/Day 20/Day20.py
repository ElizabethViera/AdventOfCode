fileContents = open("AdventOfCode2022/Day 20/input.txt")
arr = fileContents.read().split("\n")
arr = [int(a)* 811589153 for a in arr]
# print(arr)

def mixArr(arr: list[int]):
    arr_dict = []
    for i,a in enumerate(arr):
        arr_dict.append((i,a))

    for j in range(10):
        for i in range(len(arr)):
            for x,y in enumerate(arr_dict):
                if y[0] == i:
                    break
            arr_dict.pop(x)
            arr_dict.insert((x+y[1])%len(arr_dict), y)
    return arr_dict

arr_dict = mixArr(arr)
for x,y in enumerate(arr_dict):
            if y[1] == 0:
                break
print(arr_dict[(x + 1000)%len(arr_dict)][1] + arr_dict[(x + 2000)%len(arr_dict)][1] + arr_dict[(x + 3000)%len(arr_dict)][1])



# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
fileContents = open("AdventOfCode2018/Day 8/sampleInput.txt")
nodes = fileContents.read().split(" ")
nodes = [int(x) for x in nodes]

def processNode(n) -> int:
    num_children, metadata_len = n[0], n[1]
    if num_children == 0:
        return metadata_len
    if num_children > 0:
        next_child = processNode(n[2:])
        
        for i in num_children:
            

        this_node_end = 
    
    return 0
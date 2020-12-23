fileContents = open("Day 23/input")
arr = fileContents.read().split('\n')
arr = [int(c) for c in arr[0]]
print(arr)
for i in range(10, 1000001):
    arr.append(i)

highest_node_val = 1000000

node_dict = {}


class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None
        node_dict[value] = self

    def removesNextNeighbor(self):
        cut_node = self.next
        self.next = self.next.next
        cut_node.next = None
        return cut_node

    def insertNextNeighbor(self, node):
        node.next = self.next
        self.next = node


currentNode = None
for v in arr:
    if currentNode:
        oldNode = currentNode
        currentNode = ListNode(v)
        oldNode.next = currentNode
    else:
        currentNode = ListNode(v)
        firstNode = currentNode
currentNode.next = firstNode

currentNode = firstNode
for i in range(10000000):
    if i % 10000 == 0:
        print(i)
    firstNode = currentNode.removesNextNeighbor()
    secondNode = currentNode.removesNextNeighbor()
    thirdNode = currentNode.removesNextNeighbor()
    destination = currentNode.val - 1
    while destination in [firstNode.val, secondNode.val, thirdNode.val, 0]:
        if destination == 0:
            destination = highest_node_val
            continue
        destination -= 1
    node_dict[destination].insertNextNeighbor(thirdNode)
    node_dict[destination].insertNextNeighbor(secondNode)
    node_dict[destination].insertNextNeighbor(firstNode)
    currentNode = currentNode.next
cup1 = node_dict[1].next.val
cup2 = node_dict[1].next.next.val
print(cup1 * cup2)
current_cup_index = 0

# Part 1:


# for i in range(100):
#     current_cup_value = arr[current_cup_index]
#     try:
#         value1 = arr.pop(current_cup_index+1)
#     except:
#         value1 = arr.pop(0)
#     try:
#         value2 = arr.pop(current_cup_index+1)
#     except:
#         value2 = arr.pop(0)
#     try:
#         value3 = arr.pop(current_cup_index+1)
#     except:
#         value3 = arr.pop(0)
#     destination_cup_value = current_cup_value - 1
#     while(destination_cup_value not in arr):
#         destination_cup_value -= 1
#         if destination_cup_value < 1:
#             destination_cup_value = 12
#     if destination_cup_value in arr:
#         destination_index = arr.index(destination_cup_value)
#         arr = arr[:destination_index+1] + \
#             [value1, value2, value3] + arr[destination_index+1:]
#     # re get the current cup index in case insertions changed it, add one
#     current_cup_index = arr.index(current_cup_value) + 1
#     if current_cup_index >= len(arr):
#         current_cup_index %= len(arr)

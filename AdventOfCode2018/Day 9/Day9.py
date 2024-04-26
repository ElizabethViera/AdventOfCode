from dataclasses import dataclass
from typing import cast

@dataclass
class DLLNode:
    value: int
    left: "DLLNode"
    right: "DLLNode"

    def __repr__(self) -> str:
        if self.left != None and self.right != None:
            return "value: " + str(self.value) + " left: " + str(self.left.value) + " right: " + str(self.right.value)
        else:
            return "left or right is undefined for " + str(self.value)

zero_node = DLLNode(0, cast("DLLNode", None), cast("DLLNode", None))
one_node = DLLNode(1, cast("DLLNode", None), cast("DLLNode", None))
two_node = DLLNode(2, zero_node, one_node)
zero_node.left = one_node
zero_node.right = two_node
one_node.right = zero_node
one_node.left = two_node


PLAYERS = 11 # fake number
LAST_MARBLE = 11 # fake number

scores = [0 for _ in range(PLAYERS)]


current_player = 2
current_value = 2
current_node = two_node

while current_value <= LAST_MARBLE:
    # print(current_node)
    current_node = current_node.right
    current_player += 1
    if current_player >= PLAYERS:
        current_player = 0
    current_value += 1
    if current_value % 23 == 0:
        scores[current_player] += current_value
        for i in range(8):
            current_node = current_node.left
        scores[current_player] += current_node.value
        current_node.right.left, current_node.left.right = current_node.left, current_node.right
        current_node = current_node.right
    else:
        new_node = DLLNode(current_value, current_node, current_node.right)
        current_node.right, new_node.right.left = new_node, new_node
        current_node = new_node

print(sorted(scores)[-1])
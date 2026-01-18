# Course Section: CSC 2720-012

"""
Assignment: Parse Tree, create a evaluate function
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Construct the parse tree for ((7 + 3) * (5 - 2))
root = Node("*")
root.left = Node("+")
root.right = Node("-")
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(2)


def evaluate(node):
    # TODO: Implement this method
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.value

    leftSubtree = evaluate(node.left)
    rightSubtree = evaluate(node.right)

    if node.value == "+":
        return leftSubtree + rightSubtree
    elif node.value == "-":
        return leftSubtree - rightSubtree
    elif node.value == "*":
        return leftSubtree * rightSubtree
    elif node.value == "/":
        return leftSubtree / rightSubtree


print(evaluate(root))  # Should print 30.0

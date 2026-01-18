# Course Section: CSC 2720-012

"""
Assignment: Recover a Tree from a Preorder Traversal

Goal: Write a function that reconstructs the binary tree from this traversal string and returns the level order traversal of the tree.
"""

from collections import deque
from typing import List, Optional


# Structure for the binary tree node
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class TreeReconstructor:
    # Parses a node string to get its' depth and value.
    def parse_node_info(self, node_str: str) -> tuple[int, int]:
        depth = 0
        while depth < len(node_str) and node_str[depth] == "-":
            depth += 1
        value = int(node_str[depth:])
        return depth, value

    # Reconstructs the binary tree from its' preorder traversal string.
    def build_tree(self, traversal: str) -> Optional[TreeNode]:
        # Split traversal string into nodes, based on dashes
        nodes = []
        i = 0
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == "-":
                depth += 1
                i += 1
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            nodes.append((depth, value))

        # Create the root node
        root = None
        stack: deque[TreeNode] = deque()

        for depth, value in nodes:
            new_node = TreeNode(value)

            # If stack is not empty and the current depth is less than the depth of the last node in stack, pop
            while len(stack) > depth:
                stack.pop()

            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = new_node
                else:
                    parent.right = new_node
            else:
                root = new_node

            # Push the current node onto the stack
            stack.append(new_node)

        return root

    # Performs a level order traversal of the tree.
    def get_level_order(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if not root:
            return []

        result: List[Optional[int]] = []
        queue: deque[Optional[TreeNode]] = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values for a cleaner result
        while result and result[-1] is None:
            result.pop()

        return result

    # Method to reconstruct the tree and get its level order traversal.
    def reconstruct_and_traverse(self, traversal: str) -> List[Optional[int]]:
        root = self.build_tree(traversal)
        return self.get_level_order(root)


def main():
    # Test cases
    test_cases = ["1-2--3--4-5--6--7", "1-2--3---4-5--6---7"]

    solver = TreeReconstructor()
    for test in test_cases:
        result = solver.reconstruct_and_traverse(test)
        print(f"Input: {test}")
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()

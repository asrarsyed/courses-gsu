# Course Section: CSC 2720-012

"""
Assignment: 450. Delete Node in a BST
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root  # Best Case, Node not Found

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Get the smallest number in the right subtree
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.deleteNode(root.right, root.val)
        return root

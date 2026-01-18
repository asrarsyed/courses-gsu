# Course Section: CSC 2720-012

"""
Assignment: Write a function to insert a value into the list such that it remains as a sorted circular list.
            Keep sorted in non-descending order.

            The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

Limitations: If there are multiple suitable places for insertion, you may choose any place to insert the new value.
             After the insertion, the circular list should remain sorted.

             If the list is empty (i.e., the given node is null),
             you should create a new single circular list and return the reference to that single node.
             Otherwise, you should return the originally given node.

# Sample Input: head = [3,4,1], insertvalue = 2
# Sample Output: [3,4,1,2]
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Solution:
    def insert(self, head, insertVal):
        node = Node(insertVal)  # Create the new node to insert

        # Case 1: Empty list
        if head is None:
            node.next = node  # Single node points to itself
            return node

        # Case 2: Non-empty list
        prev = head
        curr = head.next

        while curr != head:
            # Find the correct spot to insert the new node
            if prev.value <= insertVal <= curr.value:  # In between two values
                break
            if prev.value > curr.value and (insertVal >= prev.value or insertVal <= curr.value):
                # Insert at the end or before the smallest value (wrap-around)
                break
            prev, curr = curr, curr.next

        # Insert the new node between prev and curr
        prev.next = node
        node.next = curr
        return head

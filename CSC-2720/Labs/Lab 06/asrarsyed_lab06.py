# Course Section: CSC 2720-012

'''
Assignment: Find length of a cycle in a Linked List using Floyd’s Cycle Detection Algorithm

Write a Python function named ‘get_cycle_length(node)’ that takes the head of a singly linked list as a parameter and returns:
	- 0 (if there is no cycle in the linked list)
	- ‘length_of_the_cycle’ (otherwise)

    No Cylce - Should return 0 for this linked list
    Yes Cycle - Should return 4 for this linked list, As the cycle has 4 nodes
'''

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def get_cycle_length(node):
    slow, fast = node, node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return length_of_the_cycle(slow)
    return 0

def length_of_the_cycle(slow):
    current = slow
    length = 0

    while True:
        current = current.next
        length += 1
        if current == slow:
            break
    return length
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedCircularQueue:
    """A Queue Implemented using Circularly Linked List"""

    def __init__(self):
        """Initialize an empty queue."""
        self.tail = None  # Tail points to the most recently added node
        self.size = 0  # Tracks the number of elements in the queue

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    def enqueue(self, element):
        """Add an element to the back of the queue."""
        new_node = Node(element)  # Create a new node
        if self.is_empty():
            new_node.next = new_node  #
        else:
            new_node.next = self.tail.next  # New node points to the head
            self.tail.next = new_node  # Old tail points to new node
        self.tail = new_node  # New node becomes the new tail
        self.size += 1

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        old_head = self.tail.next  # The front of the queue (head)
        if self.size == 1:
            self.tail = None  # Queue will become empty
        else:
            self.tail.next = old_head.next  # Bypass the old head
        self.size -= 1
        return old_head.value

    def front(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        head = self.tail.next  # The front of the queue (head)
        return head.value

    def rotate(self):
        """Rotate the front element to the back of the queue."""
        if self.size > 0:
            self.tail = self.tail.next


lcQ = LinkedCircularQueue()
lcQ.enqueue(1)
lcQ.enqueue(2)
lcQ.enqueue(3)
print(f"front = {lcQ.front()}")

lcQ.rotate()
print(f"front = {lcQ.front()}")

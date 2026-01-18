# Array based implementation of Stack ADT
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data.pop()  # remove last item from list


# Array based implementation of Queue ADT
class ArrayQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]


# Array based implementation of Deque ADT
class ArrayDeque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        return self.items.pop()

    def remove_front(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]
